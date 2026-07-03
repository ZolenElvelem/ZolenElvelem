"""All text for the prototype, keyed by perception tier.

VARIANTS[key] maps Tier -> the version of a scene that tier receives.
Where a tier is missing, fall back down the dict (OPAQUE text is the
floor everyone gets). Simulation code never contains prose; prose never
contains simulation logic.
"""

from .world import Tier

INTRO = """
KŌTUKU BAY

You are forty-one. Three years ago you came back to the bay you grew up
in — the surf, the estuary, the dairy, the one pub. You know everyone
and everyone knows you, which is both things at once.

You have ten days of an ordinary fortnight. Live them the way you would
actually live them.

(A text prototype. Ten to twenty minutes. Nothing will be explained in
advance; choose honestly, not tactically.)
"""

WEATHER = [
    "Monday. A long low swell from the east.",
    "Tuesday. Clean offshore morning.",
    "Wednesday. Grey, warm, windless.",
    "Thursday. A southerly building all afternoon.",
    "Friday. The southerly through; the bay rinsed.",
    "Saturday. High cloud, glassy sea.",
    "Sunday. Rain coming and going like it can't decide.",
    "Monday. Cold and bright as a struck bell.",
    "Tuesday. The first kōwhai out along Rise Road.",
    "Wednesday. Still. The kind of still that feels aimed.",
]

# Ambient/action prose is authored in VARIANT LISTS per tier and rotated
# (by day for ambient, by use-count for actions) so the register stays
# constant while the surface changes — repetition of register is the
# design; repetition of sentences is a bug (playtest finding #1). In the
# full game this variety is the batched-LLM text layer's job.

AMBIENT = {
    Tier.OPAQUE: ["""
The street is grey and quick. People keep their heads down over their
errands; the sea is just weather. You get where you're going.
""", """
The town does its errands around you. Someone says your name outside
the dairy; by the time you turn they've moved on, which suits you.
""", """
Low-tide smell, gulls arguing over something by the ramp. You take the
short way. There's nothing on the street you need.
"""],
    Tier.TRANSLUCENT: ["""
A tūī is working the flame tree by the dairy. Mrs Hema lifts two fingers
off the pump handle as you pass — the full local salute. Out past the
bar, the bay is gunmetal turning green.
""", """
Shona's chalkboard says the pies are back. Two kids' bikes lie outside
the dairy at angles that mean their owners left in a hurry, happily.
The bay is doing its slow silver thing.
""", """
Old Man Tāne's dog inspects you at the corner and approves. Down the
street someone's hammering — the roof going on at the Hemara place,
one sheet of iron a weekend.
"""],
    Tier.CLEAR: ["""
The morning is enormous. Light moves on the estuary like something
poured; kids drag boards down Rise Road arguing about whose wave it was;
behind the takeaway someone is laughing in two languages. The bay keeps
opening the longer you look at it.
""", """
Everything is specific today: the exact green of the estuary over the
sandbars, the squeak of the pub sign, Mrs Hema singing to the pie warmer
when she thinks the shop's empty. The town is made of ten thousand small
kept promises.
""", """
You catch yourself grinning at nothing on Rise Road. A kererū crashes
about in the pūriri like a drunk angel. The morning doesn't ask you to
earn it.
"""],
}

SURF = {
    Tier.OPAQUE: ["""
You paddle out because it's what you do. The sets are workmanlike and so
are you. You put in your time, catch a few, come in cold. Something in
you unclenches, barely, like a fist relaxing one finger.
""", """
Grey walls, close together. You go through the motions, and the motions
— to be fair — go through you too. You come in when your arms say so.
"""],
    Tier.TRANSLUCENT: ["""
Second wave of the set, and for six or seven seconds there is nothing in
the world that needs anything from you. You come in with salt in your
eyebrows and your shoulders an inch lower than they went out.
""", """
You trade waves with a kid who's better than you and generous about it.
On the drive home your hands remember the water and keep being quietly
pleased about it on the wheel.
"""],
    Tier.CLEAR: ["""
The wave stands up and you are in the exact place the ocean decided to
be generous. Time goes wide. You can hear your own laugh over the
whitewater, fourteen again in the only way that was ever good, and when
you finally wade in, the whole bay is lit like it's pleased with you.
""", """
Between sets the bay goes so quiet you can hear a dog barking a
kilometre of water away. You sit up on the board, legs in the green
light, exactly the size you actually are — which today, for once, is
not a problem.
"""],
}

