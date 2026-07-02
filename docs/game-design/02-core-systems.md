# Core Systems

Each system below is written as: concept → what state it needs → what it produces for the player → open questions to resolve before content is authored at scale. This is the layer between the ChatGPT vision and something a solo/small team can actually build.

---

## 1. Shadow Opacity (the central mechanic)

**Concept (revised — the frozen-age model):** Every character (player and NPC) carries a small set of **capacities** — recommend five: *trust, intimacy, conflict, grief, play* — and each major unprocessed wound **freezes the relevant capacity at the age it happened**. Betrayed at fourteen, and your capacity for trust stays fourteen: a fifty-year-old who handles suspicion with a fourteen-year-old's toolkit. This is real psychology (developmental arrest; in parts-work therapy, parts of the self frozen at the age of the wound with protectors formed around them) and it *is* the game's original metaphor made precise: the six-year-old is simply the deepest frozen part — the original one — with later freezes stacked on top.

A capacity's **Shadow thickness is the gap between chronological age and frozen age**. Freeze trust at fourteen and do nothing, and by fifty that layer is thirty-six years thick — the compounding of deflected pain happens automatically, just by living. The aggregate across capacities drives the visual/audio presentation below; the per-capacity frozen ages drive behavior. To keep authoring bounded, frozen ages snap to a handful of **age bands** (6, 10, 14, 17, adult), giving a content matrix (5 capacities × 5 bands) a small team can actually write.

**How a frozen capacity manifests — verbs, not numbers:** in any situation that touches a frozen domain, the player's *available actions and dialogue options regress to that age's vocabulary*. An adult's options in a work conversation; a twelve-year-old's — deflect, sulk, explode, flee — in a conflict with your father. The player feels the arrest from the inside ("why do I always act like a kid around him?") without a single stat shown. **Hard rule: the lock is never UI.** No meters, no "Trust: age 14" — the moment it's a visible stat it becomes something to optimize and the humanity dies. It lives entirely in which verbs appear and how scenes play; the player infers it, and the inferring is the game teaching self-awareness.

**Drives, mechanically:**
- Color grading LUT blend (muted ↔ vibrant)
- Ambient sound layer count/richness (fewer birds/waves/distant voices ↔ full soundscape)
- Wildlife spawn density
- NPC disposition bias (thicker shadow → NPCs read as more guarded/hostile by default, independent of their actual state — this is the "your perception, not the world, changed" promise)
- **Opportunity visibility**: some interactables/threads are not merely locked but literally not rendered/hinted below a translucency threshold. This must be a rendering-layer decision (an object doesn't spawn or its interaction prompt doesn't fire), not a UI grey-out — the promise is "the world hasn't changed, your perception has," so hidden things must be *actually* hidden, not disabled-and-visible.

**Healing — the memory-reprocessing loop:** unfreezing a capacity is not talk, and never a single dialogue choice. The mechanic is **going back to the moment it froze** — a readiness-gated, lighter version of the memory-revisiting verb (system 4), available all game, mirroring how trauma reprocessing actually works. The loop: present-day safety (trust built, presence accumulated, honesty risked) earns the *readiness* to face a memory → facing it unfreezes the capacity → the capacity starts growing again → deepened present relationships earn readiness for the next, older, deeper memory. Crucially, **healing resumes growth, it does not teleport**: an unfrozen fourteen-year-old trust doesn't snap to your current age — it grows from fourteen, through lived use. Heal at thirty and you get decades to grow into it; heal at sixty and it's still worth it, but you feel what the waiting cost. And per pillar 2: **some wounds never fully unfreeze** — a few only ever get lighter. Processing is not a checklist the game lets you complete, and the design must never accidentally argue that it is. The six-year-old is the deepest memory of all — the last one you become ready for, which is why the endgame was always going to be there.

**The tradeoff: the Shadow protects (load-bearing design decision).** A thick Shadow must confer real mechanical benefit, not just impairment — otherwise translucency is strictly better and the whole mechanic degrades into a debuff players min-max away, with the systems contradicting pillar 2. Concretely: incoming wound events are *blunted* in proportion to current opacity (an armored character absorbs a loss that would devastate an open one; e.g. `felt_wound = base_wound × (1 − k × opacity)` with k around 0.5–0.7, to be tuned in Phase 0), and certain hard situations — confrontations, funerals, enduring a bad stretch — are more survivable while guarded. Translucency means feeling *everything* at full volume: richer world, deeper connection, and losses that land undampened. Opening up is therefore always a genuine wager, never a free upgrade. This single rule is what turns the metaphor into a game.

