"""Simulation state for the Phase 0 prototype.

One player, one frozen capacity (trust, frozen at fourteen — `guard` is
how thick that layer has grown since), one NPC thread (Mara), ten days.

The rules this file exists to prove (see docs/game-design/07):

1. Perception is a function of guard: text and menu options are filtered
   by tier, so a guarded player literally reads a different town.
2. The Shadow protects — and numbness isn't selective: wounds are
   blunted in proportion to guard (PROTECTION), and so is joy (the
   content layer handles that side).
3. Verbs regress in the frozen domain: the naming scene offers a
   fourteen-year-old's moves until presence is earned.
4. Healing is gradual: presence accumulates one visit-day at a time.
5. The world moves without you: the thread resolves either way.
"""

from dataclasses import dataclass, field
from enum import IntEnum


class Tier(IntEnum):
    CLEAR = 0        # guard < 0.35 — you feel everything, both directions
    TRANSLUCENT = 1  # 0.35 <= guard < 0.65 — an ordinary adult
    OPAQUE = 2       # guard >= 0.65 — protected, and blind


def tier_of(guard: float) -> Tier:
    if guard < 0.35:
        return Tier.CLEAR
    if guard < 0.65:
        return Tier.TRANSLUCENT
    return Tier.OPAQUE


# Fraction of an incoming wound a fully-opaque shadow absorbs.
PROTECTION = 0.6

DAYS = 10

# The naming option (the adult verb) appears at this much presence;
# helping Mara requires having named it plus this much total presence.
NAME_TRUST = 2
TRUST_NEEDED = 3


@dataclass
class Player:
    guard: float = 0.55            # trust froze at fourteen; this is the layer since
    trust: int = 0                 # presence built with Mara (max +1 per day)
    named_it: bool = False
    signals: set = field(default_factory=set)    # thread signals noticed
    witnessed: set = field(default_factory=set)  # optional discoveries
    last_visit_day: int = 0

    @property
    def tier(self) -> Tier:
        return tier_of(self.guard)

    def soften(self, amount: float) -> None:
        self.guard = max(0.05, self.guard - amount)

    def harden(self, amount: float) -> None:
        self.guard = min(0.95, self.guard + amount)

    def wound(self, base: float) -> float:
        """Apply a wound blunted by current guard. Returns what was felt."""
        felt = base * (1 - PROTECTION * self.guard)
        self.harden(felt)
        return felt


@dataclass
class World:
    day: int = 1
    mara_helped: bool = False
    resolved: bool = False
    father_felt: float = 0.0
    father_tier: Tier = Tier.TRANSLUCENT
    tier_time: dict = field(default_factory=lambda: {t: 0 for t in Tier})
