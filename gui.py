import random
import time
import tkinter as tk
import typing_speed_calc as mainfile

init = 0
def start_typing():
    global init
    init = time.time()
    t_typed_phrase.config(state="normal")

def typ_speed_calc():

    average_wpm = sum_wpm/5
    typ_speed.config(text=f"Your typing speed is : {average_wpm}")

phrase_list = mainfile.phrase_list
already_asked = []
iter_time = 0
mistake_dict = {}
sum_wpm = 0

def stop_typing():

    final = time.time()
    global iter_time
    iter_time += 1
    t_typed_phrase.delete("1.0", "end")
    if iter_time == 5:
        typ_speed_calc()
        quit()

    while True:
        # generating unused phrase
        phrase = random.choice(phrase_list)
        if phrase in already_asked:
            continue
        else:
            already_asked.append(phrase)
            t_given_phrase.config(state="normal")
            t_given_phrase.delete("1.0", "end")
            t_given_phrase.insert("1.0", phrase)
            t_given_phrase.config(state="disabled")
            phrase_ques = phrase.split(" ")
            break

    while 1:
        
        # time taken by user for response
        user_ans = t_typed_phrase.get("1.0", "end")
        user_ans = user_ans.split(" ")
        
        if len(user_ans) == len(phrase_ques):
            difference = final - init
            wpm = (len(phrase_ques)*60)//difference
            global sum_wpm
            sum_wpm += wpm
            for i in range(len(user_ans)):
                # checking for mistakes
                if user_ans[i] == phrase_ques[i]:
                    pass
                else:
                    mistakes += 1
                    mistake_dict.update({phrase_ques[i]:user_ans[i]})
            break


window = tk.Tk()
window.title("Typing Speed Calculator")
window.geometry("800x600")

lname = tk.Label(window, text="Enter your name")
lname.config(font=("Arial", 15))
lname.pack(padx = 10, pady= 10)

tname = tk.Text(window, height=1, width=140)
tname.config(font=("Arial", 15), bg="#dddddd")
tname.pack(padx = 10, pady= 10)

l_given_phrase = tk.Label(window, text="Phrase")
l_given_phrase.config(font=("Arial", 15))
l_given_phrase.pack(padx = 10, pady= 10)

t_given_phrase = tk.Text(window, height=1, width=140)
t_given_phrase.insert("1.0", random.choice(phrase_list))
t_given_phrase.config(font=("Arial", 15), state="disabled", bg="#dddddd")
t_given_phrase.pack(padx = 10, pady= 10)


btn_1 = tk.Button(window, text="Start Typing", command=start_typing)
btn_1.pack()


l_typed_phrase = tk.Label(window, text="Type the given phrase below:")
l_typed_phrase.config(font=("Arial", 15))
l_typed_phrase.pack(padx = 10, pady= 10)


t_typed_phrase = tk.Text(window, height=1, width=140)
t_typed_phrase.config(font=("Arial", 15), state="disabled", bg="#dddddd")
t_typed_phrase.pack(padx = 10, pady= 10)

btn_2 = tk.Button(window, text="Done", command=stop_typing)
btn_2.pack()

# btn_3 = tk.Button(window, text="My typing speed", command=typ_speed_calc)
# btn_3.pack()


typ_speed = tk.Label(window)
typ_speed.config(font=("Arial", 15))
typ_speed.pack()

window.mainloop()
