from tkinter import *
from tkinter import messagebox
import pygame
import random
import time
from math import sqrt
import socket
import pickle
from ObjectCodeV6 import Player, Enemy,bulletArray, Projectile

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

player_data = [] 
def login():
    global player_data
    valid_entries = False
    logged_in = False
    #This will check if the user has entered anything in the entry widgets
    if username_entry.get() == "":
        username_entry.delete(0,END)
        messagebox.showerror("Username","No username entered")
        valid_entries = False
    
    if password_entry.get() == "":
        password_entry.delete(0,END)
        messagebox.showerror("Password","No password entered")
        
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
                #Used to update player's highscore
                player_data.append(user[0])
                player_data.append(user[1])
                player_data.append(user[2])
                player_data.append(user[3])
                
            else:
                password_entry.delete(0,END)
                messagebox.showerror("Password","Incorrect Password")
                
    if valid_entries == False:
        username_entry.delete(0,END)
        messagebox.showerror("Username","User does not exist")
        
            
          
    database_file.close()

    #If the code is valid and the user has been logged in, it will start the quiz        
    if logged_in == True and valid_entries == True:
       
        window.destroy()
        quiz()
    
    
student_house = ""
def sign_up_menu():
    global confirm_p_entry, confirm_pass_label, house_label, darwin_button, faraday_button, newton_button, back_button, sign_up_button, quit_button, password_requirements
    
    #Entry widgets
    confirm_p_entry = Entry (frame_entry, width = 15, bg = "white")
    confirm_p_entry.grid(row = 3, column = 1, padx = 5, pady = 0)

    #Labels
    sign_up_label = Label(frame_heading,text="Sign Up",font=('Arial',12))
    sign_up_label.grid(row = 1, column = 1, padx = 0, pady = 5)

    confirm_pass_label = Label(frame_entry, text ="Confirm Password: ")
    confirm_pass_label.grid(row = 3, column = 0,padx = 10, pady = 5)

    password_requirements = Label(frame_entry, text = "Include: Between 8 and 20 characters,\n at least 1 capital letter\n and at least 1 unique symbol")
    password_requirements.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 5)
                                  
    house_label = Label(frame_entry, text ="House ")
    house_label.grid(row = 4, column = 1,padx = 10, pady = 5)
    
    #House Buttons
    #The house buttons will pass the character that represents their house into a procedure to set the variable "student_house"
    darwin_button = Button(window, text = "Darwin", width = 7,bg = "green", command = lambda *args: select_house("D"))
    darwin_button.grid(row = 2, column = 0, padx = 0, pady = 5)
    
    faraday_button = Button(window, text = "Faraday", width = 7,bg = "blue", command = lambda *args: select_house("F"))
    faraday_button.grid(row = 2, column = 1, padx = 0, pady = 5)
    
    newton_button = Button(window, text = "Newton", width = 7,bg = "red", command = lambda *args: select_house("N"))
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
    password_requirements.destroy()
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
        remove_from_window()

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
        messagebox.showerror("Username","Username already exists")

    username_valid = True
    #Check the length of the username
    if len(username_entry.get()) > 20 and user_exists == False:
        username_entry.delete(0,END)
        messagebox.showerror("Username","Username too long")
        username_valid = False
    elif len(username_entry.get()) < 1 and user_exists == False:
        username_entry.delete(0,END)
        messagebox.showerror("Username","Username too short")
        username_valid = False
    
    #Check if passwords match
    if password_entry.get() == confirm_p_entry.get() and username_valid == True:
        confirm_password = True
    else:
        confirm_p_entry.delete(0,END)
        messagebox.showerror("Password", "Passwords don't match")
        confirm_password = False

    
    #Check if password is valid
    valid_password = True
    #Check length
    if len(password_entry.get()) < 8 and confirm_password == True:
        valid_password = False
    if len(password_entry.get()) > 20 and confirm_password == True:
        valid_password = False
    #Check special character
    if not any (character in special_symbols for character in password_entry.get()) and confirm_password == True:
        valid_password = False
    #Check capital letter
    if not any (character.isupper() for character in password_entry.get()) and confirm_password == True:
        valid_password = False
    #Display message
    if valid_password == False:
        password_entry.delete(0,END)
        messagebox.showerror("Password","Password not valid.\nEnsure that there is between 8 and 20 characters,\n at least 1 capital letter and \n one unque symbol ")

    #Check if a house is selected
    if student_house == "" and valid_password == True:
        messagebox.showerror("House", "No house has been selected")
        house_selected = False
    else:
        house_selected = True
        
    if user_exists == False and username_valid == True and confirm_password == True and valid_password == True and house_selected == True:
        return True
    else:
        return False


screenwidth = 1600
screenheight = 720


QuizBackground = pygame.image.load("MatrixPhoto.jpg")

question_num = 0
score_gained = 0
health_gained = 0
damage_multiplier = 0




#This function will show which one of the 3 options each answer box will be
def random_answer():
    global answer1_hitbox, answer2_hitbox, answer3_hitbox
    answer1_hitbox = [120, 180, 1360, 90]
    answer2_hitbox = [120, 350, 1360, 90]
    answer3_hitbox = [120, 520, 1360, 90]
    
    random_options = [1,2,3]
    answer1_hitbox.append((random_options[(random.randint(0,(len(random_options)-1)))]))
    random_options.remove((answer1_hitbox[4]))
    answer2_hitbox.append((random_options[(random.randint(0,(len(random_options)-1)))]))
    random_options.remove((answer2_hitbox[4]))
    answer3_hitbox.append((random_options[(random.randint(0,(len(random_options)-1)))]))