PUB = {
    Tier.OPAQUE: ["""
The pub is loud in a way that asks nothing. You have one, watch the
replay above the bar, nod to the same four people you always nod to,
and leave. Transaction complete.
""", """
Same stool, same replay, same nods. Rewi asks how the family's keeping
and you say good thanks, and that is the whole of the transaction.
"""],
    Tier.TRANSLUCENT: ["""
Rewi pours yours before you reach the bar. The talk is snapper and
council rates and whose kid made the rep team. It's nothing, and it's
also the sound of the town holding itself together.
""", """
Darts night. You're rubbish, publicly, and it's somehow the best hour
of the day — being rubbish at darts here is a kind of citizenship.
"""],
    Tier.CLEAR: ["""
Rewi pours yours before you reach the bar and slides it over with the
exact nod his father used to use. Around you the pub is a loom — every
conversation a thread you can see being woven into the town. Old Man
Tāne is telling the eel story again and three people who've heard it
fifty times are leaning in anyway, because that's what the story is for.
""", """
Someone's guitar has come out of someone's ute. By nine the whole bar is
finding the harmonies to a song about a river none of them have seen,
and Rewi turns the tap off so he can listen properly.
"""],
}

PUB_WORD = """
Rewi wipes a glass that is already dry, which means he's deciding
something. "Your Mara was in Tuesday lunchtime," he says, not looking
up. "And Wednesday. And it wasn't lunch she was here for." He puts the
glass down. "You didn't hear it from me."
"""

BENCH = {
    Tier.OPAQUE: ["""
The bench above the point. You sit for a while. The sea does what the
sea does. Your phone stays in your pocket, which is something.
""", """
You sit. Boats come in around the point, one by one, on rails of their
own wake. Your shoulders drop half an inch without asking you first.
"""],
    Tier.TRANSLUCENT: ["""
The bench above the point, initials carved all over it like a guest
book. Yours are here somewhere. You were seventeen, terrified, and she
kissed you first. The memory arrives and you let it sit down next to
you.
""", """
A woman you half-know is leaving as you arrive; you swap the nod of two
people who use the same church at different hours. The old initials
hold the armrest together like stitching.
"""],
    Tier.CLEAR: ["""
The bench above the point. Yours are here somewhere among the initials —
seventeen, terrified, kissed first. Today you can also see all the
others: dates and hearts and one set of tiny letters low on the leg
where a child could reach. Sixty years of people bringing the biggest
thing they had up to this bench because the view was the only thing big
enough to hold it. You are in a long queue of hearts. It helps.
""", """
A grandfather is teaching a small girl how to hold her chips so the
gulls miss her fingers. Their laughter goes up the hill like smoke.
You'll remember this one; you can tell while it's still happening.
"""],
}

RESERVE = """
You follow the tūī calls up the track into the reserve, past the water
tank, to the big tōtara where the track gives up. And there — chest
height, grey with age, cut deep by children's hands a long time ago — a
spiral, and two stick figures holding hands. Under it, in letters that
took someone a whole afternoon: "WE PROMISED."

You stand there for a long time. You have walked past the bottom of this
track a thousand times. It has been here the whole of your life.
"""

STAY_IN = ["""
You keep the curtains half-drawn and the day at arm's length. Toast,
admin, the radio talking to itself in the kitchen. Nothing gets in.
It works.
""", """
Curtains, kettle, radio. The day knocks a couple of times and gives up.
Quiet as an unplugged fridge, and about as nourishing.
"""]

