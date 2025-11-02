import pygame, math

class Screen():    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((64*10,32*10))
        self.pos = pygame.Vector2(0,0)


    def render(self):    

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
            
                
    def exit():
        pygame.quit()
        

