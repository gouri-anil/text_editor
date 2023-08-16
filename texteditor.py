import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import font

root = tk.Tk()      #opens root window
root.title("Text Editor")
text = tk.Text(root)  #text editor
text.grid()

#function to save file as
def save():    
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text Files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")])
    if savelocation==True:
        with open(savelocation, "w") as file:
            file.write(t)

#code for save button
save_button = tk.Button(root, text="Save File", command=save) 
save_button.grid();

#function for font
def attribute(event):
    global text
    
    #to accept both font and size
    fontchoice = font_cbox.get()
    sizechoice = size_cbox.get()
    colorchoice = color_cbox.get()   

    #if size has nto been selected
    if sizechoice == "Size":
        sizechoice = "12" 
    
    #to change font and size
    text.configure(font=(fontchoice, int(sizechoice)), fg=colorchoice)

    
#code for font drop down list
font_cbox=ttk.Combobox(root)
font_cbox.set("Font")
font_cbox["values"] = ("Arial", "Times New Roman", "Helvetica", "Consolas")
font_cbox.bind("<<ComboboxSelected>>", attribute)
font_cbox.grid()

#code for size drop down list
size_cbox=ttk.Combobox(root)
size_cbox.set("Size")
size_cbox["values"] = ("10", "12", "14", "16", "18", "20")
size_cbox.bind("<<ComboboxSelected>>", attribute)
size_cbox.grid()

#code for color drop down list
color_cbox=ttk.Combobox(root)
color_cbox.set("Color")
color_cbox["values"] = ("Black", "Red", "Green", "Blue", "Yellow", "Brown")
color_cbox.bind("<<ComboboxSelected>>", attribute)
color_cbox.grid()

root.mainloop()

