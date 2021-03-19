from SQLCall import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # py -m pip install Pillow


class Dirs:
    parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    # Img
    img = os.path.join(parentDirectory, "img")


def alert(title, message, kind="info"):
    if kind not in ("error", "warning", "info"):
        raise ValueError("Unsupported alert kind.")
    show_method = getattr(messagebox, "show{}".format(kind))
    show_method(title, message)


# Login menu
class LoginMenu:
    def __init__(self):
        self.login = False
        # Generate Main Window
        self.login_menu = tk.Tk()
        self.login_menu.title('Login Menu')
        self.login_menu.resizable(0, 0)
        self.login_menu.configure(width=480, height=320)
        self.login_icon = tk.PhotoImage(file=os.path.normcase(Dirs.img + "/pokemon_icon.png"))
        self.login_menu.iconphoto(False, self.login_icon)

        # Logo
        self.logo_path = Image.open(os.path.normcase(Dirs.img + "/pokemon-fire-red.png"))
        self.logo_img = ImageTk.PhotoImage(self.logo_path)
        self.logo_label = tk.Label(self.login_menu, image=self.logo_img)
        self.logo_label.image = self.logo_label

        # User labels and entry
        self.user_label1 = tk.Label(self.login_menu, text="Username", font=16)
        self.user_entry1 = tk.Entry(self.login_menu, state="normal")

        # Passwd labels and entry
        self.passwd_label1 = tk.Label(self.login_menu, text="Password", font=16)
        self.passwd_entry1 = tk.Entry(self.login_menu, state="normal", show="*")

        # Buttons
        self.login_usr = tk.Button(self.login_menu, text="Login", command=self.login_user)
        self.create_usr = tk.Button(self.login_menu, text="Create User", command=self.create_user_canvas)
        self.del_usr = tk.Button(self.login_menu, text="Delete User", command=self.delete_user_canvas)

        # Load logo, user, and passwd labels
        self.place_objects()

        # Handle window close
        self.login_menu.protocol("WM_DELETE_WINDOW", self.on_closing_main)
        self.login_menu.mainloop()

    # Place Logo, User, Passwd label and entry
    def place_objects(self):
        self.logo_label.place(x=50, y=10)

        self.user_label1.place(x=75, y=175)
        self.user_entry1.place(width=215, height=30, x=190, y=175)

        self.passwd_label1.place(x=75, y=215)
        self.passwd_entry1.place(width=215, height=30, x=190, y=215)

        self.login_usr.place(x=340, y=260)
        self.create_usr.place(x=205, y=260)
        self.del_usr.place(x=70, y=260)

    def login_user(self):
        getuser = self.user_entry1.get()
        user = getuser

        getpasswd = self.passwd_entry1.get()
        passwd = getpasswd

        if SQL().ConnectUser(user, passwd):
            alert("Login", "Login in...\nWelcum %s!" % user)

        elif (user == "") or (passwd == ""):
            alert("Login Failed", "Please introduce a valid Username or Password")

        else:
            alert("Login Failed", "User not registered")

    def create_user_canvas(self):
        self.create_usr_canvas = tk.Toplevel(self.login_menu)
        self.create_usr_canvas.title("Create User")
        self.create_usr_canvas.resizable(0, 0)
        self.create_usr_canvas.wm_attributes("-topmost", 1)
        self.create_usr_canvas.configure(width=400, height=250)

        self.header_create = tk.Label(self.create_usr_canvas, text="Create User", font="Arial 18")
        self.user_label = tk.Label(self.create_usr_canvas, text="Username", font="Arial 14")
        self.user_entry = tk.Entry(self.create_usr_canvas, state="normal")
        self.passwd_label = tk.Label(self.create_usr_canvas, text="Password", font="Arial 14")
        self.passwd_entry = tk.Entry(self.create_usr_canvas, state="normal", show="*")
        self.header_create.place(x=150, y=10)
        self.user_label.place(x=25, y=50)
        self.user_entry.place(x=25, y=75, width=215, height=30)
        self.passwd_label.place(x=25, y=115)
        self.passwd_entry.place(x=25, y=145, width=215, height=30)

        self.create_usr = tk.Button(self.create_usr_canvas, text="Create User", command=self.create_user)
        self.create_usr.place(x=130, y=190)

        self.cancel_usr = tk.Button(self.create_usr_canvas, text="Cancel", command=self.on_closing_create)
        self.cancel_usr.place(x=25, y=190)

        self.create_usr_canvas.protocol("WM_DELETE_WINDOW", self.on_closing_create)
        #self.create_usr_canvas.mainloop()


    def create_user(self):
        getuser = self.user_entry.get()
        user = getuser
        print("User: " + user)

        getpasswd = self.passwd_entry.get()
        passwd = getpasswd
        print("Password: " + passwd)

        if SQL().CheckUser(user):
            alert("Username already exist", "There is an account with that username, choose other name")
        
        elif not SQL().ConnectUser(user, passwd):
            if (user == "") or (passwd == ""):
                alert("Need more info", "Please introduce a username and a password", kind="error")
        
            elif (len(user) < 3) or (len(passwd) < 4):
                alert("Create user policy", "You need a Username at least 3 character and 4 for the Password")
        
            else:
                SQL().NewUser(user, passwd)
                alert("User Created", "Your user was created successfully")

    def delete_user_canvas(self):
        self.delete_usr_canvas = tk.Toplevel(self.login_menu)
        self.delete_usr_canvas.title("Delete User")
        self.delete_usr_canvas.resizable(0, 0)
        self.delete_usr_canvas.wm_attributes("-topmost", 1)
        self.delete_usr_canvas.configure(width=400, height=250)

        self.delete_usr_canvas.protocol("WM_DELETE_WINDOW", self.on_closing_delete)
        #self.delete_usr_canvas.mainloop()

    # Ask to quit when closing window
    def on_closing_main(self):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.login_menu.destroy()

    def on_closing_delete(self):
        if messagebox.askyesno("Exit Create User", "Do you want to cancel?"):
            self.delete_usr_canvas.destroy()

    def on_closing_create(self):
        if messagebox.askyesno("Exit Create User", "Do you want to cancel?"):
            self.create_usr_canvas.destroy()
    # or self.delete_usr_canvas
    # self.delete_usr_canvas.destroy()

# print("Exist User: ", SQL().ConnectUser("user12", "0"))
# SQL().NewUser("user12", "0")
# print("Exist User: ", SQL().ConnectUser("user12", "0"))
# SQL().RemoveUser("user12", "0")
# print("Exist User: ", SQL().ConnectUser("user12", "0"))


LoginMenu()
