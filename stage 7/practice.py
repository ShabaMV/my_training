import tkinter
from fileinput import filename
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/",title="Выберите файл", filetypes=(
        ("Текствый файл",".txt"),("Все файлы","*")))

window = tkinter.Tk()
window.title("Проводник")
window.geometry("350x350")
window.configure(bg="black")
window.resizable(False, False)
text = tkinter.Label(window, text="Файл: ", width=50, height=5, background="silver", foreground="blue")
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text = "Выбрать файл", foreground="blue", command=file_select())
button_select.grid(column=1, row=2, pady=5)
window.mainloop()