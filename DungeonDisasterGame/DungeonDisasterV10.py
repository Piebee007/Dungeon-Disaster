import pygame
import time
import random
from math import sqrt


pygame.init()
pygame.mixer.init() 
#The dimensions of the screen
screenwidth = 1600
screenheight = 720

#These are the limits for the in-game wall so that players, enemies or bullets can go outside of the walls.
wall_limit_x1 =405
wall_limit_x2 = 1520
wall_limit_y1 = 50
wall_limit_y2 = 665

screen = pygame.display.set_mode((screenwidth,screenheight))



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
        self.map_num = map_num
        self.room_x_pos = 0
        self.room_y_pos = 0
        #This is the start time of the game. It is responsible for the delay when shooting
        self.previous_click = time.time()

        #Super means that the player inherits the parent class' attributes and methods
        super().__init__(x_pos, y_pos,health,weapon,damage_mult, image_array)
        self.ammo = weapon_data[self.weapon][3]
        
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
        if self.image_index >=len(self.image_array[0]):
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

#This array will store all the enemies
enemyArray = []
def spawnEnemies(num_enemies):
    #This for loop is responsible for creating all the enemies
    for i in range(num_enemies):
        #This decides if the player is ranged or melee randomly
        enemy_type = random.randint(1,2)
        if enemy_type == 1:
           enemyArray.append(Enemy((random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), 50,0,1, ranged_enemies_images, "R"))
        elif enemy_type == 2:
           enemyArray.append(Enemy((random.randint(wall_limit_x1, wall_limit_x2)), (random.randint(wall_limit_y1, wall_limit_y2)), 50,0,1, melee_enemies_images, "M"))
      
#This array will store all the bullets
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


        #This section is to calculate the proportion of its x and y velocity
        self.change_x = self.end_x_pos - self.x_pos
        self.change_y = self.end_y_pos - self.y_pos
        self.distance = sqrt(((self.change_x)**2 + (self.change_y)**2))
        self.x_vel = self.speed * (self.change_x/self.distance)
        self.y_vel = self.speed * (self.change_y/self.distance)

    #This moves the projectile's position by a certain value 
    def moveProjectile(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    #The projectiles are all circles so they can simply use this method
    def drawProjectile(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x_pos), int(self.y_pos)), self.radius)



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
    player_mask = pygame.mask.from_surface(player.image_array[player.direction][int(player.image_index)])
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
    player_mask = pygame.mask.from_surface(player.image_array[player.direction][int(player.image_index)])
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

def BottomHitbox(player):
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
            spawnEnemies(2 + current_level)
            
    #Display the entrance to the next dungeon room
    screen.blit(verticalDoor, (840, 675))
    

def TopHitbox(player):
    global current_level
    if player.x_pos < top_hitbox[0] + top_hitbox[2] and player.x_pos + player.width > top_hitbox[0]:
        if player.y_pos + player.height > top_hitbox[1] and player.y_pos < top_hitbox[1] + top_hitbox[3]:
            player.room_y_pos -= 1
            player.x_pos = 970
            player.y_pos = 585
            current_level += 1
            spawnEnemies(2 + current_level)
    

    screen.blit(verticalDoor, (840, 0))



def LeftHitbox(player):
    global current_level
    if player.x_pos < left_hitbox[0] + left_hitbox[2] and player.x_pos + player.width > left_hitbox[0]:
        if player.y_pos + player.height > left_hitbox[1] and player.y_pos < left_hitbox[1] + left_hitbox[3]:       
            player.room_x_pos -= 1
            player.x_pos = 1455
            player.y_pos = 360
            current_level += 1
            spawnEnemies(2 + current_level)

    screen.blit(horizontalDoor, (340, 240))



def RightHitbox(player):
    global current_level
    if player.x_pos < right_hitbox[0] + right_hitbox[2] and player.x_pos + player.width > right_hitbox[0]:
        if player.y_pos + player.height > right_hitbox[1] and player.y_pos < right_hitbox[1] + right_hitbox[3]:
            player.room_x_pos +=1
            player.x_pos = 450
            player.y_pos = 360
            current_level += 1
            spawnEnemies(2 + current_level)

    screen.blit(horizontalDoor, (1535, 240))


    
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

#This procedure checks what room the player is in and will show the appropriate exits to the dungeon
def WhatRoomIsPlayer(player):

    if maps[player.map_num][player.room_y_pos][player.room_x_pos] == "UTJ":
        UpTJunction(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "DTJ":
        DownTJunction(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "RTJ":
        RightTJunction(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "LTJ":
        LeftTJunction(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "TRC":
        TopRightCorner(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "TLC":
        TopLeftCorner(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "BRC":
        BottomRightCorner(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "BLC":
        BottomLeftCorner(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "XC":
        HorizontalCorridor(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "YC":
        VerticalCorridor(player)
    
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "FWJ":
        FourWayJunction(player)

    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWU":
        OneWayUp(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWD":
        OneWayDown(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWL":
        OneWayLeft(player)
    elif maps[player.map_num][player.room_y_pos][player.room_x_pos] == "OWR":
        OneWayRight(player)

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

        


player1 = Player(1340, 50,50,0,1,random.randint(0,2), player_images)

#This procedure is responsible for drawing everything on the screen
def redraw_game_window():
    screen.fill([255,255,255])
    screen.blit(dungeonBackground, (340,0))#Responsible for drawing the background
    if level_complete == True:
        #This procedure needs to be in the "redraw...()" as the game is drawing the doors to the next dungeons
        WhatRoomIsPlayer(player1)
    drawMiniMap(player1.map_num)#This draws a player on the minimap
    pygame.draw.rect(screen, (255, 0, 0), [((player1.room_x_pos*42)+13),((player1.room_y_pos*24)+8),15, 12])#Draw player1 on minimap
    #Draw the player's score
    font2 = pygame.font.SysFont('comicsans', 50)
    player_score_text = font2.render(("Score: " + str(player1.score)),1,(0,0,0))
    screen.blit(player_score_text, (25, 225))

    health_text1 = font2.render(("Health: " + str(player1.health)),1,(0,255,0))
    health_text2 = font2.render(("Health: " + str(player1.health)),1,(255,170,0))
    health_text3 = font2.render(("Health: " + str(player1.health)),1,(255,0,0))

    if player1.health >= 40:
        screen.blit(health_text1, (25, 300))
    elif player1.health >= 20 and player1.health < 40:
        screen.blit(health_text2, (25, 300))
    else:
        screen.blit(health_text3, (25, 300))

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

        
    
    player1.draw(screen)#Draw player
    pygame.display.update()







def main_game_loop():
    global level_complete,game_loop, current_level, music, soundEffects
    #http://pygametutorials.wikidot.com/book-time
    #Set some variables at the start of the loop
    game_loop = True
    level_complete = False
    current_level = 0
    music = True
    soundEffects = True
    #Spawn the start enemies and collectables
    spawnEnemies(2)
    spawnCollectables()
    while game_loop == True:
        #If the player clicks the "X" button on the window, the program will close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
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
                enemy.attack(player1)
            else:
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
        if player1.health <= 0:
            music = False
            if soundEffects == True:
                fail_sound_effect.play()
            time.sleep(3)
            end_game(player1)
            game_loop = False

        
        #print(player1.health)
        player1.movePlayer()
        player1.shoot()
        redraw_game_window()

main_game_loop()

pygame.quit()
