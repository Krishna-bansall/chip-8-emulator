import pygame, math


class Screen():
    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((64*10,32*10))
        self.clock = pygame.time.Clock()
        self.Running = True
        self.dt=0 # delta time?  
        self.frame = 0
        self.pos = pygame.Vector2(0,0)

    def run_screen_loop(self):    
        print("Screen Module Attached!")
        
        while self.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                    
            self.screen.fill("yellow")
            pygame.draw.circle(self.screen, "red", self.pos, 50 )
            

            self.pos.y -= math.sin(self.frame / 10)
            self.pos.x += math.sin(self.frame / 10)

            pygame.display.flip()
            dt = self.clock.tick(60)
            print(self.frame)
            self.frame += 1            
                
    def exit():
        pygame.quit()
        

