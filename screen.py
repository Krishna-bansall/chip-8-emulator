import pygame, math

class Screen():    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((64*10,32*10))
        self.pos = pygame.Vector2(0,0)


    def render(self, sprite, height):    
            self.screen.fill("black")
                        
            pygame.Surface()
            sprite_surface = pygame.Surface((height, len(sprite)))
            
            for y, byte in enumerate(sprite):
                for x in range(height):
                    if byte & (0x80 >> x):
                        sprite_surface.set_at((x,y), (255, 255,255))
            
            scaled = pygame.transform.scale(sprite_surface, (8*10,len(sprite)*10))
            self.screen.blit(scaled, (0,0))      
            
                
    def exit():
        pygame.quit()
        