mouse_in_hitbox1 = False
mouse_in_hitbox2 = False
mouse_in_hitbox3 = False
def quiz():
    global mouse_in_hitbox1, mouse_in_hitbox2, mouse_in_hitbox3, question_num, score_gained, health_gained, damage_multiplier, screen
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screenwidth,screenheight))
    #The program will retrieve the questions from the text file and choose what questions will be chosen
    retrieve_questions()
    
    #This will randomly arrange the answers
    random_answer()
    
    #The while loop will continue until all the questions have been completed or if the user clicks on the "x" button
    quiz_loop = True
    while quiz_loop == True:
        #This will close the while loop if the user clicks on the red "x" button. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quiz_loop = False
        #Retrieve data from the mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        
        #Answer box 1
        #This code is responsible for checking if the mouse is in the answerbox
        if mouse[0] > answer1_hitbox[0] and mouse[0] < answer1_hitbox[0] + answer1_hitbox[2]:
            if mouse[1] > answer1_hitbox[1] and mouse[1] < answer1_hitbox[1] + answer1_hitbox[3]:
                mouse_in_hitbox1 = True
                #If the user clicks whilst in the answer box, it will check if the user got the answer right or wrong
                if click[0] == 1:
                    time.sleep(1)
                    if questions[(questions_to_be_selected[question_num])][(answer1_hitbox[4])] == questions[(questions_to_be_selected[question_num])][4]:
                        #If the user's answer is correct, it will give a reward depending on its difficulty
                        #After each question, it will check if the quiz has been completed (the number of questions being greater than 5)
                        if questions[(questions_to_be_selected[question_num])][5] == "E":
                            score_gained += 50
                            if question_num < 4:
                                question_num += 1
                                #When the question number goes up, it will shuffle the answer positions for the next question
                                random_answer()
                            #If the quiz has been completed, it will stop the while loop and start the game
                            else:
                                quiz_loop = False
                                main_game_loop()
                        elif questions[(questions_to_be_selected[question_num])][5] == "M":
                            health_gained += 25
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()
                        else:
                            damage_multiplier += 0.25
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()

                        #Plays the correct sound effect when correct
                        pygame.mixer.music.load("Correct Sound Effect.wav")
                        pygame.mixer.music.play(0)
                    else:
                        #Plays the incorrect sound effect when incorrect
                        pygame.mixer.music.load("Fail Sound Effect.mp3")
                        pygame.mixer.music.play(0)
                        if question_num < 4:
                            question_num += 1
                            random_answer()

                        else:
                            quiz_loop = False
                            main_game_loop()
            #This section of code stops the error indicated in "Quiz Errors", Error Number 3.1
            else:
                mouse_in_hitbox1 = False

        else:
            mouse_in_hitbox1 = False

        
        #Answer box 2
        if mouse[0] > answer2_hitbox[0] and mouse[0] < answer2_hitbox[0] + answer2_hitbox[2]:
            if mouse[1] > answer2_hitbox[1] and mouse[1] < answer2_hitbox[1] + answer2_hitbox[3]:
                mouse_in_hitbox2 = True
                if click[0] == 1:
                    time.sleep(1)
                    if questions[(questions_to_be_selected[question_num])][(answer2_hitbox[4])] == questions[(questions_to_be_selected[question_num])][4]:
                        if questions[(questions_to_be_selected[question_num])][5] == "E":
                            score_gained += 50
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                main_game_loop()
                        elif questions[(questions_to_be_selected[question_num])][5] == "M":
                            health_gained += 25
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()
                        else:
                            damage_multiplier += 0.25
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()

                        pygame.mixer.music.load("Correct Sound Effect.wav")
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load("Fail Sound Effect.mp3")
                        pygame.mixer.music.play(0)
                        if question_num < 5:
                            question_num += 1
                            random_answer()

                        else:
                            quiz_loop = False
                            main_game_loop()
            else:
                mouse_in_hitbox2 = False

        else:
            mouse_in_hitbox2 = False


        #Answer box 3
        if mouse[0] > answer3_hitbox[0] and mouse[0] < answer3_hitbox[0] + answer3_hitbox[2]:
            if mouse[1] > answer3_hitbox[1] and mouse[1] < answer3_hitbox[1] + answer3_hitbox[3]:
                mouse_in_hitbox3 = True
                if click[0] == 1:
                    time.sleep(1)
                    if questions[(questions_to_be_selected[question_num])][(answer3_hitbox[4])] == questions[(questions_to_be_selected[question_num])][4]:
                        if questions[(questions_to_be_selected[question_num])][5] == "E":
                            score_gained += 50
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()
                        elif questions[(questions_to_be_selected[question_num])][5] == "M":
                            health_gained += 25
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()
                        else:
                            damage_multiplier += 0.25
                            if question_num < 4:
                                question_num += 1
                                random_answer()
                            else:
                                quiz_loop = False
                                main_game_loop()
                        pygame.mixer.music.load("Correct Sound Effect.wav")
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load("Fail Sound Effect.mp3")
                        pygame.mixer.music.play(0)
                        if question_num < 4:
                            question_num += 1
                            random_answer()

                        else:
                            quiz_loop = False
                            main_game_loop()
            else:
                mouse_in_hitbox3 = False

        else:
            mouse_in_hitbox3 = False

        #After each loop, the pygame window will be updated using the redraw_quiz_window procedure
        redraw_quiz_window()





def retrieve_questions():
    global questions, questions_to_be_selected
    #This section gets all the questions and stores it in a 2D array
    quiz_file = open("ESafetyQuestionsQuiz.txt", "r")
    questions= []
    total_questions = 0
    for line in quiz_file.readlines():
        line = line.strip()
        esafety_questions = line.split("#")
        questions.append([esafety_questions[0],esafety_questions[1],esafety_questions[2],esafety_questions[3],esafety_questions[4],esafety_questions[5]])
        total_questions +=1
    quiz_file.close()
    #There will be 5 questions that will be randomly selected to play
    questions_to_be_selected = []
    for i in range (0,5):
       questions_to_be_selected.append(random.randint(0,(total_questions-1)))
    

question_box = [125, 45, 945, 100]
difficulty_box = [1150, 30, 320, 55]
reward_box = [1150, 115, 320, 55]

