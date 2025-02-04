import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Application")
root.geometry("300x400")

nr_click=0

def click_button():
    global nr_click
    nr_click+=1
    label.config(text=f"Butonul a fost apasat de {nr_click} ori")

def reset_button():
    global nr_click
    nr_click=0
    label.config(text="Numarul a fost resetat")

def exit_button():
    raspuns=messagebox.askquestion("Exit","Doriti sa iesiti?")
    if raspuns=="yes":
        root.destroy()

label=tk.Label(root,text="Apasa pe buton!")
label.pack(pady=10)

buton_click=tk.Button(root,text="Click me!",command=click_button)
buton_click.pack(pady=10)

buton_reset=tk.Button(root,text="Reset!",command=reset_button)
buton_reset.pack(pady=10)

buton_exit=tk.Button(root,text="Exit!",command=exit_button)
buton_exit.pack(pady=10)

root.mainloop()