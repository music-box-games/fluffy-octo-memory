label demostart:
    scene school front winter
    show father smile at tq_center

    dad "Well, here we are. Seems pretty nice huh?"
    dad "So, I'll take your stuff up to the dormitories, you may want to go visit the school nurse before class, or you could visit them after class...your choice."
    menu:
        "Go to the Nurse's Office":
            jump gotonursefirst
        "Go to Class":
            jump gotoclassfirst

label gotonursefirst:
    mc "I think I should head to the nurse's first. Get everything squared away first."
    dad "That sounds like a good idea, alright, I don't think I'll see you after I take your stuff up to the dorms..."
    mc "Wait, Dad."
    "Before he could reach down to pick up my lugge I stepped over and wrapped my arms around him."
    hide father
    "His hand clenched against the back of my head."
    "My father and I were rarely ever apart when I was younger. Most everything I know how to do, I owe to him."
    "He always wore this cologne that made him smell like lavender and pine trees. It isn't overbearing but I could still make it out through his coat."
    "Leaving my friends for a year is going to be tought, but it can't be helped, they were all very understanding when we were texting lsat night."
    "I think it's all just hitting me now. Everything's changing and there's no going back."
    dad "I love you Hayato. You know that right?"
    mc "I know Dad, I know."
    "It's only a year."
    "We let go of each other and he reaches down to lift my luggage."
    show father normal at tq_center
    "My dad never expressed his emotions as much as I think he'd like to. My grandfather was very muhc of the \"suck it up and walk it off\" variety."
    dad "I'll be sure to email you, I now Anko will."
    "The thought of my cute little sister sitting diligently at a desk trying to write a cohoesive letter makes me feel a little happy, something I don't think will happen often at this place."
    "It may just be me, but this place feels more like a western college than a high school for the disabled. Idon't know, Yale, Hardvard, Brown. All the famous red brick, ivy-covered colleges."
    "I wave my Dad off and make my way toward the school."
    hide father
    "It is a bit chilly out, the walk to and from the dorms isn't that far. Maybe a hundred yards? I'll probably only need to wear a coat if it gets super cold."
    scene school side entrance winter
    "Stepping up to the side door of the school's main building I take a deep breath."
    # TODO running sfx
    "What is that-..."
    "I look back and see a girl running right up behind me."
    "She's moving fast"
    show masuyo normal at zoom_tqosl_to_tqosr
    girl "Huff-hu excuse me, sorry."
    hide masuyo normal
    "Before I can even try to open the door for her, she darts in front of me and grabs the door handle herself."
    "She flings the door open and rushes inside. The door slowly closes, while I look around for anyone to confirm what I just saw."
    "After taking a second to confirm with myself that I wasn't imagining things, I turn back to the door and reach for the handle."
    "The door flings back open, I pull my hand out of the way just in time."
    show masuyo normal at tq_right
    # TODO masuyo's theme
    "Sure enough, it's that same girl. Out of breath and with a considerably less menacing look on her face."
    "She has short coffee-brown hair. Parted in the middle with one side tucked behind her ear, and the other side covering up much of her other eye. Her eyes are a bright brown, almost a shiny amber color."
    "If it wasn't for the small curl at the edge of her lips, she'd give of a rather mysterious vibe. That and she has what appear to be hiking book on, definitely not the attire of a demure girl."
    girl "Hey, you're new here, aren't you?"
    "She asks between breaths."
    "Part of me wants to ask for an apology, or at the very least an explanation as to why that's the way she wants to introduce herself to me."
    mc "Uh-yeah. My names Hayato."
    "She stops herself. She takes in a deep breath and slowly lets it out, her breath visible in the cold."
    show masuyo smile
    girl "My name's Masuyo Matsushita."
    "I hesitate before responding, watching as her huffing and puffing slows down."
    mc "Good to meet you Masuyo."
    show masuyo bashful
    myo "Again, sorry about that."
    mc "No, no, it's fine. Why were you running, by the way?"
    "She just has her normal uniform on. At the very least I'd expect someone that was out running to have some gym clothes on, or something similar considering the temperature."
    show masuyo normal
    myo "Sorry, when you say you're new here, how new do you mean?"
    mc "First day. I was actually on my way to the nurse's office. Do you know where it is?"
    myo "Oh yeah. Here let's get inside."
    "Masuyo steps back a big, holding the door open for me. I step inside and she immediately points to the staircase in front of us, still breathing beavily as she begins to talk."
    scene school main stars
    show masuyo normal at tq_center
    myo "Oh yeah, you just go through these doors, take a right into the next hall, when you reach teh stairs go down one floor and go to the end of the hall."
    myo "Not sure which one it would be exactly. It should say her name on the sign by the door though."
    mc "Sweet, thanks."
    myo "Sorry, I'd walk you there but I'm late as it is. Maybe I'll see you around sometime. Bye!"
    mc "Oh, no, it's totally alright."
    hide masuyo
    "I wave her off and she begins briskly walking up the stairs, skipping every other step."
    # TODO stop mausyo's theme
    scene nurse hallway
    # TODO nurse's theme
    "Following Masuyo's instructions, I head down the stairs and start walking to the other end of the hall, looking at the nameplates by each door as I pass."
    "After following the hall down a ways, I find a door labeled \"Nurse's Office \". I knock on the door and wait in the empty hallway."
    scene nurse door closed
    u "Just a moment."
    "I raise my hand up to knock once more when the door quickly opens and out walks a tall woman with blue hair. She turns back towards the woman, waves, and heads off down the hall without even noticing me."
    show nurse talking at tq_center
    nur "Hello, can I help you?"
    mc "Uh yes, my name is Hayato Ahearne, I was told to come here before class."
    show nurse smile
    nur "Ah yes, Hayato, please come in."
    scene nurse office
    show nurse smile at tq_center
    nur "So, how are you doing today?"
    mc "Well, first day at a new school that's located 300 miles from my home, found out that I had a disease that makes paper cuts something I need to watch out for, oh and I almost died a few weeks ago."
    show nurse normal
    "The chipper smile from her face quickly drops into a frown. I feel like an ass for unloading all of that on her. I should apologize."
    mc "I'm sorry about that. I really haven't had anyone to talk to for the past few days other than my dad, so..."
    show nurse talking
    nur "No need to apologize."
    nur "You'd be surprised at how many other students here are in a similar situation."
    nur "Now then, I'm going to need you to take off your shirt so I can check your bandages."
    "I sit down on the hospital bed next to me and unbutton my shirt."
    ## TODO: close up nurse?
    hide nurse
    "I feel the nurse slowly unravel the bandages on my chest. As it gets to the last layer it feels more like she is peeling them off."
    nur "Well, hello....What do we have here?"
    "She begins to poke one of my stiches with her hand, granted she had the decency to put on a latex glove first."
    nur "It appears one of your stitches has come a little loose."
    "A rush of panic wipes over my body. I try to speak but little more than a stammer comes out."
    mc "I-I-is that bad?"
    nur "Well, not necessarily. Let's say you yawn and stretch, then your stitches would rip open and cause you to start bleeding."
    mc "That sounds pretty bad!"
    "She seems incredibly calm for this sort of situation."
    "The doctor at the hospital made it clear how dangerous things could get if I was injured without taking my medication, and I really don't want to find out how effective my meds are."
    "She stands up."
    show nurse talking at tq_center
    nur "Don't worry about it. I'm going to find my suture and fix this right up."
    "I sit there looking around the room. Given the scattered papers on the desk, and the various medical posters hanging on the walls, I can only assume this doubles as her office."
    nur "Alright, this will only take a sec."
    ## TODO: close up nurse again
    hide nurse
    "I look away as she starts to work on my upper waist. I try to not focus on the feeling of wire moving through my skin."
    "After a minute or so she begins to wrap my waist up with fresh gauze."
    nur "Alright now this is gonna be uncomfortable but I have to check your thigh."
    "I stand up and shuffle off my pants. It wasn't the cuts on my torso that almost killed me, it was my thigh. Now the nurse is removing the bandages."
    "Once again, I hear the peeling sound but coming from... lower down."
    "Apparently the rock I hit cut right through my femoral artery. If we weren't sledding on a hill near the base I would have easily died from blood loss. Doctor said I went through enough blood to fill me up three times. But I am not dead yet, so I guess that's a plus."
    nur "The stiches on your inner thigh are fine. I applied new bandages so you should be good for a few days. Just be sure to come back here every few days so I can re-apply the bandages."
    "I start putting my clothes back on."
    mc "What happens if I don't get them changed?"
    show nurse normal at tq_center
    nur "Infection. And I doubt anyone wants an infection...down there."
    "Jeez, I guess that's one way to put it."
    mc "I'll be sure to remember, thanks Ms. N. I think I should be getting to class."
    nur "Alright you stay safe now."
    scene nurse hallway
    ## TODO: stop nurses theme
    ## TODO: start light winter theme
    "That's one crisis averted. I make my way down the hall and up the stairs, towards my classroom."
    scene school main stairs
    "Repeating the directions over and over again in my head so I won't forget."
    scene classroom hallway day
    "Looking at the plaque next to the door I see the numbers \"3-2\" scrawled across it."
    "Just as I start to reach for the handle, the door swings open."
    #TODO: scenename You're Young Again
    ## TODO: stop light winter theme
    ## TODO: start classroom theme
    show sato excited at tq_center
    sat "Ah, Mr. Ahearne, good of you to join us! Come, you can introduce yourself to the class."
    "Wait what?!"
    "Before I know it, I am pulled into the classroom and I am staring blankly at the class, still trying to comprehend what happened."
    scene classroom dynamic
    "The classroom is surprisingly small. Well, fewer students than I expected, heck there are even a few empty seats. Most of the students don't really look all that different from some of the kidns you would find at a regular school."
    "Most everyone just looks...normal."
    "There is one girl in the far back with an eye-patch over her left eye and an empty seat on either side of her. To her left and a seat over is another girl who seems...normal. She has navy blue hair and, just like the girl next to her, has a very wide smile."
    "There's a guy in the front with brown hair down past his ears and his left arm missing, and a girl with long white hair. At least it looks mostly white, there's a hint of cream color to it, but that could be the sun from outside. She has her earbuds in and I doubt she noticed I entered."
    show sato talking at tq_right
    sat "Alright, Mr. Ahearne if you could introduce yourself to the class."
    mc "Hello, my name is uh, Hayato Ahearne, I'm 18 years old, I like to fish, play video games, and read."
    sat "Excellent! Plenty of rivers up here, I am sure if you catch anything you'll bring it to class to show, eh? Now, please take a seat in the back."
    "Show it to the class, what?"
    "Mr. Sato pats me on the back and I snap out of my confusion from what he just said."
    "I give a bow to the class and make my way to some of the empty desks in the back of the room. I can sit either to the right of the girl with the eye-patch or between her and the girl with the navy-blue hair."
    menu:
        "Where should I sit?"
        "Sit next to the girl with the eye-patch":
            jump sit_by_eyepatch
        "Sit between the two girls":
            jump sit_between


