import customtkinter as ctk
from CTkTable import *
import json
import random
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox

text = '#16161b'
background = '#f0f0fa'
primary = '#363a4f'
secondary = '#1d1d28'
accent = '#ffe8af'
neu = '#515461'

Head = ('Arial Rounded MT Bold', 32, 'bold')
txt1 = ('Arial Rounded MT Bold', 20, 'bold')

class Quiz:
    def __init__(self):
        pass

    def main_page(self):
        global main_title, tutorial_btn, review_btn, quiz_btn

        main.geometry('600x500+600+200')

        main_title = ctk.CTkLabel(
            main,
            text="Welcome \n to the \n multiplication learner",
            text_color=text,
            font=Head
        )
        main_title.pack(pady=5)

        tutorial_btn = ctk.CTkButton(
            main,
            text="An introduction to multiplication",
            fg_color=primary,
            font=txt1,
            height=45,
            command=self.start_tutorial
        )
        tutorial_btn.pack(pady=10)

        review_btn = ctk.CTkButton(
            main,
            text="Review your multiplication tables",
            fg_color=primary,
            font=txt1,
            height=45,
            command=self.start_review
        )
        review_btn.pack(pady=10)

        quiz_btn = ctk.CTkButton(
            main,
            text="Start the quiz",
            fg_color=primary,
            font=txt1,
            height=45,
            command=self.start_quiz
        )
        quiz_btn.pack(pady=10)
    
    def review_main_page(self):
        self.main_page()

        table.pack_forget()
        review_back.pack_forget()

    def tutorial_next_cmd4(self):
        global tutorial_review_btn, tutorial_quiz_btn

        main.geometry('600x700+600+200')

        tutorial_image4.pack_forget()
        tutorial_next.pack_forget()
        tutorial_image5.pack()

        tutorial_review_btn = ctk.CTkButton(
            main,
            text="Review your multiplication tables",
            fg_color=primary,
            font=txt1,
            height=45,
            command=self.tutorial_start_review
        )
        tutorial_review_btn.pack(pady=10)

        tutorial_quiz_btn = ctk.CTkButton(
            main,
            text="Start the quiz",
            fg_color=primary,
            font=txt1,
            height=45,
            command=self.start_quiz
        )
        tutorial_quiz_btn.pack(pady=10)

    def tutorial_next_cmd3(self):
        tutorial_image3.pack_forget()
        tutorial_next.pack_forget()
        tutorial_image4.pack()
        tutorial_next.pack()
        tutorial_next.configure(command=self.tutorial_next_cmd4)

    def tutorial_next_cmd2(self):
        tutorial_image2.pack_forget()
        tutorial_next.pack_forget()
        tutorial_image3.pack()
        tutorial_next.pack()
        tutorial_next.configure(command=self.tutorial_next_cmd3)

    def tutorial_next_cmd1(self):
        tutorial_image1.pack_forget()
        tutorial_next.pack_forget()
        tutorial_image2.pack()
        tutorial_next.pack()
        tutorial_next.configure(command=self.tutorial_next_cmd2)


    def start_tutorial(self):
        global tutorial1, tutorial2, tutorial3, tutorial4, tutorial5,  tutorial_image1, tutorial_image2, tutorial_image3, tutorial_image4, tutorial_image5, tutorial_next

        main.geometry('600x650+600+200')


        main_title.pack_forget()
        tutorial_btn.pack_forget()
        review_btn.pack_forget()
        quiz_btn.pack_forget()

        tutorial1 = ImageTk.PhotoImage(Image.open("p1.png"))
        tutorial2 = ImageTk.PhotoImage(Image.open("p2.png"))
        tutorial3 = ImageTk.PhotoImage(Image.open("p3.png"))
        tutorial4 = ImageTk.PhotoImage(Image.open("p4.png"))
        tutorial5 = ImageTk.PhotoImage(Image.open("p5.png"))

        tutorial_image1 = ctk.CTkLabel(
            main,
            image=tutorial1,
            text=""
        )
        tutorial_image1.pack()

        tutorial_image2 = ctk.CTkLabel(
            main,
            image=tutorial2,
            text=""
        )

        tutorial_image3 = ctk.CTkLabel(
            main,
            image=tutorial3,
            text=""
        )

        tutorial_image4 = ctk.CTkLabel(
            main,
            image=tutorial4,
            text=""
        )

        tutorial_image5 = ctk.CTkLabel(
            main,
            image=tutorial5,
            text=""
        )

        tutorial_next = ctk.CTkButton(
            main,
            text="next",
            font=txt1,
            text_color=background,
            fg_color=primary,
            command=self.tutorial_next_cmd1
        )
        tutorial_next.pack(pady=20)

    
    def start_review(self):
        global table, review_back

        main_title.pack_forget()
        tutorial_btn.pack_forget()
        review_btn.pack_forget()
        quiz_btn.pack_forget()

        main.geometry('600x500+600+200')

        mults = [['Multiples of 1', 'Multiples of 2', 'Multiples of 3', 'Multiples of 4', 'Multiples of 5', 'Multiples of 6'],
            ['1 x 1 = 1 \n 1 x 2 = 2 \n 1 x 3 = 3 \n 1 x 4 = 4 \n 1 x 5 = 5 \n 1 x 6 = 6 \n 1 x 7 = 7 \n 1 x 8 = 8 \n 1 x 9 = 9 \n 1 x 10 = 10 \n 1 x 11 = 11 \n 1 x 12 = 12',
            '2 x 1 = 2 \n 2 x 2 = 4 \n 2 x 3 = 6 \n 2 x 4 = 8 \n 2 x 5 = 10 \n 2 x 6 = 12 \n 2 x 7 = 14 \n 2 x 8 = 16 \n 2 x 9 = 18 \n 2 x 10 = 20 \n 2 x 11 = 22 \n 2 x 12 = 24',
            '3 x 1 = 3 \n 3 x 2 = 6 \n 3 x 3 = 9 \n 3 x 4 = 12 \n 3 x 5 = 15 \n 3 x 6 = 18 \n 3 x 7 = 21 \n 3 x 8 = 24 \n 3 x 9 = 27 \n 3 x 10 = 30 \n 3 x 11 = 33 \n 3 x 12 = 36',
            '4 x 1 = 4 \n 4 x 2 = 8 \n 4 x 3 = 12 \n 4 x 4 = 16 \n 4 x 5 = 20 \n 4 x 6 = 24 \n 4 x 7 = 28 \n 4 x 8 = 32 \n 4 x 9 = 36 \n 4 x 10 = 40 \n 4 x 11 = 44 \n 4 x 12 = 48',
            '5 x 1 = 5 \n 5 x 2 = 10 \n 5 x 3 = 15 \n 5 x 4 = 20 \n 5 x 5 = 25 \n 5 x 6 = 30 \n 5 x 7 = 35 \n 5 x 8 = 40 \n 5 x 9 = 45 \n 5 x 10 = 50 \n 5 x 11 = 55 \n 5 x 12 = 60',
            '6 x 1 = 6 \n 6 x 2 = 12 \n 6 x 3 = 18 \n 6 x 4 = 24 \n 6 x 5 = 30 \n 6 x 6 = 36 \n 6 x 7 = 42 \n 6 x 8 = 48 \n 6 x 9 = 54 \n 6 x 10 = 60 \n 6 x 11 = 66 \n 6 x 12 = 72'],
            ['Multiples of 7', 'Multiples of 8', 'Multiples of 9', 'Multiples of 10', 'Multiples of 11', 'Multiples of 12'],
            ['7 x 1 = 7 \n 7 x 2 = 14 \n 7 x 3 = 21 \n 7 x 4 = 28 \n 7 x 5 = 35 \n 7 x 6 = 42 \n 7 x 7 = 49 \n 7 x 8 = 56 \n 7 x 9 = 63 \n 7 x 10 = 70 \n 7 x 11 = 77 \n 7 x 12 = 84',
            '8 x 1 = 8 \n 8 x 2 = 16 \n 8 x 3 = 24 \n 8 x 4 = 32 \n 8 x 5 = 40 \n 8 x 6 = 48 \n 8 x 7 = 56 \n 8 x 8 = 64 \n 8 x 9 = 72 \n 8 x 10 = 80 \n 8 x 11 = 88 \n 8 x 12 = 96',
            '9 x 1 = 9 \n 9 x 2 = 18 \n 9 x 3 = 27 \n 9 x 4 = 36 \n 9 x 5 = 45 \n 9 x 6 = 54 \n 9 x 7 = 63 \n 9 x 8 = 72 \n 9 x 9 = 81 \n 9 x 10 = 90 \n 9 x 11 = 99 \n 9 x 12 = 108',
            '10 x 1 = 10 \n 10 x 2 = 20 \n 10 x 3 = 30 \n 10 x 4 = 40 \n 10 x 5 = 50 \n 10 x 6 = 60 \n 10 x 7 = 70 \n 10 x 8 = 80 \n 10 x 9 = 90 \n 10 x 10 = 100 \n 10 x 11 = 110 \n 10 x 12 = 120',
            '11 x 1 = 11 \n 11 x 2 = 22 \n 11 x 3 = 33 \n 11 x 4 = 44 \n 11 x 5 = 55 \n 11 x 6 = 66 \n 11 x 7 = 77 \n 11 x 8 = 88 \n 11 x 9 = 99 \n 11 x 10 = 110 \n 11 x 11 = 121 \n 11 x 12 = 132',
            '12 x 1 = 12 \n 12 x 2 = 24 \n 12 x 3 = 36 \n 12 x 4 = 48 \n 12 x 5 = 60 \n 12 x 6 = 72 \n 12 x 7 = 84 \n 12 x 8 = 96 \n 12 x 9 = 108 \n 12 x 10 = 120 \n 12 x 11 = 132 \n 12 x 12 = 144']
            ]

        table = CTkTable(
            main,
            row=4,
            column=6,
            values=mults,
            padx=0,
            pady=0,
            corner_radius=10,
            colors=(accent, background),
            text_color=(text)
        )
        table.pack()

        review_back = ctk.CTkButton(
            main,
            text="back",
            fg_color=primary,
            font=txt1,
            command=self.review_main_page
        )
        review_back.pack()
    
    def tutorial_start_review(self):
        self.start_review()
        tutorial_image5.pack_forget()
        tutorial_review_btn.pack_forget()
        tutorial_quiz_btn.pack_forget()


    def start_quiz(self):
        main_title.pack_forget()
        tutorial_btn.pack_forget()
        review_btn.pack_forget()
        quiz_btn.pack_forget()

    

    
main = ctk.CTk(
    fg_color=background
)
main.title('Multiplication learner')
main.geometry('600x700+600+200')
main.resizable(False, False)


Quiz().main_page()
main.mainloop()