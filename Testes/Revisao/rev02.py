import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class MyGUI():
    def __init__(self):
        self.janela = tk.Tk()
    
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)

        self.frame1.pack()
        self.frame2.pack()

        self.label1 = tk.Label(self.frame1, text = 'Digite algo')
        self.label2 = tk.Label(self.frame2, text = 'Nada')

        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')

        self.buttomSubmit = tk.Button(self.janela, text = 'Enter', command = self.submit)
        self.buttomSubmit.pack(side = 'left')

        self.buttomClear = tk.Button(self.janela, text = 'Clear', command = self.clear)
        self.buttomClear.pack(side = 'left')

        self.inputText = tk.Entry(self.frame1, width = 20)
        self.inputText.pack(side = 'left')

    
        tk.mainloop()

    def submit(self):
        self.label2["text"] = self.inputText.get()

    def clear(self):
        self.inputText.delete(0, len(self.inputText.get()))
        self.label2["text"] = "Nada"

def main():
    MyGUI()

main()


