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
    


label sit_between:

label gotoclassfirst:
    mc "fuck"
