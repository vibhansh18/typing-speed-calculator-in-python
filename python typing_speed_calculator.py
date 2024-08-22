import time
import random

with open(r"typing_speed_phrases.txt") as p:
    ps = p.read()
    phrase_list = ps.split("\n")


def save_history(name: str, wpm, mistakes: int):
    """
    Saves the result of the typing speed test.
    """
    text = f"{name.capitalize()} had an average typing speed of {wpm} wpm with {mistakes} mistakes commited.\n"
    try:
        with open(r"typing_speed_history.txt", "a") as f:
            f.write(text)
    except Exception as e:
        print(e)


def read_history():
    """
    Reads the typing speed test history.
    """
    try:
        with open(r"typing_speed_history.txt", "r") as f:
            fc = f.read()
            print(fc)
    
    except FileNotFoundError:
        print("No history yet.")


def calc_typing_speed(name: str):
    """
    Main code.
    """
    sum_wpm = 0
    already_asked = []
    mistakes = 0
    mistake_dict = {}

    for i in range(1, 6):
        while True:
            # generating unused phrase
            phrase = random.choice(phrase_list)
            if phrase in already_asked:
                continue
            else:
                print(f"Phrase {i}: {phrase}")
                phrase_ques = phrase.split(" ")
                already_asked.append(phrase)
                break

        while 1:
            input(
                "Press enter and start typing the phrase immediately and again press enter once you've written the phrase."
            )
            # time taken by user for response
            init = time.time()
            user_ans = input()
            finish = time.time()

            user_ans = user_ans.split(" ")

            if len(user_ans) == len(phrase_ques):
                difference = finish - init
                wpm = (len(phrase_ques) * 60) // difference
                sum_wpm += wpm
                for i in range(len(user_ans)):
                    # checking for mistakes
                    if user_ans[i] == phrase_ques[i]:
                        pass
                    else:
                        mistakes += 1
                        mistake_dict.update({phrase_ques[i]: user_ans[i]})
                break

            else:
                print("You didn't type the whole phrase!")

        print("\n---------------------------------------------\n")

    average_wpm = sum_wpm / 5
    result = f"Hey {name.capitalize()}, your average words per minute typing speed counts {average_wpm}.\n You commited {mistakes} mistakes.\n"
    print(result)

    if len(mistake_dict.keys()) != 0:
        print("Your typing mistakes are:\n")
        for key, value in mistake_dict.items():
            print(f"{key} --> {value}")

    save_history(name, average_wpm, mistakes)


if __name__ == "__main__":
    print("WELCOME TO THE TYPING SPEED COUNTER!\n")
    name = input("Enter your name: ")

    while True:
        task = int(
            input(
                "What to do?\n 1. Take a typing speed test \n 2. Read old typing speed test history \n 3. Quit \n"
            )
        )

        if task == 1:
            calc_typing_speed(name)

        elif task == 2:
            read_history()

        else:
            print("Thanks for visiting!")
            quit()
