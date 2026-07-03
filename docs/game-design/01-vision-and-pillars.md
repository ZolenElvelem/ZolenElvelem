# Vision & Design Pillars

## The Pitch

A generational life-simulation set in one small New Zealand coastal town, played across decades and multiple lives. The player does not level up — they accumulate experiences that make an inherited "Shadow" (the adult self, formed by pain and protection) either more opaque or more translucent. The entire world — color, sound, wildlife, which opportunities are even visible — is rendered through that opacity. There is no combat, no game over, and no villain. The mystery underneath everyday life is not "what happened" but "why" — and the answer, arrived at slowly through decades of relationships, is that people stopped seeing each other's six-year-old selves and only ever meet each other's armor.

## Design Pillars

These are the filters every feature must pass. If a proposed feature doesn't serve at least one of these, cut it.

1. **Perception is the mechanic, not a skill tree.** The player's only "stat" that matters is how clearly they see — themselves and others. Every system (visuals, audio, quest visibility, dialogue options, NPC behavior toward the player) is a function of Shadow opacity, not of gear or XP.
2. **The Shadow is not the enemy — so it must be mechanically worth having.** It is never framed as something to defeat, min-max away, or "cleanse" in a single climactic choice. Healing makes it translucent, never absent. Design corollary: there is no final boss fight against your own Shadow. The climax is a *recognition*, not a battle. Crucially, this pillar has a systems requirement, not just a tonal one: a thick Shadow must genuinely *protect* — blunting the impact of new wounds, letting a character function through grief that would flatten an open one — while translucency means feeling everything at full volume, the beauty *and* the losses. If translucency is strictly better, opacity is just a debuff, healing collapses into min-maxing, and the systems contradict the theme. The player must face a real human tradeoff, not a stat to optimize. And the blunting is not selective: protection dampens joy at exactly the same rate as pain — you cannot selectively numb — so the armored life is a gray half-life, and the pull toward openness is missing being alive, not avoiding a penalty.
3. **No game over, only continuation.** Death hands the player a new character in the same persistent town. This is a structural commitment, not a narrative flourish — it must shape the save system, the world model, and the pacing of every arc from day one.
4. **The town remembers.** Every choice a player makes should be capable of resurfacing, unprompted, in a descendant's or stranger's story a generation later. If the world can't recall it, don't let the player do it as a "meaningful choice."
5. **Understanding over completion.** Emergent threads are noticed, not quest-logged. The correct player skill is attention, not backtracking to a marker. Threads that go uninvestigated must resolve on their own and leave a visible trace — the world moves without the player.
6. **Show the theme, never say it.** The "everyone is someone's six-year-old" thesis must be delivered entirely through mechanics and emergent scenes. No NPC should ever explain the metaphor aloud. This is the single biggest risk to the project's credibility (see `05-risks-and-scope-control.md`) and needs to be treated as a hard constraint on writing, not a nice-to-have. Two structural corollaries: not every tragedy in the town may trace back to the central cause — some griefs must be blameless (the boat that just sank, the illness that just came), because a monocausal world reads as a sermon even with zero preachy dialogue, and the theme lands harder against genuine randomness. And the "everyone is one consciousness" reading stays *unconfirmed* — something an attentive player can construct, never something the game asserts as lore.
7. **The first hour must work for a player who will never finish the game.** The emotional payoff is structurally backloaded — years of relationships before the reveal — so the opening has to be charming, tactile, and quietly mysterious entirely on its own merits, before the player has any reason to care about the thesis. Games in this genre die in the first hour, not the last. If the first hour is homework, nobody reaches the cathedral.

## What this game is *not*

- Not an RPG progression loop (no XP, no gear score, no skill trees).
- Not a morality-meter game (no karma bar telling the player if they were "good").
- Not a combat game. Conflict is emotional/social, resolved through presence, attention, or absence — never through a fight system.
- Not a multi-generation epic in version one. The v1 arc is **one complete life** — roughly age six to death, one town, several decades — which contains the full thesis: wounds, armor, integration, the perception unlock, death without a game-over screen. The town persists *across* lives (see `06-retention-and-replay.md` for the persistent-town New Game+ model), but continuous generational simulation is deferred to post-v1.

## The emotional target (how you'll know it's working)

Playtests succeed when a player, unprompted, starts talking about someone in their *own* life differently after a session — not when they praise the plot twist. Track this explicitly in playtesting (see roadmap milestone gates). If testers only talk about mechanics or story cleverness, the theme isn't landing yet, regardless of how technically complete the build is.
