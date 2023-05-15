from text import text_to_edit

class Text_editor():
    def __init__(self):
        self.nr_of_char_per_row = 35
        self.list_of_rows = []
        self.ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", " "]
        self.text_to_edit = text_to_edit

    def clear_text_of_symbols(self, text:str):
        initial_text = text.lower()
        list_symbols_to_remove = []
        for symbol in initial_text:
            if symbol not in self.ALPHABET and symbol not in list_symbols_to_remove:
                list_symbols_to_remove.append(symbol)
        # print(f"Removed symbols = {list_symbols_to_remove}")

        for letter in initial_text:
            if letter in list_symbols_to_remove:
                    initial_text = initial_text.replace(letter,"")
        # print(initial_text)

        initial_list_text = initial_text.split()
        # print(initial_list_text)

    #   Delete duplicate words
        no_duplicate_list = []
        for element in initial_list_text:
            if element not in no_duplicate_list:
                no_duplicate_list.append(element)
        # print(no_duplicate_list)
        return no_duplicate_list

    def make_list_of_rows_to_type(self):
        initial_list_text = self.clear_text_of_symbols(self.text_to_edit)
        list_of_rows_to_type = {}
        nr_of_acum_elem = 0
        row_nr = 1
        row = []
        while len(initial_list_text)>0:
            for element in initial_list_text:
                if nr_of_acum_elem <= self.nr_of_char_per_row:
                    row.append(element)
                    nr_of_acum_elem += len(element)
            for word in row:
                initial_list_text.remove(word)
            list_of_rows_to_type[row_nr] = row
            row_nr+=1
            row=[]
            nr_of_acum_elem = 0

        # print(row)
        # print(list_of_rows_to_type)
        return list_of_rows_to_type

text_processor = Text_editor()

text_processor.make_list_of_rows_to_type()