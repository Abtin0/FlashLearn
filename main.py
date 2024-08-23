from tkinter import *
from customtkinter import *
import pyglet
from PIL import Image
import pandas
import random
import pywinstyles

BACKGROUND = "#F1F1F8"
CARD_BACKGROUND = "#FFFFFF"
ACCENT = "#5352ED"
HOVER = "#3836cf"
CORRECT_GREEN = "#35dd02"
CORRECT_HOVER = "#2f8a3d"
WRONG_RED = "#e70052"
WRONG_HOVER = "#640023"
FONT_COLOR = "#3A3A3A"
FONT_NAME = "Giphurs ExtraBlack"
pyglet.font.add_file("Giphurs-ExtraBlack.ttf")
flipped = False

words_df = pandas.read_csv("data/words_to_learn.csv")
csv_length = len(words_df)
card_index = random.randint(0, csv_length - 1)
words_dict = pandas.read_csv("data/words_to_learn.csv").to_dict()

root = CTk()
root.title("FlashLearn")
root.iconbitmap("images/logo.ico")
set_appearance_mode("dark")
root.geometry("600x630+560+135")
root.resizable(False, False)


def get_definition():
    global card_index
    card_label.configure(image=back_card_img)
    en_words = words_dict.get("English")
    card_label.configure(text=en_words.get(card_index))


def get_word():
    global card_index
    fr_words = words_dict.get("French")
    card_label.configure(text=fr_words.get(card_index))


# Functions
def new_word():
    global card_index, csv_length
    if flipped:
        flip_card()
    if not flipped:
        csv_length = len(words_df)
        card_index = random.randint(0, csv_length - 1)
        get_word()


def remove_word():
    global card_index, words_df
    # Remove the word from the DataFrame
    words_df = words_df.drop(card_index).reset_index(drop=True)
    words_df.to_csv("data/words_to_learn.csv", index=False)
    # Update words_dict
    words_dict = words_df.to_dict(orient="list")
    new_word()


def flip_card():
    global flipped
    if not flipped:
        get_definition()
        flip_button.configure(text="Show Front")
        flipped = True
    else:
        card_label.configure(image=card_img)
        get_word()
        flip_button.configure(text="Show Back")
        flipped = False


# Top Box
top_box_img = CTkImage(light_image=Image.open("images/top_box.png"), dark_image=Image.open("images/top_box.png"),
                       size=(600, 250))

top_box_label = CTkLabel(root, width=600, height=0, text="", image=top_box_img)
top_box_label.place(x=0, y=0)

box_text_label = CTkLabel(root, text="Learn The            \nFrench Language", font=(FONT_NAME, 45), bg_color=ACCENT)
box_text_label.grid(row=0, column=0, padx=50, pady=35, sticky="NW")

# Card
card_img = CTkImage(light_image=Image.open("images/dark_card.png"), dark_image=Image.open("images/dark_card.png"),
                    size=(450, 300))
back_card_img = CTkImage(light_image=Image.open("images/dark_card_back.png"),
                         dark_image=Image.open("images/dark_card_back.png"), size=(450, 300))
card_label = CTkLabel(root, text='', font=(FONT_NAME, 35), text_color=FONT_COLOR,
                      image=card_img)
card_label.place(x=75, y=180)

# Flip Button
flip_button = CTkButton(root, text="Show Back", font=(FONT_NAME, 20), fg_color=ACCENT, hover_color=HOVER,
                        command=flip_card)
flip_button.place(x=232, y=550)

# Correct Button
check_img = CTkImage(light_image=Image.open("images/correct.png"), dark_image=Image.open("images/correct.png"),
                     size=(30, 30))
correct_button = CTkButton(root, width=50, height=50, image=check_img, text="", font=(FONT_NAME, 30), fg_color="black",
                           hover_color=CORRECT_HOVER, command=remove_word)
correct_button.place(x=430, y=520)

# Wrong Button
wrong_img = CTkImage(light_image=Image.open("images/wrong.png"), dark_image=Image.open("images/wrong.png"),
                     size=(30, 30))
wrong_button = CTkButton(root, width=50, height=50, text="", image=wrong_img, font=(FONT_NAME, 30), fg_color="black",
                         hover_color=WRONG_HOVER, command=new_word)
wrong_button.place(x=120, y=520)

new_word()

root.mainloop()
