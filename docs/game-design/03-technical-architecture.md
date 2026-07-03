# Technical Architecture

Scoped for a solo/small-team build with a stated preference for Python and AI tooling. The core architectural bet: **keep the NPC simulation and world-persistence logic in pure Python** (where the AI/data ecosystem is strongest and a solo dev can iterate fastest), and choose the rendering/engine layer based on how much of that Python logic it lets you keep in one process.

## Engine options, evaluated against this project's actual needs

The visual mechanic (color grading, dynamic post-processing, layered ambient audio, aging character models, hidden/visible interactables) and the generational simulation (hundreds of NPCs, decades of event log, deterministic saves) matter more here than cutting-edge graphics. That changes the usual engine calculus.

| Engine | Python-native? | Fit here |
|---|---|---|
| **Panda3D** (+ optionally the **Ursina** wrapper for faster prototyping) | Yes — pure Python, engine and game logic share one process/codebase | **Recommended for prototyping and likely for the full build.** Open source, free, real 3D + shader support (needed for the color-grading/LUT-driven Shadow visuals), and — critically — your NPC simulation, event log, and dialogue-generation calls live in the *same* Python codebase as the engine loop. No IPC boundary, no serialization tax, fastest iteration for a solo Python-comfortable developer. Smaller ecosystem/asset store than Unity/Unreal and a smaller community, so expect to write more of your own tooling. |
| **Godot 4** | No (GDScript primarily; C# also supported) | Best out-of-the-box post-processing/shader editor and a more polished editor/animation workflow than Panda3D, free and open source, lighter weight than Unreal. If used, run the NPC simulation as a separate Python process/library and talk to it via a local socket or embedded via GDExtension — adds an integration seam but is very buildable. Worth switching to this if the pure-Python engine's editor tooling becomes a bigger bottleneck than the integration seam. |
| **Unity / Unreal** | No (C# / C++/Blueprints) | Strongest asset ecosystems and visual fidelity ceiling, but pulls you away from the stated Python preference entirely, and neither's strengths (AAA rendering, complex physics) are what this game actually needs. Not recommended given the stated constraints. |
| **Pygame** | Yes | Too primitive for the visual mood system and 3D-ish town exploration this design implies — but genuinely the right tool for the **Phase 0 paper/text prototype** (see roadmap) to test the "noticing" mechanic and thread pacing before committing engine time to anything else. |

**Recommendation:** start the technical prototype (roadmap Phase 1) in **Panda3D/Ursina**. It keeps everything — rendering, simulation, world persistence, LLM calls — in one Python codebase, which is the highest-leverage choice for a solo developer validating a very systems-heavy design. Revisit Godot specifically if the post-processing/shader workflow becomes a real bottleneck once the vertical slice (Phase 2) needs polish, not before.

## Simulation core (engine-independent, pure Python)

- **NPC state & relationships:** plain Python dataclasses for memory/drives/`shadow_density` vector per system 2 of the core-systems doc; `networkx` for the relationship graph (trust/resentment/love edges with decay) — good fit, well-documented, no need to hand-roll graph traversal for "who would plausibly hear this rumor."
- **World event log:** append-only table of `(tick, actor, target, event_type, location, payload)` — this is the backbone that both the thread-template system and generational memory ("your grandfather used to sit on that bench") read from.
- **Persistence:** SQLite. Ships with Python, zero ops overhead, transactional, and trivially inspectable during development (you can literally open the save file and read the town's history in a DB browser while debugging). Reassess only if save files get large enough to need something heavier — unlikely before Phase 4.
- **Persistent-town NG+ handoff:** end-of-life transition is a *single snapshot operation* — the event log, family records, and NPC states aged forward into a new life's starting world — not continuous multi-generation simulation. This is deliberately cheap; the same schema supports full generational simulation later if post-v1 scope ever funds it, so nothing is lost by deferring.
- **Scene capture for memory-revisiting:** key scenes must be replayable from the event log (actors, dialogue keys, state at the time), because the endgame verb re-enters them through new perception. Design the log's payload format with this in mind from day one — flagged-scene capture is nearly free up front and prohibitively expensive to retrofit.
- **Thread templates:** parameterized Python classes/config (recommend simple YAML or TOML definitions loaded into Python objects) so non-code thread variants can be authored without touching engine code — important for keeping content authoring separate from simulation code as the town grows.

## Dialogue / text generation layer

- Treat LLM calls as **offline/batched content generation, not live gameplay logic.** Generate and cache dialogue/flavor text from NPC state snapshots (ahead of time for background NPCs at world-seed time; on-demand-but-cached for the player's actual encounters), never require a live API call to be on a player-facing critical path.
- Keep this layer swappable behind a small interface (`generate_line(npc_state) -> str`) so the "deep NPC" upgrade path (system 5, Option A/B hybrid) can call a different, more expensive path for the dozen story-critical characters without touching the rest of the pipeline.
- Budget and reliability matter here for a solo dev shipping a game with no ongoing revenue model assumed — cost-model this explicitly before Phase 3 content generation begins (see roadmap and risks docs).

## Visual mood system

- Shadow opacity → a single blended parameter (0–1 per wound category, aggregated) drives: a LUT/color-grade blend, fog density, and a spawn-density multiplier for ambient wildlife/crowd agents. In Panda3D this is a standard GLSL post-process shader driven by a uniform you update each frame from the simulation's aggregate `shadow_density`.
- Audio: layer ambient stems (birds, waves, distant voices, music) and crossfade layer volumes by the same parameter. A basic custom mixer is sufficient at prototype scale; only reach for something like FMOD if the layering needs get more complex than simple crossfades.

## Suggested repo structure (once code work starts)

```
/sim/          # pure Python simulation core: npc, relationships, event_log, threads
/content/      # town/family/thread data (YAML/TOML), no logic
/engine/       # Panda3D app: rendering, input, shaders, audio mixing
/tools/        # world-seed generator, save inspector, thread-authoring helpers
/docs/game-design/   # this design documentation
```

## Solo-dev tooling notes

- Build a **save/world inspector** (a simple CLI or lightweight local web view over the SQLite file) early — for a game whose entire premise is "the town remembers," you will spend enormous time debugging *what the world actually believes happened*, and eyeballing a database table beats print-debugging a live 3D scene.
- Log every thread-template instantiation and its resolution outcome; this doubles as your procedural-content QA and as raw material for tuning the utility-AI weights in system 5.