MARA_PLAIN = {
    Tier.OPAQUE: ["""
Mara's place smells of toast and WD-40 like always. You talk about the
rugby and the roof she keeps meaning to do. The conversation stays in
the shallows where it's safe to stand. It's fine.
""", """
Tea at Mara's, strong enough to stand a spoon in. She tells the story
about the courier and the goat and you both laugh in the right places.
Nothing is said. Nothing was going to be.
"""],
    Tier.TRANSLUCENT: ["""
Mara's place, toast and WD-40. She's glad to see you — she's always glad
to see you — but twice she starts a sentence and lets it go, like a wave
she decided not to catch.
""", """
She's rearranged the kitchen again — third time this year, everything a
handspan from where it lived. "Keeps me busy," she says, to the cupboard
she's holding open, not really to you.
"""],
    Tier.CLEAR: ["""
Mara's laugh is a beat late today, and it doesn't get all the way to her
eyes. She fills the kettle and watches it like it might say something.
The kitchen is very clean. It's the cleanness of someone gripping the
edges of their days.
""", """
There's a glass upside-down on the draining rack that she moves out of
your eyeline with one practised motion, mid-sentence, the way you'd
brush away a fly. Her voice doesn't change at all while she does it.
That's the part that stays with you on the walk home.
"""],
}

MARA_EMPTIES = """
You carry the recycling out for her on your way — old habit — and the
bin swings heavier than it should, with a clinking in it like a chord.
Heavier than one person's fortnight. You stand in the driveway holding
the lid a second longer than you need to.
"""

MARA_NAMED = ["""
You don't talk about it every time now. You don't have to. You wash, she
dries, and the radio does the heavy lifting. Once she looks over at you
and doesn't say thanks, and you don't say you're welcome.
""", """
She's counting days now, privately — you can tell because Tuesday she
said "eleven" to the window, apropos of nothing, and dared you with the
back of her head to ask. You didn't. You put the kettle on. That was
the right answer.
"""]

REGRESSED_INTRO = """
There's a moment — she's at the sink, back to you — when the thing
you've noticed is suddenly right there in the room with the two of you.

And you are, all at once, fourteen about it. You can feel the exact
size and age of the part of you that's been handed this moment.
"""

REGRESSED_OPTIONS = [
    "Make a joke of it — \"big recycling week, eh?\"",
    "Keep your excuse ready and talk about the surf instead",
    "Remember somewhere you need to be",
]

REGRESSED_OUTCOMES = [
    """
"Big recycling week, eh?" you say, and she laughs the laugh you both
know is a door closing. The joke works. That's the worst part. The
moment folds itself away and the armour holds.
""",
    """
You tell her about Thursday's southerly and the set that cleaned
everyone up, and she leans on the bench and listens, grateful — you can
see it — for every sentence that isn't the other sentence. The moment
passes at a safe distance. The armour holds.
""",
    """
You look at your watch and it's true, technically, that you have places
to be — there are always places to be if you need one. Her "no worries,
eh" follows you down the steps. The armour holds all the way home.
""",
]

NAME_IT_OPTION = "Say what you've actually seen, plainly"

NAME_IT = """
You say it plainly and badly, which is the only way it ever gets said:

"I've seen the bin, Mar. And Rewi talks. I'm not going anywhere — I just
can't keep pretending with you. That's all."

The silence goes on so long you nearly take it back twice. She doesn't
turn round. The tap drips once.

"I know," she says finally, to the window. "I know, eh."

Nothing is fixed. Something is different.
"""

DINNER_FACT = """
A text from Mara, mid-morning: "cant do tea tonight sorry. next week
promise x". You put the phone down.
"""

DINNER_SIGNIFICANCE = """
Halfway through the afternoon it surfaces again, snagged on something:
that's the third cancel this month. Mara doesn't cancel things. Mara
*organises* things. Mara is the person who rings *you*.
"""

FATHER_FACT = """
Mum rings before seven, her voice doing the thing where it's being very
calm. Dad's had a turn — dizzy, a fall, nothing broken — but they've
kept him in overnight at Whangārei for tests. "He's cross about the
jelly," she says, "so he's mostly himself."
"""

