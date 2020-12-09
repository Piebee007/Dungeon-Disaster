import pygame
import random
import time
from math import sqrt

#The array for the weapon data
weapon_data = [[0.5, 5, 3, 20, 0], [0.05, 2, 6, 100, 500], [3, 50, 2, 5, 1500]]

wall_limit_x1 =405
wall_limit_x2 = 1520
wall_limit_y1 = 50
wall_limit_y2 = 665

bulletArray = []



#This is the parent class that the player and enemy will inherit
class ParentObject (object):

    def __init__(self, x_pos, y_pos,health,weapon,damage_mult, image_array):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 50
        self.height = 50
        self.health = health
        self.weapon = weapon
        self.speed = 3
        self.damage_mult = damage_mult
        #This has been changed from the previous method.
        #It makes other algorithms more efficient and simplifies implementation
        #0 = Right
        #1 = Left
        #2 = Up
        #3 = Down
        self.direction = 0
        self.image_array = image_array
        self.image_index = 0
        self.hitbox = ((self.x_pos - 3), (self.y_pos - 3), self.width, self.height)

    #This method is responsible for drawing the particular images  of either the player or the object
    def draw(self, screen):
        screen.blit(self.image_array[self.direction][int(self.image_index)], (self.x_pos, self.y_pos))

    def hit(self, damage):
        self.health -= damage
        

