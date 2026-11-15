# Idea Advisor V0.1.1

Idea Advisor (创意顾问) helps users move from an unclear idea to an evidence-aware, compared, decision-ready design. It is a general-purpose Agent Skill for AI Skills, software products, tools, and technical projects. It advises on design; it does not implement the product or manage its delivery.

## Install and use

Copy the whole `idea-advisor` directory into the Skills directory supported by your agent. For Codex on Windows, for example:

```powershell
Copy-Item -Recurse -LiteralPath .\skills\idea-advisor -Destination "$env:USERPROFILE\.codex\skills\idea-advisor"
```

Check for an existing destination before copying so you do not overwrite local changes. Use `$idea-advisor` if your agent supports explicit Skill invocation, or describe a product/solution design task and let the agent select it. Discovery and reload behavior depend on the client.

Example: “I keep losing track of small team decisions. Help me decide whether a lightweight app is worth building.”

## What it can produce

As useful for the decision, it can produce a problem definition, sourced landscape review, options comparison, recommendation, lightweight PRD, scope and non-goals, acceptance criteria, decision records, or an implementation handoff. It does not require every task to produce every artifact.

The workflow is adaptive: explore, research, compare, decide, deliver. Existing context is reused; questions are reserved for choices that could change the design. Decisions can be revisited while preserving history. If the agent has no persistence, it provides a portable recovery summary.

V0.1.1 clarifies design-versus-execution intent, protects the advisor role from drifting into a tool tutorial, encourages proactive first proposals, and adds restrained 💡 / 🔎 / ❓ conversation markers.

## Limits

Research depends on the agent's available browsing and connected tools. The Skill does not guarantee source freshness or a high-quality design; users should inspect evidence and confirm consequential decisions. V0.1 has no executable runtime, database, automatic cross-session memory, or required platform integration.

## Validation

See [tests/README.md](tests/README.md) for scenario-based manual evaluation. Static checks can verify package structure and links, but cannot establish that an agent consistently reasons well. No scenario results should be described as real-agent acceptance unless actually run in an agent that loaded this Skill.

MIT License; see the repository [LICENSE](../../LICENSE).
