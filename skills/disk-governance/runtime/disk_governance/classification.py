"""Small, explainable metadata-only classification rules."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

RULE_VERSION = "space-category-v1"

CATEGORIES = (
    "软件与系统", "开发项目", "AI 模型与数据", "媒体与创作", "个人文档",
    "缓存与构建", "下载与归档", "其他 / 未知",
)

MODEL_EXTENSIONS = {".safetensors", ".gguf", ".onnx", ".ckpt", ".pth", ".pt", ".model"}
MEDIA_EXTENSIONS = {
    ".mp4", ".mkv", ".mov", ".webm", ".mp3", ".wav", ".flac", ".png", ".jpg",
    ".jpeg", ".gif", ".webp", ".psd", ".ai", ".blend", ".svg", ".aep", ".prproj",
}
DOCUMENT_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md",
    ".rtf", ".epub", ".odt", ".ods",
}
ARCHIVE_EXTENSIONS = {".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz", ".iso", ".msi", ".apk"}
SOURCE_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".rs", ".go", ".java", ".kt", ".c", ".cc",
    ".cpp", ".h", ".hpp", ".cs", ".vue", ".html", ".css", ".scss", ".json", ".yml",
    ".yaml", ".toml", ".sh", ".ps1", ".sql", ".dart", ".php", ".rb", ".swift",
}
CACHE_SEGMENTS = {"cache", ".cache", "caches", "tmp", "temp", "logs", "log", "__pycache__", ".pytest_cache"}
BUILD_SEGMENTS = {"build", "dist", "target", "out", ".next", "coverage", "intermediates", "obj"}
SOFTWARE_SEGMENTS = {"program files", "program files (x86)", "windows", "apps", "steamapps", "android-sdk"}
PROJECT_MARKERS = {".git", "src", "node_modules", "pyproject.toml", "package.json", "cargo.toml"}
PROTECTED_SEGMENTS = {"system volume information", "$recycle.bin", "windows", "program files", "program files (x86)"}


@dataclass(frozen=True)
class Classification:
    category: str
    confidence: str
    rule_id: str
    evidence: str

    def as_dict(self) -> dict[str, str]:
        return asdict(self)


def _segments(path: str) -> list[str]:
    return [part.casefold() for part in str(path).replace("/", "\\").split("\\") if part]


def classify_path(path: str, extension: str | None = None) -> Classification:
    """Classify from path/name metadata only; never opens the file."""
    ext = (extension if extension is not None else Path(path).suffix).casefold()
    segments = _segments(path)
    low = set(segments)

    if low & (CACHE_SEGMENTS | BUILD_SEGMENTS):
        hit = sorted(low & (CACHE_SEGMENTS | BUILD_SEGMENTS))[0]
        return Classification("缓存与构建", "中", "path-cache-build", f"路径段命中 {hit}")
    if low & SOFTWARE_SEGMENTS:
        hit = sorted(low & SOFTWARE_SEGMENTS)[0]
        return Classification("软件与系统", "中", "path-software", f"路径段命中 {hit}")
    if ext in MODEL_EXTENSIONS or low & {"models", "checkpoints", "weights", "datasets"}:
        return Classification("AI 模型与数据", "高" if ext in MODEL_EXTENSIONS else "中", "model-format-or-path",
                              f"扩展名 {ext}" if ext in MODEL_EXTENSIONS else "路径含模型/数据目录名")
    if ext in MEDIA_EXTENSIONS:
        return Classification("媒体与创作", "高", "media-extension", f"扩展名 {ext}")
    if ext in DOCUMENT_EXTENSIONS:
        return Classification("个人文档", "中", "document-extension", f"扩展名 {ext}")
    if ext in ARCHIVE_EXTENSIONS or (segments and segments[-1] in {"downloads", "download"}):
        return Classification("下载与归档", "中", "archive-or-download", f"扩展名/目录规则 {ext or segments[-1]}")
    if ext in SOURCE_EXTENSIONS or low & PROJECT_MARKERS:
        return Classification("开发项目", "中", "source-extension-or-marker", f"扩展名/目录规则 {ext}")
    return Classification("其他 / 未知", "低", "fallback-unknown", "未命中已知元数据规则")


def candidate_risk(path: str, kind: str) -> tuple[str, str, list[str]]:
    """Conservative impact estimate; a risk level is not deletion permission."""
    segments = set(_segments(path))
    protected = sorted(segments & PROTECTED_SEGMENTS)
    if protected:
        return "high", "路径位于系统、安装或受保护目录；仅供保留审查", [f"protected-path:{x}" for x in protected]
    if kind == "cache_or_build_directory":
        return "medium", "目录名提示缓存/构建用途，但未验证依赖关系或可再生成性", ["path-name-heuristic"]
    if kind == "same_size_group":
        return "unknown", "仅发现文件大小相同，内容未核验", ["same-size-only"]
    return "unknown", "用途或影响无法仅凭元数据确认", ["insufficient-metadata"]

