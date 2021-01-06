from tkinter import *


def send_email():

    root = Tk()
    root.title("Sending Emails")
    root.geometry("1000x600")

    def my_function():
        import smtplib
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            sender_email = txt1.get()
            receiver_email = txt2.get()
            password = txt3.get()

            server.starttls()

            server.login(sender_email, password )
            message = txt4.get
            server.sendmail(sender_email, receiver_email, 'This isa test email')
            print("the message has been successfully sent")

        except Exception as err:
            print("Something went wrong..", err)
        finally:
            server.close()
    my_function()

    label_frame1= Frame(root)
    label_frame1.pack()
    label_frame2=Frame(root)
    label_frame2.pack()
    label_frame3=Frame(root)
    label_frame3.pack()
    label_frame4=Frame(root)
    label_frame4.pack()
    label_frame5=Frame(root)
    label_frame5.pack()

    lab1 = Label(label_frame1,text="Please enter sender email :")
    lab1.grid(row=1, column=1)

    lab2 = Label(label_frame2, text="Please enter receiver email :")
    lab2.grid(row=2, column=1)

    lab3 = Label(label_frame3, text="Please enter your password :")
    lab3.grid(row=3, column=1)

    txt1 = Entry(label_frame1)
    txt1.grid(row=1, column=3)

    txt2 = Entry(label_frame2)
    txt2.grid(row=2, column=3)

    txt3 = Entry(label_frame3)
    txt3.grid(row=3, column=3)

    txt4 = Entry(label_frame4, )
    txt4.grid(row=1, column=1, padx=100, pady=100, ipady=100, ipadx=200)


    btn1 = Button(label_frame5, text="SEND", command=my_function)
    btn1.grid(row=4, column=2)

    root.mainloop()


send_email()



