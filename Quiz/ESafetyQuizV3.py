import pygame
import random
import time

pygame.init()
screenwidth = 1600
screenheight = 720
screen = pygame.display.set_mode((screenwidth,screenheight))

QuizBackground = pygame.image.load("MatrixPhoto.jpg")

question_num = 0
score_gained = 0
health_gained = 0
damage_multiplier = 1



answer1_hitbox = [120, 180, 1360, 90]
answer2_hitbox = [120, 350, 1360, 90]
answer3_hitbox = [120, 520, 1360, 90]
mouse_in_hitbox1 = False
mouse_in_hitbox2 = False
mouse_in_hitbox3 = False
def quiz():
    global mouse_in_hitbox1, mouse_in_hitbox2, mouse_in_hitbox3, question_num, score_gained, health_gained, damage_multiplier
    #The program will retrieve the questions from the text file and choose what questions will be chosen
    retrieve_questions()
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
                    if questions[(questions_to_be_selected[question_num])][1] == questions[(questions_to_be_selected[question_num])][4]:
                        #If the user's answer is correct, it will give a reward depending on its difficulty
                        #After each question, it will check if the quiz has been completed (the number of questions being greater than 5)
                        if questions[question_num][5] == "E":
                            score_gained += 50
                            if question_num < 4:
                                question_num += 1
                            #If the quiz has been completed, it will stop the while loop and start the game
                            else:
                                quiz_loop = False
                                game()
                        elif questions[question_num][5] == "M":
                            health_gained += 25
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()
                        else:
                            damage_multiplier += 0.25
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()

                        #Plays the correct sound effect when correct
                        pygame.mixer.music.load("Correct Sound Effect.wav")
                        pygame.mixer.music.play(0)
                    else:
                        #Plays the incorrect sound effect when incorrect
                        pygame.mixer.music.load("Fail Sound Effect.mp3")
                        pygame.mixer.music.play(0)
                        if question_num < 4:
                            question_num += 1

                        else:
                            quiz_loop = False
                            game()
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
                    if questions[(questions_to_be_selected[question_num])][2] == questions[(questions_to_be_selected[question_num])][4]:
                        if questions[question_num][5] == "E":
                            score_gained += 50
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()
                        elif questions[question_num][5] == "M":
                            health_gained += 25
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()
                        else:
                            damage_multiplier += 0.25
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()

                        pygame.mixer.music.load("Correct Sound Effect.wav")
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load("Fail Sound Effect.mp3")
                        pygame.mixer.music.play(0)
                        if question_num < 5:
                            question_num += 1

                        else:
                            quiz_loop = False
                            game()
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
                    if questions[(questions_to_be_selected[question_num])][3] == questions[(questions_to_be_selected[question_num])][4]:
                        if questions[question_num][5] == "E":
                            score_gained += 50
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()
                        elif questions[question_num][5] == "M":
                            health_gained += 25
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()
                        else:
                            damage_multiplier += 0.25
                            if question_num < 4:
                                question_num += 1
                            else:
                                quiz_loop = False
                                game()
                        pygame.mixer.music.load("Correct Sound Effect.wav")
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load("Fail Sound Effect.mp3")
                        pygame.mixer.music.play(0)
                        if question_num < 4:
                            question_num += 1

                        else:
                            quiz_loop = False
                            game()
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
    if (questions[(questions_to_be_selected[question_num])][4]) == "E":
        reward_text = font2.render("50 Points", 1, (0,0,0))
        difficulty_text = font2.render("Easy", 1, (0,0,0))

    elif (questions[(questions_to_be_selected[question_num])][4]) == "M":
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
    answer_text1 = font1.render((questions[(questions_to_be_selected[question_num])][1]), 1, (0,0,0))
    answer_text2 = font1.render((questions[(questions_to_be_selected[question_num])][2]), 1, (0,0,0))
    answer_text3 = font1.render((questions[(questions_to_be_selected[question_num])][3]), 1, (0,0,0))

    screen.blit(answer_text1, (answer1_hitbox[0]+15, (answer1_hitbox[1] + (answer1_hitbox[3]/2))))
    screen.blit(answer_text2, (answer2_hitbox[0]+15, (answer2_hitbox[1] + (answer2_hitbox[3]/2))))
    screen.blit(answer_text3, (answer3_hitbox[0]+15, (answer3_hitbox[1] + (answer3_hitbox[3]/2))))
    
    pygame.display.update()

def game():
    pass

quiz()
pygame.quit()
