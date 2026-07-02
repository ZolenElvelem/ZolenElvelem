# FPP Direction & Migration Plan

**Decision (2026-07-02):** the game moves to stylised first-person perspective. The 2D side-view sketch line ends at v4, preserved on branch `interactive-resume-base` (also earmarked as the base for a separate interactive-resume project — do not delete or rebase that branch).

## Why first person

The core mechanic is perception; first person is the perception camera. Everything the Shadow does (mutes color, thins sound, hides opportunities, makes people read as hostile) happens *to* the player instead of being displayed near them. Specific unlocks:

- **Gaze as a verb.** Holding or failing to hold eye contact; at high guard the camera drifts off faces and the player fights their own neck. "You are fourteen about it," embodied.
- **Child height.** Lives start at six → 1.1 m camera. Return to the same rooms grown and everything is small. Zero words.
- **The camera grammar (first-class design idea):**
  - *Living* — first person: you are inside the glass.
  - *Remembering* (the healing verb) — third person: you watch your younger self from outside; therapeutic distance as a camera position.
  - *Endgame perception* — first person **as someone else**: re-living a remembered scene through the other person's eyes. The one-consciousness reading delivered purely as camera language, never as lore.
- **Solo-dev economics:** protagonist model/animation mostly evaporates; reflections (shop windows, mirrors, your shadow on the sand — six years old when you're translucent enough) become the device instead of the limitation.
- **Genre precedent:** Firewatch, Gone Home, Edith Finch, Outer Wilds, Before Your Eyes — stylised FPP + one systemic twist is the proven indie-viable shape for emotional games.

## Known costs & mitigations

1. **3D production cost.** Mitigate with radical flat-shaded stylisation (suits the color-as-perception mechanic better than realism) and ruthless geography: one street, one beach, one hill, few interiors.
2. **The surf toy.** FPP surfing is hard to read and a motion-sickness risk. Default plan: **camera pulls to third person for surfing** (prototype this first); fallback: over-the-shoulder curl-check as a deliberate mechanic. The land/water camera contrast may read as intentional (embodied on land; watching the body do the one fluent thing it has, on water).
3. **Engine:** strengthens Godot's case over Panda3D (better 3D tooling); decision deferred until the browser spike validates feel (F0/F1 below).

## Migration phases (browser spikes first, engine after)

- **F0 — FPP feel spike** (`prototype/fpp/`): walkable flat-shaded street (three.js vendored locally, no CDN), WASD + mouse-look, guard-driven palette/fog/vignette lerp, child-height toggle, one gaze interaction (look at the tūī ~1 s → it sings → slight softening). Accept: no console errors; a blind viewer can tell open from armored; gaze trigger works.
- **F1 — the personal layer**: gaze-aversion at high guard (camera drift off an NPC face), one doorway conversation with regressed/adult verb menus, Mara's bin as a 3D clickable, spatial audio port (ocean by proximity, birdsong by openness).
- **F2 — the camera grammar demo**: one scripted memory that replays in third person; if it lands, the grammar goes into the vision doc as pillar-level.
- **F3 — surf camera decision**: port the v4 surf toy behind a third-person camera switch; test for readability and nausea.
- **Engine milestone:** after F1 passes with testers, port the validated feel to Godot (or Panda3D if 2D-adjacent tooling wins) per the existing Phase 1 roadmap gate — the browser spikes replace nothing in the roadmap; they de-risk its Phase 1.

## Token-economy workflow (how this gets built from here)

Main session (expensive model): design decisions, playtest synthesis, reviews, and unblocking — nothing mechanical. Execution goes to cheaper agents:

- **Haiku agents:** well-specified mechanical packets — ports, spikes with precise specs, test scripts, asset generation, doc formatting.
- **Sonnet agents:** gameplay code requiring judgment (F1 gaze feel, surf camera) when a Haiku attempt underdelivers.

**Every agent brief must be self-contained:** exact files to touch, the spec, the acceptance test it must run (headless Chromium at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`), commit message style, and the branch (never switch branches; never rebase `interactive-resume-base`). Agents commit and push; the main session reviews diffs and playtests, then issues the next packet. Findings continue to accrue in `prototype/README.md`.
