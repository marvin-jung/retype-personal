import sys, time, os

"""
    ### Introduction: Game Info ###

    You’re getting into a future world, also you will meet a nearest and dearest 
    friend of Yoshimi. As you expected from the game title, you will be in a danger 
    and experienced a series of threats from artificial interlligence machines. 
    Together with your friend Yoshimi, the pair must clear the four main quests 
    (including bonus stage). 

    Quest 1: Choose from the options
    Quest 2: Win the enemies with a random skill guess 
    Quest 3: True or False guess game
    Bunus Quest: Number Guess game

    ### Known Bugs and/or Errors ###
    quit() or exit() funtion can't work in the Jupyter Notebook
      1. After a user failed the game, 'Would you like to play again? ( Yes / No )'
         message keeps looping although he/she entered 'No'. (But, No bug happened on the Powershell Prompt)
      2. Although a user takes the victory of the game, the quiz input message keeps looping.
         Therefore, the user must interrupt kernel after the final victory.
         (But, No bug happened on the Powershell Prompt)
    
"""

####################################################################################
### Classes for Text Animation - typewriter, progressbar, initalizing, interlude ###
####################################################################################

def typewriter(message) :
    import sys, time, os
    for char in message :
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n" :
            time.sleep(0.1)
        else :
            time.sleep(1)

