import asyncio
import random

from userbot import legend

menu_category = "useless"


@legend.legend_cmd(
    pattern="snow$",
    command=("snow", menu_category),
    info={
        "header": "try it Yourself ",
        "usage": [
            "{tr}snow",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Hmm...")
    await asyncio.sleep(1)
    x = random.randrange(1, 11)
    if x == 1:
        await event.edit(
            "Never forget what you are. The rest of the world will not.Wear it like armor,\n and it can never be used to hurt you."
        )
    elif x == 10:
        await event.edit(
            "When the snows fall and the white winds blow,\n the lone wolf dies, but the pack **survives**."
        )
    elif x == 2:
        await event.edit("There is only one thing we say to death: **Not today.**")
    elif x == 3:
        await event.edit(
            "If you think this has a happy ending, you haven’t been **paying attention**."
        )
    elif x == 4:
        await event.edit("Chaos isn’t a pit. Chaos is a ladder.")
    elif x == 5:
        await event.edit("You know nothing, **Jon Snow**")
    elif x == 6:
        await event.edit("**Winter** is coming.")
    elif x == 7:
        await event.edit("When you play the **game of thrones**, you win or you die.")
    elif x == 8:
        await event.edit(
            "I'm not going to **stop** the wheel, I'm going to **break** the wheel."
        )
    elif x == 9:
        await event.edit(
            "When people ask you what happened here, tell them the **North remembers**. Tell them winter came for **House Frey**."
        )


@legend.legend_cmd(
    pattern="bels$",
    command=("bels", menu_category),
    info={
        "header": "To Get Data From Holy Bible",
        "description": "Random Select From Holy Bible",
        "usage": [
            "{tr}bels",
        ],
    },
)
async def _(event):

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x = random.randrange(1, 96)

    if x == 1:
        await event.edit(
            '`"Underwater bubbles and raindrops are total opposites of each other."`'
        )

    elif x == 10:
        await event.edit(
            '`"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."`'
        )

    elif x == 11:
        await event.edit('`"A folder is for things that you don\'t want to fold."`')

    elif x == 12:
        await event.edit(
            '`"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."`'
        )

    elif x == 13:
        await event.edit(
            '`"If everything goes smoothly, you probably won\'t remember today."`'
        )

    elif x == 14:
        await event.edit(
            '`"When you meet new people in real life, you unlock more characters for your dream world."`'
        )

    elif x == 15:
        await event.edit(
            '`"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it."`'
        )

    elif x == 16:
        await event.edit(
            '`"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."`'
        )

    elif x == 17:
        await event.edit(
            '`"Parents worry about what their sons download and worry about what their daughters upload."`'
        )

    elif x == 18:
        await event.edit(
            '`"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."`'
        )

    elif x == 19:
        await event.edit(
            "`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`"
        )

    elif x == 2:
        await event.edit(
            '`"If you buy an eraser you are literally paying for your mistakes."`'
        )

    elif x == 20:
        await event.edit('`"Technically, no one has ever been in an empty room."`')

    elif x == 21:
        await event.edit(
            '`"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there."`'
        )

    elif x == 22:
        await event.edit(
            "`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`"
        )

    elif x == 23:
        await event.edit(
            '`"Every single decision you ever made has brought you to read this sentence."`'
        )

    elif x == 24:
        await event.edit("`\"The word 'quiet' is often said very loud.\"`")

    elif x == 25:
        await event.edit(
            '`"Everybody wants you to work hard, but nobody wants to hear about how hard you work."`'
        )

    elif x == 26:
        await event.edit(
            '`"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."`'
        )

    elif x == 27:
        await event.edit(
            '`"No one remembers your awkward moments but they’re too busy remembering their own."`'
        )

    elif x == 28:
        await event.edit(
            '`"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."`'
        )

    elif x == 29:
        await event.edit(
            "`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`"
        )

    elif x == 3:
        await event.edit(
            '`"The Person you care for most has the potential to destroy you the most."`'
        )

    elif x == 30:
        await event.edit(
            '`"The biggest irony is that computers & mobiles were invented to save out time!"`'
        )

    elif x == 31:
        await event.edit(
            '`"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."`'
        )

    elif x == 32:
        await event.edit(
            '`"You know you’re getting old when your parents start disappointing you, instead of you disappointing them."`'
        )

    elif x == 33:
        await event.edit(
            '`"Humans are designed to learn through experience yet the education system has made it so we get no experience."`'
        )

    elif x == 34:
        await event.edit(
            '`"By focusing on blinking, you blink slower... Same for breathing."`'
        )

    elif x == 35:
        await event.edit(
            '`"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."`'
        )

    elif x == 36:
        await event.edit(
            '`"Characters that get married in fiction were literally made for each other."`'
        )

    elif x == 37:
        await event.edit(
            '`"Babies are a clean hard drive that can be programmed with any language."`'
        )

    elif x == 38:
        await event.edit(
            "`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`"
        )

    elif x == 39:
        await event.edit(
            "`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`"
        )

    elif x == 4:
        await event.edit(
            '`"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."`'
        )

    elif x == 40:
        await event.edit(
            '`"Maybe we don\'t find time travelers because we all die in 25-50 years."`'
        )

    elif x == 41:
        await event.edit(
            '`"Sleep is the trial version of death, It even comes with ads based on your activity."`'
        )

    elif x == 42:
        await event.edit(
            '`"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"`'
        )

    elif x == 43:
        await event.edit(
            '`"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."`'
        )

    elif x == 44:
        await event.edit(
            '`"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."`'
        )

    elif x == 45:
        await event.edit('`"If Greenland actually turns green, we\'re all screwed."`')

    elif x == 46:
        await event.edit(
            '`"If someone says clever things in your dream, it actually shows your own cleverness."`'
        )

    elif x == 47:
        await event.edit(
            '`"Famous movie quotes are credited to the actor and not the actual writer who wrote them."`'
        )

    elif x == 48:
        await event.edit(
            '`"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."`'
        )

    elif x == 49:
        await event.edit('`"Ask yourself why the the brain ignores the second the."`')

    elif x == 5:
        await event.edit(
            '`"Any video with “wait for it” in the title is simply too long."`'
        )

    elif x == 50:
        await event.edit(
            '`"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."`'
        )

    elif x == 51:
        await event.edit(
            '`"It will be a lot harder for kids to win against their parents in video games in the future."`'
        )

    elif x == 52:
        await event.edit(
            '`"Everyone has flaws, if you don\'t recognize yours, you have a new one."`'
        )

    elif x == 53:
        await event.edit('`"Raising a child is training your replacement."`')

    elif x == 54:
        await event.edit(
            "`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`"
        )

    elif x == 55:
        await event.edit(
            '`"There\'s always someone who hated you for no reason, and still does."`'
        )

    elif x == 56:
        await event.edit(
            '`"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."`'
        )

    elif x == 57:
        await event.edit(
            '`"The more important a good night\'s sleep is, the harder it is to fall asleep."`'
        )

    elif x == 58:
        await event.edit(
            '`"Blessed are those that can properly describe the type of haircut they want to a new stylist."`'
        )

    elif x == 59:
        await event.edit(
            "`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`"
        )

    elif x == 6:
        await event.edit(
            '`"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you."`'
        )

    elif x == 60:
        await event.edit(
            '`"Theme park employees must be good at telling the difference between screams of horror and excitement."`'
        )

    elif x == 61:
        await event.edit('`"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"`')

    elif x == 62:
        await event.edit(
            '`"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."`'
        )

    elif x == 63:
        await event.edit(
            '`"Listening to podcasts before bed is the adult version of story-time."`'
        )

    elif x == 64:
        await event.edit(
            '`"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."`'
        )

    elif x == 65:
        await event.edit('`"A ton of whales is really only like half a whale."`')

    elif x == 66:
        await event.edit(
            '`"When you get old, the old you is technically the new you, and your young self is the old you."`'
        )

    elif x == 67:
        await event.edit(
            '`"You probably won\'t find many negative reviews of parachutes on the Internet."`'
        )

    elif x == 68:
        await event.edit(
            '`"We show the most love and admiration for people when they\'re no longer around to appreciate it."`'
        )

    elif x == 69:
        await event.edit(
            "`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`"
        )

    elif x == 7:
        await event.edit(
            '`"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."`'
        )

    elif x == 70:
        await event.edit(
            '`"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."`'
        )

    elif x == 71:
        await event.edit(
            "`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`"
        )

    elif x == 72:
        await event.edit('`"The most effective alarm clock is a full bladder."`')

    elif x == 73:
        await event.edit(
            '`"You probably just synchronized blinks with millions of people."`'
        )

    elif x == 74:
        await event.edit(
            '`"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."`'
        )

    elif x == 75:
        await event.edit(
            '`"Night before a day off is more satisfying than the actual day off."`'
        )

    elif x == 76:
        await event.edit('`"We put paper in a folder to keep it from folding."`')

    elif x == 77:
        await event.edit(
            '`"Somewhere, two best friends are meeting for the first time."`'
        )

    elif x == 78:
        await event.edit(
            '`"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."`'
        )

    elif x == 79:
        await event.edit(
            '`"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."`'
        )

    elif x == 8:
        await event.edit(
            '`"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."`'
        )

    elif x == 80:
        await event.edit(
            '`"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."`'
        )

    elif x == 81:
        await event.edit('`"Wikipedia is what the internet was meant to be."`')

    elif x == 82:
        await event.edit(
            '`"A theme park is the only place that you can hear screams in the distance and not be concerned."`'
        )

    elif x == 83:
        await event.edit(
            '`"A wireless phone charger offers less freedom of movement than a wired one."`'
        )

    elif x == 84:
        await event.edit(
            "`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`"
        )

    elif x == 85:
        await event.edit(
            '`"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."`'
        )

    elif x == 86:
        await event.edit(
            '`"If someday human teleportation becomes real, people will still be late for work."`'
        )

    elif x == 87:
        await event.edit(
            '`"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"`'
        )

    elif x == 88:
        await event.edit(
            '`"Doing something alone is kind of sad, but doing it solo is cool af."`'
        )

    elif x == 89:
        await event.edit(
            '`"Your brain suddenly becomes perfect at proofreading after you post something."`'
        )

    elif x == 9:
        await event.edit(
            '`"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back."`'
        )

    elif x == 90:
        await event.edit(
            '`"There\'s always that one song in your playlist that you always skip but never remove."`'
        )

    elif x == 91:
        await event.edit(
            '`"Kids next century will probably hate us for taking all the good usernames."`'
        )

    elif x == 92:
        await event.edit('`"Bubbles are to fish what rain is to humans."`')

    elif x == 93:
        await event.edit(
            '`"The more people you meet, the more you realise and appreciate how well your parents raised you."`'
        )

    elif x == 94:
        await event.edit('`"A comma is a short pause, a coma is a long pause."`')

    elif x == 95:
        await event.edit('`"Someday you will either not wake up or not go to sleep."`')

    elif x == 96:
        await event.edit(
            '`"Bermuda Triangle might be the exit portal of this simulation."`'
        )

    elif x == 97:
        await event.edit(
            '`"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."`'
        )


@legend.legend_cmd(
    pattern="bbl$",
    command=("bbl", menu_category),
    info={
        "header": "To Get Data From Holy Bible",
        "description": "Random Select From Holy Bible",
        "usage": [
            "{tr}bbl",
        ],
    },
)
async def _(event):
    "Random Thoughts"
    await event.edit("1 Min Pls!...")

    await asyncio.sleep(2)

    x = random.randrange(1, 101)

    if x == 1:
        await event.edit(
            '`"Underwater bubbles and raindrops are total opposites of each other."`'
        )

    elif x == 10:
        await event.edit(
            '`"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."`'
        )

    elif x == 100:
        await event.edit(
            '`"These words spake Jesus, and lifted up his eyes to heaven, and said, Father, the hour is come; glorify thy Son, that thy Son also may glorify thee:  <John 17:1>."`'
        )

    elif x == 101:
        await event.edit(
            '`"As thou hast given him power over all flesh, that he should give eternal life to as many as thou hast given him.  <John 17:2>."`'
        )
    elif x == 11:
        await event.edit('`"A folder is for things that you don\'t want to fold."`')

    elif x == 12:
        await event.edit(
            '`"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."`'
        )

    elif x == 13:
        await event.edit(
            '`"If everything goes smoothly, you probably won\'t remember today."`'
        )

    elif x == 14:
        await event.edit(
            '`"When you meet new people in real life, you unlock more characters for your dream world."`'
        )

    elif x == 15:
        await event.edit(
            '`"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it."`'
        )

    elif x == 16:
        await event.edit(
            '`"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."`'
        )

    elif x == 17:
        await event.edit(
            '`"Parents worry about what their sons download and worry about what their daughters upload."`'
        )

    elif x == 18:
        await event.edit(
            '`"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."`'
        )

    elif x == 19:
        await event.edit(
            "`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`"
        )

    elif x == 2:
        await event.edit(
            '`"If you buy an eraser you are literally paying for your mistakes."`'
        )

    elif x == 20:
        await event.edit('`"Technically, no one has ever been in an empty room."`')

    elif x == 21:
        await event.edit(
            '`"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there."`'
        )

    elif x == 22:
        await event.edit(
            "`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`"
        )

    elif x == 23:
        await event.edit(
            '`"Every single decision you ever made has brought you to read this sentence."`'
        )

    elif x == 24:
        await event.edit("`\"The word 'quiet' is often said very loud.\"`")

    elif x == 25:
        await event.edit(
            '`"Everybody wants you to work hard, but nobody wants to hear about how hard you work."`'
        )

    elif x == 26:
        await event.edit(
            '`"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."`'
        )

    elif x == 27:
        await event.edit(
            '`"No one remembers your awkward moments but they’re too busy remembering their own."`'
        )

    elif x == 28:
        await event.edit(
            '`"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."`'
        )

    elif x == 29:
        await event.edit(
            "`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`"
        )

    elif x == 3:
        await event.edit(
            '`"The Person you care for most has the potential to destroy you the most."`'
        )

    elif x == 30:
        await event.edit(
            '`"The biggest irony is that computers & mobiles were invented to save out time!"`'
        )

    elif x == 31:
        await event.edit(
            '`"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."`'
        )

    elif x == 32:
        await event.edit(
            '`"You know you’re getting old when your parents start disappointing you, instead of you disappointing them."`'
        )

    elif x == 33:
        await event.edit(
            '`"Humans are designed to learn through experience yet the education system has made it so we get no experience."`'
        )

    elif x == 34:
        await event.edit(
            '`"By focusing on blinking, you blink slower... Same for breathing."`'
        )

    elif x == 35:
        await event.edit(
            '`"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."`'
        )

    elif x == 36:
        await event.edit(
            '`"Characters that get married in fiction were literally made for each other."`'
        )

    elif x == 37:
        await event.edit(
            '`"Babies are a clean hard drive that can be programmed with any language."`'
        )

    elif x == 38:
        await event.edit(
            "`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`"
        )

    elif x == 39:
        await event.edit(
            "`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`"
        )

    elif x == 4:
        await event.edit(
            '`"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."`'
        )

    elif x == 40:
        await event.edit(
            '`"Maybe we don\'t find time travelers because we all die in 25-50 years."`'
        )

    elif x == 41:
        await event.edit(
            '`"Sleep is the trial version of death, It even comes with ads based on your activity."`'
        )

    elif x == 42:
        await event.edit(
            '`"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"`'
        )

    elif x == 43:
        await event.edit(
            '`"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."`'
        )

    elif x == 44:
        await event.edit(
            '`"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."`'
        )

    elif x == 45:
        await event.edit('`"If Greenland actually turns green, we\'re all screwed."`')

    elif x == 46:
        await event.edit(
            '`"If someone says clever things in your dream, it actually shows your own cleverness."`'
        )

    elif x == 47:
        await event.edit(
            '`"Famous movie quotes are credited to the actor and not the actual writer who wrote them."`'
        )

    elif x == 48:
        await event.edit(
            '`"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."`'
        )

    elif x == 49:
        await event.edit('`"Ask yourself why the the brain ignores the second the."`')

    elif x == 5:
        await event.edit(
            '`"Any video with “wait for it” in the title is simply too long."`'
        )

    elif x == 50:
        await event.edit(
            '`"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."`'
        )

    elif x == 51:
        await event.edit(
            '`"It will be a lot harder for kids to win against their parents in video games in the future."`'
        )

    elif x == 52:
        await event.edit(
            '`"Everyone has flaws, if you don\'t recognize yours, you have a new one."`'
        )

    elif x == 53:
        await event.edit('`"Raising a child is training your replacement."`')

    elif x == 54:
        await event.edit(
            "`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`"
        )

    elif x == 55:
        await event.edit(
            '`"There\'s always someone who hated you for no reason, and still does."`'
        )

    elif x == 56:
        await event.edit(
            '`"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."`'
        )

    elif x == 57:
        await event.edit(
            '`"The more important a good night\'s sleep is, the harder it is to fall asleep."`'
        )

    elif x == 58:
        await event.edit(
            '`"Blessed are those that can properly describe the type of haircut they want to a new stylist."`'
        )

    elif x == 59:
        await event.edit(
            "`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`"
        )

    elif x == 6:
        await event.edit(
            '`"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you."`'
        )

    elif x == 60:
        await event.edit(
            '`"Theme park employees must be good at telling the difference between screams of horror and excitement."`'
        )

    elif x == 61:
        await event.edit('`"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"`')

    elif x == 62:
        await event.edit(
            '`"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."`'
        )

    elif x == 63:
        await event.edit(
            '`"Listening to podcasts before bed is the adult version of story-time."`'
        )

    elif x == 64:
        await event.edit(
            '`"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."`'
        )

    elif x == 65:
        await event.edit('`"A ton of whales is really only like half a whale."`')

    elif x == 66:
        await event.edit(
            '`"When you get old, the old you is technically the new you, and your young self is the old you."`'
        )

    elif x == 67:
        await event.edit(
            '`"You probably won\'t find many negative reviews of parachutes on the Internet."`'
        )

    elif x == 68:
        await event.edit(
            '`"We show the most love and admiration for people when they\'re no longer around to appreciate it."`'
        )

    elif x == 69:
        await event.edit(
            "`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`"
        )

    elif x == 7:
        await event.edit(
            '`"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."`'
        )

    elif x == 70:
        await event.edit(
            '`"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."`'
        )

    elif x == 71:
        await event.edit(
            "`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`"
        )

    elif x == 72:
        await event.edit('`"The most effective alarm clock is a full bladder."`')

    elif x == 73:
        await event.edit(
            '`"You probably just synchronized blinks with millions of people."`'
        )

    elif x == 74:
        await event.edit(
            '`"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."`'
        )

    elif x == 75:
        await event.edit(
            '`"Night before a day off is more satisfying than the actual day off."`'
        )
    elif x == 76:
        await event.edit('`"We put paper in a folder to keep it from folding."`')

    elif x == 77:
        await event.edit(
            '`"Somewhere, two best friends are meeting for the first time."`'
        )

    elif x == 78:
        await event.edit(
            '`"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."`'
        )

    elif x == 79:
        await event.edit(
            '`"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."`'
        )

    elif x == 8:
        await event.edit(
            '`"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."`'
        )

    elif x == 80:
        await event.edit(
            '`"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."`'
        )

    elif x == 81:
        await event.edit('`"Wikipedia is what the internet was meant to be."`')

    elif x == 82:
        await event.edit(
            '`"A theme park is the only place that you can hear screams in the distance and not be concerned."`'
        )

    elif x == 83:
        await event.edit(
            '`"A wireless phone charger offers less freedom of movement than a wired one."`'
        )

    elif x == 84:
        await event.edit(
            "`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`"
        )

    elif x == 85:
        await event.edit(
            '`"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."`'
        )

    elif x == 86:
        await event.edit(
            '`"If someday human teleportation becomes real, people will still be late for work."`'
        )

    elif x == 87:
        await event.edit(
            '`"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"`'
        )

    elif x == 88:
        await event.edit(
            '`"Doing something alone is kind of sad, but doing it solo is cool af."`'
        )

    elif x == 89:
        await event.edit(
            '`"Your brain suddenly becomes perfect at proofreading after you post something."`'
        )

    elif x == 9:
        await event.edit(
            '`"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back."`'
        )

    elif x == 90:
        await event.edit(
            '`"There\'s always that one song in your playlist that you always skip but never remove."`'
        )

    elif x == 91:
        await event.edit(
            '`"Kids next century will probably hate us for taking all the good usernames."`'
        )

    elif x == 92:
        await event.edit('`"Bubbles are to fish what rain is to humans."`')

    elif x == 93:
        await event.edit(
            '`"The more people you meet, the more you realise and appreciate how well your parents raised you."`'
        )

    elif x == 94:
        await event.edit('`"A comma is a short pause, a coma is a long pause."`')

    elif x == 95:
        await event.edit('`"Someday you will either not wake up or not go to sleep."`')

    elif x == 96:
        await event.edit(
            '`"Bermuda Triangle might be the exit portal of this simulation."`'
        )

    elif x == 97:
        await event.edit(
            '`"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."`'
        )

    elif x == 98:
        await event.edit(
            '`"By faith Abraham, when he was called to go out into a place which he should after receive for an inheritance, obeyed; and he went out, not knowing whither he went.  <Hebrews 11:8>."`'
        )

    elif x == 99:
        await event.edit(
            '`"By faith Noah, being warned of God of things not seen as yet, moved with fear, prepared an ark to the saving of his house; by the which he condemned the world, and became heir of the righteousness which is by faith.  <Hebrews 11:7>."`'
        )


@legend.legend_cmd(
    pattern="facts$",
    command=("facts", menu_category),
    info={
        "header": "To Get Data From Facts",
        "description": "Random Select From Facts",
        "usage": [
            "{tr}facts",
        ],
    },
)
async def _(event):
    "Random Facts"

    await event.edit("Typing...")

    await asyncio.sleep(2)

    x = random.randrange(1, 96)

    if x == 1:
        await event.edit(
            '`"Underwater bubbles and raindrops are total opposites of each other."`'
        )

    elif x == 10:
        await event.edit(
            '`"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."`'
        )

    elif x == 11:
        await event.edit('`"A folder is for things that you don\'t want to fold."`')

    elif x == 12:
        await event.edit(
            '`"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."`'
        )

    elif x == 13:
        await event.edit(
            '`"If everything goes smoothly, you probably won\'t remember today."`'
        )

    elif x == 14:
        await event.edit(
            '`"When you meet new people in real life, you unlock more characters for your dream world."`'
        )

    elif x == 15:
        await event.edit(
            '`"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it."`'
        )

    elif x == 16:
        await event.edit(
            '`"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."`'
        )

    elif x == 17:
        await event.edit(
            '`"Parents worry about what their sons download and worry about what their daughters upload."`'
        )

    elif x == 18:
        await event.edit(
            '`"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."`'
        )

    elif x == 19:
        await event.edit(
            "`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`"
        )

    elif x == 2:
        await event.edit(
            '`"If you buy an eraser you are literally paying for your mistakes."`'
        )

    elif x == 20:
        await event.edit('`"Technically, no one has ever been in an empty room."`')

    elif x == 21:
        await event.edit(
            '`"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there."`'
        )

    elif x == 22:
        await event.edit(
            "`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`"
        )

    elif x == 23:
        await event.edit(
            '`"Every single decision you ever made has brought you to read this sentence."`'
        )

    elif x == 24:
        await event.edit("`\"The word 'quiet' is often said very loud.\"`")

    elif x == 25:
        await event.edit(
            '`"Everybody wants you to work hard, but nobody wants to hear about how hard you work."`'
        )

    elif x == 26:
        await event.edit(
            '`"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."`'
        )

    elif x == 27:
        await event.edit(
            '`"No one remembers your awkward moments but they’re too busy remembering their own."`'
        )

    elif x == 28:
        await event.edit(
            '`"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."`'
        )

    elif x == 29:
        await event.edit(
            "`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`"
        )

    elif x == 3:
        await event.edit(
            '`"The Person you care for most has the potential to destroy you the most."`'
        )

    elif x == 30:
        await event.edit(
            '`"The biggest irony is that computers & mobiles were invented to save out time!"`'
        )

    elif x == 31:
        await event.edit(
            '`"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."`'
        )

    elif x == 32:
        await event.edit(
            '`"You know you’re getting old when your parents start disappointing you, instead of you disappointing them."`'
        )

    elif x == 33:
        await event.edit(
            '`"Humans are designed to learn through experience yet the education system has made it so we get no experience."`'
        )

    elif x == 34:
        await event.edit(
            '`"By focusing on blinking, you blink slower... Same for breathing."`'
        )

    elif x == 35:
        await event.edit(
            '`"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."`'
        )

    elif x == 36:
        await event.edit(
            '`"Characters that get married in fiction were literally made for each other."`'
        )

    elif x == 37:
        await event.edit(
            '`"Babies are a clean hard drive that can be programmed with any language."`'
        )

    elif x == 38:
        await event.edit(
            "`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`"
        )

    elif x == 39:
        await event.edit(
            "`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`"
        )

    elif x == 4:
        await event.edit(
            '`"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."`'
        )

    elif x == 40:
        await event.edit(
            '`"Maybe we don\'t find time travelers because we all die in 25-50 years."`'
        )

    elif x == 41:
        await event.edit(
            '`"Sleep is the trial version of death, It even comes with ads based on your activity."`'
        )

    elif x == 42:
        await event.edit(
            '`"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"`'
        )

    elif x == 43:
        await event.edit(
            '`"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."`'
        )

    elif x == 44:
        await event.edit(
            '`"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."`'
        )

    elif x == 45:
        await event.edit('`"If Greenland actually turns green, we\'re all screwed."`')

    elif x == 46:
        await event.edit(
            '`"If someone says clever things in your dream, it actually shows your own cleverness."`'
        )

    elif x == 47:
        await event.edit(
            '`"Famous movie quotes are credited to the actor and not the actual writer who wrote them."`'
        )

    elif x == 48:
        await event.edit(
            '`"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."`'
        )

    elif x == 49:
        await event.edit('`"Ask yourself why the the brain ignores the second the."`')

    elif x == 5:
        await event.edit(
            '`"Any video with “wait for it” in the title is simply too long."`'
        )

    elif x == 50:
        await event.edit(
            '`"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."`'
        )

    elif x == 51:
        await event.edit(
            '`"It will be a lot harder for kids to win against their parents in video games in the future."`'
        )

    elif x == 52:
        await event.edit(
            '`"Everyone has flaws, if you don\'t recognize yours, you have a new one."`'
        )

    elif x == 53:
        await event.edit('`"Raising a child is training your replacement."`')

    elif x == 54:
        await event.edit(
            "`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`"
        )

    elif x == 55:
        await event.edit(
            '`"There\'s always someone who hated you for no reason, and still does."`'
        )

    elif x == 56:
        await event.edit(
            '`"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."`'
        )

    elif x == 57:
        await event.edit(
            '`"The more important a good night\'s sleep is, the harder it is to fall asleep."`'
        )

    elif x == 58:
        await event.edit(
            '`"Blessed are those that can properly describe the type of haircut they want to a new stylist."`'
        )

    elif x == 59:
        await event.edit(
            "`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`"
        )

    elif x == 6:
        await event.edit(
            '`"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you."`'
        )

    elif x == 60:
        await event.edit(
            '`"Theme park employees must be good at telling the difference between screams of horror and excitement."`'
        )

    elif x == 61:
        await event.edit('`"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"`')

    elif x == 62:
        await event.edit(
            '`"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."`'
        )

    elif x == 63:
        await event.edit(
            '`"Listening to podcasts before bed is the adult version of story-time."`'
        )

    elif x == 64:
        await event.edit(
            '`"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."`'
        )

    elif x == 65:
        await event.edit('`"A ton of whales is really only like half a whale."`')

    elif x == 66:
        await event.edit(
            '`"When you get old, the old you is technically the new you, and your young self is the old you."`'
        )

    elif x == 67:
        await event.edit(
            '`"You probably won\'t find many negative reviews of parachutes on the Internet."`'
        )

    elif x == 68:
        await event.edit(
            '`"We show the most love and admiration for people when they\'re no longer around to appreciate it."`'
        )

    elif x == 69:
        await event.edit(
            "`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`"
        )

    elif x == 7:
        await event.edit(
            '`"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."`'
        )

    elif x == 70:
        await event.edit(
            '`"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."`'
        )

    elif x == 71:
        await event.edit(
            "`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`"
        )

    elif x == 72:
        await event.edit('`"The most effective alarm clock is a full bladder."`')

    elif x == 73:
        await event.edit(
            '`"You probably just synchronized blinks with millions of people."`'
        )

    elif x == 74:
        await event.edit(
            '`"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."`'
        )

    elif x == 75:
        await event.edit(
            '`"Night before a day off is more satisfying than the actual day off."`'
        )

    elif x == 76:
        await event.edit('`"We put paper in a folder to keep it from folding."`')

    elif x == 77:
        await event.edit(
            '`"Somewhere, two best friends are meeting for the first time."`'
        )

    elif x == 78:
        await event.edit(
            '`"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."`'
        )

    elif x == 79:
        await event.edit(
            '`"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."`'
        )

    elif x == 8:
        await event.edit(
            '`"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."`'
        )

    elif x == 80:
        await event.edit(
            '`"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."`'
        )

    elif x == 81:
        await event.edit('`"Wikipedia is what the internet was meant to be."`')

    elif x == 82:
        await event.edit(
            '`"A theme park is the only place that you can hear screams in the distance and not be concerned."`'
        )

    elif x == 83:
        await event.edit(
            '`"A wireless phone charger offers less freedom of movement than a wired one."`'
        )

    elif x == 84:
        await event.edit(
            "`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`"
        )

    elif x == 85:
        await event.edit(
            '`"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."`'
        )

    elif x == 86:
        await event.edit(
            '`"If someday human teleportation becomes real, people will still be late for work."`'
        )

    elif x == 87:
        await event.edit(
            '`"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"`'
        )

    elif x == 88:
        await event.edit(
            '`"Doing something alone is kind of sad, but doing it solo is cool af."`'
        )

    elif x == 89:
        await event.edit(
            '`"Your brain suddenly becomes perfect at proofreading after you post something."`'
        )

    elif x == 9:
        await event.edit(
            '`"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back."`'
        )

    elif x == 90:
        await event.edit(
            '`"There\'s always that one song in your playlist that you always skip but never remove."`'
        )

    elif x == 91:
        await event.edit(
            '`"Kids next century will probably hate us for taking all the good usernames."`'
        )

    elif x == 92:
        await event.edit('`"Bubbles are to fish what rain is to humans."`')

    elif x == 93:
        await event.edit(
            '`"The more people you meet, the more you realise and appreciate how well your parents raised you."`'
        )

    elif x == 94:
        await event.edit('`"A comma is a short pause, a coma is a long pause."`')

    elif x == 95:
        await event.edit('`"Someday you will either not wake up or not go to sleep."`')

    elif x == 96:
        await event.edit(
            '`"Bermuda Triangle might be the exit portal of this simulation."`'
        )

    elif x == 97:
        await event.edit(
            '`"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."`'
        )
