import pygame, math, random, vector
 
pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

class Player():
    def __init__(self):
        self.pos = vector.CreateVector2(287.5, 287.5)
        self.hook = vector.CreateVector2(287.5, 287.5)
        self.hookVelocity = vector.CreateVector2(0, 0)
        self.attached = False
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.pos.x, self.pos.y, 25, 25))
        pygame.draw.ellipse(screen, (0, 0, 255), (self.hook.x, self.hook.y, 5, 5))
    def key(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos.x-=1
        elif keys[pygame.K_RIGHT]:
            self.pos.x+=1
        if keys[pygame.K_UP]:
            self.pos.y-=1
        elif keys[pygame.K_DOWN]:
            self.pos.y+=1
        if keys[pygame.K_SPACE]:
            self.attached = True
        if self.pos.collideRect(self.pos, 25, 25, self.hook, 5, 5):
            self.attached = False
            if not self.attached:
                self.hook.move(self.pos.x + 12.5, self.pos.y + 12.5)
                if pressed[0]:
                    r = math.atan2(self.pos.y - mouse[1], self.pos.x - mouse[0])
                    dist = math.dist([self.pos.x, self.pos.y], [mouse[0], mouse[1]])
                    self.hookVelocity.push(-math.cos(r) * dist/10, -math.sin(r) * dist/10)
                    self.hook.push(-math.cos(r) * 20, -math.sin(r) * 20)
    def update(self):
        self.pos.x = vector.constrain(self.pos.x, 0, 575)
        self.pos.y = vector.constrain(self.pos.y, 0, 575)
        # Hook Movement
        self.hook.x+=self.hookVelocity.x
        self.hook.y+=self.hookVelocity.y
        self.hookVelocity.move(self.hookVelocity.x * 0.9, self.hookVelocity.y * 0.9)
        # Makes sure the Player can reach the floor
        if self.hook.x < 0:
            self.hookVelocity.move(-self.hookVelocity.x, self.hookVelocity.y)
            self.hook.x = 0
        elif self.hook.x > 600:
            self.hookVelocity.move(-self.hookVelocity.x, self.hookVelocity.y)
            self.hook.x = 600
        if self.hook.y < 0 :
            self.hookVelocity.move(self.hookVelocity.x, -self.hookVelocity.y)
            self.hook.y = 0
        elif self.hook.y > 600:
            self.hookVelocity.move(self.hookVelocity.x, -self.hookVelocity.y)
            self.hook.y = 600
        # Player is attracted to the Hook when attched
        if self.attached:
            movement = self.pos.sub(self.hook)
            self.pos.push(-movement[0]/20, -movement[1]/20)
            pygame.draw.line(screen, (0, 0, 0), [self.pos.x + 2.5, self.pos.y + 2.5], [self.hook.x, self.hook.y], 5)
p = Player()
class Enemy():
    def __init__(self):
        self.pos = vector.CreateVector2(round(random.randint(0, 400)), -100)
        self.ppos = vector.CreateVector2(round(random.randint(0, 400)), -100)
        self.spd = 0.9
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.pos.x, self.pos.y, 25, 25))
    def follow(self):
        self.ppos = self.pos
        if self.pos.x > p.pos.x:
            self.pos.x-=self.spd
        elif self.pos.x < p.pos.x:
            self.pos.x+=self.spd
        if self.pos.y > p.pos.y:
            self.pos.y-=self.spd
        elif self.pos.y < p.pos.y:
            self.pos.y+=self.spd
    def collide(self, t, type = "UNI"):
        if type != "Player" or type == "Player" and t.attached == False:
            moveBy = self.pos.sub(t.pos, self.spd/2)
            while self.pos.collideRect(self.pos, 25, 25, t.pos, 25, 25):
                self.pos.push(moveBy[0], moveBy[1])
                t.pos.push(-moveBy[0], -moveBy[1])

enemys = []

for i in range(10):
    enemys.append(Enemy())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill((255, 255, 255))
    p.draw()
    p.key()
    p.update()
    for i in range(len(enemys)):
        enemys[i].draw()
        enemys[i].follow()
        enemys[i].collide(p, "Player")
        for j in range(len(enemys)):
            if i != j:
                enemys[i].collide(enemys[j])
    pygame.display.update()
    clock.tick(60)
pygame.done()
