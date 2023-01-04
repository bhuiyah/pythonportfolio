from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FILE = "data.json"

def find_password():
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found")
    else:
        try:
            user = data[website_entry.get()]["email/user"]
            passw = data[website_entry.get()]["password"]
            pyperclip.copy(passw)
            messagebox.showinfo(title=f"{website_entry.get()}", message=f"Email/UserName: {user}\nPassword: {passw}")
        except KeyError:
            messagebox.showinfo(title="Error", message=f"No details for the website exists, please retry.")
            
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "email/user": user,
            "password": password,
        }
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(FILE, "r") as file:
                #Reading old data
                data = json.load(file)
                    
        except FileNotFoundError:
            with open(FILE, "w") as file:
                json.dump(new_data, file, indent=4)

        else: 
            #Updating old data with new data
            data.update(new_data)
            with open(FILE, "w") as file:
                json.dump(data, file,  indent=4)
        
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showinfo(title="Success", message=f"Saved the password for {web}")
            
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

search = Button(text="Search", command=find_password)
search.grid(column=2, row=1, sticky="EW")

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(END, "bhuiyah")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
