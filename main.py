from memory import Memory
from screen import Screen
import pygame

# Custom font data
font = bytearray([
    0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
    0x20, 0x60, 0x20, 0x20, 0x70,  # 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
    0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
    0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
    0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
    0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
    0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
    0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
    0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
    0xF0, 0x80, 0xF0, 0x80, 0x80   # F
])

keyboard = [49,50,51,52,113,119,101,114,97,115,100,102, 122,120,99,118]
class CHIP8():
    def __init__(self) -> None:
        self.ram = Memory()
        self.ram.write(0x050, font)
        self.screen = Screen()
        print("Ram Memory Attached!")
        self.stack = []
        
    def stack_push (self, item):
        self.stack.insert(0, item)

    def stack_pop(self):
        self.stack.pop(0)


chip = CHIP8()

Running = True
frame = 0


# while Running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             Running = False
        
#         if event.type == pygame.KEYDOWN:
#             if event.key in keyboard:
#                 print(event.unicode.lower())                            
#     chip.screen.render()
    
    
#     pygame.display.flip()
#     # dt = pygame.time.Clock().tick(60)
#     # frame += 1        

# chip.ram.read_all()
