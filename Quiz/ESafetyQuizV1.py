import pygame
import random

pygame.init()
screenwidth = 1600
screenheight = 720
screen = pygame.display.set_mode((screenwidth,screenheight))

QuizBackground = pygame.image.load("MatrixPhoto.jpg")


question_num = 0
score_gained = 0
health_gained = 0
damage_multiplier = 0

answer1_hitbox = [120, 180, 200, 90]
answer2_hitbox = [120, 350, 200, 90]
answer3_hitbox = [120, 520, 200, 90]
mouse_in_hitbox1 = False
mouse_in_hitbox2 = False
mouse_in_hitbox3 = False
def quiz():
    global mouse_in_hitbox1, mouse_in_hitbox2, mouse_in_hitbox3
    retrieve_questions()
    quiz_loop = True
    while quiz_loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quiz_loop = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > answer1_hitbox[0] and mouse[0] < answer1_hitbox[0] + answer1_hitbox[2]:
            if mouse[1]> answer1_hitbox[1] and mouse[1] < answer1_hitbox[1] + answer1_hitbox[3]:
                mouse_in_hitbox1 = True
        else:
            mouse_in_hitbox1 = False

        if mouse[0] > answer2_hitbox[0] and mouse[0] < answer2_hitbox[0] + answer2_hitbox[2]:
            if mouse[1]> answer2_hitbox[1] and mouse[1] < answer2_hitbox[1] + answer2_hitbox[3]:
                mouse_in_hitbox2 = True
        else:
            mouse_in_hitbox2 = False

        if mouse[0] > answer3_hitbox[0] and mouse[0] < answer3_hitbox[0] + answer3_hitbox[2]:
            if mouse[1]> answer3_hitbox[1] and mouse[1] < answer3_hitbox[1] + answer3_hitbox[3]:
                mouse_in_hitbox3 = True
        else:
            mouse_in_hitbox3 = False
        
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
    
    
def redraw_quiz_window():
    #Display the picture on the background
    screen.blit(QuizBackground,(0,0))
    #Display the question box and the text
    font1 = pygame.font.SysFont('comicsans', 30)
    text1 = font1.render((questions[(questions_to_be_selected[question_num])][0]), 1, (0,0,0))
    screen.blit(text1, (20, 20))
    #Display the difficulty box and reward box

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
    pygame.display.update()

quiz()
pygame.quit()
