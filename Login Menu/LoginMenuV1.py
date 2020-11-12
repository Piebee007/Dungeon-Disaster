from tkinter import *

#This section of code is responsible for creating the tkinter window
window = Tk()
window.title("Login Menu")
window.geometry("350x350")
window.resizable(True, True)
window.configure(background = "Light Blue")


#This is creating a frame which will be used to place a heading for that page
frame_heading = Frame(window)
frame_heading.grid(row = 0, column = 0, columnspan = 2, padx = 30, pady = 5)

#Create a frame to place the entry widgets and labels. It can help to organise details.
frame_entry = Frame(window)
frame_entry.grid(row = 1, column = 0, columnspan = 2, padx = 25, pady = 5)


def login_menu():
    global login_button
    #This label doesn't need a variable as it is constantly going to be there
    Label(frame_heading, text="Dungeon Disaster",font=('Arial',16)).grid(row = 0, column = 1, padx = 0, pady = 5)
    #This label has spaces before and after it so that it can go perfectly on top of the "sign_up_label". Doing this, these labels don't need to be removed.
    login_label = Label(frame_heading,text=" Login  ",font=('Arial',12))
    login_label.grid(row = 1, column = 1, padx = 0, pady = 5)
    
    #Place the entry widgets
    username_entry = Entry (frame_entry, width = 15, bg = "white")
    username_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

    password_entry = Entry (frame_entry, width =15, bg = "white")
    password_entry.grid(row = 1, column = 1,padx = 5, pady = 5)

    #Place the labels next to the entry widget so that the user knows what each entry widget is for
    username_label = Label (frame_entry, text ="Username: ")
    username_label.grid(row = 0, column = 0,padx = 10, pady = 5)

    password_label = Label (frame_entry, text ="Password: ")
    password_label.grid(row = 1, column = 0,padx = 10, pady = 5)

    #Buttons
    quit_button = Button(window, text = "QUIT", width = 7,bg = "RED", command = quit)
    quit_button.grid(row = 2, column = 0, padx = 0, pady = 5)
    
    sign_up_menu_button = Button(window, text = "SIGN UP", width = 7,bg = "Grey", command = sign_up_menu)
    sign_up_menu_button.grid(row = 2, column = 1, padx = 0, pady = 5)
    
    login_button = Button(window, text = "LOG IN", width = 7,bg = "Green", command = login)
    login_button.grid(row = 2, column = 2, padx = 0, pady = 5)

def login():
    pass

student_house = ""
def sign_up_menu():
    global confirm_p_entry, confirm_pass_label, house_label, darwin_button, faraday_button, newton_button, back_button, sign_up_button, quit_button
    
    #Entry widgets
    confirm_p_entry = Entry (frame_entry, width = 15, bg = "white")
    confirm_p_entry.grid(row = 2, column = 1, padx = 5, pady = 0)

    #Labels
    sign_up_label = Label(frame_heading,text="Sign Up",font=('Arial',12))
    sign_up_label.grid(row = 1, column = 1, padx = 0, pady = 5)

    confirm_pass_label = Label(frame_entry, text ="Confirm Password: ")
    confirm_pass_label.grid(row = 2, column = 0,padx = 10, pady = 5)

    house_label = Label(frame_entry, text ="House ")
    house_label.grid(row = 3, column = 1,padx = 10, pady = 5)
    
    #House Buttons
    #The house buttons will pass the character that represents their house into a function to set the variable "student_house"
    darwin_button = Button(window, text = "Darwin", width = 7,bg = "green", command = lambda *args: select_house("D"))
    darwin_button.grid(row = 2, column = 0, padx = 0, pady = 5)
    
    faraday_button = Button(window, text = "Faraday", width = 7,bg = "blue", command = lambda *args: select_house("F"))
    faraday_button.grid(row = 2, column = 1, padx = 0, pady = 5)
    
    newton_button = Button(window, text = "Faraday", width = 7,bg = "red", command = lambda *args: select_house("N"))
    newton_button.grid(row = 2, column = 2, padx = 0, pady = 5)
    
    #Buttons
    #The login button must be replaced by the sign up button
    login_button.destroy()

    back_button = Button(window, text = "BACK", width = 7,bg = "Grey", command = remove_from_window)
    back_button.grid(row = 3, column = 1, padx = 0, pady = 5)

    sign_up_button = Button(window, text = "SIGN UP", width = 7,bg = "Grey", command = sign_up)
    sign_up_button.grid(row = 3, column = 2, padx = 0, pady = 5)

    quit_button = Button(window, text = "QUIT", width = 7,bg = "RED", command = quit)
    quit_button.grid(row = 3, column = 0, padx = 0, pady = 5)
    
    
def select_house(letter):
    global student_house
    student_house = letter
    
def remove_from_window():
    confirm_p_entry.destroy()
    confirm_pass_label.destroy()
    house_label.destroy()
    darwin_button.destroy()
    faraday_button.destroy()
    newton_button.destroy()
    back_button.destroy()
    sign_up_button.destroy()
    quit_button.destroy()
    login_menu()

def sign_up():
    pass
login_menu()
window.mainloop()



