def redraw_quiz_window():
    #Display the picture on the background
    screen.blit(QuizBackground,(0,0))
    #Display the question box and the text

    pygame.draw.rect(screen, (255,255,255),[question_box[0],question_box[1],question_box[2],question_box[3]])
    pygame.draw.rect(screen, (0,0,0),[question_box[0],question_box[1],question_box[2],question_box[3]],5)
    
    font1 = pygame.font.SysFont('comicsans', 30)
    question_text = font1.render((questions[(questions_to_be_selected[question_num])][0]), 1, (0,0,0))
    screen.blit(question_text, (question_box[0]+15, (question_box[1] + (question_box[3]/2))))
    
    #Display the difficulty box and reward box

    pygame.draw.rect(screen, (255,255,255),[difficulty_box[0],difficulty_box[1],difficulty_box[2],difficulty_box[3]])
    pygame.draw.rect(screen, (0,0,0),[difficulty_box[0],difficulty_box[1],difficulty_box[2],difficulty_box[3]],5)

    pygame.draw.rect(screen, (255,255,255),[reward_box[0],reward_box[1],reward_box[2],reward_box[3]])
    pygame.draw.rect(screen, (0,0,0),[reward_box[0],reward_box[1],reward_box[2],reward_box[3]],5)
    #Displaying text for difficulty and reward box
    font2 = pygame.font.SysFont('comicsans', 25) #A new font so that this text will be smaller
    if (questions[(questions_to_be_selected[question_num])][5]) == "E":
        reward_text = font2.render("50 Points", 1, (0,0,0))
        difficulty_text = font2.render("Easy", 1, (0,0,0))

    elif (questions[(questions_to_be_selected[question_num])][5]) == "M":
        reward_text = font2.render("25 Extra Health", 1, (0,0,0))
        difficulty_text = font2.render("Medium", 1, (0,0,0))
          
    else:
        reward_text = font2.render("25% Damage Boost", 1, (0,0,0))
        difficulty_text = font2.render("Hard", 1, (0,0,0))

    screen.blit(reward_text,(reward_box[0]+15, (reward_box[1] + (reward_box[3]/2))))
    screen.blit(difficulty_text,(difficulty_box[0]+15, (difficulty_box[1] + (difficulty_box[3]/2))))
                                   

    #Display the 3 answers
    
    
    #Answer box 1
    pygame.draw.rect(screen, (255, 255,255),[answer1_hitbox[0],answer1_hitbox[1],answer1_hitbox[2],answer1_hitbox[3]])
    if mouse_in_hitbox1 == True:
        pygame.draw.rect(screen, (255, 0,0),[answer1_hitbox[0],answer1_hitbox[1],answer1_hitbox[2],answer1_hitbox[3]], 5)
    else:
        pygame.draw.rect(screen, (0, 0,0),[answer1_hitbox[0],answer1_hitbox[1],answer1_hitbox[2],answer1_hitbox[3]], 5)

    #Answer box 2
    pygame.draw.rect(screen, (255, 255,255),[answer2_hitbox[0],answer2_hitbox[1],answer2_hitbox[2],answer2_hitbox[3]])
    if mouse_in_hitbox2 == True:
        pygame.draw.rect(screen, (255, 0,0),[answer2_hitbox[0],answer2_hitbox[1],answer2_hitbox[2],answer2_hitbox[3]],5)
    else:    
        pygame.draw.rect(screen, (0, 0,0),[answer2_hitbox[0],answer2_hitbox[1],answer2_hitbox[2],answer2_hitbox[3]],5)

    #Answer box 3
    pygame.draw.rect(screen, (255, 255,255),[answer3_hitbox[0],answer3_hitbox[1],answer3_hitbox[2],answer1_hitbox[3]])
    if mouse_in_hitbox3 == True:
        pygame.draw.rect(screen, (255, 0,0),[answer3_hitbox[0],answer3_hitbox[1],answer3_hitbox[2],answer3_hitbox[3]],5)
    else:    
        pygame.draw.rect(screen, (0, 0,0),[answer3_hitbox[0],answer3_hitbox[1],answer3_hitbox[2],answer3_hitbox[3]],5)


    #Text for the answer boxes
    
    answer_text1 = font1.render((questions[(questions_to_be_selected[question_num])][(answer1_hitbox[4])]), 1, (0,0,0))
    answer_text2 = font1.render((questions[(questions_to_be_selected[question_num])][(answer2_hitbox[4])]), 1, (0,0,0))
    answer_text3 = font1.render((questions[(questions_to_be_selected[question_num])][(answer3_hitbox[4])]), 1, (0,0,0))

    
    screen.blit(answer_text1, (answer1_hitbox[0]+15, (answer1_hitbox[1] + (answer1_hitbox[3]/2))))
    screen.blit(answer_text2, (answer2_hitbox[0]+15, (answer2_hitbox[1] + (answer2_hitbox[3]/2))))
    screen.blit(answer_text3, (answer3_hitbox[0]+15, (answer3_hitbox[1] + (answer3_hitbox[3]/2))))
    
    pygame.display.update()


#These are the limits for the in-game wall so that players, enemies or bullets can go outside of the walls.
wall_limit_x1 =405
wall_limit_x2 = 1520
wall_limit_y1 = 50
wall_limit_y2 = 665


#Here is where all the images will be loaded
player_images = [[(pygame.image.load('Player1.png')),  (pygame.image.load('Player2.png')),  (pygame.image.load('Player3.png'))],[(pygame.transform.flip((pygame.image.load('Player1.png')), True, False)), (pygame.transform.flip((pygame.image.load('Player2.png')), True, False)),(pygame.transform.flip((pygame.image.load('Player3.png')), True, False))],[(pygame.image.load('Player4.png')),  (pygame.image.load('Player5.png')),  (pygame.image.load('Player6.png'))], [(pygame.image.load('Player7.png')),  (pygame.image.load('Player8.png')),  (pygame.image.load('Player9.png'))]]

dungeonBackground = pygame.image.load('DungeonBackground.png')
melee_enemies_images = [[(pygame.image.load('Goblin1.png')),  (pygame.image.load('Goblin2.png')),  (pygame.image.load('Goblin3.png'))],[(pygame.transform.flip((pygame.image.load('Goblin1.png')), True, False)), (pygame.transform.flip((pygame.image.load('Goblin2.png')), True, False)),(pygame.transform.flip((pygame.image.load('Goblin3.png')), True, False))],[(pygame.image.load('Goblin4.png')),  (pygame.image.load('Goblin5.png')),  (pygame.image.load('Goblin6.png'))], [(pygame.image.load('Goblin7.png')),  (pygame.image.load('Goblin8.png')),  (pygame.image.load('Goblin9.png'))]]
ranged_enemies_images = [[(pygame.image.load('Ranged1.png')),  (pygame.image.load('Ranged2.png')),  (pygame.image.load('Ranged3.png'))],[(pygame.transform.flip((pygame.image.load('Ranged1.png')), True, False)), (pygame.transform.flip((pygame.image.load('Ranged2.png')), True, False)),(pygame.transform.flip((pygame.image.load('Ranged3.png')), True, False))],[(pygame.image.load('Ranged4.png')),  (pygame.image.load('Ranged5.png')),  (pygame.image.load('Ranged6.png'))], [(pygame.image.load('Ranged7.png')),  (pygame.image.load('Ranged8.png')),  (pygame.image.load('Ranged9.png'))]]

#Y Scale Factor = 1.2
#x Scale Factor = 1.575
dungeonBackground = pygame.transform.scale(dungeonBackground, (1260, 720))
horizontalDoor = pygame.image.load('HorizontalDoor.png')
horizontalDoor = pygame.transform.scale(horizontalDoor,(65,250))
verticalDoor = pygame.image.load('VerticalDoor.png')
verticalDoor = pygame.transform.scale(verticalDoor,(250,50))

rules_image = pygame.image.load("RulesImage.png")
#Collectable images
common_collectable = pygame.image.load("Shoe.png")
rare_collectable = pygame.image.load("Cube.png")
epic_collectable = pygame.image.load("Trophie.png")
legendary_collectable = pygame.image.load("Diamond.png")



pygame.mixer.init()
#The array for the weapon data
weapon_data = [[0.5, 5, 3, 20, 0], [0.05, 2, 6, 100, 500], [3, 50, 2, 5, 1500]]

gunShot = pygame.mixer.Sound("Gunshot.wav")
machineGun = pygame.mixer.Sound("MachineGun.wav")
wand = pygame.mixer.Sound("MachineGun.wav")
fail_sound_effect = pygame.mixer.Sound("FailSoundEffect.wav")
purchased_sound = pygame.mixer.Sound("PurchaseSound.wav")
death_sound =  pygame.mixer.Sound("DeathSound.wav")
hit_sound = pygame.mixer.Sound("HitSound.ogg")

#Music: https://freesound.org/people/edwardszakal/sounds/514154/
music = pygame.mixer.music.load ('GameMusic.mp3')
pygame.mixer.music.play(-1)