def progressbar(it, prefix="", size=60, file=sys.stdout) :
    import sys
    sys_count = len(it)
    def show(j):
        x = int(size * j / sys_count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, sys_count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def initalizing() :
    n = 50  # or however many loading slots you want to have
    load = 0.05  # artificial loading time!
    loading = '.' * n  # for strings, * is the repeat operator

    print("Initalizing the game...")
    for m in range(n+1):
        # this loop replaces each dot with a hash!
        print('\r%s Loading at %3d percent!' % (loading, m*100/n), end='')
        loading = loading[:m] + '#' + loading[m+1:]
        time.sleep(load)

def interlude() :
    import time
    for i in progressbar(range(15), "Processing: ", 50):
        time.sleep(0.1) # any calculation you need

###################
###  Game Over  ###
###################

def fail() :
    retake_yes = ['Y', 'y', 'Yes', 'yes']
    retake_no = ['N', 'n', 'No', 'no']
    
    print(f"\n    We're sorry to say that you’re failed to conquer the quest. Game over!")
    
    while True :
        retake = input("\n    Would you like to play again? ( Yes / No ) ")

        if retake in retake_yes :
            print("\n\n")
            break

        elif retake in retake_no :
            print(f"\n    Bye! See you next time.\n")
            exit(0)

        # Spelling Check
        else :
            print("\n    Invalid input format. Check your spelling!\n")

    if retake in retake_yes :
        GameStart()

def end() :
    exit(0)

####################
###  Start Game  ###
####################

def GameStart() :
    initalizing()
    
    # Ask player name and home country.
    player = input("\n\n    Hello and welcome to the game. May I ask for your name please? ")
    print(f"    Yay. I am so excited to see you, {player}.\n")
    country = input("    Where are you from? ")
    print(f"    Pardon me ??, Oh my god. I know the {country}. That‘s so nice, beautiful, cool and awesome place.")

    print("""
    Now, it’s time to tell you where you are. 
    Here you stay in the San Francisco city where becomes famous for ‘cyberfunk’ and today is 
    the Columbus Day in 2081. 
    Compared to 2020, the city changed a lot with technological innovations such as flying cars, 
    teleportation, robot bartender and so on.
    It happened many bitter wars and many unusual weather phenomena for decades. But this year 
    we are enjoying peace, no wars or violent conflits going on.
    """)
    input("    Press any key to continue")

    UnionSquare()

###############################
###  Quest 1: Union Square  ###
###############################

def UnionSquare() :
  
    quiz_1_count = 2 # Maximum Tries for Quiz 1
    quiz_2_count = 3 # Maximum Tries for Quiz 2

    print("""
    Sencing chilled vibe at the Union Square, you’re eating the brunch in the cafeteria 
    with your lovely and dearest friend Yoshimi. 
    She was born from Japan. She is satisfying running her own detective agency and 
    she is very energetic, enthusiastic in exploring and dealing with social issues. 

    Since she knows that you're interested in Japanese language, she is about to give 
    you a quiz as regards Japanese symbols.
    """)

    input("    Press any key to continue")

    ######################
    ###  Quiz 1 Start  ###
    ######################

    print("""
    “Hey, can you hear the music playing in the cafeteria? This song is 'Do You Realize' 
    recorded by The Flaming Lips.” I really like the lyrics of the song. And I just 
    come up with a quiz for you. I will pick three phrases on the song then show you them
    in Japanese and English. I would like you to choose the one, a valid English interpretation, 
    from three options.

    1) 君は一番美しい顔をしている。= Happiness makes you cry
    2) 君の知っている人は皆、いつか死ぬ。= Everyone you know someday will die.
    3) 幸せだと泣きたくなる。= You have the most beautiful face.
    """)
    
    while (quiz_1_count > 0) :
        try :
            quiz_1 = int(input(f"Choose between 1 and 3 >>> "))
        
        # Validate Inputs only Number
        except ValueError: 
            print(f"    Invalid input format. Please enter a number between 1 - 3\n")
            continue

        # Validate Inputs only 1, 2, 3
        if quiz_1 :
            if quiz_1 < 1 or quiz_1 > 3 :
                print("Out of choice. You must choose number between 1 and 3\n")
                continue

        # Mission Success
        if 2 == quiz_1 :
            print("""
    That’s correct. Awesome!! 
    Meanwhile, 幸せだと泣きたくなる。means ‘Happiness makes you cry’ 
    and 君は一番美しい顔をしている。means You have the most beautiful face. 
        """)
            input("    Press any key to continue")
            break
        
        # Try again
        if 1 == quiz_1 or 3 == quiz_1 :
            if quiz_1_count > 1 :
                print("\n    That’s incorrect. You selected wrong statement. Make a guess again.\n")
            elif quiz_1_count == 1 :
                print("\n    That’s incorrect. You selected wrong statement. \n")
            quiz_1_count = quiz_1_count - 1
            
        # Mission Failed
        if quiz_1_count == 0 :
            fail()

    ######################
    ###  Quiz 2 Start  ###
    ######################

    print("""
    Quite a while you are having fun with her, a breaking news alerts on your Twitter.

    "A terrible crash happened on Oracle Park in SF. A group of armed pink robots terrify 
    and terrorise east of San Francisco. They killed 11 security forces and injured dozens
    of civilians."
    """)

    input("    Press any key to continue")

    print("""
    As Yoshimi is a strong and brave lady, she wants to fight with those evil robots. 
    She believes she can disrupt them with her particular combat skill. 
    What is her super speciality?

    1) Karate
    2) Shot guns 
    3) Crossbow
    4) Beast animal control
    """)

    while (quiz_2_count > 0) :
        try :
            quiz_2 = int(input(f"Choose between 1 and 4 >>> "))
        
        # Validate Inputs only Number
        except ValueError: 
            print(f"    Invalid input format. Please enter a number between 1 - 4\n")
            continue

        # Validate Inputs only 1, 2, 3, 4
        if quiz_2 :
            if quiz_2 < 1 or quiz_2 > 4 :
                print("Out of choice. You must choose number between 1 and 4\n")
                continue

        # Mission Success
        if 1 == quiz_2 :
            print("""
    That’s correct. she's a black belt in Karate and she had an unofficial record 
    for beating a men’s UFC champion in 2079. 
    She determined to discipline her body after she watched ‘Karate Kid’ film series
    when she was a kid.
        """)
            break

        # Try again
        if 2 == quiz_2 :
            print("""
    That’s incorrect. Although she is good at tactical shotguns, the robots are so swift
    that they can dodge bullets very easily.
        """)
            quiz_2_count = quiz_2_count - 1

        if 3 == quiz_2 :
            print("\n    That’s incorrect. Regret to say, she’s never triggered crossbow before.\n")
            quiz_2_count = quiz_2_count - 1

        if 4 == quiz_2 :
            print("\n    That’s incorrect. She can resist against savage beasts, but she is not able to control them.\n")
            quiz_2_count = quiz_2_count - 1

        # Mission Failed
        if quiz_2_count == 0 :
            fail()

    # Go to next Quest
    if 1 == quiz_2 :
        typewriter("    Congratulation! You break the Quest 1, let’s move forward to Quest 2.\n")
        input("\n    Press any key to continue")
        print("")
        interlude()
        OraclePark()


##############################
###  Quest 2: Oracle Park  ###
##############################

def OraclePark() :
  
    # Call randint function
    from random import randint

    ##########################
    ###  Game Instruction  ###
    ##########################

    print("""
    Now you arrive at the Oracle Park. 
    
    There are evil-natured pink robots which are programmed to destroy human. It would be tragic if those evil robots win. 
    Like major sport ‘best-of-five’ playoff, there will be five matches as opposed to them.
    You must win at least three games to take the victory.

    It's demanding to defeat those evil machines. You’re going to support Yoshimi who fights
    against them by providing marvelous vitamin capsules that will give her potent abilities
    for a limited time.
    """)
    
    input("    Press any key to continue")

    print("""
    Vitamin capsules have 3 main benefits, each with a particular function. 
    However, unfortunately it is impossible for you to provide all benefits at one time. 
    So, you are required to make a single pick per each match.

        A. endurance - improves defense skills and get her vitality boosted
        B. speed -  increases her movement that attack 50% faster 
        C. power - triggers a burst of energy that strikes critical damages
    """)
    
    input("    Press any key to continue")

    print("""
    Likewise, pink robots comprises mixed AI machines that has particular capacity.  
    It means your choice can be super effective that make enemy vulnerable or become 
    no effectiveness because they also strong against her ability.

    I hope you remind that following principle will work for the game:

        A. endurance vs speed --> speed wins
        B. speed vs power --> power wins
        C. power vs endurance --> endurance wins
    
    Now it’s time to jump ride in. If you get ready to first match
    """)

    input("    Press any key to continue")

    #######################
    ###  Mission Start  ###
    #######################

    # Setup Choices: 1. endurance / 2. speed / 3. power
    v = [1, 2, 3]
    choose = ["endurance", "speed", "power"]
    dict_choose = {v[0]:choose[0], v[1]:choose[1], v[2]:choose[2]}
    inv_dict_choose = {v: k for k, v in dict_choose.items()}  # Reverse dictionary = {"endurance": 1, "speed": 2, "power": 3}

    # Setup Round and Score
    i = 0
    win_score = 0
    lose_score = 0
    draw_score = 0

    # Round 1 to 5
    while i < 5:
        human = input(f"\n    Round {i + 1} Pick \n\n    {v[0]}. {choose[0]}\n    {v[1]}. {choose[1]}\n    {v[2]}. {choose[2]}\n\n    >>> ")
        robots = v[randint(0,2)]

        # Validate Inputs only 1, 2, 3
        if human.isdigit() :
            if int(human) < 1 or int(human) > 3 :
                print("    Out of choice. You must choose number between 1 and 3\n")
                continue
            else:
                print(f"\n    You picked {dict_choose[v[int(human)-1]]}, Good Luck !!\n")
            
        # Validate Inputs only endurance, speed, human
        else :        
            if 'endurance' and 'speed' and 'power' not in human :
                print("    Invalid input format. Check your spelling!\n")
                continue
            else:
                print(f"\n    You picked {human}, Good Luck !!\n")

        
        input("    Press any key to continue..")

        # Assumption & Logic (https://rosettacode.org/wiki/Rock-paper-scissors#Python)
            ## 0 is always a draw, 
            ## -1 is always a lose, -2 is a win, 
            ## 1 is a win and 2 is a loss
        
        if human.isdigit() :
            calc = int(human) - robots
        else:
            calc = inv_dict_choose[human] - robots  # Caculation with reverse dictionary 

        # Display victory result
        if calc in (1, -2) :
            if human.isdigit() :
                print(f"\n    Hooray~ She won the round {i + 1} ==> {dict_choose[int(human)]} wins over {dict_choose[robots]}")
            else:
                print(f"\n    Hooray~ She won the round {i + 1} ==> {human} wins over {dict_choose[robots]}")
            win_score += 1

        # Display defeat result
        elif calc in (-1, 2) :
            if human.isdigit() :
                print(f"\n    Opps! Robots won the round {i + 1} ==> {dict_choose[robots]} wins over {dict_choose[int(human)]}")
            else:
                print(f"\n    Opps! Robots won the round {i + 1} ==> {dict_choose[robots]} wins over {human}")
            lose_score += 1

        # Display draw result
        else :
            if human.isdigit() :
                print(f"\n    Round {i + 1} is draw! ==>  Both are same {dict_choose[int(human)]}")
            else:
                print(f"\n    Round {i + 1} is draw! ==>  Both are same {human}")
            draw_score += 1

        # Display cumulative score
        print(f"\n    Cumulative Score >> Win: {win_score} Lose: {lose_score} Draw: {draw_score} \n")
        print("   ", "-" * 60)
        
        # Next Round
        i += 1

    # Mission Success
    if win_score > 2 :
        print("""
    Victory! you destroy enemies and save the planet. However, they were just Stormtroopers 
    of the giant pink robot.
    Now, the most powerful opponent is waiting for you at the Alcatraz Island.
    Let's go forward the Alcatraz Island and challenge the final boss.
        """)
        
        typewriter("    Congratulation! You break the Quest 2, let’s move forward to Quest 3.\n")
        input("\n    Press Enter to continue")
        print("")
        # Go to next Quest
        interlude()
        Alcatraz()

    # Mission Failed
    else :    
        fail()


##################################
###  Quest 3: Alcatraz Island  ###
##################################

def Alcatraz() :
    # Call random function
    import random

    ##########################
    ###  Game Instruction  ###
    ##########################   
    
    print("""
    Now you arrive at the Alcatraz Island. 

    You and Yoshimi stand opposed to the giant pink robot, the overwhelming menace of the rogue. 
    In this battle, you need to support Yoshimi who is fighting against the strongest enemy. 
    Your mission is testing your knowledge – and learn some interesting things along the way.
    We prepared some tricky statements for you. You are going to differentiate the statements 
    whether each statement is true or false.
    
    There exists 30 statements you have to think of. If you reply a right answer, you will get 
    +1 point score, otherwise you will lose -1 point score. The game will be stopped in the moment
    whether you earn +5 point for victory or run out of -5 point for defeat. 
    Unless you gain +5 point score before you complete 30 statements, you will be failed this 
    mission.
    """)
    
    input("    Now it’s time to jump ride in. If you get ready to last match, press Enter to continue")

    # List of questions
    Quiz = [
        ['Prince Harry is taller than Prince William', 'F', 'False', 'Prince William is 1.91m, Prince Harry is 1.86m'],
        ['The star sign Aquarius is represented by a tiger', 'T', 'True'],
        ['Meryl Streep has won two Academy Awards', 'F', 'False', 'she\'s won three! She won Best Actress for The Iron Lady in 2012, Best Actress for Sophie\'s Choice in 1983, Best Supporting Actress for Kramer vs. Kramer in 1980.'],
        ['Marrakesh is the capital of Morocco', 'F', 'False', 'it\'s Rabat'],
        ['Idina Menzel sings \'let it go\' 20 times in \'Let It Go\' from Frozen', 'F', 'False', 'she sings it 21 times!'],
        ['Waterloo has the greatest number of tube platforms in London', 'T', 'True'],
        ['M&M stands for Mars and Moordale', 'F', 'False', 'M&M stands for Mars and Murrie'],
        ['Gin is typically included in a Long Island Iced Tea', 'T', 'True', 'as is vodka, white rum, lemon juice, triple sec, sugar syrup and Coca-Cola'],
        ['The unicorn is the national animal of Scotland', 'T', 'True'],
        ['There are two parts of the body that can\'t heal themselves', 'F', 'False', 'there\'s only one: the teeth.'],
        ['Howard Donald is the oldest member of Take That', 'T', 'True', 'He was born in 1968, while Jason Orange was born in 1970, Gary Barlow was born in 1971, Mark Owen in 1972 and Robbie Williams in 1974'],
        ['The Great Wall of China is longer than the distance between London and Beijing', 'T', 'True', 'London to Beijing is only 8,136km, The Great Wall of China is 21,196.18km'],
        ['There are 219 episodes of Friends', 'F', 'False', 'there are 236'],
        ['\'A\' is the most common letter used in the English language', 'F', 'False', '\'E\' is the most common letter and appears in 11 percent of all english words, according to Oxford Dictionaries'],
        ['A lion\'s roar can be heard up to eight kilometres away', 'T', 'True'],
        ['In Harry Potter, Draco Malfoy has no siblings', 'F', 'False', 'Skylar Malfoy is his younger sister'],
        ['Louis Walsh is older than Simon Cowell', 'T', 'True', 'at the time of writing, Louis Walsh is 67 while Simon Cowell is 60'],
        ['Monaco is the smallest country in the world', 'F', 'False', 'Vatican City is, with only 0.44 sq.km.'],
        ['\'What Do You Mean\' was Justin Bieber\'s first UK number one single', 'T', 'True'],
        ['The river Seine in Paris is longer than the river Thames in London', 'T', 'True', 'The Seine is 777km, while the Thames is 346km'],
        ['A cara cara navel is a type of orange', 'T', 'True'],
        ['There are five different blood groups', 'F', 'False', 'There are four: A, B, AB, and O'],
        ['Cinderella was the first Disney princess', 'F', 'False', 'Snow White and the Seven Dwarfs was released first in December 1937'],
        ['ASOS stands for As Seen On Screen', 'T', 'True'],
        ['The Battle Of Hastings took place in 1066', 'T', 'True'],
        ['H&M stands for Hennes & Mauritz', 'T', 'True'],
        ['Canis lupur is the scientific name for a wolf', 'F', 'False', 'It\'s Canis lupus'],
        ['K is worth four points in Scrabble', 'F', 'False', 'It\'s worth five'],
        ['Alaska is the biggest American state in square miles', 'T', 'True', 'It spans a total area of 665,384 square miles. Texas comes in next with a total area of 268,596 square miles.'],
        ['Ariana Grande is 25 or under', 'F', 'False', 'she turned 26 on 25 June 2019'],
        ['Australia is wider than the moon', 'T', 'True', 'The moon sits at 3400km in diameter, while Australia\'s diameter from east to west is almost 4000km'],
        ['Queen Elizabeth II is currently the second longest reigning British monarch', 'F', 'False', 'Queen Elizabeth II became the longest-reigning British monarch on 9 September 2015 when she surpassed the reign of her great-great-grandmother Victoria.'],
        ['Madonna\'s real name is Madonna', 'T', 'True', 'Madonna Louise Ciccone in full'],
        ['Serena Williams has one more singles tennis Grand Slam titles than sister Venus', 'T', 'True', 'As of June 2020, Venus has won 49 singles titles, and Serena has won 72.'],
        ['Alexander Fleming discovered penicillin', 'T', 'True']
        ]

    score_board = [
        [-5, "[-5 #####|      +5]"],
        [-4, "[-5  ####|      +5]"],
        [-3, "[-5   ###|      +5]"],
        [-2, "[-5    ##|      +5]"],
        [-1, "[-5     #|      +5]"],
        [0, "[-5      |      +5]"],
        [1, "[-5      |#     +5]"],
        [2, "[-5      |##    +5]"],
        [3, "[-5      |###   +5]"],
        [4, "[-5      |####  +5]"],
        [5, "[-5      |##### +5]"],
    ]

    # Setup random sampling, count and score
    order = random.sample(range(1,35),30) 
    count = 1
    score = 0

    ##################################
    ###  True or False Game Start  ###
    ##################################

    for i in order:        
        # Answer T or F
        print("\n")
        print("   ", "-" * 45)
        print(f"    Seq: {count} / 30    Score :   {score_board[score + 5][1]}")
        print("   ", "-" * 45)
        print("\n    Statement : \'%s\'" %Quiz[i][0])
        response = input("\n    Enter T or F:  ")
        if response == 'T' or response == 't' or response == 'F' or response == 'f' :
            pass
        else :
            # Validate Inputs only T, F
            print("    Input T or F properly, otherwise you'll lose this opportunity!")
            response = input("\n    Enter T or F:  ")

        # Compare response with answer
        if response.upper() == Quiz[i][1] :
            print(f"\n    Correct. That's right!\n")
            score += 1
        else:
            print(f"\n    Incorrect, That's wrong choice.\n")
            score -= 1

        # Tell answers and explanations
        # If explanation is missing, show only answer
        try :
            print("    Answer is \"%s\"." %Quiz[i][2], "%s" %Quiz[i][3])
        except :
            print("    Answer is \"%s\"" %Quiz[i][2])

        # Mission Success
        if score == 5 :
            print("\n")
            print("   ", "-" * 45)
            print(f"    Victory!!        Score :   {score_board[score + 5][1]}")
            print("   ", "-" * 45)
            print("\n")
            # print("Victory! Ultimately, as the dawn began to break, The giant pink robot surrendered.")
            # print("Now, the most powerful opponent is waiting for you at the Alcatraz Island.")
            # print("Let's jump into the Alcatraz Island and challenge the final boss.")
            # input("Press Enter to continue..")
            break
        
        # Mission Failed
        elif score == -5 :
            print("\n")
            print("   ", "-" * 45)
            print(f"    Defeat !!        Score :   {score_board[score + 5][1]}")
            print("   ", "-" * 45)
            print("\n")
            break
        count += 1
    
    if score == 5 :
        print("""
    Victory! When the dawn began to break, the giant pink robot surrendered. 
    The robot promised us not to make an attack on human again. Then it delivered 
    oneself to the FBI police.
        """)

        input("    Press Enter to continue")
        
        print("""
    Millions of people saw the victory on news program around world.  
    As the award, a big ceremony happened from government. 
    Yoshimi was joyful for the reason that she can finally go home and get back to 
    being a detective agent. You were also so proud of yourself that you had 
    the greatest match in history.
        """)

        typewriter("    Congratulation! You break the Quest 3, let’s move forward to Bonus Quest. \n")
        input("\n    Press Enter to continue")
        print("")
        interlude()
        BonusStage()

    # Mission Failed
    else :    
        fail()

##############################
###  Quest 4: Bonus Stage  ###
##############################

def BonusStage() :
    # Call randint function
    from random import randint
    
    ##########################
    ###  Game Instruction  ###
    ##########################   

    print("""
    One week later…  

    You and Yoshimi has met again at a cafe in Filmore street. She says she always be thankful 
    to you. And she express her appreciation for the small gift. But she won’t give you the gift
    if you can’t find out the lucky number between 1 - 99.

    “Let’s go ahead. You’ve got a ultimate mission to complete!”

    “Yes, for sure!”
    """)
    input("    Press Enter to continue")

    #######################
    ###  Mission Start  ###
    #######################
    
    countdown = 7 # Maximum Tries
    answer = randint(1,99) # Random number
    
    while (countdown > 0):
        try:
            guess = int(input(f"\n    You have {countdown} attempt(s) remaining. Take a guess between 1-99 lucky number: "))
        
        # Validate Inputs only Number
        except ValueError :
            print(f"    Invalid input format. Please enter a number between 1 - 99\n")
            continue    
        
        if guess < 1 or guess > 99:
            print(f"    Out of range. You must guess a lucky number between 1 - 99\n")
            continue
        
        # Mission Success
        if answer == guess :
            
            if countdown > 6 :
                print(f"\n    Fantastic!!!! How could you guess the lucky number at one time? Awesome!!!\n")
                print("    Here's our prize for you : https://bit.ly/2T77ALr\n")
                typewriter("    Thank you for enjoying our game :D\n\n")
                end()
            
            else :
                print(f"\n    Congrats. You guessed the lucky number in {8 - countdown} attempts. Well done!\n")
                print("    Here's our prize for you : https://bit.ly/2T77ALr\n")
                typewriter("    Thank you for enjoying our game :D\n\n")
                end()
        
        # Try again
        elif answer > guess :
            print("    Try again. Your guess is lower than mine")
        elif answer < guess :
            print("    Try again. Your guess is higher than mine")
        
        countdown = countdown - 1
        
        # Mission Failed
        if (countdown == 0):
            typewriter(f"\n    Sorry. The answer is {answer}.")
            typewriter("    You are out of tries. Better luck next time.\n\n")
            fail()

GameStart()