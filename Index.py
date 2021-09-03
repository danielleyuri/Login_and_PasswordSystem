from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import DataBaser

# =======Create Window
wind = Tk()
wind.title('DYS System - Access panel')
wind.geometry('550x300')
wind.configure(background='White')
wind.resizable(width=False, height=False)
# wind.attributes('-alpha',0.9)
wind.iconbitmap(default='icons/LogoIcon.ico')

# =========Loading Imagens
logo = PhotoImage(file='icons/logo.png')

# ======Widgets===============
LeftFrame = Frame(wind, width=180, height=300, bg='Light Gray', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(wind, width=365, height=300, bg='Gray', relief='raise')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='Light Gray')
LogoLabel.place(x=15, y=72)

UserLabel = Label(RightFrame, text='Username:', font=('Century Gothic', 20), bg='Gray', fg='white')
UserLabel.place(x=5, y=96)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text='Password:', font=('Century Gothic', 20), bg='Gray', fg='white')
PassLabel.place(x=5, y=134)

PassEntry = ttk.Entry(RightFrame, width=30, show='•')
PassEntry.place(x=150, y=148)


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute('''
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    ''', (User, Pass))
    print('Select')
    VerifyLogin = DataBaser.cursor.fetchone()
    # noinspection PyBroadException
    try:
        if User in VerifyLogin and Pass in VerifyLogin:
            messagebox.showinfo(title='Login Info', message='Access confirmed.Welcome!')
    except:
        messagebox.showinfo(title='Login Info', message='Access denied check your registration!')


# ======Buttons
LoginButton = ttk.Button(RightFrame, text='Login', width=25, command=Login)
LoginButton.place(x=85, y=200)


def Register():
    # Remove Widgets Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # Insert Widgets in the register
    NameLabel = Label(RightFrame, text='Name:', font=('Century Gothic', 20), bg='gray', fg='white')
    NameLabel.place(x=5, y=20)

    NameEntry = ttk.Entry(RightFrame, width=39)
    NameEntry.place(x=100, y=34)

    EmailLabel = Label(RightFrame, text='E-mail:', font=('Century Gothic', 20), bg='gray', fg='white')
    EmailLabel.place(x=5, y=58)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=72)

    def RegisterToDataBase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == '' and Email == '' and User == '' and Pass == '':
            messagebox.showerror(title='Register Error', message='Fill in all fields')
        else:
            DataBaser.cursor.execute('''
            INSERT INTO Users(Name, Email, User, Password)VALUES(?,?,?,?)
            ''', (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Access Info', message='Account Successfully')

    Register = ttk.Button(RightFrame, text='Register', width=30, command=RegisterToDataBase)
    Register.place(x=85, y=200)

    def BackToLogin():
        # Remove widgets in the Register
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # Bringing back login
        LoginButton.place(x=85)
        RegisterButton.place(x=100)

    Back = ttk.Button(RightFrame, text='<<<Back', width=20, command=BackToLogin)
    Back.place(x=115, y=230)


RegisterButton = ttk.Button(RightFrame, text='Register', width=20, command=Register)
RegisterButton.place(x=100, y=230)

wind.mainloop()
