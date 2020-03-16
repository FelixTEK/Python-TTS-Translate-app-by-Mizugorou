from tkinter import *
from tkinter.ttk import *
from gtts import gTTS
from googletrans import Translator
import os
translator: Translator = Translator()
val = 0

class Application(Frame):
    def __init__(self, master):
        # initialize frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # add label for text
        self.label2 = Label(self)
        self.label2["text"] = "Please insert your text."
        self.label2.grid(column=0, row=2)

        # add Entry
        self.entry = Entry(self, width=20)
        self.entry.grid(column=1, row=2)

        # add label for language selection
        self.label1 = Label(self)
        self.label1["text"] = "Voice Language:"
        self.label1.grid(column=2, row=2)

        # create combobox for select number
        self.box = Combobox(self)
        self.box['values'] = ('en', 'ru', 'th', 'ja', 'de')
        self.box.current(0)
        self.box.bind("<<>ComboboxSelected>")
        self.box.grid(column=3, row=2)

        # create print button
        self.button = Button(self)
        self.button["text"] = "Speak"
        self.button["command"] = self.translate
        self.button.grid(column=2, row=3)

    # copy source file from eimer to destination folder
    def translate(self):
        lang = self.box.get()
        myinput = self.entry.get()
        if lang != 'en':
            result = translator.translate(text=myinput, dest=lang)
            result = result.text
        else:
            result = self.entry.get()
        tts = gTTS(text=result, lang=lang)
        tts.save("Res.mp3")
        os.startfile('Res.mp3')
        print(self.box.get())

# for debug
if __name__ == "__main__":
    root = Tk()
    root.title("TTS Translate App by Mizugorou, Powered by Google.")
    root.geometry("500x50")

    app = Application(root)

    root.mainloop()