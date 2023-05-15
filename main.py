from tkinter import *
from text_editor_class import Text_editor
from game_class import Game_processor

text_dictionary_rows_to_type = Text_editor().make_list_of_rows_to_type()
print(text_dictionary_rows_to_type)

game = Game_processor()
game.apreciate_first_2_rows_to_show()

base_screen = Tk()
base_screen.title('Typing speed tester')
base_screen.minsize(700,600)

game.update_screen(base_screen)

base_screen.mainloop()