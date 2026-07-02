# Production Roadmap

Scoped for a solo developer or very small team (1–3 people), Python-first stack. Every phase has a **go/no-go test tied to the emotional target** (see `01-vision-and-pillars.md`), not just a feature checklist — a phase that hits every feature but fails its test should not proceed to the next phase without redesign.

## Phase 0 — Paper Prototype (4–6 weeks, no engine)

**Goal:** validate the "noticing" mechanic, the protection tradeoff, and thread pacing before spending any engine time.

- Build the text prototype specified in full in `07-phase0-prototype-spec.md`: ten days, one street, one wound scalar, the Mara thread with its "resolves without you" outcome, the blunted-wound event, one CLEAR-only hidden discovery, and the epilogue that surfaces what the player never saw.
- Playtest with 3–5 people outside the project using the debrief protocol in that spec. Ask afterward: *did you notice the thread yourself, or did you need it pointed out? did the resolution feel like the world moved on, or like it froze waiting for you? how did the wound event feel at the guard level you were carrying?*

**Go/no-go:** testers notice at least one thread unprompted and can describe how it changed without their input. If not, the noticing mechanic's signal design is broken — fix it here, where a fix costs an afternoon, not after Phase 1 where it costs weeks.

## Phase 1 — Technical Prototype (2–3 months)

**Goal:** prove the Shadow-opacity visual/audio mechanic actually produces the intended feeling, in engine, with the simulation core wired up minimally.

- Panda3D/Ursina scene: a single small block of the town, day/night cycle, 2–3 hand-scripted NPCs (no AI simulation yet — hard-code their state).
- Wire `shadow_density` to the full visual/audio pipeline described in `03-technical-architecture.md`: LUT blend, fog, ambient layer crossfade, wildlife density, and at least one literally-hidden-below-threshold interactable (the first engineered "it was always there" moment).
- First playable version of the tactile toy (surfing), fun with no rewards attached — per pillar 7, this carries the minutes and must exist before any theme is layered onto it.
- Build the save/world inspector tool now, even though there's barely a world yet — it's cheap at this scale and painful to retrofit.

**Go/no-go:** a blind playtester (no explanation given beforehand) can correctly describe, after moving through a translucent vs. opaque state, which one represents "seeing more clearly" — without being told the metaphor. If the mapping isn't legible without explanation, the visual language needs iteration before any more content is built on top of it.

## Phase 2 — Vertical Slice (3–4 months)

**Goal:** the first slice that could be shown to a publisher/collaborator or used to validate the full loop end to end.

- Expand to one small neighborhood, ~10 NPCs on the Option-A simulated-state core (relationship graph, memory, drives — no LLM decision-making, per the recommended hybrid in `02-core-systems.md`).
- 3–5 emergent threads, at least one built from a reusable thread template (not hand-scripted) to prove that pipeline. At least one blameless grief among them (not everything traces to the central cause).
- One complete "life chapter" for the player character — the childhood arc, starting at age six, in which the first Shadow layers form on-screen (per system 2's "playing the wounds" decision).
- Key scenes flagged for event-log capture from the start, so the late-game memory-revisiting verb (system 4) can replay them — this cannot be retrofitted cheaply in Phase 4.
- First authored fragment of the meta-mystery (one dream/song/symbol clue), not the full mystery.
- Cached LLM-generated dialogue for at least a few NPCs, to test the offline/batched pipeline for real.

**Go/no-go:** run the full pillar-6 test from the vision doc — does at least one external playtester, unprompted, connect something in the game to a person in their own life? This is the real gate before investing in systemic depth (Phase 3) and generational scale (Phase 4).

## Phase 3 — Systemic Depth (6+ months)

**Goal:** turn the vertical slice into one complete, systemically deep life — plus the persistent-town NG+ handoff. (Scope revised after design review: continuous generational simulation is deferred post-v1; see `06-retention-and-replay.md`.)

- Implement the full life arc structure (childhood → adulthood → elder → death), the epilogue (including the surfaced-incompleteness glimpse), and the **persistent-town NG+ world-state snapshot handoff** with inherited `shadow_density` shaping for the next life's character.
- Event log query system NPCs/dialogue can reference for callbacks within a life and across NG+ lives.
- Procedural background-NPC history generation at world-seed time via the thread-template system, so the town has decades of plausible history without hand-authoring all of it.
- Expand the town geographically (a few more streets/locations) and the family roster (aim for the "5–8 founding families" content seed referenced in the core-systems doc).

**Go/no-go:** seed a fresh world, fast-forward it procedurally through ~20 simulated years with no player interaction, then inspect the event log — does it read as a plausible, non-repetitive town history? If the thread-template system is producing obviously repetitive or contradictory outcomes at this scale, fix the template/utility-AI design before writing more hand-authored content on top of it.

## Phase 4 — Content & Meta-Mystery Completion

**Goal:** full authored content pass.

- Complete the meta-mystery clue chain end to end (dreams/songs/drawings/symbols) and the late-game "see the six-year-old in everyone" perception unlock, including the **memory-revisiting** endgame verb (re-entering flagged scenes through the new perception) and its carry-forward into NG+ lives.
- Author the dozen or so "deep NPC" story-critical characters (the Option-B upgrade path from system 5).
- Full era progression content (technology/culture shifts across the decades the game spans).
- Content and balance pass on wound/healing event weights across all wound categories.

## Phase 5 — Polish & Release Prep

- Accessibility pass (color-grading-driven mechanics need a colorblind-safe/alternate signal path — do not rely on hue shift alone for the opacity mechanic).
- Performance pass on NPC simulation at full town scale.
- Final playtesting focused specifically on the emotional-target metric from the vision doc, with fresh (non-team) testers.
- Store page / distribution prep.

---

## Sequencing discipline for a solo/small team

Do not start Phase 2's NPC simulation work before Phase 1's go/no-go passes — the visual/perception mechanic is the entire bet this project makes, and every later system (threads, mystery, generations) is built to serve it. If it doesn't land in a bare-bones scene with scripted NPCs, no amount of procedural depth added later will fix that; it will only make the failure more expensive to diagnose.
