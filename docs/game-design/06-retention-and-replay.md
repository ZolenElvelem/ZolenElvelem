# Retention & Replay Model

Added after design review. This doc answers "what keeps people coming back?" honestly, by separating two things that usually get conflated: **replaying** (starting over) and **returning** (coming back to a game you're in the middle of, or coming back after finishing). This design is naturally strong at returning, naturally middling at cold replay — like every game in its genre — and has one unusual structural asset that closes the gap.

## The genre truth first

Emotionally-driven narrative games are mostly played once (Disco Elysium, To The Moon, Outer Wilds — whose most common piece of praise is "I wish I could forget it and play it again," the highest compliment in games, from a title with zero replay value). For this genre, the commercially load-bearing metrics are **completion rate and word-of-mouth**, not hours-played. Rule one, therefore: never trade single-playthrough impact for replayability.

## Returning mid-game (session-to-session retention)

The real retention question for a life-sim is what pulls someone back on a Tuesday night. The design's existing rules already are the retention engine:

- **The world moves without you** (pillar 5 / thread lifecycle). An unresolved thread in a town that keeps moving creates a mild, humane urgency no quest log can — "has dad come back to dinner yet?"
- **Rhythm and open loops**: seasons turning, half-finished relationships, a small goal always dangling (the Stardew property). The daily "Living" layer makes the town a place you *check in on*, like a garden.
- **The tactile toy** (surfing) makes checking in intrinsically pleasant even on days when no thread advances.

No new systems are needed for this — it falls out of designs already committed. It just needs to be *protected* during production (e.g., never letting threads freeze while waiting for the player).

## Replay assets, ranked by confidence

1. **Persistent-town New Game+** — the one to bet on. New game ≠ reset town: the next life begins as a different person (naturally, a child born during the previous playthrough) in the town the previous character shaped, where that character is now an NPC, a grave, a story people tell. Replaying isn't repetition; it's *returning somewhere that remembers you*. Nobody else is doing this, and it is dramatically cheaper than the original continuous-generational vision because it's one world-state snapshot handoff per life, not ongoing simulation (see system 7 in `02-core-systems.md`). This is simultaneously the retention model and the theme.
2. **Structural incompleteness.** Perception-gating means one playthrough mathematically cannot see the whole game — a life spent with maxed distrust never saw the threads that only open to trusting characters, and vice versa. Two friends comparing notes and discovering they played *different towns* is a built-in word-of-mouth machine. Requirement: the epilogue must let the player sense the shape of what they missed (one glimpsed scene), because invisible missed content motivates nothing.
3. **Simulation variance.** Template-instantiated threads over simulated NPC state genuinely diverge between runs (the Crusader Kings / RimWorld property). Real, but ranked third: at indie scale the variance will be modest, and overselling it to ourselves leads to under-authoring the fixed content that actually carries the emotion.
4. **The recontextualization replay.** The earned "see the six-year-old in everyone" perception carries into the next life, so a returning player sees the early game completely differently from hour one (the NieR: Automata structure). Costs almost nothing — the perception mode already exists; carrying it is one flag — and converts the twist into a replay motive.

## What not to do

- No extrinsic retention scaffolding: no meta-progression currencies, no unlockable cosmetics, no "see all endings" achievements. The game's whole argument is that accumulation isn't the point; reward scaffolding would poison this design specifically.
- Never gate the theme behind multiple runs. The full emotional arc must land in **one life**. Replay is a deepening for the people who can't leave — never homework for the ones who can.
