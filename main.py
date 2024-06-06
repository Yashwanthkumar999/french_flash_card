from tkinter import *
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

# using pandas create dictionary

data = pandas.read_csv("french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_type, text="French")
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_card, text=current_card["French"], fill="black")
    window.after(3000, func=meaning)


def meaning():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_type, text="English")
    canvas.itemconfig(title_card, text=current_card["English"], fill="white")


# french_list = data.French.to_list()
# random_fr_word = random.choice(french_list)
# x = (data[data.French == random_fr_word])
# print(f"{random_fr_word}:", x.English)

# creating dictionary format data using json
# with open("data.json", mode="w") as data_file:


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
no_btn_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
card_type = canvas.create_text(400, 150, text=" ", font=("arial", 20, "italic"))
title_card = canvas.create_text(400, 263, text=" ", font=("arial", 24, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

no_button = Button(image=no_btn_img, width=100, highlightthickness=0, command=meaning)
no_button.grid(row=2, column=0)

yes_button = Button(image=right_img, width=100, highlightthickness=0, command=next_card)
yes_button.grid(row=2, column=1)

next_card()

window.mainloop()
