import random
import lists


# Function for prompting the user to input their choice corresponding to the two choices
def input_func():
    return int(input("\nEnter 1 or 2: "))


# Initialize all 5 values to False
sunny = calm = flexible = serious = cooperate = False

# TODO: Turn inputs and if-else statements into a function with a while loop
# One of the two questions for question 1 are randomly picked and assigned to a variable. The corresponding answers are
# outputted depending on the question picked.
q1_var = random.choice(lists.questions[0])
print(q1_var)

if q1_var == lists.questions[0][0]:
    print(lists.answers[0][0])
else:
    print(lists.answers[0][1])

# User is prompted to input either 1 or 2. Otherwise the program ends.
input_choice = input_func()

# If-else statement continues if the input is either 1 or 2. The value for sunny is set to true if 1 was picked.
# Otherwise, the value remains false and the program continues.
if input_choice == 1 or input_choice == 2:
    if input_choice == 1:
        sunny = True

    q2_var = random.choice(lists.questions[1])
    print(q2_var)

    if q2_var == lists.questions[1][0]:
        print(lists.answers[1][0])
    else:
        print(lists.answers[1][1])

    input_choice = input_func()
    if input_choice == 1 or input_choice == 2:
        if input_choice == 1:
            calm = True

        q3_var = random.choice(lists.questions[2])
        print(q3_var)

        if q3_var == lists.questions[2][0]:
            print(lists.answers[2][0])
        else:
            print(lists.answers[2][1])

        input_choice = input_func()
        if input_choice == 1 or input_choice == 2:
            if input_choice == 1:
                flexible = True

            q4_var = random.choice(lists.questions[3])
            print(q4_var)

            if q4_var == lists.questions[3][0]:
                print(lists.answers[3][0])
            else:
                print(lists.answers[3][1])

            input_choice = input_func()
            if input_choice == 1 or input_choice == 2:
                if input_choice == 1:
                    serious = True

                q5_var = random.choice(lists.questions[4])
                print(q5_var)

                if q5_var == lists.questions[4][0]:
                    print(lists.answers[4][0])
                else:
                    print(lists.answers[4][1])

                input_choice = input_func()
                if input_choice == 1 or input_choice == 2:
                    if input_choice == 1:
                        cooperate = True
                    for x in range(50):
                        print('-', end='')

                    if not sunny and not calm and not flexible and not serious:
                        # Unmoving
                        print(lists.results[0])
                    elif not sunny and not calm and serious and not cooperate:
                        # Man
                        print(lists.results[1])
                    elif not sunny and not calm and not flexible and serious and cooperate:
                        # Docile
                        print(lists.results[2])
                    elif not sunny and not calm and flexible and not serious and not cooperate:
                        # Man
                        print(lists.results[3])
                    elif not sunny and not calm and flexible and cooperate:
                        # Unmoving
                        print(lists.results[4])
                    elif not sunny and calm and not flexible and not cooperate:
                        # Unmoving
                        print(lists.results[5])
                    elif not sunny and calm and not flexible and cooperate:
                        # Unmoving
                        print(lists.results[6])
                    elif not sunny and calm and flexible and not cooperate:
                        # Docile
                        print(lists.results[7])
                    elif not sunny and calm and flexible and not serious and cooperate:
                        # Comfortable
                        print(lists.results[8])
                    elif not sunny and calm and flexible and serious and cooperate:
                        # Comfortable
                        print(lists.results[9])
                    elif sunny and not calm and not flexible and not serious:
                        # Calm
                        print(lists.results[10])
                    elif sunny and not calm and not flexible and serious:
                        # Calm
                        print(lists.results[11])
                    elif sunny and not calm and flexible and not serious:
                        # Man
                        print(lists.results[12])
                    elif sunny and not calm and flexible and serious and not cooperate:
                        # Docile
                        print(lists.results[13])
                    elif sunny and not calm and flexible and serious and cooperate:
                        # Docile
                        print(lists.results[14])
                    elif sunny and calm and not flexible and not serious and not cooperate:
                        # Man
                        print(lists.results[15])
                    elif sunny and calm and not flexible and cooperate:
                        # Comfortable
                        print(lists.results[16])
                    elif sunny and calm and serious and not cooperate:
                        # Calm
                        print(lists.results[17])
                    elif sunny and calm and flexible and not serious and not cooperate:
                        # Calm
                        print(lists.results[18])
                    elif sunny and calm and flexible and cooperate:
                        # Comfortable
                        print(lists.results[19])
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