**Numbness is not selective — the blunting dampens joy at the same rate.** The protection formula applies to *everything felt*, not just wounds: your daughter's wedding, your kid's first wave, the sunset after the southerly clears all arrive "at a distance, like weather offshore," exactly like the bad news. This is not a penalty the game imposes; it is the honest property of numbness — you cannot selectively numb. Played out over hours, high opacity isn't safety, it's a gray half-life, and the player lowers their guard not because armor was punished but because they start to *miss being alive*.

**What pulls the player toward openness (the anti-turtling design):** players are loss-averse, and a wound landing at full force is vivid while dampened joy is an absence — so the pull side must be engineered, not assumed. Four pulls, all already in the design, all to be validated in Phase 0: (1) *joy-dampening* above; (2) *the age-gap sediment* — armor is a loan against the future, optimal this week and compounding for a decade, arriving at sixty with a Shadow so thick the world has gone nearly silent; (3) *curiosity* — the mystery, the hidden paths, and the threads live behind perception, so the armored playthrough is a visibly smaller game; (4) *connection* — NPCs respond to openness with intimacy, confidence, and love, while the armored player gets functional service and quiet evenings where nobody drops by. Narrative reinforcement at zero cost: the town contains the player's possible futures, walking around — the perfectly safe old man at the end of the bar who feels nothing and is utterly alone; the repeatedly-hurt open woman who is somehow the most alive person in town. No dialogue about it.

**The real skill is modulation, not minimization.** The game never asks the player to remove the Shadow — there should be moments where raising the guard is *correct* (getting through the funeral, standing in front of the person screaming at you, surviving the bad year). Neither state is a penalty; misreading which one the moment calls for is. That is the skill the game teaches, and the same skill it's quietly arguing for in life.

**Open questions to lock before content production:**
- Is `shadow_density` per-category visible to the player at all (a subtle UI), or fully implicit or fully hidden and only inferable, in keeping with "no stat screens"? Recommendation: hidden entirely for the first prototype; a diegetic mirror/journal reflection mechanic can surface it later instead of a UI meter.
- What's the minimum event weight to move the needle — i.e., how many written "wound" and "healing" events are needed before Phase 2 content lock (see roadmap)?

---

## 2. Living (the open simulation layer)

**Concept:** A schedule/needs simulation the player exists inside rather than "plays" in the quest sense — job, hobby (surf/fish/etc.), sleep, relationships, aging. This is the connective tissue between emergent threads and the meta-mystery; without it those systems are just a quest list with better prose.

**State needed:** a day/season/year clock with a defined time-compression rule (recommend: 1 real-time hour ≈ 1 in-game day for "Living" scenes, with explicit sleep/skip-ahead to compress downtime — do not simulate every day 1:1 or content production becomes impossible for a small team).

**Aging:** player and NPCs move through defined life-stage bands (child/teen/adult/elder) that swap character models, voice ranges, and available actions, not a continuous morph — cheaper to build and easier to make legible to the player.

**The tactile toy (added after design review):** one physical activity — surfing, given the setting — must be built as a genuinely fun toy with *no rewards attached*, because a contemplative game lives or dies on whether simply existing in the town is pleasant for hours between the emotional beats. Curiosity carries the hours; the toy carries the minutes. It's also a free thematic channel: board feel, water rendering, and audio can all be modulated by Shadow opacity without a word of dialogue. This is a first-class deliverable of the Phase 1 technical prototype, not polish for later.

**Playing the wounds, not just carrying them:** each life *starts at six*. The player is present when the first layers of Shadow form — they experience the moment the armor became necessary, rather than reading it as backstory. This makes the childhood arc the emotional load-bearing wall of the whole life, not a tutorial.

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

**Two constraints added after design review:**

- **Not monocausal.** The "people meet only each other's Shadows" cause chain applies to the *avoidable* tragedies — the estrangements, the betrayals, the slow abandonments. Some griefs in the town must be genuinely blameless (illness, storm, accident), with no lesson attached. A world where every sorrow traces to the one cause reads as authored sermon even without preachy dialogue; against a backdrop of real randomness, the avoidable tragedies become the devastating category, which is exactly the point.
- **"One consciousness" stays unconfirmed.** Of the three original mystery candidates, this is the one that tips into new-age territory if ever asserted. The Forgotten Promise is the plot mechanism; Shadow-as-exhausted-love is the personal payoff; the one-consciousness reading remains something an attentive player can construct and the game never confirms or denies. Ambiguity is what keeps people arguing about a game for years.

**Clue delivery:** dreams, songs, children's drawings, recurring symbols scattered across eras. These should be *diegetic and skippable* — nothing the player needs a wiki to find, but nothing that interrupts a player who's not pursuing it either.

