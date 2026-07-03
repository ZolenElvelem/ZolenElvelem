# Phase 0 Prototype — Build Specification

This is the concrete construction plan for the Phase 0 paper prototype from the roadmap: exactly what to build, how it's structured, and what it must prove. It's deliberately tiny — pure-Python, text-only, stdlib-only, one or two weekends of work — because its entire job is to answer the project's core bet *before* any engine time is spent: **can modulating what a player perceives (rather than what they can do) carry emotional weight?**

## What it is

A terminal-based, menu-driven slice of one life: **ten in-game days, two action slots per day, one street of the town, one NPC thread, one wound event, one hidden discovery.** A playtest session runs 15–25 minutes. Everything is deterministic (no RNG), so every tester experiences differences *only* through their own choices — which is the point.

## The one simplification that makes it buildable

The full design's frozen-age capacity set (system 1 in `02-core-systems.md`) collapses to a **single scalar, `guard` (0.0–1.0)** — narratively framed as *one* frozen domain: **the character's trust froze at fourteen**, and `guard` is how thick that layer has grown since. It's mapped to three perception tiers:

| Tier | Guard range | What it means |
|---|---|---|
| CLEAR | < 0.35 | you feel everything — both directions |
| TRANSLUCENT | 0.35–0.65 | an ordinary adult (the starting state, 0.55) |
| OPAQUE | ≥ 0.65 | protected, and blind |

Every piece of content in the prototype is authored in **layers keyed by tier**: a base line everyone gets, extra lines that appear at TRANSLUCENT, and lines/options that only exist at CLEAR. A guarded player literally reads a shorter, flatter town. This is the text-medium stand-in for the eventual color-grading/audio/spawn pipeline.

## The five rules it exercises (one per design decision from review)

1. **Perception gating** — descriptions, thread signals, and *menu options themselves* are filtered by tier. At OPAQUE, some choices simply don't appear; the player never knows a door existed.
2. **The Shadow protects — and numbness isn't selective** — the one scripted wound event applies `felt = base_wound × (1 − 0.6 × guard)`. An armored player takes roughly half the hit an open one does, and the text renders the difference ("you feel it at a distance, like weather offshore" vs. the full force). But the same dampening applies to the good moments: the OPAQUE surf paragraph is flat and functional where the CLEAR one sings. This is the tradeoff made playable: softening yourself to see more means the wound lands harder *and* the wave finally feels like something.
3. **Verbs regress in the frozen domain** — in the one scene that touches the frozen capacity (naming what you've seen to Mara — an act of trust), the menu initially offers only the fourteen-year-old's moves: make a joke of it, get an excuse ready, leave early. The adult option — *say what you've actually seen, plainly* — appears only once enough presence has been built. The player should feel the regression before they can name it.
4. **Healing is gradual** — helping the thread NPC requires accumulated presence across multiple visits plus one costly moment of honesty, never a single dialogue pick.
5. **The world moves without you** — the thread resolves on its own, badly but survivably, if ignored. No freeze, no fail state.

## Content spec

**Setting:** one street — the beach, the pub, Mara's place, the bench above the bay, the bush reserve on the hill. NZ coastal-town texture throughout (tui, pōhutukawa, the estuary, a southerly coming through).

**Verbs (per slot):** surf · go to the pub · visit Mara · sit on the bench · walk the reserve *(only visible at CLEAR — see below)* · rest. Each nudges `guard` a little (surfing and the bench soften; grinding through days armored does not).

**The thread — Mara's drinking.** Fixed signal schedule; each signal registers only if the player is in the right place *and* at TRANSLUCENT or better:

- Day 2 — she cancels the standing dinner (the fact reaches everyone; its *significance* only lands below OPAQUE)
- Day 3+ — visiting her, the empties are visible in the recycling
- Day 5 — the pub keeper says something sideways
- Day 6 — **the wound event**: the player's father has a health scare. Deliberately *blameless* — an illness, no villain, no lesson — per the not-monocausal constraint. This is where rule 2 fires.
- Day 8 — Mara misses work; the whole street hears
- End of day 9 — resolution: if the player has noticed at least one signal, *named it to her* (the honesty moment: costs a visible chunk of guard), and built presence ≥ 3 visits → she asks them to drive her to her first meeting. Otherwise → her car in the ditch by the estuary; she's okay, but everyone knows now. The town logs either outcome.

**The hidden discovery ("it was always there"):** the reserve walk exists only at CLEAR. Taking it finds a decades-old carving on a tōtara — the prototype's single meta-mystery seed. Most testers will never see it. That's intended.

**The epilogue (the actual test instrument):** after day 10, the game shows — in prose, no numbers — what happened, how the father's news *felt* at the guard level the player carried, and then surfaces structural incompleteness: what this particular player never saw ("On the hill above the town, a tōtara carries a carving you never found. Mara set three places for dinner on day 2; you read the message and put the phone down."). It closes with the game's real questions — *when did your own Shadow become so thick?* — followed by the facilitator's debrief prompts.

## Code structure (mirrors the planned full architecture in miniature)

```
prototype/
  README.md    # how to run, facilitator script, debrief questions
  __main__.py  # python -m prototype
  world.py     # state: Player (guard, trust, signals, witnessed), World (day, log);
               # tier_of(), soften(), wound() — the protection formula lives here
  content.py   # ALL text, authored in tier-keyed layers; the thread schedule as data
  render.py    # paragraph wrapping, menus, robust input
  main.py      # the day/slot loop, event firing, epilogue assembly
```

Total on the order of 500–700 lines. The separation matters more than the size: `world.py` is the embryo of the eventual `/sim` package, `content.py` of `/content`, `render.py` of `/engine` — the prototype rehearses the real architecture's boundary (simulation knows nothing about presentation) at throwaway scale.

## Playtest protocol

3–5 testers, none from the project, **told nothing about the Shadow metaphor beforehand**. Facilitator watches silently, then asks:

1. Did you notice something was wrong in Mara's life? When — which signal? *(tests: do the signals read without markers?)*
2. What happened while you weren't looking? *(tests: does the world visibly move without the player?)*
3. When the news about your father came — how did it feel? *(tests: does the protection tradeoff register emotionally, not just numerically?)*
4. Was there anything you suspect you didn't see? *(tests: does surfaced incompleteness create the itch?)*
5. In the conversation where you told Mara what you'd seen — how did the options you were given feel? *(tests: does verb regression read as "a younger me handles this," or just as a locked menu?)*
6. For testers who stayed armored: at any point did you *want* out of that state? *(tests: the anti-turtling pulls — if OPAQUE players sit at high guard feeling fine, the joy-dampening and loneliness writing needs work before anything else does)*
7. Unprompted only — do they connect anything to a person in their own life? *(the pillar-6/emotional-target metric; never ask directly)*

**Pass condition (unchanged from the roadmap gate):** testers notice at least one thread signal unprompted and can describe how the situation changed without their input. **Strong pass:** any tester answers question 7's territory without being asked. **Fail:** testers describe guard as "the stat that makes text longer" — meaning the perception layers read as content-gating, not as *seeing*; rework the writing, not the systems.

## What deliberately isn't in it

No LLM anywhere (nothing procedural to test yet), no relationship graph, no NG+, no second NPC thread, no surfing minigame (the surf verb is one evocative paragraph — the *toy* is a Phase 1 problem). Every one of these was cut because it isn't load-bearing for the core bet, and Phase 0's value is inversely proportional to how long it takes to throw away.
