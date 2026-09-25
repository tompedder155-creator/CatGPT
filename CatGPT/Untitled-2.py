import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from PIL import Image, ImageTk

import time
import random
import math
class quiz(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets_start()

    def create_widgets_start(self):
        # create a font after the root exists
        self.normal_font = tkFont.Font( family="Helvetica", size=16)
        for widget in self.winfo_children():
            widget.destroy()
        
        image = Image.open("Evil Larry.png")
        image = ImageTk.PhotoImage(image.resize([40,40]))

        self.question_label = tk.Label(self, text="CatGPT", font=self.normal_font)
        self.question_label.pack()
        self.text = tk.Text(self,background="light gray",yscrollcommand=True)
        self.text.pack()        
        self.image_labelz = tk.Label(self, image=image)
        self.image_labelz.pack()
        self.submit_button = tk.Button(self, text="Ask", font=self.normal_font, command=self.check_answer, width=20, height=3)
        self.submit_button.pack()

    def create_widgets_awnser(self,prompt):
        self.question_label.config(text="CatGPT")
        self.question_label.pack()

        self.question_label.config(text="CatGPT")
        self.question_label.pack()
        self.response_label = tk.Label(self,text="My awnser :   ",wraplength=500,background="light gray")
        self.response_label.pack()
        count = len(prompt)
        total_meow = round(random.randint(1,4) + math.sqrt(count+1)*4)
        response = ""
        for x in range (total_meow): 
            response = response + random.choice(["purr","meow","Mao","Meow","Pur","meeeoooow","meow", "purr","meow","meow"])
            response = response +" "
            self.response_label.config(text="My awnser :   "+response)
            time.sleep(random.random()/2)
            self.update()
    
        
        self.next_button = tk.Button(self, text="Next prompt", font=self.normal_font, command=self.create_widgets_start, width=20, height=3)
        self.next_button.pack()
        

  

    def create_widgets_loading(self,prompt):
        dots = ""
        image = Image.open("Thinking Cat.png")
        image = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self, image=image)
        self.image_label.pack()
        for x in range (1,4):
            dots = dots + "."
            self.question_label.config(text="Thinking"+ dots)
            self.question_label.pack()
            self.update()
            time.sleep(1)
        self.image_label.destroy()
        self.create_widgets_awnser(prompt)




    def check_answer(self):
        print("ask")
        prompt = self.text.get("1.0", "end-1c")
        
        self.submit_button.destroy()
        self.text.destroy()
        self.create_widgets_loading(prompt)
        
    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("750x700")

    quiz(root)
    root.mainloop()