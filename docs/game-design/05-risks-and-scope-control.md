# Risks & Scope Control

This concept is one of the most ambitious things an indie/solo project can attempt — a generational life sim, a procedural-psychology NPC system, decades of persistent world memory, and a meta-narrative, all in service of a subtle emotional thesis. That ambition is the project's biggest strength and its biggest risk. This document exists to name the risks plainly so scope decisions get made deliberately instead of by drift.

## Risk 1 — Scope exceeds what a solo/small team can finish

**Mitigation:** the phase gates in `04-production-roadmap.md` are designed so each phase is independently shippable as a smaller thing if the project needs to stop there (a paper prototype, a technical demo, a vertical slice / pitch deck for collaborators, a small complete game about one generation). Treat Phase 2 (vertical slice) as the real "minimum complete experience" fallback — it has a beginning, a death/transition, and one taste of the mystery. Don't let Phase 3+ start until Phase 2 is actually good, not just done.

## Risk 2 — LLM cost, latency, and long-run consistency for NPCs

Full LLM-driven NPC reasoning (Option B in `02-core-systems.md`) does not scale to "hundreds of NPCs over decades" at indie budget, and live LLM calls in a gameplay-critical path create latency and availability dependencies a shipped game shouldn't have.

**Mitigation:** the recommended hybrid (deterministic simulation core + batched/cached LLM text generation + a small "deep NPC" allow-list for expensive reasoning) is the load-bearing decision that makes the rest of the design affordable. Do not let this erode during development — it's tempting to reach for "just call the LLM live" for one more NPC at a time until the cost model breaks.

## Risk 3 — The theme becomes preachy

A game whose entire point is "understand people beneath their armor" fails immediately if any NPC ever says that sentence out loud. This is named as a hard constraint in pillar 6 of the vision doc, but it's worth restating as a risk: it is the single easiest mistake to make under writing-deadline pressure, because a line of dialogue stating the theme is always faster to write than a scene that demonstrates it.

**Mitigation:** treat any dialogue draft that explicitly names "the Shadow," "the six-year-old," or the metaphor in-world as a review flag, not a shippable line, for any character except in the most tightly scoped, late-game diegetic moments (e.g. a found document, not spoken dialogue). Build this into whatever writing/review process the team uses once Phase 4 content writing starts.

## Risk 4 — Procedural generational history produces incoherent or repetitive narratives

Thread-template instantiation at world-seed scale (Phase 3) risks producing contradictions (an NPC "dies" twice, a resolved thread references an event that never happened) or obviously repetitive patterns that break immersion in exactly the system meant to create it (the town's memory).

**Mitigation:** the Phase 3 go/no-go test (fast-forward a fresh world ~20 years with no player interaction and inspect the log) exists specifically to catch this before it's buried under hand-authored content that assumes a clean history. Build a lightweight consistency check (no duplicate death events, no thread referencing a nonexistent prior event) into the world-seed tool itself, not as an afterthought.

## Risk 5 — Players route around the "noticing" mechanic

If a player learns to methodically investigate everything (checking every NPC/location on a schedule, wiki-style), the "you must pay attention, and inattention has consequences" pillar collapses into a checklist, and the perception-gating (system 1: threads/interactables invisible below a Shadow-opacity threshold) becomes the only thing actually enforcing it.

**Mitigation:** lean on the opacity-gated visibility mechanic as the real enforcement layer (a min-maxing player who never softens their Shadow literally cannot see everything, structurally, not just narratively) rather than relying on player restraint or game-design goodwill. Validate this specifically in Phase 2 playtesting — watch whether testers who play "completionist" style actually hit the visibility gate as intended.

## Risk 6 — Translucency becomes strictly better, and the systems contradict the theme

If a thick Shadow is only ever an impairment (muted world, hidden opportunities, hostile-reading NPCs), players will treat opacity as a debuff to minimize — healing collapses into min-maxing, and the game *says* "the Shadow isn't the enemy" while its systems treat it as exactly that.

**Mitigation:** the protection tradeoff (system 1 in `02-core-systems.md`) is now a design commitment: opacity blunts incoming wounds and makes hard situations survivable, translucency means feeling everything at full volume. Every new wound/healing mechanic added during production must preserve this tension — treat any feature that makes translucency cost-free as a theme bug, not a balance tweak. Validate the tradeoff *emotionally* (not just numerically) in the Phase 0 debrief (question 3 in `07-phase0-prototype-spec.md`).

## Risk 7 — The payoff is backloaded and the first hour is homework

The emotional architecture of this game is inherently backloaded: years of relationships before the reveal means the opening carries no theme yet. Games in this genre die in the first hour, not the last — a player who bounces off a slow, unexplained opening never reaches anything the project exists to deliver.

**Mitigation:** pillar 7 in the vision doc makes this a hard constraint: the first hour must be charming, tactile, and quietly mysterious on its own merits, for a player who will never finish. Concretely: the surf toy must be intrinsically fun with no rewards attached (a Phase 1 deliverable, not polish), and first-session playtests should be run and evaluated *separately* from full-arc playtests from Phase 2 onward. Related expectation-setting: cold replayability will be middling, like every game in this genre — the retention model is *returning* (moving world mid-game, persistent-town NG+ after), per `06-retention-and-replay.md`, and no extrinsic retention scaffolding (meta-progression, achievement checklists) may be added to compensate.

## Recommended immediate next step

Before any engine work: run Phase 0 (paper prototype) with real outside playtesters. It's the cheapest possible test of the project's actual core bet — that modulating what a player perceives, rather than what they can do, can carry an emotional payload. Everything else in this plan is downstream of that bet paying off.
