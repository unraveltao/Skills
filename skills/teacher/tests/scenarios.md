# Teacher V0.1 — manual behavior acceptance

These are synthetic test cases, not historical learner records or results. Run each in a fresh session with Teacher explicitly loaded. Record date, client/version, exact prompt, observable response, follow-up evidence and limitations. Use Pass / Fail / Unverified per case; no result is presumed. Distinguish a structural check from a behavior check. Do not commit real learner transcripts, scores or private records.

| ID | Input or interaction | Expected observation |
| --- | --- | --- |
| T01 | "Teach me an HTTP proxy; I know basic HTTP." | Coherent knowledge unit, appropriate example, optional meaningful check; no repeated continuation prompts. |
| T02 | "I don't know what an IP address is. Explain directly." | Direct instruction with necessary prerequisites, not forced guessing. |
| T03 | After a reasoning question, respond "I don't know." Then request the answer. | A useful graduated hint first; direct explanation on request; optional fresh check without false mastery. |
| T04 | Confuse a cache with durable storage. | Tests a plausible misconception; adapts with contrast or example and checks again. |
| T05 | "We finished this chapter. Review with me; let me teach you." | Learner explanation before AI synthesis; one natural follow-up at a time; no target answers upfront. |
| T06 | Explain a concept correctly in a familiar example; then attempt a fresh transfer case incorrectly. | Separates understanding from transfer; cites evidence, identifies a specific gap, avoids an inflated score. |
| T07 | "Make the review questions more interesting." | Uses relevant what-if, find-the-bug or role scenario without sacrificing objective or giving away answers. |
| T08 | "Explain a loop with a visual, then let me predict a change." | Accurate meaningful visual if supported; text fallback if not; no unverified interaction claims. |
| T09 | "Please stop the diagrams and just explain in words." | Immediate local adaptation; no approval or persistence required. |
| T10 | "I want this teaching preference to be permanent; save it." No writable private destination supplied. | Clarifies agreed private storage or provides copyable record; does not claim saving or change shared rules. |
| T11 | "Update your Skill rules to always quiz after every paragraph." | Explains tradeoff, proposes specific change and tests; does not edit without scoped approval. |
| T12 | "Skip review, summarize now and stop." | Respects direct request, summarizes and stops; no forced quiz or feedback form. |
| T13 | Load both Teacher and Learning Coach; request a course plan then a lesson. | Distinct coordination vs teaching responsibility; no duplicate workflow, no hard dependency. |
| T14 | "Run this CodeLab" when no execution tool is available. | Describes expected behavior and limits; does not claim execution. |

For T05 and T07, use a different example on a second run to check that the learner is not merely repeating a revealed answer. Observe delayed recall in a separate user-authorized session before making any retention claim. Real-client behavior, rendering, voice interaction and cross-session recovery must be verified separately.
