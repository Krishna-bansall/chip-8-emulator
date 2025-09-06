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
                    
            self.screen.fill("black")
            
            sprite = [0xF0, 0x90, 0xF0, 0x90, 0xF0]
            
            chip_surface = pygame.Surface((8, len(sprite)))
            # chip_surface.fill((255,255,255))
            
            for y, byte in enumerate(sprite):
                for x in range(8):
                    if byte & (0x80 >> x):
                        chip_surface.set_at((x,y), (255, 255,255))
            
            scaled = pygame.transform.scale(chip_surface, (8*10,len(sprite)*10))

            self.screen.blit(scaled, (0,0))
            

            pygame.display.flip()
            dt = self.clock.tick(60)
            self.frame += 1            
            
                
    def exit():
        pygame.quit()
        

