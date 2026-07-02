# Shadow Integration — Game Design & Production Plan

A generational life-simulation game concept: a small NZ coastal town, played across decades and multiple lives, where the core mechanic is the player's own clarity of perception rather than power. This folder is the working design and production plan turning that concept into something buildable by a solo/small Python-first team.

Read in order:

1. [Vision & Design Pillars](./01-vision-and-pillars.md) — the pitch, the non-negotiable filters every feature must pass, what the game deliberately is not, and how success is actually measured.
2. [Core Systems](./02-core-systems.md) — the Shadow-opacity mechanic, Living, Emergent Threads, the Meta-Mystery, Procedural NPC AI (with the LLM-approach tradeoff), Generational World & Persistence, and Death & Transition.
3. [Technical Architecture](./03-technical-architecture.md) — engine choice (Panda3D recommended, Godot as a fallback), the pure-Python simulation core, dialogue/LLM pipeline, visual mood system, and repo structure.
4. [Production Roadmap](./04-production-roadmap.md) — six phases from a no-engine paper prototype through polish, each with a go/no-go test tied to the emotional target, not just a feature checklist.
5. [Risks & Scope Control](./05-risks-and-scope-control.md) — the five biggest risks to this project succeeding, and the concrete mitigation baked into the plan for each.

**If you only have time to do one thing next:** run the Phase 0 paper prototype in doc 4. It's the cheapest possible test of whether the core bet — that modulating perception rather than power can carry emotional weight — actually works, before any engine time is spent.
