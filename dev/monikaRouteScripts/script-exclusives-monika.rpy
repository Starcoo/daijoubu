label monika_exclusive_1:
    scene bg club_day
    with wipeleft_scene
    "Considering how I'm not too settled into the club at the moment, I don't particularly feel like bothering either Yuri or Natsuki."
    "At the same time, however, I don't want to bother Monika and Sayori's conversation..."
    play music t6 fadeout 1.0
    "I look over at the two of them."
    "They're just next to me and appear to be deep in discussion..."
    show monika 2b at f22 zorder 3
    show sayori 1a at t21 zorder 2
    m "In any case, we really need these new members, Sayori. I'm just not sure that the others are as keen as me, you know?"
    show monika 2a at t22 zorder 2
    show sayori 1j at f21 zorder 3
    s "Yeah..."
    show sayori 1i at t21 zorder 2
    show monika 2e at f22 zorder 3
    m 2f "[player] is the first new member we've had in months. I get that we're already an official club~"
    show monika 2e at t22 zorder 2
    show sayori 2c at f21 zorder 3    
    s "...But it makes you upset that you can't get others interested in literature?"
    show sayori 2b at t21 zorder 2
    show monika 2j at f22 zorder 3
    m "Yes! Exactly!" 
    m 2l "It's {i}so{/i} frustrating!"
    show monika 2j zorder 3
    "As I listen in on their talk, I can't help but notice how passionate Monika is about the club."
    "It makes sense that she would want the best for the club, her being the club president and everything, but I never would have expected someone like her to be so into books."
    show sayori 1b at t21 zorder 2
    show monika 2e at f22 zorder 3
    m 1m "...Though it's not really like I can blame anyone~"
    show monika 1e at t22 zorder 2
    "Monika's eyes meet mine and we gaze at eachother for a moment."
    show monika 3l at f22 zorder 3
    m 3l "...You okay, [player]?"
    "I snap out of the half-awake state I was in and my face reddens slightly."
    show monika 2l at t22 zorder 2
    mc "I-I'm sorry... I was lost in thought..."
    show monika 2j at f22 zorder 3
    m "Aha, don't worry!" 
    m 2b "If anything, I should be the one apologising, I didn't realise you had nothing to read."
    "Well, I do have Yuri's book, but I'm not really feeling like reading right now..."
    m "Sorry Sayori, I'll sort this out with you another time if that's okay~"
    show sayori 1a at f21 zorder 3
    s "Yeah, no problem!"
    hide sayori
    with wipeleft
    "Sayori leaves Monika to go and talk to Natsuki, who is still in the closet."
    show monika 2a at f11 zorder 3
    m "So, [player], since it's your first day at the club, I think it would be good if I helped you settle in!"
    mc "Ah, you don't have to~"
    m 2b "It's my duty as Club President!" 
    "I feel bad for stopping her conversation with Sayori, but Monika seems commited now."
    mc "Well, if you insist..."
    m 3k "Of course! It's my job to please all my club members~"
    "Monika briefly smiles at me."
    m 1b "Anyway, let me think of something we could do..."
    m 4k "Oh, I know!" 
    m 4b "Since you're new to the club, why don't you tell me a little more about yourself?"
    "That's...oddly personal."
    "I'm not bothered by the question, but I would have assumed that her suggestion would be a little more literature based."
    mc "Ah, well...there's not much to know, really."
    m 2a "Aw [player], I'm sure that's not true!"
    mc "Heh, I'd like to think so. But really, all I do is read manga, watch anime and play video games."
    m 2l "...Okay, maybe it is true, aha!"
    mc "Hey!~"
    show monika 3a 
    "I'm a little embarrased, but it's the truth."
    m 3b "Just a joke, [player]! Remember, everyone is more deep and complex than they are willing to let on."
    mc "Ah..."
    show monika 3a
    "Monika's sudden shift in tone catches me by surprise."
    "Though, I guess me thinking that only proves what she said to be true..."
    mc "...Well, anyway, what about you Monika?"
    m 2b "Glad you asked!"
    m 4b"Well, I like literature..."
    m 2l "If you couldn't already tell, aha!"
    m 3j "I really like keeping active too. Running is a great way to stay in shape!~"
    m 2b "And I really enjoy this club. Watching everyone get along so well is really satisfying, you know?"
    mc "Yeah..."
    m 2k "Including you, [player]!"
    show monika 5a
    m "I'm going to make sure you have a great time here, okay?"
    "I nod in agreement."
    m 2b "By the way, do you have a preferred writing style?"
    mc "...Eh?"
    "'Preferred writing style...?'"
    m 1l "Oh, right. I forget that you're kinda new to this stuff. Sorry!"
    mc "Ah, don't worry. I don't want to hold you back or anything."
    m 1b "Let me rephrase the question into a more everyday example."
    "Monika pauses for a second."
    m 3c "...Okay. Do you mystery films, or action movies?"
    mc "Hmm..."
    mc "Well, I don't really watch movies, but I've seen more than my fair share of anime..."
    m 3l "Of course~"
    $ choice = 0
    menu:
        "So I'd have to say..."
        "Mystery films!":
            call detectiveChoice
        "Action movies!":
            call actionChoice
        "Neither!":
            call neitherChoice
    
    if choice == 1:
        m 2m "You know, Yuri's kind of into that stuff..."
        mc "Eh?"
        m 2l "Um, never mind!"
        m 2e "Anyway, based on that... I'd say you should definitely give that book, the one Yuri gave you, a read."
        mc "You think so?"
        "I mean, I was going to read at least some of it anyway..."
        m 3b "Yeah! Yuri's taste in books is usually deep and complex and they need you to read in between the lines..."
        m 2j "Sounds like something you'd be into!"
        mc "You could be right..."
        "There's no harm in at least trying to read it anyway."
        mc "I think I'll do that then. Thanks."
    elif choice == 2:
        m 2m "I hear Natsuki's into that kind of stuff, you know..."
        mc "Hm?"
        m 2l "Um, never mind!"
        m 2e "Anyway, based on that... I'd say you should ask Natsuki about some of her literature."
        mc "Eh?"
        m 3b "Yeah! She's totally into manga, you know? She could give you some good recommendations!"
        m 2j "Manga is usually pretty action-packed and fun, which sounds like something you'd enjoy."
        "Well there's no harm in at least asking..."
        mc "I think I'll do that then. Thanks."
    else:
        m 2b "Anyway, based on that... I'd say that you'd prefer a more mild book to get you started."
        mc "What do you mean?"
        m 2a "A book that's not too deep and not too simple. Something in between, you know?"
        mc "I guess..."
        m 2e "I know you're pretty into manga, but it sounds like you might enjoy something like..."
        m 4j "Oh, I know!"
        hide monika
        with wipeleft
        "Monika walks over to the desk."
        m "Something like this!"
        "She walks back over to me, holding a book of some sort."
        show monika at t21 zorder 3
        mc "What is it?"
        m 2a "It's one of my favorite books. It's called 'Summer Tales'"
        m 2b "To put it simply, it's a collection of short stories that all take place in the summer time."
        m 2d "There's quite a variety in the stories. Some are happy, some are sad and some are bittersweet."
        m 2k "It's quite the read!"
        m 3l "This is my own copy, so don't crease it~"
        "I take the book enthusiastically."
        mc "Thank you, Monika! I'll definitely read this."
        show monika 5a
        m "You're welcome, [player]"
    return

