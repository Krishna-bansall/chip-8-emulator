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

program_counter = 511

registers = {}
for i in range(15):
    registers[format(i, '0x')] = ""
class CHIP8():
    def __init__(self) -> None:
        # 0 - 512 is reserved for interpreter, 512 - 4095 program data.
        self.memory = bytearray(4096)
        self.pointer = 0     
        self.screen = Screen()
        self.stack = []
        
    def mem_write (self, buffer, index):
        self.pointer = index
        for i, byte in enumerate(buffer):
            self.memory[self.pointer + i] = byte
            
        self.pointer += len(buffer) 
        
    def stack_push (self, item):
        self.stack.insert(0, item)

    def stack_pop(self):
        self.stack.pop(0)


chip = CHIP8()

Running = True
frame = 0

chip.mem_write(font, 0)
# print(chip.memory)
# print(chip.memory[500])


def decode(instruction):
    n1 = instruction[0:1]
    match n1.lower():
        case '0':
            # clear_screen()
            print("case 0 trig")
        case '1':
            print("case 1 trig")
        case '6':
            print("case 6 trig")
        case '7':
            print("case 7 trig")
        case 'a':
            print("case A trig")
        case 'd':
            print("case D trig")
    
print("Chip8 emulator start")
path = 'ibm.ch8'

romobj = open(path, "rb")
rom_arr = bytearray(romobj.read())
chip.mem_write(rom_arr, 511)

# for idx, byte in enumerate(chip.memory):
#     if idx == 511: print("ROM STARTS HERE")
#     print(hex(byte), end=' ')

while Running:
    current_instruction = format(chip.memory[program_counter], '02x') + format(chip.memory[program_counter + 1], '02x')
    decode(current_instruction)
    program_counter += 2

    if program_counter >= 1000: Running = False

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
