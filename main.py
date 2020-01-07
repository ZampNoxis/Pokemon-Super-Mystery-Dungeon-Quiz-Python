import random
import questions

# Function for prompting the user to input their choice corresponding to the two choices
def input_func():
    return int(input("\nEnter 1 or 2: "))

# Initialize all 5 values to False
sunny = calm = flexible = serious = cooperate = False
# TODO: Turn inputs and if-else statements into a function with a while loop
q1_var = random.choice(questions.question1)
print(q1_var)

# The two questions for question 1 are randomly picked. The corresponding answers are outputted depending on the
# question picked.
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
                                # TODO: If-else statements for all 5 boolean values
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
