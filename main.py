import mysql.connector
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Login_database")
root.config(bg="Black")
root.geometry("600x600")

# start of label name
lab_name = Label(root, text="Enter your Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=20)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=260, y=20, width=220, height=30)
# end of label name
# start of label password
lab_password = Label(root, text="Enter your Password: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_password.place(x=60, y=70)
entry_password = Entry(root, show="*", bg="lightblue", fg="black")
entry_password.place(x=310, y=70, width=220, height=30)
# end of password label


# login function
def login():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospital',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Login')
    for i in mycursor:
        if i[1] == entry_password.get() and i[0] == entry_name.get():
            messagebox.showinfo("Output", "Login")
    if i[1] != entry_password.get() or i[0] != entry_name.get():
            messagebox.showinfo("Output", "Enter correct information")
            entry_password.delete(0, END)
            entry_name.delete(0, END)


# login button
login_btn = Button(root, text="Login", borderwidth="10", command=login, font=("Consolas 13 bold"), bg="black", fg="lightblue")
login_btn.place(x=80, y=150)


# clear function
def clear():
    entry_name.delete(0, END)
    entry_password.delete(0, END)


# clear button
clear_button = Button(root, text="Clear", borderwidth="10", command=clear, font=("Consolas 13 bold"), bg="black", fg="lightblue")
clear_button.place(x=240, y=150)


# exit function
def register():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='Hospital', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "INSERT INTO Login (username, password) Value(%s, %s)"
    val = (entry_name.get(), entry_password.get())
    mycursor.execute(sql, val)
    messagebox.showinfo("Output", "Registration Done.You can login.")
    entry_password.delete(0, END)
    entry_name.delete(0, END)
    mydb.commit()



# exit button
exit_button = Button(root, text="Register", borderwidth="10", command=register, font=("Consolas 13 bold"), bg="black", fg="lightblue")
exit_button.place(x=390, y=150)


root.mainloop()
