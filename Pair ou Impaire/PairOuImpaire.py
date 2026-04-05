import tkinter as tk
M = tk.Tk()
label = tk.Label(M, text="")
label.grid(row=0, column=0, columnspan=3)
def verif():
    try:
        valeur = ENTRY.get()
        if int(valeur)%2==0:
            label.config(text="Pair")
        else:
            label.config(text="Impair")
    except:
        label.config(text="Ce n'est pas un nombre !")
M.title("Page")
M.geometry("1000x500")
M.resizable(False, False)
ENTRY = tk.Entry(font=("Arial", 24), width=50, justify = "center")
ENTRY.grid(row=3, column=0, padx=30)
Button1 = tk.Button(text="Entrée", bg="red", command=verif, width=40)
Button1.grid(row=4, column=0, columnspan=3)
M.mainloop()
