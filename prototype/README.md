# Kōtuku Bay — Phase 0 Prototype

The playable implementation of `docs/game-design/07-phase0-prototype-spec.md`: ten days in a small NZ coastal town, one NPC thread, one wound event, one hidden discovery. A session runs 10–20 minutes. Pure Python, standard library only, no dependencies.

## Run it

```
python3 -m prototype
```

(Run from the repository root. Python 3.8+.)

**Browser version:** open `prototype/web/index.html` — the same game as a single self-contained HTML file, click-to-choose, no server or dependencies. Easiest way to hand it to playtesters; the page tint also shifts subtly with the perception tier (the visual mechanic in miniature). The Python version remains the reference implementation; if the two diverge, the Python one wins.

**Phase 1 preview sketch:** open `prototype/web/bay.html` — a playable 2D canvas scene (procedural art, synthesized audio, no assets) built in response to playtest finding #2: the text format itself was the barrier for some testers. Walk the bay, surf, sit on the bench, knock on doors; color saturation, birdlife, NPC liveliness, ambient sound layers, and the vignette all track your hidden state in real time, and the reserve track is literally not rendered until you're open enough. It demonstrates the perception-rendering pipeline and the toy — it does *not* carry the story or the thread system (that's what the text prototype tests). Ninety seconds to two minutes.

## What it is testing

The project's core bet: **can modulating what a player perceives — rather than what they can do — carry emotional weight?** Everything in the game is filtered through a single hidden value (`guard`, the thickness of one Shadow layer: the character's trust, frozen at fourteen). It rises and falls with how you spend your days. It is never shown.

Five rules under test (see the spec for detail):

1. **Perception gating** — descriptions, thread signals, and menu options themselves are filtered by guard. Some options simply don't exist for a guarded player.
2. **The Shadow protects, and numbness isn't selective** — the one wound event lands blunted in proportion to guard; so do the good moments.
3. **Verbs regress in the frozen domain** — in the scene that touches the frozen capacity, the menu initially offers only a fourteen-year-old's moves.
4. **Healing is gradual** — the adult option is earned through presence across days, and never pays off instantly.
5. **The world moves without you** — the thread resolves either way at the end of day 9.

## Facilitator protocol

3–5 testers, none from the project, **told nothing about the Shadow metaphor beforehand**. Ask them to choose honestly, not tactically. Watch silently. Then ask, in order:

1. Did you notice something was wrong in Mara's life? When — which moment tipped you off? *(do the signals read without quest markers?)*
2. What happened while you weren't looking? *(does the world visibly move without the player?)*
3. When the news about your father came — how did it feel? *(does the protection tradeoff register emotionally, not just numerically?)*
4. Was there anything you suspect you didn't see? *(does surfaced incompleteness create the itch?)*
5. In the conversation where you told Mara what you'd seen (if they did) — how did the options you were given feel? *(does verb regression read as "a younger me handles this," or just as a locked menu?)*
6. For testers who stayed guarded: at any point did you *want* out of that state? *(the anti-turtling pulls — if guarded players feel fine, the joy-dampening and loneliness writing needs work first)*
7. Never ask directly — note only if it happens unprompted: do they connect anything to a person in their own life? *(the emotional-target metric)*

**Pass:** testers notice at least one thread signal unprompted and can describe how the situation changed without their input.
**Strong pass:** anything in question 7's territory, unprompted.
**Fail:** testers describe the hidden value as "the stat that makes text longer" — the perception layers are reading as content-gating, not as *seeing*. Rework the writing, not the systems.

## Playtest log

**Finding #1 (first tester, 2026-07-02):** verbatim repetition of ambient/action prose read as emptiness and made the format itself hard to see past — "got sick of" the identical tūī paragraph. Diagnosis: repetition of *register* is the design (a closed player's world should keep feeling flat), but repetition of *sentences* is a bug — it reads as "the game has no content" rather than "your perception is static." Fix applied: prose is now authored in variant lists per tier, rotated deterministically (ambient by day, morning only; action scenes by use-count). Implication for the full game: perception tiers need surface variety at constant emotional register, at volumes a small team can't hand-author — this is precisely the batched-LLM text layer's job (`03-technical-architecture.md`), and the tester independently arrived at the same conclusion. Second implication, already in the plan: text has no toy — the minutes drag without one (pillar 7); Phase 1's surf toy exists for exactly this.

## Notes for developers

- Fully deterministic — no RNG. Two players who make the same choices see exactly the same ten days; all divergence is choice.
- `world.py` is the embryo of the eventual `/sim` package, `content.py` of `/content`, `render.py` of `/engine`. The boundary rehearsed here (simulation knows nothing about prose; prose contains no logic) is the real architecture's, at throwaway scale.
- Useful smoke tests: `yes 1 | python3 -m prototype` (surf every slot — goes CLEAR, finds nothing about Mara), `yes 5 | python3 -m prototype` (stay in every slot — goes OPAQUE; note the menu shrinks so option 5 *is* "Stay in").
