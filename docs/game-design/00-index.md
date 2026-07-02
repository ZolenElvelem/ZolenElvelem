# Shadow Integration — Game Design & Production Plan

A generational life-simulation game concept: a small NZ coastal town, played across decades and multiple lives, where the core mechanic is the player's own clarity of perception rather than power. This folder is the working design and production plan turning that concept into something buildable by a solo/small Python-first team.

Read in order:

1. [Vision & Design Pillars](./01-vision-and-pillars.md) — the pitch, the non-negotiable filters every feature must pass, what the game deliberately is not, and how success is actually measured.
2. [Core Systems](./02-core-systems.md) — the Shadow-opacity mechanic, Living, Emergent Threads, the Meta-Mystery, Procedural NPC AI (with the LLM-approach tradeoff), Generational World & Persistence, and Death & Transition.
3. [Technical Architecture](./03-technical-architecture.md) — engine choice (Panda3D recommended, Godot as a fallback), the pure-Python simulation core, dialogue/LLM pipeline, visual mood system, and repo structure.
4. [Production Roadmap](./04-production-roadmap.md) — six phases from a no-engine paper prototype through polish, each with a go/no-go test tied to the emotional target, not just a feature checklist.
5. [Risks & Scope Control](./05-risks-and-scope-control.md) — the seven biggest risks to this project succeeding, and the concrete mitigation baked into the plan for each.
6. [Retention & Replay Model](./06-retention-and-replay.md) — what keeps people coming back: returning vs. replaying, the persistent-town New Game+ model, structural incompleteness, and what retention scaffolding is banned.
7. [Phase 0 Prototype Spec](./07-phase0-prototype-spec.md) — the concrete build plan for the first playable test: content, code structure, playtest protocol, and pass/fail conditions.
8. [Prior Art](./08-prior-art.md) — the competitive/novelty check: which ingredients of this design exist in other games, and what remains (as far as searching can tell) unbuilt.

## Key decisions locked after design review

- **The frozen-age model (the keystone).** Each unprocessed wound freezes a specific capacity — trust, intimacy, conflict, grief, play — at the age it happened, expressed as *age-regressed verb sets* in that domain, never as visible stats. Shadow thickness in a domain is the gap between chronological age and frozen age, so deflected pain compounds just by living (system 1).
- **The Shadow protects — and numbness isn't selective.** Opacity blunts incoming wounds *and joy at the same rate*; translucency means feeling everything. Opening up is a wager, and the pull toward it is missing being alive, not avoiding a penalty (pillar 2, system 1).
- **The real skill is modulation, not minimization** — there are moments when raising the guard is correct (system 1).
- **Healing is memory reprocessing:** present-day safety earns readiness to revisit the moment a capacity froze; facing it *resumes* growth from the frozen age rather than teleporting to maturity. Some wounds never fully unfreeze (system 1, system 4).
- **v1 is one complete life,** age six to death. Continuous generational simulation deferred; the town persists across lives via a cheap NG+ snapshot handoff (system 7, doc 6).
- **Each life starts at six** — the player is present when the first armor forms; the six-year-old is the deepest frozen part, the last memory you become ready for (system 2).
- **NPCs share the frozen-age skeleton** — two or three frozen capacities per NPC generate specific, explainable behavior and condition LLM dialogue cheaply (system 5); the late-game perception generalizes to *seeing the frozen ages in everyone* (system 7).
- **Not every tragedy traces to the central cause** — some griefs are blameless; and "one consciousness" stays forever unconfirmed (pillar 6, system 4).
- **Pillar 7:** the first hour must work for a player who will never finish the game.

**If you only have time to do one thing next:** build the Phase 0 prototype per doc 7. It's the cheapest possible test of whether the core bet — that modulating perception rather than power can carry emotional weight — actually works, before any engine time is spent.
