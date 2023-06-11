from tkinter import*

window = Tk()


def clicked_button():
    user= username_entry.get()
    password= username_password.get()
    if user == "David" and password == "5555":
        print("Hey  " + user)
        username_entry.config(state=DISABLED)
        window.destroy()
        new_window = Tk()

        def withdraw():
            remove =ask1entry.get()
            take=((int(balance)-int(remove)))

            do=str(take)

            balance_label.config(text=("Your balance: "+str(do)))

            ask1_button.config(state=DISABLED)
            ask2_button.config(state=DISABLED)

        def deposit():
            remove =ask1entry.get()
            take = ((int(balance) + int(remove)))

            do = str(take)

            balance_label.config(text=("Your balance: " + str(do)))
            ask1_button.config(state=DISABLED)
            ask2_button.config(state=DISABLED)

        new_window.title('EREN BANK', )
        bg=PhotoImage(file='pg3.png')
        new_window.geometry('300x300')
        new_window.config(background='white')
        global balance
        balance ='100000'



        new_label1 = Label( font=("Century Gothic", 20), text='Welcome to  Eren Bank',
                        compound='top', bg='white')
        username_label1 = Label(font=("Century Gothic", 20), text=('Hey David'),bg="white")
        accounttype_label = Label(font=("Century Gothic", 20), text=('SAVINGS ACCOUNT'),bg="white")
        balance_label = Label(font=("Century Gothic", 20), text= ('Your balance:' +balance),bg="white")
        ask1_label = Label(text="Amount you want:",bg="white",font=('Century Gothic',20))
        ask1entry= Entry()
        ask1_button= Button(text="Withdraw",font=('Arial',10),command=withdraw)
        ask2_button = Button(text='Deposit',font=('Arial',10),command=deposit)








        username_label1.place(y=100,x=0)
        accounttype_label.place(y=150,x=0)
        balance_label.place(y=200,x=0)
        ask1_label.place(y=250,x=0)
        ask1_button.place(y=300,x=300)
        ask2_button.place(y=300,x=390)
        ask1entry.place(y=270,x=300)
        new_label1.pack()





        new_window.mainloop()





window.title('EREN BANK',)
window.geometry('300x300')
wallpaper=PhotoImage(file='wp9334095-demon-slayer-black-and-white-wallpapers.png')
window.config(background='white')

eren = PhotoImage(file='logo.png')
window.iconphoto(True,eren)
label_1 = Label(image=eren,font=("Century Gothic",20),text='Welcome to  Eren Bank',
                compound='top',bg='white')
motto =Label(font=("Century Gothic",9),text='TITANS IN BANKING', compound= 'bottom',bg='white',)
username_label= Label(font=('Century Gothic',15),text='Username',bg='white')
password_label= Label(font=('Century Gothic',15),text='Password',bg="white")
username_entry = Entry(window,font=('Myanmar Text',13))
username_password = Entry(window,font=("Myanmar Text",13))

submit_button= Button(window,text='Submit',font=('Arial',12,'italic'),command=clicked_button)



username_label.place(x=550,y=250)
password_label.place(x=550,y=300)
label_1.pack()
motto.pack()
username_entry.place(x=660,y=260)
username_password.place(x=660,y=310)
submit_button.place(x=759,y=350)









window.mainloop()