**The endgame verb (decided): memory revisiting — now also the all-game healing loop.** "Realization" needs a verb, not a cutscene. Memory revisiting exists in two registers. *All game long*, a readiness-gated version is the healing mechanic itself (system 1): going back to the moment a capacity froze is how it unfreezes. *Late game*, when the "see the six-year-old in everyone" perception unlocks, the same verb turns outward and retrospective: the player can re-enter scenes they already played — the argument, the betrayal, the schoolyard — and watch them again through the new perception: same scene, same events, and now the terrified child inside the person who hurt you is visible, and you can see exactly how old the part of them doing the shouting is. The realization is delivered as gameplay, and it only works because the player has years of first-hand scenes banked. The whole game is the staircase down to the six-year-old; the endgame is the bottom step. Technical note: this requires scenes to be replayable from the event log from day one — flag key scenes for capture during Phase 2, not retrofitted in Phase 4.

**Engineered "it was always there" moments.** Opacity-gated invisibility only teaches the player anything if they eventually *learn* things were hidden — otherwise hidden content is indistinguishable from content that doesn't exist. At least one designed moment must exist where new translucency reveals something on a path the player has walked dozens of times. That single moment retroactively re-frames the entire world and teaches the player to re-see everything. Build one such moment into the Phase 1 prototype and one into the vertical slice.

---

## 5. Procedural NPC AI — the tradeoff

This is the highest-risk, highest-cost system in the whole design, and it deserves an explicit tradeoff rather than a default choice.

### NPCs share the frozen-age skeleton (added after design review)
"NPCs have fears, hopes, regrets" is too vague to simulate. The frozen-age model (system 1) gives every NPC the same generative structure as the player at almost no cost: **two or three frozen capacities with ages** ("the mechanic's conflict-handling froze at nine; the widow's intimacy froze at twenty-three") produce specific, consistent, *explainable* behavior from a dict-sized state. It also conditions LLM text generation beautifully and cheaply — "write this fifty-year-old's response to criticism as handled by his nine-year-old self" is a prompt that produces characterful, non-generic dialogue from a tiny state snapshot. This replaces most of the hand-tuned "drives" design work below with something both simpler and truer.

### Option A — Simulated state + LLM for text only (recommended default)
NPCs run on a deterministic core: a memory list, a relationship graph (who they trust/resent/love and why, with decay), a small set of drives (safety, belonging, purpose, autonomy), and the frozen-age capacity set like the player's. Decisions ("does this NPC visit their father this week") come from simple utility scoring over that state — cheap, fast, fully deterministic, fully debuggable, and works for hundreds of background NPCs simulated over decades without per-tick API calls. An LLM is called *only* to turn a snapshot of that state into flavor text — a line of dialogue, a diary entry, a rumor overheard at the pub — generated in batches, cached, and reviewable/editable by hand, not on a real-time critical path.

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

## 7. Death, the Epilogue & Persistent-Town New Game+ (revised scope)

**v1 scope decision:** one complete life is the game. Death is the ending — there is still no game-over screen, but "the world continues without you" is delivered as an **epilogue**, not a respawn: the town years later, someone retelling something you did, a place you shaped. Feeling the continuation may be more powerful than consuming it. The epilogue is also where **structural incompleteness is surfaced** — a glimpse of the shape of what this life never saw (a scene from a thread that was invisible to this character's wound profile), because missed content only motivates a return if the player can sense it exists.

**Persistent-town New Game+ (the retention model, kept from the generational vision at a fraction of its cost):** starting a new game does *not* reset the town. The player begins as a different person — most naturally a child who was born during the previous playthrough — in the town the previous character shaped, where that character now exists as an NPC, a grave, a story people tell. Replaying isn't repetition; it's returning somewhere that remembers you. Mechanically this is a **single world-state snapshot handoff** at the end of a life (the event log, family records, and NPC states, aged forward), not continuous multi-generation simulation — which is what makes it affordable where full generational play is not. Full continuous generational simulation (the original vision) is deferred to post-v1 / expansion, and loses nothing by the deferral because the SQLite event-log architecture supports it from day one.

**Inherited Shadow:** the NG+ character's starting `shadow_density` vector is partly shaped by what the previous character did (a parent who was present lowers a child's starting wounds in specific categories; one who wasn't raises them) — this is what makes cross-life play feel causally connected rather than cosmetic.

**Late-game unlock carries forward:** "seeing the six-year-old in everyone" (system 4) generalizes under the frozen-age model into **seeing the frozen ages in everyone** — looking at the furious man at the bar and seeing exactly how old the part of him doing the shouting is. Once earned, it persists into the NG+ life — a returning player sees the early game through the earned perception from hour one, converting the game's least-replayable asset (the reveal) into its recontextualization-replay motive. See `06-retention-and-replay.md`.
