# Core Systems

Each system below is written as: concept → what state it needs → what it produces for the player → open questions to resolve before content is authored at scale. This is the layer between the ChatGPT vision and something a solo/small team can actually build.

---

## 1. Shadow Opacity (the central mechanic)

**Concept:** Every character (player and NPC) has a hidden `shadow_density` value, roughly 0.0 (fully translucent) to 1.0 (fully opaque). It is not a single global number — it's a small vector of *wound categories* (e.g. `distrust`, `isolation`, `cynicism`, `grief`) that individually rise from specific life events and individually soften through specific healing events. The number the player *feels* is a weighted aggregate of that vector, not a single dial an event moves directly.

**Drives, mechanically:**
- Color grading LUT blend (muted ↔ vibrant)
- Ambient sound layer count/richness (fewer birds/waves/distant voices ↔ full soundscape)
- Wildlife spawn density
- NPC disposition bias (thicker shadow → NPCs read as more guarded/hostile by default, independent of their actual state — this is the "your perception, not the world, changed" promise)
- **Opportunity visibility**: some interactables/threads are not merely locked but literally not rendered/hinted below a translucency threshold. This must be a rendering-layer decision (an object doesn't spawn or its interaction prompt doesn't fire), not a UI grey-out — the promise is "the world hasn't changed, your perception has," so hidden things must be *actually* hidden, not disabled-and-visible.

**Softens through:** vulnerability moments, sustained presence with another character, honesty at a cost, grief processed (not avoided), reconciliation. Explicitly: softening is never a single dialogue choice with an instant payoff — model it as an exponential decay applied over multiple qualifying interactions, so healing reads as gradual, matching the design pillar that the Shadow is never removed, only made transparent.

**Open questions to lock before content production:**
- Is `shadow_density` per-category visible to the player at all (a subtle UI), or fully implicit or fully hidden and only inferable, in keeping with "no stat screens"? Recommendation: hidden entirely for the first prototype; a diegetic mirror/journal reflection mechanic can surface it later instead of a UI meter.
- What's the minimum event weight to move the needle — i.e., how many written "wound" and "healing" events are needed before Phase 2 content lock (see roadmap)?

---

## 2. Living (the open simulation layer)

**Concept:** A schedule/needs simulation the player exists inside rather than "plays" in the quest sense — job, hobby (surf/fish/etc.), sleep, relationships, aging. This is the connective tissue between emergent threads and the meta-mystery; without it those systems are just a quest list with better prose.

**State needed:** a day/season/year clock with a defined time-compression rule (recommend: 1 real-time hour ≈ 1 in-game day for "Living" scenes, with explicit sleep/skip-ahead to compress downtime — do not simulate every day 1:1 or content production becomes impossible for a small team).

**Aging:** player and NPCs move through defined life-stage bands (child/teen/adult/elder) that swap character models, voice ranges, and available actions, not a continuous morph — cheaper to build and easier to make legible to the player.

**Open question:** what is the *smallest* set of "Living" verbs that still makes the town feel alive (recommend starting with 4: work, socialize, pursue-a-hobby, rest) — resist the urge to build a full life-sim verb set before Phase 2.

---

## 3. Emergent Story Threads

**Concept:** The world presents situations, never quest markers. A thread has a lifecycle: `dormant → noticeable → noticed → (investigated | ignored) → resolved → memorialized`.

- **Noticeable** is gated by the player's own Shadow opacity in the *relevant category* — a player deep in isolation may simply not notice a friend's drinking starting, because withdrawn people stop noticing withdrawal in others. This is the single mechanic that ties system 1 and system 3 together and should be the first thing prototyped (see roadmap Phase 1).
- **Ignored threads must still resolve.** Author every thread with a default "world moves on without you" outcome, not a frozen state. This is non-negotiable for the "the world doesn't wait for you" pillar and is also what makes replay-as-a-descendant meaningful.
- **Memorialized**: resolved threads write a compact record into the world event log (see system 6) so they can be referenced by NPC dialogue and by descendants' stories.

**Authoring at scale (the real risk for a solo dev):** don't hand-write every thread as a bespoke script. Build a small number of **thread templates** (parameterized patterns — e.g. "a family member withdraws," "a business fails," "a child hides something") that get instantiated against different NPCs/locations/eras with different specifics pulled from that NPC's simulated state. Hand-author only the handful of threads that carry the meta-mystery; procedurally instantiate the rest. This is the difference between a buildable game and an unbounded writing commitment.

---

## 4. The Meta-Mystery

**Recommendation: merge the three candidate mysteries into one throughline** rather than picking one — they're not actually competing ideas, they're three altitudes of the same idea:

