from tkinter import messagebox
from random import choice, randint, shuffle
import json
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_number + password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)



# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    web = web_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data Not Found")
    else:
        if web in data:
            values = data[web]
            emails = values["email"]
            passwords = values["password"]
            messagebox.showinfo(title=web, message=f"Email: {emails}\nPassword: {passwords}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details found for {web}")





# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_save = web_entry.get()
    email_save = email_entry.get()
    password_save = password_entry.get()
    new_data = {
        website_save:{
            "email": email_save,
            "password": password_save
        }

    }

    if len(website_save) == 0 or len(email_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title=f"OOps", message="No field should be left empty")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"you entered the follow deatils\nEmail: {email_save}\n Password: {password_save}\n is it ok to save")
        if is_ok:
            try:
#............... load the file if it does exist..............................
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)

#.................. create the file if it does not exist.......................
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

#...................... update the file................................
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.config(pady=20, padx=20)
window.title("Password Manager")
canvas = Canvas(width=200, height=200)
image_file = PhotoImage(file="logo.png")

#...............canvas...............................................


canvas.create_image(100,100,image=image_file )
canvas.grid(column=1,)

#..............Labels......................................


web = Label(text="Website")
web.grid(row=1, column=0, sticky="e", padx=20)
email = Label(text="Email/Username")
email.grid(row=2, column=0, sticky="e", padx=20)
password = Label(text="Password")
password.grid(row=3, column=0, sticky="e", padx=20)

#..........................Entries..........................


web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, sticky="w")
web_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2,sticky="w")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")


#........................... Buttons..........................


generate = Button(text="Generate Password", width=15, command=generate_password)
generate.grid(row=3, column=2, sticky="w")
add = Button(text="Add", width=45, command=save)
add.grid(row=4, column=1, columnspan=2, sticky="w")

search_b = Button(text="Search", width=15, command=search)
search_b.grid(row=1, column=2, sticky="w")











window.mainloop()