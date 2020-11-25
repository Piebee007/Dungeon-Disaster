import pygame
import time
import random
from math import sqrt


pygame.init()

screenwidth = 1600
screenheight = 720

#These are the limits for the in-game wall so that players, enemies or bullets can go outside of the walls.
wall_limit_x1 =530
wall_limit_x2 =1370
wall_limit_y1 =0
wall_limit_y2 = 560

screen = pygame.display.set_mode((screenwidth,screenheight))



#Here is where all the images will be loaded
enemy_images = [[(pygame.image.load('Goblin1.png')),  (pygame.image.load('Goblin2.png')),  (pygame.image.load('Goblin3.png'))],[]]

weapon_data = [[0.05, 5, 1, 20, 0], [0.05, 2, 6, 100, 500], [3, 50, 2, 5, 1500]]

#This is the parent class that the player and enemy will inherit
class ParentObject (object):

    def __init__(self, x_pos, y_pos,health,weapon,damage_mult, image_array):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 50
        self.height = 50
        self.health = health
        self.weapon = weapon
        self.speed = 1
        self.damage_mult = damage_mult
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        self.image_array = image_array
        self.image_index = 0
        self.hitbox = (self.x_pos - 3, self.y_pos - 3, self.width, self.height)

    #This method is responsible for drawing the particular images  of either the player or the object
    def draw(self, screen):
        if self.up == True:
            screen.blit(self.image_array[0][int(self.image_index)], (self.x_pos, self.y_pos))
        elif self.down == True:
            screen.blit(self.image_array[0][int(self.image_index)], (self.x_pos, self.y_pos))
        elif self.left == True:
            screen.blit(self.image_array[0][int(self.image_index)], (self.x_pos, self.y_pos))
        else:
            screen.blit(self.image_array[0][int(self.image_index)], (self.x_pos, self.y_pos))

    
    def hit(self, damage):
        self.health - damage


