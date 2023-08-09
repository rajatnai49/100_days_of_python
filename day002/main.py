from data_set import questions


def run_quiz():
    score = 0
    attempted = 0
    for i, question in enumerate(questions, start=1):
        print(f"Q {i}: {question['text']}")
        for idx, choice in enumerate(question['choices'], start=1):
            print(f"{idx}: {choice}")
        user_answer = input("What do you think?: ")
        if (user_answer == "quit"):
            break
        if (int(user_answer) == question['correct_choice']+1):
            score += 1
        attempted += 1
    if (attempted > 10 and score == attempted):
        print("You are true anime nerd ^_~!!")
    elif (attempted > 10 and score >= 7):
        print("You are one of the crazy anime ^_^!!")
    else:
        print("Society will not accept you ^_____^.")

    print(f"Your score is {score} out of {attempted}")


def main():
    print("You are entering in the anime quiz!! write quit for the end game")
    run_quiz()


if __name__ == "__main__":
    main()