#This is the 2D array to create the map. It can be edited but for a fully functioning map they will need ot piece together correctly
#TRC = TopRightCorner
#TLC = TopLeftCorner
#BRC = BottomRightCorner
#BLC = BottomLefCorner
#XC = Horizontal Corridoor
#YC = Vertical Corridoor
#E = Empty
#UTJ = UpTJunction
#DTJ = DownTJunction
#LTJ = LeftTJunction
#RTJ = RightTJunction
#FWJ = 4 way junction
#OWU = OneWayUp
#OWD = OneWayDown
#OWL = OneWayleft
#OWR = OneWayUpRight

#These are all the maps
maps = [[["OWR", "XC", "XC", "XC", "XC", "XC", "XC", "TLC"], ["E","E","E","E","E","E","E","YC"],["TRC", "XC", "XC", "XC", "XC", "XC", "XC", "BLC"], ["YC","E","E","E","E","E","E","E"],["BRC", "XC", "XC", "XC", "XC", "XC", "XC", "TLC"], ["E","E","E","E","E","E","E","YC"], ["TRC", "XC", "XC", "XC", "XC", "XC", "XC", "BLC"], ["OWU","E","E","E","E","E","E","E"]],
        [["OWR", "XC", "XC", "XC", "DTJ", "XC", "TLC", "E"], ["E","E","E","E","YC","E","BRC","OWL"], ["E","E","E","E","YC","E","E","E"], ["TRC", "XC", "XC", "XC", "UTJ", "XC", "XC", "TLC"], ["YC","E","E","E","E","E","E","YC"],["BRC", "XC", "XC", "XC", "UTJ", "XC", "XC", "BLC"],["E","E","E","YC","E","E","E","E"],["OWR", "XC", "XC", "XC", "UTJ", "XC", "XC", "OWL"]],
        [["OWD","E","E","OWD","E","TRC","XC","TLC"], ["YX","E","E","YC","E","YC","E","YC"], ["BRC","TLC","E","BRC","XC","BLT","E","YC"], ["E","BRC","TLC","E","E","E","E","YC"], ["E","E","RTJ","TLC","E","E","E","YC"], ["E","E","RTJ","UTJ","TLC","E","E","YC"], ["E","E","YC","E","BRC","TLC","E","YC"], ["OWR","XC","BLC","E","E","BRC","XC","BLC"]]]



tileWidth = 42
tileHeight = 24
def drawMiniMap(map_number):
    x = 0
    y = 0
    #Loop through the specific map
    for row in maps[map_number]:
        for col in row:
            if col == "E":
                pygame.draw.rect(screen, (255,255,255), [x,y,tileWidth, tileHeight])

            else:
                pygame.draw.rect(screen,(0,0,0), [x,y,tileWidth, tileHeight])
            x += tileWidth
        y += tileHeight
        x = 0
        #Border around the minimap
        pygame.draw.rect(screen, (0,0,0), (0,0, 336, 192), 5)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverIP = "192.168.1.106"
port = 5555
address = (serverIP ,port)

def connect_client():
    try:
        client_socket.connect(address)
        return pickle.loads(client_socket.recv(4096))
    except:
        pass

def send(data_to_send):
    try:
        client_socket.send(pickle.dumps(data_to_send))
        return pickle.loads(client_socket.recv(4096))
    except socket.error as error:
        print(error)

  
def create_enemies (num_enemies, player, player2):
    print("created")
    player.online_enemy_array = []
    for i in range(num_enemies):
        enemy_type = random.randint(1,2)
        enemy_target = random.randint(0,1)
        if enemy_type == 1 :
            player.online_enemy_array.append([(random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), "R", enemy_target])

        else:
            player.online_enemy_array.append([(random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), "M", enemy_target])
    


    print(player.online_enemy_array)

#This array will store all the enemies
enemyArray = []


def spawnEnemies(player):
    if len(player.online_enemy_array) >0:
        print(player.online_enemy_array)
    
    while len(player.online_enemy_array) > 0:
        if player.online_enemy_array [0][2] == "R":
            enemyArray.append(Enemy(player.online_enemy_array[0][0], player.online_enemy_array[0][1],50,0,1,ranged_enemies_images, player.online_enemy_array[0][2], player.online_enemy_array[0][3]))
        
        else:
            enemyArray.append(Enemy(player.online_enemy_array[0][0], player.online_enemy_array[0][1],50,0,1,melee_enemies_images, player.online_enemy_array[0][2], player.online_enemy_array[0][3]))
        
        del player.online_enemy_array[0]

    #print(player.online_enemy_array)
    
##    #This for loop is responsible for creating all the enemies
##    for i in range(num_enemies):
##        #This decides if the player is ranged or melee randomly
##        enemy_type = random.randint(1,2)
##        if enemy_type == 1:
##           enemyArray.append(Enemy((random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), 50,0,1, ranged_enemies_images, "R"))
##        elif enemy_type == 2:
##           enemyArray.append(Enemy((random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), 50,0,1, melee_enemies_images, "M"))
##      




#This procedure is to check if the bullet is in the entity's hitbox
#If it is, it will deduct the bullets health from the entitiy and remove that bullet
def checkBulletCollision(entity, bullet):
    if bullet.x_pos - bullet.radius < entity.x_pos + entity.width and bullet.x_pos + bullet.radius > entity.x_pos:
        if bullet.y_pos - bullet.radius < entity.y_pos + entity.height and bullet.y_pos + bullet.radius > entity.y_pos:
            
            entity.health -= bullet.damage          
            try:
                bulletArray.pop(bulletArray.index(bullet))
            except:
                pass

            

def checkEnemyCollision(player, enemy):
    #This creates the masks of the player and the enemy
    player_mask = pygame.mask.from_surface(player_images[player.direction][int(player.image_index)])
    enemy_mask = pygame.mask.from_surface(enemy.image_array[enemy.direction][int(enemy.image_index)])
    #An offset is needed when overlapping
    offset = ((player.x_pos - int(enemy.x_pos)),(player.y_pos - int(enemy.y_pos)))
    #If the masks overlap, it will return a mask. Otherwise it will return nothing
    if player_mask.overlap(enemy_mask,offset) and (enemy.previous_collision + 1) < time.time():
        player.hit(weapon_data[enemy.weapon][2])
        #Have a time delay so that the player doesn't die almost instantaneously
        enemy.previous_collision = time.time()
        if soundEffects == True:
            hit_sound.play()

#This is where the collectables will be stored
collectableArray = []
#The object for the collectable
class Collectable :

    def __init__(self, x_pos, y_pos, points, image):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.points = points
        self.image = image
    def drawCollectable (self,screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))