#The player object inherits the ParentObject class
class Player (ParentObject):

    def __init__(self, x_pos, y_pos,health,weapon,damage_mult, image_array):
        self.score = 0  
        self.room_x_pos = 0
        self.room_y_pos = 0
        #This is the start time of the game. It is responsible for the delay when shooting
        self.previous_click = time.time()

        #Super means that the player inherits the parent class' attributes and methods
        super().__init__(x_pos, y_pos,health,weapon,damage_mult, image_array)
        
        self.ammo = weapon_data[self.weapon][3]
        
    #This method is responsible for the user controlling the player
    def movePlayer(self):
        
        keys = pygame.key.get_pressed()
        
        if self.x_pos > wall_limit_x1:
            if keys[pygame.K_a]:
                self.x_pos -= self.speed
                self.image_index += 0.25
                self.up = False
                self.down = False
                self.left = True
                self.right = False
        
        if self.x_pos < wall_limit_x2:
            if keys[pygame.K_d]:
                self.x_pos += self.speed
                self.image_index += 0.25
                self.up = False
                self.down = False
                self.left = False
                self.right = True
                
        if self.y_pos > wall_limit_y1:
            if keys[pygame.K_w]:
                self.y_pos -= self.speed
                self.image_index += 0.25
                self.up = True
                self.down = False
                self.left = False
                self.right = False

                
        if self.y_pos < wall_limit_y2:
            if keys[pygame.K_s]:
                self.y_pos += self.speed
                self.image_index += 0.25
                self.up = False
                self.down = True
                self.left = False
                self.right = False

        if keys[pygame.K_r]:
            self.ammo = weapon_data[self.weapon][3]
            
        if self.image_index >=len(self.image_array[0]):
            self.image_index = 0
            

    def shoot(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        if click[0] == 1 and self.ammo > 0 and (self.previous_click + weapon_data[self.weapon][0]) < time.time():
            #These if statements are responsible for creating the bullets outside of the player's hitbox
            if mouse[0] > self.x_pos - 60 and mouse[0] < self.x_pos + self.width + 50 and mouse[1] < self.y_pos:#Down
                bulletArray.append(Projectile(round(self.x_pos + self.width // 2), (round(self.y_pos + self.height//2)-35), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))

            elif mouse[0] > self.x_pos - 60 and mouse[0] < self.x_pos + self.width + 50 and mouse[1] > self.y_pos: #Up
                bulletArray.append(Projectile(round(self.x_pos + self.width // 2), (round(self.y_pos + self.height//2)+35), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
    

            elif self.x_pos < mouse[0]:#Right
                bulletArray.append(Projectile((round(self.x_pos + self.width // 2)+35), round(self.y_pos + self.height//2), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))

            elif self.x_pos > mouse[0]:#Left
                bulletArray.append(Projectile((round(self.x_pos + self.width // 2)-35), round(self.y_pos + self.height//2), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
                
            self.previous_click = time.time()



class Enemy(ParentObject):

    def __init__(self,x_pos, y_pos,health,weapon,damage_mult,image_array,enemy_type):
        self.enemy_type = enemy_type
        
        super().__init__(x_pos, y_pos,health,weapon,damage_mult, image_array)

    def moveEnemy(self):
        pass

    def attack(self):
        pass


enemyArray = []
def spawnEnemies(num_enemies):
    enemy_type = random.randint(1,2)
    if enemy_type == 1:
       enemyArray.append(Enemy((random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), 50,1,0, enemy_images, "R"))
    elif enemy_type == 2:
       enemyArray.append(Enemy((random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), 50,1,0, enemy_images, "M"))
  

bulletArray = []
class Projectile:

    def __init__(self, x_pos, y_pos, end_x_pos, end_y_pos, speed, damage, colour, radius):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.end_x_pos = end_x_pos
        self.end_y_pos = end_y_pos
        self.speed = speed
        self.damage = damage
        self.colour = colour
        self.radius = radius

        self.change_x = self.end_x_pos - x_pos
        self.change_y = self.end_y_pos - y_pos

        self.distance = sqrt(((self.change_x)**2 + (self.change_y)**2))
        self.x_vel = self.speed * (self.change_x/self.distance)
        self.y_vel = self.speed * (self.change_y/self.distance)

    def moveProjectile(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    def drawProjectile(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x_pos), int(self.y_pos)), self.radius)


def checkBulletCollision(entity, bullet):
    if bullet.x_pos - bullet.radius < entity.hitbox[0] + entity.hitbox[2] and bullet.x_pos + bullet.radius > entity.hitbox[0]:
        if bullet.y_pos - bullet.radius < entity.hitbox[1] + entity.hitbox[3] and bullet.y_pos + bullet.radius > entity.hitbox[1]:
            entity.hit(bullet.damage)
            bulletArray.pop(bulletArray.index(bullet))
            

def checkEnemyCollision(player, enemy):
    if enemy.hitbox[0] - enemy.hitbox[2] < player.hitbox[0] + player.hitbox[2] and enemy.hitbox[0] + enemy.hitbox[2] > player.hitbox[0]:
        if enemy.hitbox[1] - enemy.hitbox[3] < player.hitbox[1] + player.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > player.hitbox[1]:
            player.hit()
            if player.health <=0:
                end_game()
            

bottom_hitbox = ()
top_hitbox = ()
left_hitbox = ()
right_hitbox = ()

def BottomHitbox(player):
    if player.hitbox[0] < bottom_hitbox[0] + bottom_hitbox[2] and player.hitbox[0] + player.hitbox[2] > bottom_hitbox[0]:
        if player.hitbox[1] + player.hitbox[3] > bottom_hitbox[1] and player.hitbox[1] < bottom_hitbox[1] + bottom_hitbox[3]:
            player.room_y_pos +=1
            #Not sure where player will spawn yet
            player.x_pos = 125
            player.y_pos = 450
            #Add additional checking to ensure that the player doesn't go to an empty room
            #if grid[player1.player_y_pos][player1.player_x_pos] == "E":
                #player1.player_y_pos -= 1

def TopHitbox(player):
    if player.hitbox[0] < top_hitbox[0] + top_hitbox[2] and player.hitbox[0] + player.hitbox[2] > top_hitbox[0]:
        if player.hitbox[1] + player.hitbox[3] > top_hitbox[1] and player.hitbox[1] < top_hitbox[1] + top_hitbox[3]:
            player.room_y_pos -=1
            #Not sure where player will spawn yet
            player.x_pos = 125
            player.y_pos = 450
def LeftHitbox(player):
    if player.hitbox[0] < left_hitbox[0] + left_hitbox[2] and player.hitbox[0] + player.hitbox[2] > left_hitbox[0]:
        if player.hitbox[1] + player.hitbox[3] > left_hitbox[1] and player.hitbox[1] < left_hitbox[1] + left_hitbox[3]:
            player.room_x_pos -=1
            #Not sure where player will spawn yet
            player.x_pos = 125
            player.y_pos = 450
def RightHitbox(player):
    if player.hitbox[0] < right_hitbox[0] + right_hitbox[2] and player.hitbox[0] + player.hitbox[2] > right_hitbox[0]:
        if player.hitbox[1] + player.hitbox[3] > right_hitbox[1] and player.hitbox[1] < right_hitbox[1] + right_hitbox[3]:
            player.room_x_pos +=1
            #Not sure where player will spawn yet
            player.x_pos = 125
            player.y_pos = 450

#These procedures are responsible for checking if the player is in the room hitboxes
#Each type of dungeon room corresponds with a procedure
def UpTJunction (player):
    BottomHitbox(player)
    LeftHitbox(player)
    RightHitbox(player)

def DownTJunction(player):
    TopHitbox(player)
    LeftHitbox(player)
    RightHitbox(player)
 
def LeftTJunction(player): 
    TopHitbox(player)
    LeftHitbox(player)
    BottomHitbox(player)

def RightTJunction(player):
    TopHitbox(player)
    RightHitbox(player)
    BottomHitbox(player)
    
def TopLeftCorner(player):
    BottomHitbox(player)
    RightHitbox(player)

def TopRightCorner(player): 
    BottomHitbox(player)
    RightHitbox(player)

def BottomRightCorner(player):
    TopHitbox(player)
    LeftHitbox(player)
    
def VerticalCorridor (player):
    TopHitbox(player)
    BottomHitbox(player)

def HorizontalCorridor(player):
    LeftHitbox(player)
    RightHitbox(player)

def FourWayJunction(player): 
    TopHitbox(player)
    BottomHitbox(player)
    LeftHitbox(player)
    RightHitbox(player)

def OneWayUp(player):
    TopHitbox(player)

def OneWayDown(player):
    BottomHitbox(player)

def OneWayLeft(player):
    LeftHitbox(player)

def OneWayRight(player):
    RightHitbox(player)
    
    
player1 = Player(540, 50, 50,0,1, enemy_images)

def redraw_game_window():
    screen.fill([255,255,255])
    player1.draw(screen)
    for bullet in bulletArray:
        bullet.drawProjectile(screen)
    pygame.display.update()

def end_game():
    pass


def main_game_loop():
    game_loop = True
    while game_loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        for bullet in bulletArray:
            if bullet.x_pos < wall_limit_x2 and bullet.x_pos > wall_limit_x1 and bullet.y_pos < wall_limit_y2 and bullet.y_pos > wall_limit_y1:
                bullet.moveProjectile()

            else:
                bulletArray.pop(bulletArray.index(bullet))

            checkBulletCollision(player1, bullet)
            
        
        spawnEnemies(5)
        player1.movePlayer()
        player1.shoot()
        redraw_game_window()

main_game_loop()
