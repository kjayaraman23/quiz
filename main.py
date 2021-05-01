import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.geometry("600*400")
name_var = tk.StringVar()
passw_var = tk.StringVar()
idname = ["20ME04", "20ME05", "20ME07"]
password = ["20ME04", "20ME05", "20ME07"]
def submit():
    name = name_var.get()
    password = passw_var.get()

    for i in range(len(idname)) :
        if name== idname[i] :
            import main2.py
        else :
           import main.py
        i=+1




    name_var.set("")
    passw_var.set("")

background_image = ImageTk.PhotoImage(Image.open("pic.jpg"))
l=tk.Label(image=background_image)

title_label = tk.Label(root, text='QUIZ GAME', font=('calibre', 100, 'bold'))
name_label = tk.Label(root, text='Username', font=('calibre', 20, 'bold'))

name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 20, 'normal'))

passw_label = tk.Label(root, text='Password', font=('calibre', 20, 'bold'))

passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 20, 'normal'), show='*')

sub_btn = tk.Button(root, text='Submit', command=submit)

l.grid()
title_label.grid(row=40,column=0)
name_label.grid(row=25, column=1)
name_entry.grid(row=25, column=2)
passw_label.grid(row=45, column=1)
passw_entry.grid(row=45, column=2)
sub_btn.grid(row=50, column=3)



root.mainloop()
