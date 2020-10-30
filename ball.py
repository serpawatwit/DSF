import pygame

class Ball:
    #pass
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, color, bgcolor, BORDER, BORDERBOTTOM):
        #instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.border = BORDER + self.RADIUS
        self.borderbottom = BORDERBOTTOM - self.RADIUS
        self.screen = screen
        self.color = color
        self.bgcolor = bgcolor
        
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        #new position = old position + difference delta position (velocity)
        #delete the old ball

        self.show(self.bgcolor)
        px = self.x + self.vx
        py = self.y + self.vy
        if(px < self.border and py > self.borderbottom):
            self.vx = -self.vx
            self.x = self.x + self.vx
            self.vy = -self.vy
            self.y = self.y + self.vy
        elif(px < self.border and py < self.border):
            self.vx = -self.vx
            self.x = self.x + self.vx
            self.vy = -self.vy
            self.y = self.y + self.vy
        elif(px < self.border):
            self.vx = -self.vx
            self.x = self.x + self.vx
        elif(py > self.borderbottom):
            self.vy = -self.vy
            self.y = self.y + self.vy
        elif(py < self.border):
            self.vy = -self.vy
            self.y = self.y + self.vy
        else:
            self.x = px
            self.y = py
        self.show(self.color)
        
        