- *Everyone is one consciousness* is the metaphysical framing.
- *The Forgotten Promise* is the in-fiction mystery/plot mechanism (what the player is actually doing turn to turn: gathering dreams, songs, drawings, symbols).
- *The Shadow was never the enemy* is the personal, first-person payoff.
- Your own follow-up idea — **people forgot how to see each other's six-year-old selves, and every tragedy in the game traces back to that** — is the causal engine that ties all of the above together and should be treated as the spine, not an addendum. Concretely: every major authored tragedy in the town's history (not just the player's threads) should have, buried in its cause chain, a moment where two people met only each other's Shadows.

**Clue delivery:** dreams, songs, children's drawings, recurring symbols scattered across eras. These should be *diegetic and skippable* — nothing the player needs a wiki to find, but nothing that interrupts a player who's not pursuing it either.

**Open question:** what is the actual endgame *action*, mechanically? "Realization" needs a verb, not just a cutscene. Candidate: the "seeing the six-year-old in everyone" ability (system 7 below) becomes literally playable — the mystery's resolution is unlocking a permanent perception mode, not a cutscene reveal.

---

## 5. Procedural NPC AI — the tradeoff

This is the highest-risk, highest-cost system in the whole design, and it deserves an explicit tradeoff rather than a default choice.

### Option A — Simulated state + LLM for text only (recommended default)
NPCs run on a deterministic core: a memory list, a relationship graph (who they trust/resent/love and why, with decay), a small set of drives (safety, belonging, purpose, autonomy), and a `shadow_density` vector like the player's. Decisions ("does this NPC visit their father this week") come from simple utility scoring over that state — cheap, fast, fully deterministic, fully debuggable, and works for hundreds of background NPCs simulated over decades without per-tick API calls. An LLM is called *only* to turn a snapshot of that state into flavor text — a line of dialogue, a diary entry, a rumor overheard at the pub — generated in batches, cached, and reviewable/editable by hand, not on a real-time critical path.

- **Pros:** affordable at scale, replayable saves (same state → same outcome), no live-service dependency at runtime for anyone who doesn't want one, easy to hand-tune.
- **Cons:** emergent behavior is bounded by however good your utility model is; it can feel "systemic" rather than "alive" if under-designed.

### Option B — Full LLM-driven NPC reasoning
Each NPC's decisions are themselves produced by an LLM call reasoning over its memory/relationships each tick.

- **Pros:** highest ceiling for genuinely surprising, individuated behavior; less hand-authored utility-function tuning.
- **Cons:** cost and latency scale with NPC count × simulated years — prohibitive for "hundreds of NPCs over decades" at indie budget; harder to keep long-run consistent (an LLM can contradict an NPC's own established history); much harder to make saves replayable/deterministic, which matters for a game whose core promise is "the town remembers" accurately.

### Recommended hybrid
Use Option A as the simulation core for the entire town. Reserve a small allow-list of **"deep NPCs"** (a dozen or so named, story-critical characters) for an upgraded path where an LLM *does* reason over their state for key authored beats — this keeps the expensive, harder-to-control technique scoped to where its ceiling actually matters, instead of applying it uniformly.

**Open question to resolve before Phase 2:** what's the utility-function feature set for Option A (which drives/memories actually move the needle on an NPC's visible behavior)? This needs to be designed and playtested before any AI-text pipeline work starts — text generation is worthless on top of an unconvincing simulation.

---

## 6. Generational World & Persistence

**Concept:** Time genuinely passes; the world is a persistent event log ("who did what to whom, when, where"), not a state that resets. Background NPC history (for characters the player never directly touches) can be generated procedurally at world-seed time using the same thread-template system as system 3, so the town has a plausible history on day one without hand-authoring decades of filler.

**Family trees:** every NPC belongs to a family record (parents, siblings, children, spouse) that the aging system (system 2) advances over time — children born in-fiction eventually become playable via the death/transition mechanic (system 7).

**What must exist before Phase 3:** a query-able event log format that both (a) authored dialogue can reference ("your grandfather used to sit on that bench too") and (b) the thread-template system can read from to avoid contradictions.

---

## 7. Death & Transition

**Concept:** On a character's death, the player is offered a next character from the persistent town — a direct descendant, an unrelated townsperson whose story intersected theirs, or (rarer, later-game) someone entirely new arriving in town. There is no game-over screen.

**Mechanical requirement:** the new character's starting `shadow_density` vector should be partly inherited/environmentally shaped by what the *previous* character did (a parent who was present lowers a child's starting wounds in specific categories; one who wasn't raises them) — this is what makes multi-life play feel causally connected rather than cosmetic.

**Late-game unlock:** "seeing the six-year-old in everyone" (referenced in system 4) should be a perception mode tied to a late character's accumulated translucency, carried forward — once earned, it persists across the transition into the next life, so its meaning compounds rather than resetting each death.
