def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Skriv (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess, options[0][question_num-1])
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess, points):

    if answer == guess:
        print("CORRECT!")
        return points[1]
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTAT")
    print("-------------------------")

    print("Svar: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Gæt: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Din score er: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Vil du spille igen? (ja eller nej): ")
    response = response.upper()

    if response.upper() == "JA":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
}

options = [[["A. Guido van Rossum", 10], ["B. Elon Musk", 2], ["C. Bill Gates", -1], ["D. Mark Zuckerburg", 15]]]

new_game()

while play_again():
    new_game()

print("Godt spillet!")