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

registers = {"Vi":""}
for i in range(16):
    registers['V' + format(i, '0x')] = ""

def hex_to_int(number):
    n = int('0x' + str(number), 16)
    return n

def decode(instruction):
    
    first_nibble = (instruction & 0xf000) >> 12
    second_nibble = (instruction & 0x0F00)
    global program_counter
        
    match first_nibble:
        
        case 0:
            # clear_screen()
            print("case 0 trig")
        case 1:
            val = instruction & 0x0FFF
            program_counter = val
            print("case 1 trig")

        case 6:
            registers['V' + str(second_nibble)] = instruction & 0x00FF

        case 7:
            registers['V' + str(second_nibble)] += instruction & 0x00FF

        case 0xA:
            registers['Vi'] = instruction & 0x0FFF
        
        case 0xD:
            print("case D trig")
            
    if (first_nibble != 1):
         program_counter += 2
        
    return


class Chip8():
    def __init__(self) -> None:
        # 0 - 512 is reserved for interpreter, 512 - 4095 program data.
        self.memory = bytearray(4096)
        self.pointer = 0     
        self.program_counter = 511
        self.screen = Screen()
        self.stack = []
        
    def mem_write (self, buffer, index):
        self.pointer = index
        for i, byte in enumerate(buffer):
            self.memory[self.pointer + i] = byte
            
        self.pointer += len(buffer) 
    
    def stack_push (self, item):
        self.stack.insert(0, item)

    def set_pc(self, val):
        self.program_counter = val
    
    def stack_pop(self):
        self.stack.pop(0)


def main() -> None:
    chip = Chip8()

    Running = True
    frame = 0

    chip.mem_write(font, 0)

    print("Chip8 emulator start")
    path = 'ibm.ch8'

    rom_obj = open(path, "rb")
    rom_arr = bytearray(rom_obj.read())
    chip.mem_write(rom_arr, 511)

    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key in keyboard:
                    print(event.unicode.lower())                            
    
        current_instruction = (chip.memory[program_counter] << 8)  | chip.memory[program_counter + 1]
        # decode(current_instruction)
        print(current_instruction)
        pygame.display.flip()
    
        if program_counter >= 1000: Running = False

    # while Running:
            
    #         if event.type == pygame.KEYDOWN:
    #             if event.key in keyboard:
    #                 print(event.unicode.lower())                            
    #     chip.screen.render()
        
        
    #     # dt = pygame.time.Clock().tick(60)
    #     # frame += 1        

    # chip.ram.read_all()


if __name__ == '__main__':
    main()