#The player object inherits the ParentObject class
class Player (ParentObject):

    def __init__(self, x_pos, y_pos,health,weapon,damage_mult,map_num, image_array):
        self.score = 0
        self.bullet_array = []
        
        self.map_num = map_num
        self.room_x_pos = 0
        self.room_y_pos = 0
        #This is the start time of the game. It is responsible for the delay when shooting
        self.previous_click = time.time()

        #Super means that the player inherits the parent class' attributes and methods
        super().__init__(x_pos, y_pos,health,weapon,damage_mult, image_array)
        self.ammo = weapon_data[self.weapon][3]
        self.image_array = ""
        
    #This method is responsible for the user controlling the player
    def movePlayer(self):
        
        #This method allows the user to move
        keys = pygame.key.get_pressed()
        
        if self.x_pos > wall_limit_x1:
            if keys[pygame.K_a]:
                self.x_pos -= self.speed
                self.image_index += 0.25
                self.direction = 1
        #This had to be changed so that the player's character was in the wall or stopping before the wall
        if self.x_pos + self.width//2 < wall_limit_x2:
            if keys[pygame.K_d]:
                self.x_pos += self.speed
                self.image_index += 0.25
                self.direction = 0
                
        if self.y_pos > wall_limit_y1:
            if keys[pygame.K_w]:
                self.y_pos -= self.speed
                self.image_index += 0.25
                self.direction = 2

                
        if self.y_pos + self.height < wall_limit_y2:
            if keys[pygame.K_s]:
                self.y_pos += self.speed
                self.image_index += 0.25
                self.direction =3
        #This is responsible for the animation of the player    
        if self.image_index >=3:
            self.image_index = 0
        #Reload the player's weapon
        if keys[pygame.K_r]:
            self.ammo = weapon_data[self.weapon][3]

    def shoot(self):
        #These need to be global for the shop and change settings
        global mouse, click
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        #When the player clicks, they have ammo and they haven't shot before the fire rate delay has finished
        if click[0] == 1 and self.ammo > 0 and (self.previous_click + weapon_data[self.weapon][0]) < time.time():
            
            #These if statements are responsible for creating the bullets outside of the player's hitbox
            if mouse[0] > self.x_pos - 20 and mouse[0] < self.x_pos + self.width + 10 and mouse[1] < self.y_pos +20:#Up
                self.direction = 2
                bulletArray.append(Projectile(round(self.x_pos + self.width // 2), (round(self.y_pos + self.height//2)-35), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
            elif mouse[0] > self.x_pos - 20 and mouse[0] < self.x_pos + self.width + 10 and mouse[1] > self.y_pos -20: #Down
                bulletArray.append(Projectile(round(self.x_pos + self.width // 2), (round(self.y_pos + self.height//2)+35), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
                self.direction = 3
            elif self.x_pos < mouse[0]:#Left
                self.direction = 0
                bulletArray.append(Projectile((round(self.x_pos + self.width // 2)+35), round(self.y_pos + self.height//2), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
            elif self.x_pos > mouse[0]:#Righta
                self.direction = 1
                bulletArray.append(Projectile((round(self.x_pos + self.width // 2)-35), round(self.y_pos + self.height//2), mouse[0], mouse[1], weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
            #Remove ammo after shooting
            self.ammo -= 1
            #This timer is to create a fire rate for the player shooting 
            self.previous_click = time.time()

            
            if soundEffects == True:
                #Create the sound effect of shooting
                if self.weapon == 0:
                    gunShot.play()
                    
                elif self.weapon == 1:
                    machineGun.play()
                else:
                    wand.play()



class Enemy(ParentObject):

    def __init__(self,x_pos, y_pos,health,weapon,damage_mult,image_array,enemy_type):
        self.enemy_type = enemy_type
        #This is the start time of the game. It is responsible for the delay when shooting
        self.previous_attack = time.time()
        #This is to prevent an error when a bullet is in two enemy hitboxes
        self.previous_collision = time.time()
        #Inherit the methods and attributes from the parent object
        super().__init__(x_pos, y_pos,health,weapon,damage_mult, image_array)

    def moveEnemy(self, target):
        #This works very similar to how the projectile works (see below)
        if self.previous_collision + 1 < time.time():
            self.change_x = target.x_pos - self.x_pos
            self.change_y = target.y_pos - self.y_pos
            self.distance = sqrt(((self.change_x)**2 + (self.change_y)**2))
            self.x_vel = self.speed * (self.change_x/self.distance)
            self.y_vel = self.speed * (self.change_y/self.distance)

            self.x_pos += self.x_vel
            self.y_pos += self.y_vel
            self.image_index += 0.25 #This is responsible for the animations for the enemy

            if self.image_index >=len(self.image_array[0]):
                self.image_index = 0
            #Depending on the velocities of the enemy, it will change direction of the enemy
            if (self.change_x/self.distance) > 0.5 and (self.change_y/self.distance) < 0.5 and (self.change_y/self.distance) > -0.5:
                self.direction = 0
            elif (self.change_x/self.distance) < -0.5 and (self.change_y/self.distance) < 0.5 and (self.change_y/self.distance) > -0.5:
                self.direction = 1

            elif (self.change_y/self.distance) > 0.5 and (self.change_x/self.distance) < 0.5 and (self.change_x/self.distance) > -0.5:
                self.direction = 3
            elif (self.change_y/self.distance) < -0.5 and (self.change_x/self.distance) < 0.5 and (self.change_x/self.distance) > -0.5:
                self.direction = 2
            

            #print((self.change_x/self.distance), (self.change_y/self.distance), self.direction)
            
    def attack(self, target):
        #Depending on the player's position, the enemy will create a projectile in a particular position
        #It will also change the direction of the enemy
        if (self.previous_attack + weapon_data[self.weapon][0]) < time.time():
            #These if statements are responsible for creating the bullets outside of the enemy's hitbox
            if target.x_pos > self.x_pos - 20 and target.x_pos < self.x_pos + self.width + 10 and target.y_pos < self.y_pos +20:#Up
                self.direction = 2
                bulletArray.append(Projectile(round(self.x_pos + self.width // 2), (round(self.y_pos + self.height//2)-35), target.x_pos, target.y_pos, weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
            elif target.x_pos > self.x_pos - 20 and target.x_pos < self.x_pos + self.width + 10 and target.y_pos > self.y_pos -20: #Down
                self.direction = 3
                bulletArray.append(Projectile(round(self.x_pos + self.width // 2), (round(self.y_pos + self.height//2)+35), target.x_pos, target.y_pos, weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
    
            elif self.x_pos < target.x_pos:#Right
                self.direction = 1
                bulletArray.append(Projectile((round(self.x_pos + self.width // 2)+35), round(self.y_pos + self.height//2), target.x_pos, target.y_pos, weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
            elif self.x_pos > target.x_pos:#Left
                self.direction = 0
                bulletArray.append(Projectile((round(self.x_pos + self.width // 2)-35), round(self.y_pos + self.height//2), target.x_pos, target.y_pos, weapon_data[self.weapon][2], (weapon_data[self.weapon][1] * self.damage_mult), (0,0,0), 5))
            
            
            self.previous_attack = time.time()
