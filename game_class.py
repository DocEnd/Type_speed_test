import time
from tkinter import ttk, StringVar
from text_editor_class import Text_editor
from datetime import datetime, timedelta

class Game_processor():
    def __init__(self):
        super(Game_processor).__init__()
        self.current_nr_of_list_to_show = 1
        self.dict_of_word_rows = Text_editor().make_list_of_rows_to_type()
        self.first_row_to_show = self.dict_of_word_rows[self.current_nr_of_list_to_show]
        self.second_row_to_show = []
        self.current_word_nr_in_list = 0
        self.current_word = self.first_row_to_show[self.current_word_nr_in_list]
        self.answer_color = "black"
        self.nr_of_words_typed = 0
        self.seconds_to_play = 20
        self.play_on_off = 'off'

    def apreciate_first_2_rows_to_show(self):
        self.current_nr_of_list_to_show += 1
        self.second_row_to_show = self.dict_of_word_rows[self.current_nr_of_list_to_show]

    def change_rows_by_adding_new(self):
        self.first_row_to_show = self.second_row_to_show
        self.current_nr_of_list_to_show += 1
        self.second_row_to_show = self.dict_of_word_rows[self.current_nr_of_list_to_show]

    def verify_entered_symbols_with_current_word_by_length(self, entered_part_of_word:str):
        self.START = len(entered_part_of_word)+1
        if len(entered_part_of_word) > 0:
            if entered_part_of_word[-1] == " ":
                self.START = len(entered_part_of_word)-1

            if entered_part_of_word.lower() == self.current_word[:len(entered_part_of_word)]:
                self.answer_color = "green"
                if entered_part_of_word.lower() == self.current_word:
                    self.current_word_nr_in_list += 1
                    self.current_word = self.first_row_to_show[self.current_word_nr_in_list]
                    self.START = 0
                    self.nr_of_words_typed += 1
                    self.if_last_word_in_list_change_it()
            else:
                self.answer_color = "red"

    def if_last_word_in_list_change_it(self):
        if self.current_word_nr_in_list == len(self.first_row_to_show)-1:
            self.change_rows_by_adding_new()
            self.current_word_nr_in_list = -1


    def update_screen(self,base_screen):
        self.frame = ttk.Frame(base_screen, padding=10, borderwidth=20)
        self.frame.grid()

        self.lable_title = ttk.Label(self.frame, text='Welcome to the typing speed tester', font=("Arial", 25), padding=20)
        self.lable_title.grid(column=0, row=0)

        self.label_text_to_type_1 = ttk.Label(self.frame, text=self.first_row_to_show, font=("Arial", 15), width=50,
                                         borderwidth=2, relief="sunken",
                                         padding=20, wraplength=500, justify='center')
        self.label_text_to_type_1.grid(column=0, row=1)
        self.label_text_to_type_2 = ttk.Label(self.frame, text=self.second_row_to_show, font=("Arial", 15), width=50,
                                         borderwidth=2, relief="sunken",
                                         padding=20, wraplength=500, justify='center')
        self.label_text_to_type_2.grid(column=0, row=2)

        entered_text = StringVar()

        self.entry_input_text = ttk.Entry(self.frame, textvariable=entered_text, font=("Arial", 15), width=53)
        self.entry_input_text.grid(column=0, row=3)

        self.label_show_situation = ttk.Label(self.frame, text=self.current_word, foreground=self.answer_color,
                                         font=("Arial", 20), padding=20, justify='center')
        self.label_show_situation.grid(column=0, row=4)

        self.label_ask_to_play = ttk.Label(self.frame, text="", foreground='blue',
                                              font=("Arial", 20), padding=20, justify='center')
        self.label_ask_to_play.grid(column=0, row=5)

        self.button_start = ttk.Button(self.frame, text="To START press 'SPACE'", command=self.game_on, padding=10)
        self.button_start.grid(row=6,column=0)

        self.ask_to_play()
        self.play()

    def ask_to_play(self):
        self.label_ask_to_play.configure(text="To begin typing press 'SPACE' or the Button")
        self.button_start.focus_set()

    def game_on(self):
        self.play_on_off = "on"
        self.label_ask_to_play.configure(text="Go Go Go!")
        self.entry_input_text.focus_set()
        self.play()

    def game_off(self):
        self.play_on_off = "off"
        self.label_ask_to_play.configure(text="Game Stopped!")
        self.button_start.focus_set()


    def play(self,):
        if self.play_on_off == 'on':
            key = "<KeyRelease>"
        else:
            key = None
        self.entry_input_text.bind(key, self.play_for_seconds)


    def play_for_seconds(self,x):
        if self.current_word == self.dict_of_word_rows[1][0]:
            self.start_time = datetime.now()
        self.get_text_from_input()

    def get_text_from_input(self,):
        text = self.entry_input_text.get()
        if datetime.now() - self.start_time < timedelta(seconds=self.seconds_to_play):
            self.verify_entered_symbols_with_current_word_by_length(text)
            self.label_show_situation.configure(foreground=self.answer_color, text=self.current_word)
            self.entry_input_text.delete(self.START, 'end')
            self.label_text_to_type_1.configure(text=self.first_row_to_show)
            self.label_text_to_type_2.configure(text=self.second_row_to_show)
        else:
            print(f"you typed {self.nr_of_words_typed} words in {self.seconds_to_play} sec.")
            self.label_show_situation.configure(
                text=f"you typed {self.nr_of_words_typed} words in {self.seconds_to_play} sec.")
            self.game_off()
            time.sleep(3)
            self.reset_game()

    def reset_game(self):
        self.current_nr_of_list_to_show = 1
        self.dict_of_word_rows = Text_editor().make_list_of_rows_to_type()
        self.first_row_to_show = self.dict_of_word_rows[self.current_nr_of_list_to_show]
        self.apreciate_first_2_rows_to_show()
        self.current_word_nr_in_list = 0
        self.current_word = self.first_row_to_show[self.current_word_nr_in_list]
        self.answer_color = "black"
        self.nr_of_words_typed = 0
        self.entry_input_text.delete(0,"end")
        self.ask_to_play()