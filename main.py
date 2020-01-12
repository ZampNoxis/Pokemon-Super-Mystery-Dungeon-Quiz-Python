import random
import questions

# Function for prompting the user to input their choice corresponding to the two choices
def input_func():
    return int(input("\nEnter 1 or 2: "))

# Initialize all 5 values to False
sunny = calm = flexible = serious = cooperate = False

# TODO: Turn inputs and if-else statements into a function with a while loop
# One of the two questions for question 1 are randomly picked and assigned to a variable. The corresponding answers are
# outputted depending on the question picked.
q1_var = random.choice(questions.question1)
print(q1_var)

if q1_var == questions.question1[0]:
    print(questions.q1_answers[0])
else:
    print(questions.q1_answers[1])

# User is prompted to input either 1 or 2. Otherwise the program ends.
input_choice = input_func()

# If-else statement continues if the input is either 1 or 2. The value for sunny is set to true if 1 was picked.
# Otherwise, the value remains false and the program continues.
if input_choice == 1 or input_choice == 2:
    if input_choice == 1:
        sunny = True

    q2_var = random.choice(questions.question2)
    print(q2_var)

    if q2_var == questions.question2[0]:
        print(questions.q2_answers[0])
    else:
        print(questions.q2_answers[1])

    input_choice = input_func()
    if input_choice == 1 or input_choice == 2:
        if input_choice == 1:
            calm = True

        q3_var = random.choice(questions.question3)
        print(q3_var)

        if q3_var == questions.question3[0]:
            print(questions.q3_answers[0])
        else:
            print(questions.q3_answers[1])

        input_choice = input_func()
        if input_choice == 1 or input_choice == 2:
            if input_choice == 1:
                flexible = True

            q4_var = random.choice(questions.question4)
            print(q4_var)

            if q4_var == questions.question4[0]:
                print(questions.q4_answers[0])
            else:
                print(questions.q4_answers[1])

            input_choice = input_func()
            if input_choice == 1 or input_choice == 2:
                if input_choice == 1:
                    serious = True

                q5_var = random.choice(questions.question5)
                print(q5_var)

                if q5_var == questions.question5[0]:
                    print(questions.q5_answers[0])
                else:
                    print(questions.q5_answers[1])

                input_choice = input_func()
                if input_choice == 1 or input_choice == 2:
                    if input_choice == 1:
                        cooperate = True
                    # TODO: Add logic to if-else statements
                    for x in range(50):
                        print('-', end='')

                    if not sunny and not calm and not flexible and not serious:
                        # Unmoving
                        # You're a little shy and perhaps too concerned with others' well-being.
                        #
                        # But that's precisely why you're so kind to those around you.
                        #
                        # That warm, caring personality must be...
                        pass
                    elif not sunny and not calm and serious and not cooperate:
                        # Man
                        # Do people think you're a loner? Or that you have an unapproachable aura?
                        #
                        # The truth is that you're a decisive person who's very sure of yourself!
                        #
                        # That strong personality must be...
                        pass
                    elif not sunny and not calm and not flexible and serious and cooperate:
                        # Docile
                        # You get along with everyone. You're well liked for cherishing your friends.
                        #
                        # You're unambitious and calm, but you're actually a hard worker who everyone admires.
                        #
                        # As popular as you are, you must be...
                        pass
                    elif not sunny and not calm and flexible and not serious and not cooperate:
                        # Man
                        # You always trust your feelings, even if they get you in trouble sometimes.
                        #
                        # But clearly expressing your feelings is proof you want others to understand you.
                        #
                        # A straight shooter like you must be...
                        pass
                    elif not sunny and not calm and flexible and cooperate:
                        # Unmoving
                        # You may get upset a little easily and feel uneasy when you don't fit in.
                        #
                        # But it's your delicate heart that lets you better understand others' feelings.
                        #
                        # With that sensitive personality, you must be...
                        pass
                    elif not sunny and calm and not flexible and not cooperate:
                        # Unmoving
                        # You're sure of yourself and unflappable. You have all the qualities of a leader.
                        #
                        # Just by being around you, others feel more confident.
                        #
                        # That charismatic personality must belong to...
                        pass
                    elif not sunny and calm and not flexible and cooperate:
                        # Unmoving
                        # Some people work hard in the background. You're one of those, aren't you?
                        #
                        # When you're not around, things don't go well. Everyone can always count on you.
                        #
                        # Someone who pulls the strings in the background like that must be...
                        pass
                    elif not sunny and calm and flexible and not cooperate:
                        # Docile
                        # You love tackling new challenges with your calm, cool, collected reasoning.
                        #
                        # You're so smart, you know the answers before you've even heard the question.
                        #
                        # That calm, reliable personality must belong to...
                        pass
                    elif not sunny and calm and flexible and not serious and cooperate:
                        # Comfortable
                        # You know your place and don't overdo things, but you're really motivated.
                        #
                        # Everyone looks to you as an example. You may have many admirers...
                        #
                        # That serene, lovely personality must belong to...
                        pass
                    elif not sunny and calm and flexible and serious and cooperate:
                        # Comfortable
                        # You're never shaken and can always read between the lines. You never give up.
                        #
                        # You're quite likable, and you're always surrounded by friends.
                        #
                        # With a good-natured personality like that, you must be...
                        pass
                    elif sunny and not calm and not flexible and not serious:
                        # Calm
                        # You're very active, maybe too much so.
                        # You may tire others out.
                        #
                        # But you are amazing.
                        # You make the most of your time, after all!
                        #
                        # Being a wee bit impatient, you must be...
                        pass
                    elif sunny and not calm and not flexible and serious:
                        # Calm
                        # You might be a bit of a space cadet, but when it's time to work, you work hard.
                        #
                        # You inspire courage in others without even knowing it.
                        #
                        # With that hardworking personality, you must be...
                        pass
                    elif sunny and not calm and flexible and not serious:
                        # Man
                        # You're a fearless challenger at all times! But you're also quick to give up.
                        #
                        # It's important to try out many different things to see what's right for you, though.
                        #
                        # As playful as you are, you must be...
                        pass
                    elif sunny and not calm and flexible and serious and not cooperate:
                        # Docile
                        # You carry yourself with thunderous authority. You're brave enough to speak your mind.
                        #
                        # You can do anything well, so others rely on you.
                        #
                        # As brave as you are, you must be...
                        pass
                    elif sunny and not calm and flexible and serious and cooperate:
                        # Docile
                        # You're good natured and easygoing. But don't you feel nervous sometimes?
                        #
                        # That unique personality sets those around you at ease.
                        #
                        # As good natured as you are, you must be...
                        pass
                    elif sunny and calm and not flexible and not serious and not cooperate:
                        # Man
                        # You are you. Others are others. You stay true to what you want to do.
                        #
                        # Your actions make everyone feel all right. They all envy you.
                        #
                        # With that ability to make others happy, you must be...
                        pass
                    elif sunny and calm and not flexible and cooperate:
                        # Comfortable
                        # You're friendly and open minded. Aren't you already happy just as you are?
                        #
                        # You're so calm for your age... When you're happy, everyone is happy.
                        #
                        # As mild mannered as you are, you must be...
                        pass
                    elif sunny and calm and serious and not cooperate:
                        # Calm
                        # Everyone believes you're indecisive, but you actually just think before you act.
                        #
                        # Your positivity wins people over. It's no surprise you're so successful!
                        #
                        # With your ability to make everyone feel jolly, you must be...
                        pass
                    elif sunny and calm and flexible and not serious and not cooperate:
                        # Calm
                        # Everyone looks up to you. You're persuasive and get what you want.
                        #
                        # To those around you, your clever actions look really cool.
                        #
                        # As cool as you are, you must be...
                        pass
                    elif sunny and calm and flexible and cooperate:
                        # Comfortable
                        # Who's got time to worry? You're a genius at having fun!
                        #
                        # Your cheerfulness makes everyone smile. Every day is a happy day when you're around!
                        #
                        # With your ability to produce warm, fuzzy feelings all around you, you must be...
                        pass
                    else:
                        print('Please enter either 1 or 2.')
                else:
                    print('Please enter either 1 or 2.')
            else:
                print('Please enter either 1 or 2.')
        else:
            print('Please enter either 1 or 2.')
    else:
        print('Please enter either 1 or 2.')
else:
    print('Please enter either 1 or 2.')