FATHER = {
    Tier.OPAQUE: """
You hear yourself asking the sensible questions — which ward, what time,
does she need anything. The news lands somewhere offshore of you, like
weather over the horizon that may or may not come in. You make toast.
The toast is fine. Everything is at one remove, which is to say:
manageable.
""",
    Tier.TRANSLUCENT: """
Your chest does something complicated while you ask the sensible
questions. Afterwards you drive to nowhere in particular the long way,
past the boat ramp where he taught you to back the trailer, both of you
shouting, neither of you angry. You sit in the car park for a while.
""",
    Tier.CLEAR: """
It goes through you like cold water — all of it, at once: the trailer
lessons, the terrible whistling, the way he says "righto then" instead
of goodbye, the fact of him, the eventual subtraction of him. You stand
in the kitchen and let it hit. It hurts exactly as much as he matters,
which turns out to be the deal, and today you can afford the price of
knowing it.
""",
}

MISSED_WORK_FACT = """
Word at the dairy, passed over the counter with your milk: Mara didn't
open the shop yesterday. Didn't ring anyone, either. Shona covered the
lunch rush and is being loud about it.
"""

MISSED_WORK = {
    Tier.OPAQUE: """
People will talk; people always talk. You take your milk and stay out
of it.
""",
    Tier.TRANSLUCENT: """
The bottom of your stomach knows something before the rest of you agrees
to. Mara has opened that shop with the flu, with a broken toe, the
morning after her mum's funeral.
""",
}

OUTCOME_HELPED = """
Mara's ute pulls up outside before eight, engine running, running,
running. Then it stops and she comes to the door with her keys still in
her hand.

"There's a thing in Whangārei at ten," she says, to a point just past
your shoulder. "A meeting. The first one." A breath. "Drive me?"

You drive her. You wait in the car park for an hour with a newspaper you
don't read a word of. When she comes out she doesn't say anything and
neither do you, and the whole way home the bay keeps showing up between
the hills like it's checking on you both.
"""

OUTCOME_ALONE = """
You hear it from three different people before lunch, each of them
enjoying it a little and hating that they are: Mara's ute in the ditch
by the estuary bridge, one wheel still turning when the Hemara boy found
it. She's fine — walked away, breathalysed, everyone knows. The whole
bay knows. There are casseroles appearing on her step like apologies.

You think about the bin, swinging heavier than one person's fortnight.

You think: I knew.
"""

EPILOGUE_FATHER = {
    Tier.OPAQUE: """
When the phone rang about your father, you were behind thick glass. The
news reached you the way weather reaches a house — a sound on the roof,
managed, at one remove. What you didn't feel that morning didn't go
anywhere. It's still out there, offshore, waiting for a day when the
glass is thinner. It can wait for years. It's patient.
""",
    Tier.TRANSLUCENT: """
When the phone rang about your father, you were half-open, and it
reached you the way those calls reach most people: a cold hand on the
chest, then the long drive past the boat ramp. You felt most of it.
The rest joined the layer.
""",
    Tier.CLEAR: """
When the phone rang about your father, you were wide open, and you paid
the full price of loving him on the spot — no credit, no layaway. It
took the wind out of you for days. It also never went bad in storage,
the way the unfelt ones do. It just became true, and then became
bearable, and is now simply a thing you know: he matters exactly that
much.
""",
}

MISSED = {
    "dinner": """
The night Mara cancelled dinner, she had already set the table. Three
places, because setting it for one was the thing she couldn't look at.
You read the text and put the phone down.
""",
    "empties": """
The recycling bin clinked every week, heavier than one person's
fortnight. You never happened to carry it out.
""",
    "pub_word": """
Rewi tried to tell you, in his sideways way, wiping a glass that was
already dry. You weren't in that day — or you were in, and not
listening. He won't try twice; that's not how his kindness works.
""",
    "carving": """
High in the reserve, at chest height on the big tōtara, there is a
spiral and two stick figures holding hands, and underneath, cut by a
child's hand a long time ago: "WE PROMISED." It has been there every
single day of your life in this bay. You never found it.
""",
}

EPILOGUE_CLOSE = """
The town you walked through these ten days was not the town. It was the
town at exactly the width your glass allowed.

Somewhere you are still fourteen, holding a door shut with both hands,
because once — for good reasons, in a hard year — that was the strongest
thing you knew how to do. It kept you safe. It kept things out. It is
still doing its job, whether or not there is anything left to keep out.

Did you remember?
"""
