import random
import questions

# Function for prompting the user to input their choice corresponding to the two choices
def input_func():
    return int(input("\nEnter 1 or 2: "))

# Initialize all 5 values to False
sunny = calm = flexible = serious = cooperate = False

print(random.choice(questions.question1))

# The two questions for question 1 are randomly picked. The corresponding answers are outputted depending on the
# question picked.
if random.choice(questions.question1) == questions.question1[0]:
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
    else:
        pass

        print(random.choice(questions.question2))

        if random.choice(questions.question2) == questions.question2[0]:
            print(questions.q2_answers[0])
        else:
            print(questions.q2_answers[1])

        input_choice = input_func()
        if input_choice == 1 or input_choice == 2:
            if input_choice == 1:
                calm = True
            else:
                pass

                print(random.choice(questions.question3))

                if random.choice(questions.question3) == questions.question3[0]:
                    print(questions.q3_answers[0])
                else:
                    print(questions.q3_answers[1])

                input_choice = input_func()
                if input_choice == 1 or input_choice == 2:
                    if input_choice == 1:
                        flexible = True
                    else:
                        pass

                        print(random.choice(questions.question4))

                        if random.choice(questions.question4) == questions.question4[0]:
                            print(questions.q4_answers[0])
                        else:
                            print(questions.q4_answers[1])

                        input_choice = input_func()
                        if input_choice == 1 or input_choice == 2:
                            if input_choice == 1:
                                serious = True
                            else:
                                pass

                                print(random.choice(questions.question5))

                                if random.choice(questions.question5) == questions.question5[0]:
                                    print(questions.q5_answers[0])
                                else:
                                    print(questions.q5_answers[1])

                                input_choice = input_func()
                                if input_choice == 1 or input_choice == 2:
                                    if input_choice == 1:
                                        cooperate = True
                                    else:
                                        pass
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
