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

**Finding #3 (first tester, 2026-07-02, on bay.html):** better, but wanted more direct interaction ("mouse clicks on things should make a sound or change how they fly") and more intrigue/aha moments, with the story told in as few words as possible. Fixes applied to bay.html: everything is now clickable with a synthesized sound and a behavioral response (gulls scatter, the tūī flies off and returns, the flame tree sheds, the sea ripples, NPCs raise a hand — but only if you're open; when armored, reaching out gets silence, which is the theme in one interaction). Wordless intrigue added: three faint spirals hidden in the scene — finding all three opens the reserve track even for a guarded player (attention as an alternate path to perception); Mara's bin is a clickable prop whose *sound* is the thread signal; and a small figure sometimes appears at the edge of the screen when you're very open, and is gone the moment you approach. All captions cut to roughly half their length. Design lesson for the full game: interaction grammar should default to "touch it and the world answers, wordlessly" — dialogue is the exception, not the medium.

**Finding #4 (first tester, 2026-07-02, on bay.html):** the balance-only surf mechanic was too basic — reference given was Transworld Surf, "cut right back." Rebuilt as a full-screen ride scene with the real surfing loop: the curl chases you, the pocket is where the power is, carving down the face builds speed, climbing costs it, pumping (rhythmic up/down) is the speed engine, lingering on the lip wipes you out, the whitewater catches you if you stall, and snapping off the top (E above the shoulder line) throws spray and projects you back down the line with speed — true to how a top turn actually works. No score, no meters: stoke is expressed as spray, sound, ride length, and how much the session softens you. Wipeouts are gentle and frequent by design ("The sea shrugs you off"). Tuning lesson logged: the first physics draft made snap conditions (height + speed) mutually exclusive because climbing spent the speed — the fix was making the snap itself regenerate speed, which is also just... how surfing works. Reality is usually the right tuning target.

## Notes for developers

- Fully deterministic — no RNG. Two players who make the same choices see exactly the same ten days; all divergence is choice.
- `world.py` is the embryo of the eventual `/sim` package, `content.py` of `/content`, `render.py` of `/engine`. The boundary rehearsed here (simulation knows nothing about prose; prose contains no logic) is the real architecture's, at throwaway scale.
- Useful smoke tests: `yes 1 | python3 -m prototype` (surf every slot — goes CLEAR, finds nothing about Mara), `yes 5 | python3 -m prototype` (stay in every slot — goes OPAQUE; note the menu shrinks so option 5 *is* "Stay in").