#This procedure works similar to the checkEnemyCollision procedure by creating a mask
def checkCollectableCollision(player,collectable):
    player_mask = pygame.mask.from_surface(player_images[player.direction][int(player.image_index)])
    collectable_mask = pygame.mask.from_surface(collectable.image)
    offset = ((player.x_pos - collectable.x_pos),(player.y_pos - collectable.y_pos))
    if player_mask.overlap(collectable_mask,offset):
        #The player will get the collectables points and that collectable will be removed from its array
        player.score += collectable.points
        collectableArray.pop(collectableArray.index(collectable))

def spawnCollectables():
    #Creates the random variable to spawn the enemies
    rarity_num = random.randint(0,100)
    if rarity_num == 100:#Legendary
        #Add the collectable to the collactableArray
        collectableArray.append (Collectable((random.randint(wall_limit_x1,wall_limit_x2)), (random.randint(wall_limit_y1,wall_limit_y2)),100, legendary_collectable))

    elif rarity_num >= 85 and rarity_num < 100:#Epic
        collectableArray.append (Collectable((random.randint(wall_limit_x1,wall_limit_x2)), (random.randint(wall_limit_y1,wall_limit_y2)),50, epic_collectable))

    elif rarity_num >= 50 and rarity_num < 85:#Rare
        collectableArray.append (Collectable((random.randint(wall_limit_x1,wall_limit_x2)), (random.randint(wall_limit_y1,wall_limit_y2)),20, rare_collectable))

    elif rarity_num >= 30 and rarity_num < 50:#Commmon
        collectableArray.append (Collectable((random.randint(wall_limit_x1,wall_limit_x2)), (random.randint(wall_limit_y1,wall_limit_y2)),10, common_collectable))


#These arrays show where the hitboxes are and their dimensions    
bottom_hitbox = (840, 645, 250, 50 )
top_hitbox = (840, 20, 250, 50 )
left_hitbox = (370, 240, 65, 250)
right_hitbox = (1520, 240, 65, 250)

def BottomHitbox(player, player2):
    global current_level
    #Check if the player is in the hitbox to transition to the next room
    if player.x_pos < bottom_hitbox[0] + bottom_hitbox[2] and player.x_pos + player.width > bottom_hitbox[0]:
        if player.y_pos + player.height > bottom_hitbox[1] and player.y_pos < bottom_hitbox[1] + bottom_hitbox[3]:
            #Change their room position
            player.room_y_pos +=1
            #Put the player in a relevant place in the dungeon to look like they came from that direction
            player.x_pos = 970
            player.y_pos = 70
            #Increase the level
            current_level += 1
            #Create the enemies
            if player.ID == 0:
                create_enemies (1 + current_level, player, player2)
            #spawnEnemies(player)
            
    #Display the entrance to the next dungeon room
    screen.blit(verticalDoor, (840, 675))
    

def TopHitbox(player, player2):
    global current_level
    if player.x_pos < top_hitbox[0] + top_hitbox[2] and player.x_pos + player.width > top_hitbox[0]:
        if player.y_pos + player.height > top_hitbox[1] and player.y_pos < top_hitbox[1] + top_hitbox[3]:
            player.room_y_pos -= 1
            player.x_pos = 970
            player.y_pos = 585
            current_level += 1
            if player.ID == 0:
                create_enemies (1 + current_level, player, player2)
            #spawnEnemies(player)
    

    screen.blit(verticalDoor, (840, 0))



def LeftHitbox(player, player2):
    global current_level
    if player.x_pos < left_hitbox[0] + left_hitbox[2] and player.x_pos + player.width > left_hitbox[0]:
        if player.y_pos + player.height > left_hitbox[1] and player.y_pos < left_hitbox[1] + left_hitbox[3]:       
            player.room_x_pos -= 1
            player.x_pos = 1455
            player.y_pos = 360
            current_level += 1
            if player.ID == 0:
                create_enemies (1 + current_level, player, player2)
            #spawnEnemies(player)

    screen.blit(horizontalDoor, (340, 240))



def RightHitbox(player, player2):
    global current_level
    if player.x_pos < right_hitbox[0] + right_hitbox[2] and player.x_pos + player.width > right_hitbox[0]:
        if player.y_pos + player.height > right_hitbox[1] and player.y_pos < right_hitbox[1] + right_hitbox[3]:
            player.room_x_pos +=1
            player.x_pos = 450
            player.y_pos = 360
            current_level += 1
            if player.ID == 0:
                create_enemies (1 + current_level, player, player2)
            #spawnEnemies(player)

            

    screen.blit(horizontalDoor, (1535, 240))


    
#These procedures are responsible for checking if the player is in the room hitboxes
#Each type of dungeon room corresponds with a procedure
def UpTJunction (player, player2):
    BottomHitbox(player, player2)
    LeftHitbox(player, player2)
    RightHitbox(player, player2)

def DownTJunction(player, player2):
    TopHitbox(player, player2)
    LeftHitbox(player, player2)
    RightHitbox(player, player2)
 
def LeftTJunction(player, player2): 
    TopHitbox(player, player2)
    LeftHitbox(player, player2)
    BottomHitbox(player, player2)

def RightTJunction(player, player2):
    TopHitbox(player, player2)
    RightHitbox(player, player2)
    BottomHitbox(player, player2)
    
def TopLeftCorner(player, player2):
    BottomHitbox(player, player2)
    RightHitbox(player, player2)

def TopRightCorner(player, player2): 
    BottomHitbox(player, player2)
    RightHitbox(player, player2)

def BottomRightCorner(player, player2):
    TopHitbox(player, player2)
    LeftHitbox(player, player2)
    
def VerticalCorridor (player, player2):
    TopHitbox(player, player2)
    BottomHitbox(player, player2)

def HorizontalCorridor(player, player2):
    LeftHitbox(player, player2)
    RightHitbox(player, player2)

def FourWayJunction(player, player2): 
    TopHitbox(player, player2)
    BottomHitbox(player, player2)
    LeftHitbox(player, player2)
    RightHitbox(player, player2)

def OneWayUp(player, player2):
    TopHitbox(player, player2)

def OneWayDown(player, player2):
    BottomHitbox(player, player2)

def OneWayLeft(player, player2):
    LeftHitbox(player, player2)

def OneWayRight(player, player2):
    RightHitbox(player, player2)

