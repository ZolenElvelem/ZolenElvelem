"""The day/slot loop, scheduled events, and epilogue assembly."""

from . import content
from .render import ask, rule, say
from .world import DAYS, NAME_TRUST, TRUST_NEEDED, Player, Tier, World


def pick(variants: dict, tier: Tier):
    """Select the entry for a tier, falling back toward OPAQUE."""
    for t in range(tier, Tier.OPAQUE + 1):
        if Tier(t) in variants:
            return variants[Tier(t)]
    return variants[min(variants)]


def rotate(seq: list, n: int) -> str:
    """Cycle deterministically through authored variants."""
    return seq[n % len(seq)]


# ── actions ──────────────────────────────────────────────────────────

def do_surf(p: Player, w: World) -> None:
    say(rotate(pick(content.SURF, p.tier), w.use("surf")))
    p.soften(0.05)


def do_pub(p: Player, w: World) -> None:
    say(rotate(pick(content.PUB, p.tier), w.use("pub")))
    if w.day >= 5 and p.tier <= Tier.TRANSLUCENT and "pub_word" not in p.signals:
        say(content.PUB_WORD)
        p.signals.add("pub_word")
    p.soften(0.02)


def do_bench(p: Player, w: World) -> None:
    say(rotate(pick(content.BENCH, p.tier), w.use("bench")))
    p.soften(0.04)


def do_reserve(p: Player, w: World) -> None:
    say(content.RESERVE)
    p.witnessed.add("carving")
    p.soften(0.03)


def do_stay_in(p: Player, w: World) -> None:
    say(rotate(content.STAY_IN, w.use("stay_in")))
    p.harden(0.02)


def do_visit_mara(p: Player, w: World) -> None:
    if p.last_visit_day != w.day:
        p.last_visit_day = w.day
        p.trust += 1

    if p.named_it:
        say(rotate(content.MARA_NAMED, w.use("mara_named")))
        p.soften(0.01)
        return

    say(rotate(pick(content.MARA_PLAIN, p.tier), w.use("mara_plain")))

    if w.day >= 3 and p.tier <= Tier.TRANSLUCENT and "empties" not in p.signals:
        say(content.MARA_EMPTIES)
        p.signals.add("empties")

    if p.signals:
        say(content.REGRESSED_INTRO)
        options = list(content.REGRESSED_OPTIONS)
        if p.trust >= NAME_TRUST:
            options.append(content.NAME_IT_OPTION)
        choice = ask("What do you do?", options)
        if choice < len(content.REGRESSED_OUTCOMES):
            say(content.REGRESSED_OUTCOMES[choice])
            p.harden(0.01)
        else:
            say(content.NAME_IT)
            p.named_it = True
            p.trust += 1
            p.soften(0.06)
    else:
        p.soften(0.01)


ACTIONS = [
    ("Paddle out", do_surf),
    ("The pub", do_pub),
    ("Call in on Mara", do_visit_mara),
    ("The bench above the point", do_bench),
    ("Follow the tūī calls up into the reserve", do_reserve),  # CLEAR only
    ("Stay in", do_stay_in),
]


def available_actions(p: Player) -> list:
    acts = []
    for label, fn in ACTIONS:
        if fn is do_reserve and p.tier != Tier.CLEAR:
            continue
        acts.append((label, fn))
    return acts


# ── scheduled events ─────────────────────────────────────────────────

def day_events(p: Player, w: World) -> None:
    if w.day == 2:
        say(content.DINNER_FACT)
        if p.tier <= Tier.TRANSLUCENT:
            say(content.DINNER_SIGNIFICANCE)
            p.signals.add("dinner")
    elif w.day == 6:
        say(content.FATHER_FACT)
        w.father_tier = p.tier
        w.father_felt = p.wound(0.20)
        say(pick(content.FATHER, w.father_tier))
    elif w.day == 8:
        say(content.MISSED_WORK_FACT)
        say(pick(content.MISSED_WORK, p.tier))
        p.signals.add("missed_work")
    elif w.day == 10:
        say(content.OUTCOME_HELPED if w.mara_helped else content.OUTCOME_ALONE)


def end_of_day(p: Player, w: World) -> None:
    if w.day == 9:
        w.mara_helped = p.named_it and p.trust >= TRUST_NEEDED
        w.resolved = True


# ── epilogue ─────────────────────────────────────────────────────────

def epilogue(p: Player, w: World) -> None:
    rule("ten days later, looking back")

    if w.mara_helped:
        say("""
Mara goes on Thursdays now. Sometimes you drive her, sometimes she goes
alone, and once — one time — she asked you to come in. Nothing about her
is fixed. Everything about her is trying, out loud, where people can
see. It turns out that was the whole ask: one person who wouldn't
pretend.
""")
    else:
        say("""
Mara's shop reopened after a week, and the bay has moved on to newer
weather, the way it does. She waves when she sees you. The wave is fine.
The wave is exactly, carefully fine, and you both know what lives on
the other side of it now.
""")

    say(pick(content.EPILOGUE_FATHER, w.father_tier))

    unseen = [k for k in ("dinner", "empties", "pub_word") if k not in p.signals]
    if "carving" not in p.witnessed:
        unseen.append("carving")
    if unseen:
        rule("what you never saw")
        for key in unseen:
            say(content.MISSED[key])

    guarded_slots = w.tier_time[Tier.OPAQUE]
    open_slots = w.tier_time[Tier.CLEAR]
    total = sum(w.tier_time.values()) or 1
    if guarded_slots / total > 0.5:
        say("You spent most of these ten days behind thick glass. The town was out there the whole time.")
    elif open_slots / total > 0.5:
        say("You spent most of these ten days wide open. It cost you full price, and it paid full price.")

    say(content.EPILOGUE_CLOSE)
    rule("end of prototype")
    say("(Facilitators: debrief questions are in prototype/README.md.)")


# ── main loop ────────────────────────────────────────────────────────

def run() -> None:
    p, w = Player(), World()
    rule("kōtuku bay — phase 0 prototype")
    say(content.INTRO)

    for day in range(1, DAYS + 1):
        w.day = day
        rule(f"day {day} — {content.WEATHER[day - 1]}")
        day_events(p, w)
        for slot in ("morning", "afternoon"):
            w.tier_time[p.tier] += 1
            if slot == "morning":
                say(rotate(pick(content.AMBIENT, p.tier), w.day - 1))
            acts = available_actions(p)
            labels = [label for label, _ in acts]
            choice = ask(f"({slot}) What do you do?", labels)
            acts[choice][1](p, w)
        end_of_day(p, w)

    epilogue(p, w)