label sit_by_eyepatch:
    "I think it would be best to sit next to the girl with the eye-patch, I have never been too good with girls and it would be like fighting uphill both ways if I were between the two."
    scene classroom desk
    "As I place my book-bag at the side of the desk I glance over at the girl next to me. What seemed like a near permanent smile on her face was no a mixture of shock and maybe a dash of terror."
    "I sit down in my seat and turn towards the front only to see a face made of pure anger and eyebrows."
    "JEEZ LOUISE!!!"
    ## TODO: jeeze louise but with face instead of cock
    show sato face at in_your_face
    sat "Mr. Ahearne, thank you for choosing your seat. Now then-."
    "He turns around and walks back towards the front of the class. He starts explaining some kind of science thing, but I was more focused on the sounds of the students giggling at my expense."
    show sato normal at tq_center
    sat "Class, I have some work packets for you all. You can work in groups or you can work alone, it's your choice. Please pass any extras back up to the front. Now, if you will excuse me, I have to go discuss something with one of the other teachers."
    "The teacher hands some stacks of papers to the front row students and then waltzes out the door."
    hide sato
    "As soon as the door is closed, and his footsteps can no longer be heard walking away from the room, the entirety of the class begins conversing with each other. Soon enough the girl next to me taps me on the shoulder."
    "I look to my left to see the girl with the eye-patch smiling at me."
    show chioko smile at tq_left
    girl "Hello there."
    mc "Oh, hi, I'm-"
    girl "You're new here, Hayato, right?"
    "The girl's cheeks turn pink realizing the obvious question she just asked. I think my awkardness is rubbing off on the people around me."
    mc "Yeah that's me. I didn't catch your name?"
    show chioko normal
    girl "My name is Chioko Kai."
    "She introduces herself in a calm, almost restrained voice. I can hardly hear her speak over the sound of the class."
    "I think the best thing to do would be to take the lead in this conversation."
    mc "It's nice to meet you Chioko. Hey do you understand what we are supposed to be doing? This work seems...a little advanced."
    "Her cheeks return to normal and she seems to calm down."
    show chioko talking
    chk "Mr. Sato is one of the harder teachers here, but he is also one of the easier ones."
    "I don't think that makes sense."
    chk "He will go on about theoretical physics like it's kindergarten level stuff, but as long as you act like you know what you're talking about he should give you a good grade."
    mc "I don't know if I should be relieved or even more afraid."
    show chioko giggle
    "Chioko lets out a small giggle at my joke."
    mc "I have never been that good of a public speaker, but if that's what it takes to get a good grade in a class where the teacher's crazy, then by all means sign me up."
    chk "I wouldn't say he's crazy, more just-EEP!"
    ## TODO: paff sfx
    ## TODO: chibi thing maybe?????
    girl "Chiokooo! You wanna work togetherrrrr?"
    "Out of nowhere, the girl that was sitting two desks over plopper her head on top of Chioko's."
    chk "Oh, Mikka, of course you can."
    chk "Do you want to work with us, Hayato?"
    mc "Sure, why not?"
    "I shuffle my desk to move closer to hers, while the other girl pulls over the empty desk in between them."
    "I look down at the two-page packet of math problems in front of me. Nothing too difficult, but the help mill mak eit go by a lot faster."
    mc "I forgot to introduce myself, I'm Hayato."
    show mikka smile at tq_center
    mkk "Actually, you already did."
    mc "When did I-oh, right."
    mkk "It's okay. I don't think I could have gotten through my first day if I hadn't met Chioko."
    chk "Maybe we should get to work?"
    mc "Yeah, you're probably right."
    "We dive into the packet. Every now and then I have to confirm my answers with the two. Math has never been my strong suit. Much of it feels like memorizing equation after equation, except I seem to only be able to remember four or five at a time."
    ## TODO: light transition
    "The lunch bell rings and the rest of the class gets up and heads towards the door. The three of us move our desks back into position. Oddly enough, Mr. Sato has yet to return from wherever he went. No one seems to notice as they just stack their papers on the empty desk."
    show chioko talking at tq_left
    show mikka normal at tq_center
    chk "Hey Hayato, you want to have lunch with us? There's an extra seat at our table."
    mc "Oh, sure."
    "I pick up my work and walk it over to Mr. Sato's desk with Mikka and Chioko."
    scene classroom hallway crowded
    "I am surprised at how spacious and crowded this school is. I try to stay as close to the two girls as I can, so as to not get lost in the flurry of students."
    scene cafeteria crowded
    "After a short walk we find ourselves in the cafeteria surrounded by the smell of warm food, a hint of sanitizer, and sweet-perfume."
    "I can't tell if it's Mikka and Chioko in front of me, or one of the girls around me. Now that I look around more, there are a ton of girls here."
    "Either we just happen to be walking through a cluster of them or there must be one guy for every three girls at this school."
    show chioko talking at tq_left
    chk "Do you want to grab lunch down here then head to our table, or do you want to head straight there?"
    mc "Well, I didn't have time to cook anything for lunch, or grab anything on the way here, I'll need to grab something real quick."
    mc "I'll get something real quick and find you at your table."
    show mikka smirk at tq_center
    mkk "Oh I doubt that. We'll be right here."
    "I feel a little uneasy as Mikka flashes a sly little grin. I am pretty sure I would be able to find them, well at least Chioko. But then again, she may not be the only girl in this school with an eyepatch."
    hide chioko
    hide mikka
    "I head over to the line of students, after a moment or two it starts to move and I can get a good look at the food they have here."
    "The selection here looks surprisingly good. Stir-fry, sushi, steamed white rice, and carrots. Not bad for a first meal. I head back to where the three of us were talking and, sure enough, there they are waiting patiently."
    show chioko normal at tq_left
    show mikka smirk at tq_center
    "Mikka is standing with that same grin she had when I left and Chioko is holding her lunch in front of her."
    show mikka talking
    mkk "Alright, let's go eat."
    show mikka talking with moveoutleft
    show chioko wink with moveoutleft
    "As Mikka trots off Chioko turns her head and gives me a wink, I think. I can't tell if they are going to pull a prank on me for being the new guy, or if they're as harmless as they seem."
    "Chioko doesn't seem like th ekind of girl to pick on the new guy. Or anyone for that matter."
    "After walking no more than 10 feet we come to a nearly empty table right next to the windows of the cafeteria. I look at them puzzled."
    scene cafeteria table
    show mikka happy at tq_center
    show chioko normal at tq_left
    "Mikka sits down and spreads her arms out, as if to say \"Eh? What do you think?\""
    mc "Y'know, I expected something a bit more illustrious. You two made it seem like this was the Holy Grail of tables or something. It's just a table."
    mkk "But look around you, there's no one here! There's almost never an empty table, and when they have folks in them, people never start at the end of the table and move down-"
    "Mikka continues on her mini-rant and I glance over at Chioko, she nods at me. Maybe she can read minds, I wanted to ask her if this is normal for Mikka. But hey, at least it's entertaining to watch."
    show mikka pout
    mkk "-and then you gotta find the chair, and sometimes other people will thake the chair thinking it's theirs, and then-"
    "Chioko cuts her off."
    chk "Mikka, be a good girl and eat your food, I think you're starting to scare Hayato."
    mkk "Yes Mother."
    "I try not to choke on my food at the banter between the two. I guess Chioko is the one that \"wears the pants\" in their relationship."
    "We continue to eat our food as the tables around us and our own begin to fill up with students. I guess we're pretty lucky."
    "It's amazing how many students are here. It's also very eye opening. So many kids from all over teh country come here because of some sort of condition."
    "How can there be this many kids all with some sort of disability that precents them from functioning at a regular school? It's a bit depressing, really. Though, I am one of them now."
    show mikka talking
    show chioko smile
    mkk "And that's why I think he should have just stayed at home with his millions instead of ruining-"
    ## TODO: school bell sfx
    "Mikka is interrupted by the bell."
    scene cafeteria crowded
    "The girls make their way back to the classroom, while I take care of my tray and our extra trash."
    scene classroom hallway crowded
    "I retrace my steps and head back to class."
    scene classroom desk
    "Sitting down in my seat, I watch as more and more students fill their seats."
    show sato talking at tq_center
    sato "Sorry about the wait class. Now, let's get back to work. Uh, where were we...right! Quantum locking!"
    "A collective groan can be heard from much of the class as the teacher starts the lecture."
    ## TODO: light transition
    "The bell rings and everyone begins putting their things away. I catch myself looking over at Chioko as she carefully wraps her scarf around her neck."
    "I quickly look away, realizing I have been staring far longer than I should have."
    "I follow my classmates as they head out for the day"
    ## TODO: stop classroom theme
    ## TODO: start light winter theme
    "Classes are done, I am not sure what else I can do other than unpack my things in my dorm."
    "Well, I guess I could go walk around the school. I have the rest of the day to myself, and I'm not exactly eager to head to my room."
    "Screw it, I'll looking around a bit. I walk outside the big double doors and start walking toward the adjacent building."
    scene art building outside
    "It's a big building that looks significantly different than the main campus. I walk through the front door and I immediately know why it looks so different."
    "It's the art building. Various artworks covering a wide range of mediums and styles line the walls, from hyper-realistic drawings to abstract works."
    scene art building hallway
    "I keep walking down the hallway towards some faint singing, echoing down the long hall. I don't want to intrude just in case it's a class...maybe just a peek."
    "Classes are out for the day, and it doesn't sound like there's an instructor in there, maybe just a peek."
    "I carefully walk over to some doors, the source of the singing."
    "With my shoes now muffled by carpeting, I press my ear up into the door."
    "There is definitely someone in there, I can't tell if anyone is playing music or if someone is singing along to music."
    "Taking a step back, I look at the plaque next to the doors."
    "This is the school's theatre."
    "I move to the door again, and turn the handle as slowly as possible, making sure to not make any noise."
    ## TODO: scene name "Mouth Breather"
    scene school theatre hiding
    ## TODO: maybe not the hiding bg?
    ## TODO: heiwako theme
    "The theatre is almost pitch black except for some lights on stage. I slowly tip-toe my way behind the first row of chairs."
    "I can make out two girls on stage."
    ## TODO: heiwako and rina dynamic
    "There are two girls on stage, a girl with light brown hair in twin tails but they aren't too outwardly defined."
    "The other girl is taller, she is a bit thinner than the other girl, but her skin is very pale."
    "She has very long hair, almost like a pale-yellow color."
    "The pale girl's back is facing me and she is singing as the other girl plays on her cello, come to think of it she looks a bit like the pale girl from my class."
    "Wait, I think that is her."
    "The girl on the cello stops playing and looks in my direction!"
    "Realizing she can see me, I duck out of sight."
    ## TODO: thump sfx
    "Shit, they probably think I am some creep or something! Was that technically spying?! Oh crap this was a mistake. Wait, I think they're talking."
    u "Hey, why did you stop?"
    u "Well, I was wondering if you wanted to keep going? I mean we do have an audience now."
    u "I don't see anyone out there."
    u "I can hear him breathing."
    "Seriously?! Guess there's no point in hiding if one of them has that kind of ability."
    mc "You can hear me breathing?!"
    "I stand up and ask, trying to dodge the obvious question of why I was peeping."
    palegirl "Oh hey, you're the new guy, aren't you?"
    "I guess it is the girl from class."
    mc "Yeah, but I should probably go. I'm really, really sorry. I didn't mean to spy on you or anything."
    palegirl "No, no, it's fine really."
    twintailsgirl "At least introduce yourself before you run off."
    "I guess I don't have much of a choice now. I make my way down the middle aisle and hop up on the elevated stage."
    scene school theatre stage
    show heiwako normal at tq_left
    show rina normal at tq_right
    "The girl playing the cello is still sitting down but she is gently setting down her instrument, I don't see anything \'wrong\' with her, although something does seem a bit off."
    show rina talking
    palegirl "Sorry, I didn't introduce myself earlier, I am Rina Uta."
    mc "It's nice to meet you, you already know me, so no need for introductions, I guess."
    "We both giggle as teh girl with the twin-tails stands up, brushes off her skirt, and gives me a little smirk."
    show heiwako talking
    twintailsgirl "Well, maybe not for her, but I still haven't made your acquaintance. My name's Heiwako Inasao."
    "Heiwako extends her hand with a smile and looks right at me."
    hwk "So, Rina said you're new here?"
    mc "Oh, yeah. It's my first day actually."
    "I say, accepting her handshake."
    show heiwako smile
    hwk "I think you'll like it here, the people here are really nice. Well, most of them, but I guess that applies to most places."
    show rina normal
    rna "So, how did you like the music? Who did you like best?"
    "Oh, great. I just met them and they're already making me choose sides. This is definitely what I need right now."
    mc "You were both really, really good, but I don't think I should be picking sides just after meeting you two."
    "They both giggle."
    rna "That reminds me, Heiwako, have you heard of the thea-"
    ## TODO: phone vibrate sfx
    show heiwako surprise
    hwk "Oh, I'm sorry, that's my alarm."
    "She reaches to the cloor and picks up her phone. She presses a button on it, looks in between the two of us and pulls the hair out of her eyes, flashing a small, apologetic smile."
    show heiwako bashful
    hwk "I'm sorry but I have to go, it was nice meeting you Hayato. Rina do you mind...?"
    show rina handwave
    rna "Oh, no, don't worry about it. I think our new friend here can handle the heavy lifting."
    show rina normal
    show heiwako smile
    hwk "Thank you so much, I'll see you around, Hayato."
    "Heiwako giggles and stands up."
    ## TODO: stand up movement
    "She reaches into her pocket and with a flick of her wrist a retractable cane snaps out. She waves at Rina, turns around and walks out through the back of the theatre."
    show heiwako smile with moveoutleft
    ## TODO: stop heiwako theme
    ## TODO: rina theme
    "Wait."
    show rina giggle
    "I look over at Rina, she smirks and tries to stifle a laugh."
    rna "She loves doing that to folks who don't know her. She knows just where to look, and what to do to make you think nothings the matter and then at the last second she'll throw you that curveball."
    mc "I feel a bit bad. Should I feel bad?"
    show rina talking
    rna "Nah, you don't know her, it can't be helped. Do you think you coul dhelp me out with this? I understand, if not."
    "Yeah, I don't remember agreeing to helping with anything, but it's hard to say no to cute girls."
    menu:
        "\"Sorry, I gotta get going.\"":
            jump nohelprina
        "\"Sure, where does it need to go?\"":
            jump helprina


label gotoclassfirst:
    mc "fuck"

label sit_between:

label nohelprina:

label helprina:
    "Sure, where does it need to go?"
    show rina smile
    rna "Oh wonderful! Thank you so much! Just over here."
    "Heiwako had laid her cello next to her carrying case."
    "As gently as possible, I pull the heavy instrument off the stage floor and set it into the felt lining of the case."
    "I grab her bow, and set it in the cutout slot. After fiddling with the locks on the case, I have it closed and secure."
    "Lifting it up on its base is though, I have to handle it with care, but it's so heavy I can't help but manhandle it a bit."
    