#This procedure checks what room the player is in and will show the appropriate exits to the dungeon
def WhatRoomIsPlayer(player, player2):

    if maps[player.map_num][player.room_y_pos][player.room_x_pos] == "UTJ":
        UpTJunction(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "DTJ":
        DownTJunction(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "RTJ":
        RightTJunction(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "LTJ":
        LeftTJunction(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "TRC":
        TopRightCorner(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "TLC":
        TopLeftCorner(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "BRC":
        BottomRightCorner(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "BLC":
        BottomLeftCorner(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "XC":
        HorizontalCorridor(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "YC":
        VerticalCorridor(player, player2)
    
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "FWJ":
        FourWayJunction(player, player2)

    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWU":
        OneWayUp(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWD":
        OneWayDown(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWL":
        OneWayLeft(player, player2)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWR":
        OneWayRight(player, player2)

#This is responsible for allowing the user to enter the shop
entrance_button = (550,100,100,50)
shop_state = False
def entrance_to_shop (player):
    global shop_state 
    font1 = pygame.font.SysFont('comicsans', 25)
    entrance_text = font1.render(("Enter Shop"),1,(0,0,0))
    #This works the same as how the quiz buttons work
    pygame.draw.rect(screen, (255,255,255), entrance_button)
    screen.blit(entrance_text, (entrance_button[0] +10, entrance_button[1]+10))
    if mouse[0] > entrance_button[0] and mouse[0] < entrance_button[0] + entrance_button[2]:
        if mouse[1] > entrance_button[1] and mouse[1] < entrance_button[1] +entrance_button[3]:
            pygame.draw.rect(screen, (255,0,0), entrance_button, 3)
            if click[0] == 1:
                shop_state = True
            
        else:
            pygame.draw.rect(screen, (0,0,0), entrance_button, 3)
    else:
        pygame.draw.rect(screen, (0,0,0), entrance_button, 3)

        
#Shop buttons
machine_gun_button = (550, 210, 170, 90)
wand_button= (850, 210, 170, 90)
upgrade_button = (1150, 210, 190, 90)
leave_button = (450,100,100,50)

def shop(player):
    global shop_state
    #This is all the text that will need to be displayed
    font1 = pygame.font.SysFont('comicsans', 30)
    machine_gun_text1 = font1.render(("Machine Gun"),1,(0,0,0))
    #You cannot do "\n" in this so I had to make individual lines
    machine_gun_text2 = font1.render(("Cost: "+ str(weapon_data[1][4])),1,(0,0,0))
    wand_text1 = font1.render(("Wand"),1,(0,0,0))
    wand_text2 = font1.render(("Cost: "+ str(weapon_data[2][4])),1,(0,0,0))
    damage_multiplier_text1 = font1.render(("5% Damage Boost"),1,(0,0,0))
    damage_multiplier_text2 = font1.render(("Cost: 150"),1,(0,0,0))
    leave_text = font1.render(("LEAVE"),1,(0,0,0))
    #Machine Gun Button
    pygame.draw.rect(screen, (255,255,255), machine_gun_button)
    screen.blit(machine_gun_text1, (machine_gun_button[0] +10, machine_gun_button[1] + 10))
    screen.blit(machine_gun_text2, (machine_gun_button[0] +10, machine_gun_button[1] + 40))
    if mouse[0] > machine_gun_button[0] and mouse[0] < machine_gun_button[0] + machine_gun_button[2]:
        if mouse[1] > machine_gun_button[1] and mouse[1] < machine_gun_button[1] + machine_gun_button[3]:
            #The outline of the box will turn red when the mouse is ontop of the box
            #This is exactly the same as how the quiz boxes work
            pygame.draw.rect(screen, (255,0,0), machine_gun_button,3)
            if click[0] == 1 and player.score >= weapon_data[1][4]:
                player.weapon = 1
                #Remove points from the player's score
                player.score -=  weapon_data[1][4]
                if soundEffects == True:
                    #Play a purchased sound effect
                    purchased_sound.play()
                
                
        else:
            pygame.draw.rect(screen, (0,0,0), machine_gun_button,3)
    else:
        pygame.draw.rect(screen, (0,0,0), machine_gun_button,3)
    
    #Wand button
    pygame.draw.rect(screen, (255,255,255), wand_button)
    screen.blit(wand_text1, (wand_button[0] + 25, wand_button[1] + 10))
    screen.blit(wand_text2, (wand_button[0] + 10, wand_button[1] + 40))
    if mouse[0] > wand_button[0] and mouse[0] < wand_button[0] + wand_button[2]:
        if mouse[1] > wand_button[1] and mouse[1] < wand_button[1] + wand_button[3]:
            pygame.draw.rect(screen, (255,0,0), wand_button,3)
            if click[0] == 1 and player.score >= weapon_data[2][4]:
                player.weapon = 2
                player.score -=  weapon_data[2][4]
                if soundEffects == True:
                    purchased_sound.play()
        else:
            pygame.draw.rect(screen, (0,0,0), wand_button,3)
    else:
        pygame.draw.rect(screen, (0,0,0), wand_button,3)

        
    #Upgrade damage multiplier
    pygame.draw.rect(screen, (255,255,255), upgrade_button)
    screen.blit(damage_multiplier_text1, (upgrade_button[0] + 10, upgrade_button[1] + 10))
    screen.blit(damage_multiplier_text2, (upgrade_button[0] + 10, upgrade_button[1] + 40))
    if mouse[0] > upgrade_button[0] and mouse[0] < upgrade_button[0] + upgrade_button[2]:
        if mouse[1] > upgrade_button[1] and mouse[1] < upgrade_button[1] + upgrade_button[3]:
            pygame.draw.rect(screen, (255,0,0), upgrade_button,3)
            if click[0] == 1 and player.score >= 150:
                player.damage_mult += 0.05
                player.score -=  150
                if soundEffects == True:
                    purchased_sound.play()
            
        else:
            pygame.draw.rect(screen, (0,0,0), upgrade_button,3)
    else:
        pygame.draw.rect(screen, (0,0,0), upgrade_button,3)
    
    #Leave Button
    pygame.draw.rect(screen, (255,255,255), leave_button)
    screen.blit(leave_text, (leave_button[0] +10, leave_button[1]+10))
    if mouse[0] > leave_button[0] and mouse[0] < leave_button[0] + leave_button[2]:
        if mouse[1] > leave_button[1] and mouse[1] < leave_button[1] + leave_button[3]:
            pygame.draw.rect(screen, (255,0,0), leave_button, 3)
            if click[0] == 1:
                shop_state = False
                
            
        else:
            pygame.draw.rect(screen, (0,0,0), leave_button, 3)
    else:
        pygame.draw.rect(screen, (0,0,0), leave_button, 3)



music_button = (20,650,100,50)
sound_effects_button = (150,650,120,50)
def settings():
    global music, soundEffects
    font3 = pygame.font.SysFont('comicsans', 23)
    music_text = font3.render(("Music: "),1,(0,0,0))
    sound_effects_text = font3.render(("Sound Effects: "),1,(0,0,0))
    on_text = font3.render(("On "),1,(0,0,0))
    off_text = font3.render(("Off "),1,(0,0,0))
    #Music button
    pygame.draw.rect(screen, (255,255,255), music_button)
    screen.blit(music_text, (music_button[0] +10, music_button[1]+10))
    if music == True:
        screen.blit(on_text, (music_button[0] +15, music_button[1]+25))
    else:
        screen.blit(off_text, (music_button[0] +15, music_button[1]+25))

        
    if mouse[0] > music_button[0] and mouse[0] < music_button[0] + music_button[2]:
        if mouse[1] > music_button[1] and mouse[1] < music_button[1] + music_button[3]:
            pygame.draw.rect(screen, (255,0,0), music_button, 3)
            if click[0] == 1:
                if music == True:
                    music = False
                    pygame.mixer.music.pause()
                else:
                    music = True
                    pygame.mixer.music.unpause()
            
        else:
            pygame.draw.rect(screen, (0,0,0), music_button, 3)
    else:
        pygame.draw.rect(screen, (0,0,0), music_button, 3)

    #Sound Effects button
    pygame.draw.rect(screen, (255,255,255), sound_effects_button)
    screen.blit(sound_effects_text, (sound_effects_button[0] +10, sound_effects_button[1]+10))

    if soundEffects == True:
        screen.blit(on_text, (sound_effects_button[0] +15, sound_effects_button[1]+25))
    else:
        screen.blit(off_text, (sound_effects_button[0] +15, sound_effects_button[1]+25))
    if mouse[0] > sound_effects_button[0] and mouse[0] < sound_effects_button[0] + sound_effects_button[2]:
        if mouse[1] > sound_effects_button[1] and mouse[1] < sound_effects_button[1] + sound_effects_button[3]:
            pygame.draw.rect(screen, (255,0,0), sound_effects_button, 3)
            if click[0] == 1:
                if soundEffects == True:
                    soundEffects = False
                else:
                    soundEffects = True
            
        else:
            pygame.draw.rect(screen, (0,0,0), sound_effects_button, 3)
    else:
        pygame.draw.rect(screen, (0,0,0), sound_effects_button, 3)


rules_button = (50, 550, 100, 50)
rule = False
def rules():
    global rule
    font3 = pygame.font.SysFont('comicsans', 23)
    rules_text = font3.render(("RULES "),1,(0,0,0))
    pygame.draw.rect(screen, (255,255,255), rules_button)
    screen.blit(rules_text, (rules_button[0] +10, rules_button[1]+10))

    if mouse[0] > rules_button[0] and mouse[0] < rules_button[0] + rules_button[2]:
        if mouse[1] > rules_button[1] and mouse[1] < rules_button[1] + rules_button[3]:
            pygame.draw.rect(screen, (255,0,0), rules_button, 3)
            if click[0] == 1:
                rule = True
            
        else:
            pygame.draw.rect(screen, (0,0,0), rules_button, 3)
    else:
        pygame.draw.rect(screen, (0,0,0), rules_button, 3)

    
    if rule == True:
        leave_text = font3.render(("LEAVE"),1,(0,0,0))
        pygame.draw.rect(screen, (255,255,255), leave_button)
        screen.blit(leave_text, (leave_button[0] +10, leave_button[1]+10))
        #Draw rules image
        screen.blit (rules_image, (600,100))
        
        if mouse[0] > leave_button[0] and mouse[0] < leave_button[0] + leave_button[2]:
            if mouse[1] > leave_button[1] and mouse[1] < leave_button[1] + leave_button[3]:
                pygame.draw.rect(screen, (255,0,0), leave_button, 3)
                if click[0] == 1:
                    rule = False
                    
                
            else:
                pygame.draw.rect(screen, (0,0,0), leave_button, 3)
        else:
            pygame.draw.rect(screen, (0,0,0), leave_button, 3)

player_data = ["Myusername","password","F", "0" ]#This will be predefined when the user logs in
def end_game(player):
    #The highscore will only be updated if the player's score is greater than their previous highscore (stored in the array above)
    if player.score > int(player_data[3]): 
        line_to_change = str(player_data[0] + "|" + player_data[1] + "|" + player_data[2] + "|" + str(player.score) + "\n")
        file = open ("Student_Credentials.txt","r")
        #Find the line number where the user is stored
        for num , line in  enumerate (file):
            if player_data[0] in line:
                line_number = num
                break
        file.close()
        
        #The file has to be reopened to change the line
        #It also prevents all the other records from being deleted
        file = open ("Student_Credentials.txt","r")
        #Retrieve all the lines from the file
        lines = file.readlines()
        #Edit the line with the highscore
        lines[line_number] = line_to_change
        file.close()
        
        #Write to the text file will all the lines (including the editted one)`
        file = open ("Student_Credentials.txt","w")
        file.writelines(lines)
        file.close()

        




#This procedure is responsible for drawing everything on the screen
def redraw_game_window(player1,player2):
    screen.fill([255,255,255])
    screen.blit(dungeonBackground, (340,0))#Responsible for drawing the background
    if level_complete == True and player1.ID == 0:
        #This procedure needs to be in the "redraw...()" as the game is drawing the doors to the next dungeons
        WhatRoomIsPlayer(player1, player2)
    drawMiniMap(player1.map_num)#This draws a player on the minimap
    pygame.draw.rect(screen, (255, 0, 0), [((player1.room_x_pos*42)+13),((player1.room_y_pos*24)+8),15, 12])#Draw player1 on minimap
    #Draw the player's score
    font2 = pygame.font.SysFont('comicsans', 50)
    player1_score_text = font2.render(("Player 1 Score: " + str(player1.score)),1,(0,0,0))
    player2_score_text = font2.render(("Player 2 Score: " + str(player2.score)),1,(0,0,0))
    

    

    p1_health_text1 = font2.render(("Player 1 Health: " + str(player1.health)),1,(0,255,0))
    p1_health_text2 = font2.render(("Player 1 Health: " + str(player1.health)),1,(255,170,0))
    p1_health_text3 = font2.render(("Player 1 Health: " + str(player1.health)),1,(255,0,0))

    p2_health_text1 = font2.render(("Player 2 Health: " + str(player2.health)),1,(0,255,0))
    p2_health_text2 = font2.render(("Player 2 Health: " + str(player2.health)),1,(255,170,0))
    p2_health_text3 = font2.render(("Player 2 Health: " + str(player2.health)),1,(255,0,0))

    small_font = pygame.font.SysFont('comicsans', 20)
    you_text = small_font.render(("You"),1, (0,0,0))


    if player1.ID == 0:
        screen.blit(player1_score_text, (25, 225))
        screen.blit(you_text, (100, 275))
        
        if player1.health >= 40:
            screen.blit(p1_health_text1, (25, 300))
        elif player1.health >= 20 and player1.health < 40:
            screen.blit(p1_health_text2, (25, 300))
        else:
            screen.blit(p1_health_text3, (25, 300))


        screen.blit(player2_score_text, (25, 375))

        if player2.health >= 40:
            screen.blit(p2_health_text1, (25, 450))
        elif player2.health >= 20 and player2.health < 40:
            screen.blit(p2_health_text2, (25, 450))
        else:
            screen.blit(p2_health_text3, (25, 450))

    else:
        screen.blit(player2_score_text, (25, 225))
        
        
        if player2.health >= 40:
            screen.blit(p2_health_text1, (25, 300))
        elif player2.health >= 20 and player2.health < 40:
            screen.blit(p2_health_text2, (25, 300))
        else:
            screen.blit(p2_health_text3, (25, 300))


        screen.blit(player1_score_text, (25, 375))
        screen.blit(you_text, (100, 425))

        if player1.health >= 40:
            screen.blit(p1_health_text1, (25, 450))
        elif player1.health >= 20 and player1.health < 40:
            screen.blit(p1_health_text2, (25, 450))
        else:
            screen.blit(p1_health_text3, (25, 450))
        

    #Draw Collectables
    if len(collectableArray) >0 :
        collectableArray[0].drawCollectable(screen)
    #Draw Bullets        
    for bullet in bulletArray:
        bullet.drawProjectile(screen)
    #Draw enemies
    for enemy in enemyArray:
        enemy.draw(screen)

    #This section is responsible for the shop
    #If a level is complete, they will have the oportunity to go to the shop
    if level_complete == True:
        entrance_to_shop(player1)
    if shop_state == True:
        shop(player1)

    settings()
    rules()

    font4 = pygame.font.SysFont('comicsans', 70)
    game_over_text1 = font4.render(("GAME OVER!"),1,(255,0,0))
    game_over_text2 = font4.render(("GAME OVER!"),1,(255,170,0))
    game_over_text3 = font4.render(("GAME OVER!"),1,(255,255,0))
    high_score_text1 = font4.render(("NEW HIGH SCORE"),1,(255,0,0))
    high_score_text2 = font4.render(("NEW HIGH SCORE"),1,(255,170,0))
    high_score_text3 = font4.render(("NEW HIGH SCORE"),1,(255,255,0))

    if player1.health <= 0:
        for i in range (0,3):
           screen.blit(game_over_text1, (750, 225))
           pygame.display.update()
           time.sleep(0.5)
           screen.blit(game_over_text2, (750, 225))
           pygame.display.update()
           time.sleep(0.5)
           screen.blit(game_over_text3, (750, 225))
           pygame.display.update()
           time.sleep(0.5)
           
           
        if player1.score > int(player_data[3]):
           for i in range (0,5):
               screen.blit(high_score_text1, (750, 350))
               pygame.display.update()
               time.sleep(0.5)
               screen.blit(high_score_text2, (750, 350))
               pygame.display.update()
               time.sleep(0.5)
               screen.blit(high_score_text3, (750, 350))
               pygame.display.update()
               time.sleep(0.5)

        
    
    #player1.draw(screen)#Draw players
    screen.blit(player_images[player1.direction][int(player1.image_index)], (player1.x_pos, player1.y_pos))
    screen.blit(player_images[player2.direction][int(player2.image_index)], (player2.x_pos, player2.y_pos))
    #player2.draw(screen)
    pygame.display.update()







def main_game_loop():
    global level_complete,game_loop, current_level, music, soundEffects, click, mouse
    #http://pygametutorials.wikidot.com/book-time
    #Set some variables at the start of the loop
    game_loop = True
    level_complete = False
    current_level = 0
    music = True
    soundEffects = True
    #Spawn the collectables
    spawnCollectables()
    #The clock is to limit how many cycles occur each second (similar to the refresh rate)
    #The data being sent needs a limit as there will be a physical delay
    clock = pygame.time.Clock()

    #Connecting to the netowrk and retrieving the player code
    player1 = connect_client()
    
    print(player1.ID)

    
    while game_loop == True:
        clock.tick(60)
        #If the player clicks the "X" button on the window, the program will close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        player2 = send(player1)

        while len(player2.online_bullet_array) > 0:
            bulletArray.append(Projectile(int(player2.online_bullet_array[0][0]), int( player2.online_bullet_array[0][1]),int( player2.online_bullet_array[0][2]), int(player2.online_bullet_array[0][3]), weapon_data[player2.weapon][2],(weapon_data[player2.weapon][1] * player2.damage_mult), (0,0,0), 5))  
            player2.delete_item(0)

        if player1.ID == 0 :
            spawnEnemies(player1)
        else:
            spawnEnemies(player2)
            
        player1.online_bullet_array = []

        if player1.ID != 0:
            if player1.room_x_pos != player 2.room_x_pos or player1.room_y_pos != player 2.room_y_pos:
                player1.room_x_pos = player 2.room_x_pos
                player1.room_y_pos = player 2.room_y_pos
                player1.x_pos = player2.x_pos
                player1.y_pos = player2.y_pos
        
        #Loop through each of the bullets
        for bullet in bulletArray:
            #The bullet can only move if it is within the wall boundaries
            if bullet.x_pos < wall_limit_x2 and bullet.x_pos > wall_limit_x1 and bullet.y_pos < wall_limit_y2 and bullet.y_pos > wall_limit_y1:
                bullet.moveProjectile()
            else:
                #When hitting the wall, the bullets will be removed
                bulletArray.pop(bulletArray.index(bullet))


            #Check the collision of the bullet with player and enemies
            checkBulletCollision(player1, bullet)
            for enemy in enemyArray:
                checkBulletCollision(enemy, bullet)


        #Loop through each of the enemies      
        for enemy in enemyArray:
            #When an enemy is defeated, the player will gain points and that particular enemy will be removed from the array
            if enemy.health <= 0:
                player1.score += 50
                enemyArray.pop(enemyArray.index(enemy))
                if soundEffects == True:
                    #Play the sound for an enemy dying
                    death_sound.play()
            #Check the collision between each enemy and the player   
            checkEnemyCollision(player1, enemy)

            #Depending on the type of enemy, they will perform a certain action
            if enemy.enemy_type == "R":
                if enemy.target == 0 and player1.ID == 0:
                    enemy.attack(player1)

                elif enemy.target == 0 and player1.ID == 1:
                    enemy.attack(player2)
                    
                elif enemy.target == 1 and player1.ID == 0:
                    enemy.attack(player2)
                    
                elif enemy.target == 1 and player1.ID == 1:
                    enemy.attack(player1)   


            else:

                if enemy.target == 0 and player1.ID == 0:
                    enemy.moveEnemy(player1)

                elif enemy.target == 0 and player1.ID == 1:
                    enemy.moveEnemy(player2)
                    
                elif enemy.target == 1 and player1.ID == 0:
                    enemy.moveEnemy(player2)
                    
                elif enemy.target == 1 and player1.ID == 1:
                    enemy.moveEnemy(player1)  

                

        #This checks if all the enemies are dead which will say if the dungeon room is completed
        if len(enemyArray) == 0:
            level_complete = True
            
            
        else:
            level_complete = False


        #The program can only check for a collectable collision if there is one created
        if len(collectableArray) >0 :
            checkCollectableCollision(player1,collectableArray[0])


        #Checks if the game is over
        if player1.health <= 0 or player2.health <= 0:
            music = False
            if soundEffects == True:
                fail_sound_effect.play()
            time.sleep(3)
            end_game(player1)
            game_loop = False

        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        player1.movePlayer()
        player1.shoot(mouse,click, soundEffects)
        
        redraw_game_window(player1,player2)



    
login_menu()
window.mainloop()




pygame.quit()


