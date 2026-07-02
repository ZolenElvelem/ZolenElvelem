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

## Key decisions locked after design review

- **The Shadow protects.** Opacity blunts incoming wounds; translucency means feeling everything. Opening up is a wager, never a free upgrade (pillar 2, system 1).
- **v1 is one complete life,** age six to death. Continuous generational simulation deferred; the town persists across lives via a cheap NG+ snapshot handoff (system 7, doc 6).
- **Each life starts at six** — the player is present when the first armor forms (system 2).
- **The endgame verb is memory-revisiting:** re-entering scenes you already played, through the earned perception (system 4).
- **Not every tragedy traces to the central cause** — some griefs are blameless; and "one consciousness" stays forever unconfirmed (pillar 6, system 4).
- **Pillar 7:** the first hour must work for a player who will never finish the game.

**If you only have time to do one thing next:** build the Phase 0 prototype per doc 7. It's the cheapest possible test of whether the core bet — that modulating perception rather than power can carry emotional weight — actually works, before any engine time is spent.
