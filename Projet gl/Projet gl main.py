

from tkinter import *
from tkinter import messagebox
import mainmenu as m








def cmd():
    if (e1.get() == 'agent' and e2.get() == 'locdz' ):
        menu=m.mainmenu(w)
    elif (e1.get() == 'admin' and e2.get() == 'locdz' ):
        menu = m.mainmenu2(w)
    else:
        messagebox.showwarning("LOGIN FAILED", "        PLEASE TRY AGAIN        ")

















w = Tk()
w.geometry('500x700')
w.title(' L O G I N    L O C D Z')
w.resizable(0, 0)





l1 = Label(w, text='Username', bg='#1b9ea4',fg='white',font=("tahoma",15))

l1.place(x=100, y=280)

# e1 entry for username entry
e1 = Entry(w, width=20,font=("tahoma",15))
e1.place(x=100, y=310)

# e2 entry for password entry
e2 = Entry(w, width=20,font=("tahoma",15))
e2.place(x=100, y=380)

l2 = Label(w, text='Password', bg='#1b9ea4',fg='white',font=("tahoma",15))

l2.place(x=100, y=350)






myButton1 = Button(w, text='login',
                       width=20,
                       height=2,
                       bg='#1b9ea4',
                       fg="white",
                       command=cmd
                       )



myButton1.place(x=150, y=480)
















w.mainloop()