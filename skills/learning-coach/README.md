# Learning Coach V0.1

一个面向多种知识领域的 Agent Skill：按需规划课程、互动教学、安排实践、检查成果、针对性补学和复测。用户明确要求时可整理不同类型的学习笔记。规则均为 Markdown，不依赖外部服务或运行时程序。

## 安装与调用

将整个 `learning-coach` 目录复制到 Codex 的用户 Skills 目录。Windows PowerShell 示例（在仓库根目录执行）：

```powershell
Copy-Item -Recurse -LiteralPath .\skills\learning-coach -Destination "$env:USERPROFILE\.codex\skills\learning-coach"
```

若目标已存在，先检查并处理冲突，避免覆盖。安装后开启新的 Codex 会话以重新发现 Skill；输入 `$learning-coach` 并描述任务，也可直接描述学习需求供 Codex 自动选择。实际可发现性取决于目标客户端配置，需在安装后验证。其他支持开放 Agent Skills 格式的客户端应将整个目录放入其规定的 Skills 位置，具体发现方式以客户端文档为准。

示例：`$learning-coach 教我实例属性和类属性`；`$learning-coach 给我一个 Git 学习路线`；`$learning-coach 测试我对属性查找的理解`。

## 进度与隐私

进度由用户选择的私有 Markdown 文件保存，不放在 Skill 安装目录或公开仓库。恢复时提供路径或内容；找不到记录时需要提供记录或简要回顾。没有数据库、云同步或自动长期记忆。笔记文件的存放位置由用户选择。

## 开发和验证

入口在 `SKILL.md`，各模式细节在 `references/`。修改时保持相对链接和独立分发，避免把个人学习数据提交到仓库。实践记录和 Verified / Unverified / Needs reinforcement 状态必须关联实际证据。可用 Codex skill-creator 的 `quick_validate.py` 验证结构；它不能证明教学行为。

在新会话中人工验证：请求 Python 面向对象课程规划；学习实例属性与类属性并确认提问后等待回答；将所学整理为独立笔记；用新题测评属性查找并根据回答指出薄弱点；分别使用真实进度文件和缺失的记录尝试恢复。再用非 Python 主题检查适用范围，并检查只要求单项任务时不会强制走完整流程。记录实际结果，不把结构检查当作多轮行为验证。

MIT 许可，见 [LICENSE](LICENSE)。
