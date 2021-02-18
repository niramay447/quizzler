THEME_COLOR = "#375362"
from tkinter import *
class QuizInterface:

    def __int__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.window.mainloop()