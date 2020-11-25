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
    global login_button, username_entry, password_entry
    #This label doesn't need a variable as it is constantly going to be there
    Label(frame_heading, text="Dungeon Disaster",font=('Arial',16)).grid(row = 0, column = 1, padx = 0, pady = 5)
    #This label has spaces before and after it so that it can go perfectly on top of the "sign_up_label".
    #Doing this, these labels don't need to be removed.
    login_label = Label(frame_heading,text=" Login  ",font=('Arial',12))
    login_label.grid(row = 1, column = 1, padx = 0, pady = 5)
    
    #Place the entry widgets
    username_entry = Entry (frame_entry, width = 15
                            , bg = "white")
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
    valid_entries = True
    logged_in = False
    #This will check if the user has entered anything in the entry widgets
    if username_entry.get() == "":
        username_entry.delete(0,END)
        username_entry.insert(0,"No username entered")
        valid_entries = False
    
    if password_entry.get() == "":
        password_entry.delete(0,END)
        password_entry.insert(0,"No password entered")
        valid_entries = False


    database_file = open("Student_Credentials.txt", "r")
    for line in database_file.readlines():
        line = line.strip()
        user = line.split("|")
        #The username won't be case sensitive
        if (username_entry.get()).upper() == (user[0]).upper():
            valid_entries = True
            #The password will be case sensitive
            if password_entry.get() == user[1]:
                logged_in = True
                
            else:
                password_entry.delete(0,END)
                password_entry.insert(0,"Incorrect Password")
                
        else:
            username_entry.delete(0,END)
            username_entry.insert(0,"User does not exist")
            
          
    database_file.close()

    #If the code is valid and the user has been logged in, it will start the quiz        
    if logged_in == True and valid_entries == True:
        window.destroy()
        quiz()
    
    
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
    #The house buttons will pass the character that represents their house into a procedure to set the variable "student_house"
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
    #If the password is valid, the function will return "True"
    if validation() == True:
        #To write to the database text-file, it needs to be opened in append mode
        database_file = open("Student_Credentials.txt", "a")
        #The data will all be stored in the database and each section is divided up using | symbol
        database_file.write(username_entry.get() + "|" + password_entry.get() + "|" + student_house + "|0\n")
        database_file.close()
        #The user will return to login menu
        login_menu()

special_symbols = ["!", "£", "$", "%", "&", "*", "@", ":", ";", "~", "#","-", "_", "+", "=", "/", "<", ">", ",", ".","?"]
def validation():
    #Check if the user already exists
    user_exists = False
    database_file = open("Student_Credentials.txt", "r")
    for line in database_file.readlines():
        line = line.strip()
        user = line.split("|")
        if (username_entry.get()).upper() == (user[0]).upper():
            user_exists = True
    database_file.close()
    
    if user_exists == True:
        username_entry.delete(0,END)
        username_entry.insert(0,"Username already exists")

    username_valid = True
    #Check the length of the username
    if len(username_entry.get()) > 20:
        username_entry.delete(0,END)
        username_entry.insert(0,"Username too long")
        username_valid = False
    elif len(username_entry.get()) < 1:
        username_entry.delete(0,END)
        username_entry.insert(0,"Username too short")
        username_valid = False
    
    #Check if passwords match
    if password_entry.get() == confirm_p_entry.get():
        confirm_password = True
    else:
        confirm_p_entry.delete(0,END)
        confirm_p_entry.insert(0, "Passwords don't match")
        confirm_password = False

    
    #Check if password is valid
    valid_password = True
    #Check length
    if len(password_entry.get()) < 8:
        valid_password = False
    if len(password_entry.get()) > 20:
        valid_password = False
    #Check special character
    if not any (character in special_symbols for character in password_entry.get()):
        valid_password = False
    #Check capital letter
    if not any (character.isupper() for character in password_entry.get()):
        valid_password = False
    #Display message
    if valid_password == False:
        password_entry.delete(0,END)
        password_entry.insert(0, "Password not valid")

    #Check if a house is selected
    if student_house == "":
        confirm_p_entry.delete(0,END)
        confirm_p_entry.insert(0, "No house has been selected")
        house_selected = False
    else:
        house_selected = True
    
    if user_exists == False and username_valid == True and confirm_password == True and valid_password == True and house_selected == True:
        return True
    else:
        return False

    
def quiz():
    pass
login_menu()
window.mainloop()


