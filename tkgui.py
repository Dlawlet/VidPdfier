import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from turtle import bgcolor, color
import main

# create the root window
root = tk.Tk()
root.title('VidPdfier')
root.resizable(False, False)
root.geometry('600x300')

def convert(filenames,a,b):
    convert_label = ttk.Label(root,text=" File(s) coonvertion begin please WAIT!",foreground="green")
    convert_label.pack()
    for file in filenames:
        main.save_frame(file, "./", gap = a, pp =b)
    showinfo(
        title='PFdification finished',
        message= "There We go, your pdf is available "
    )
    convert_label.config(text="finished, waiting for next stuff")
def select_files():
    global filenames
    filetypes = (
        ('video files', '*.mp4'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Select file(s)',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
    if filenames!=[]:
        file_label.config(text="File(s) Selected : 'YES'",background='green')
    
def retrieve_input():
    global filenames
    inputValue1=textBox1.get("1.0","end-1c")
    inputValue2=textBox2.get("1.0","end-1c")
    if inputValue1 == "":
         inputValue1=1000
    if inputValue2 == "":
         inputValue2=1
    convert(filenames,inputValue1,inputValue2)


filenames = []


# open button
open_button = ttk.Button(
    root,
    text='Choose Video(s)',
    command=select_files
)
file_label = ttk.Label(root,text= "File(s) Selected : 'NO'")
file_label.pack()
label1=tk.Label(root,text="Choose the Frame rate (default = 1000)")
label1.pack()
textBox1=tk.Text(root, height=2, width=10)
textBox1.pack()
label2=tk.Label(root,text="Choose the number of slide per page [1 or 2](default = 1)")
label2.pack()
textBox2=tk.Text(root, height=2, width=10)
textBox2.pack()

buttonCommit=tk.Button(root, height=1, width=15, text="Start Pdfication", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

open_button.pack(expand=True)

root.mainloop()