label detectiveChoice:
    $ choice = 1
    mc "I'm gonna have to say mystery films."
    m 1d "Oh?"
    mc "Yeah. I love the way that they often leave in little secrets and clues for those who are attentive."
    show monika 1a
    mc "It's like they're rewarding you for paying attention and reading between the lines..."
    mc "Not only that, but they often get you to think about deeper meanings behind both people and objects."
    mc "It really gets the gears in my head to turn."
    m 2k "Yeah, totally!"
    m 3b "I usually find myself looking for clues in those kinds of movies too."
    m 1l "...Though, most of the time I find myself lost along the way, aha!"
    return

label actionChoice:
    $ choice = 2
    mc "I'm gonna have to say action movies."
    m 1d "Yeah?"
    mc "Mhm. I just love the fast-pace and in-your-face nature of them."
    show monika 1a
    mc "It gets me all riled up and makes me feel like I can do anything I want!"
    mc "And I like how you don't really have to pay too much attention to what's going on."
    mc "They're not overly complicated but you still manage to have fun watching them. And I'm all about fun!"
    m 2k "Yeah, totally!"
    m 3b "I always expect a fun time from an action movie."
    show monika 5a
    m "They're great to watch with friends, too~"
    return

label neitherChoice:
    mc "Honestly...I'm not really into either."
    m 1d "Is that so?"
    show monika 1a
    mc "Yeah. It's not that I think they're bad."
    mc "Don't get me wrong, there are some brilliant mystery films out there. Same with action movies."
    mc "They're both a bit extreme though..."
    m 1c "What do you mean?"
    mc "Ah, well..."
    show monika 1a
    mc "Mystery films often require a lot of intense thought if you want to get the most out of them."
    mc "You're expected to pay attention and pick up on some subtle clues that take you to the end..."
    mc "And I'm just not a fan of that, really. It's extra effort."
    m 2e "Yeah, that's understandable."
    mc "For action movies, it's the opposite end of the same extremity."
    show monika 1a
    mc "They're too simple. They throw in a really loose plot..."
    mc "And try to tie it together with action scenes."
    mc "Sometimes it doesn't connect with me at all."
    mc "Not to mention that half of the time, those 'action' scenes are just a bunch of visual effects..."
    mc "It's kind of like they're trying to hide the flaws in the movie by throwing stuff at you."
    m 3j "Wow [player], I never would've expected you to be so passionate about movies."
    mc "Well, it's like you said..."
    m 2b "'More to people than they are willing to let on', right?"
    m 4k"You've certainly proved that to be true, aha!"
    return

