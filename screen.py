import pygame, math

height = 32
width = 64
scale = 10
tup = (width * scale , height * scale)
class Screen():    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(tup)
        self.pos = pygame.Vector2(0,0)

    def cls(self):
        self.screen.fill("black")
    
    def render(self, sprite, x_coordinate, y_coordinate, height):    
            # sprite = pygame.transform.scale_by(framebuffer, 10)
            surf = pygame.Surface((8, height))
                    
            for y, byte in enumerate(sprite):
                for x in range(height):
                    if byte & (0x80 >> x):
                        surf.set_at((x,y), (255, 255,255))
            
            scaled_surf = pygame.transform.scale_by(surf,10)
            self.screen.blit(scaled_surf, (x_coordinate*10,y_coordinate*10))      
            
                
    def exit():
        pygame.quit()
        

