# from memory import Memory
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


class Cpu():
    def __init__(self) -> None:
        # 0 - 512 is reserved for interpreter, 512 - 4095 program data.
        self.memory = bytearray(4096)
        
        self.pointer = 0     
        self.pc = 512
        self.screen = Screen()
        self.stack = []        
        self.current_instruction : hex
        self.instruction_is_1nnn = False
            
        self.registers = {"Vi":""}
        for i in range(16):
            self.registers['V' + format(i, '0x')] = ""       
        
      
    def mem_write (self, buffer, index):
        self.pointer = index
        for i, byte in enumerate(buffer):
            self.memory[self.pointer + i] = byte
        self.pointer += len(buffer) 
    
    def stack_push (self, item):
        self.stack.insert(0, item)

    def stack_pop(self):
        self.stack.pop(0)

    def set_pc(self, val):
        self.pc = val
    def reset_flags(self):
        self.instruction_is_1nnn = False
    # opcodes
    def op_1nnn(self, instruction):
        val = instruction & 0x0FFF
        self.pc = val
        self.instruction_is_1nnn = True
            
    def op_6xnn(self, instruction):
        second_nibble = (instruction & 0x0F00)    
        self.registers['V' + str(second_nibble >> 8)] = instruction & 0x00FF

    def op_7xnn(self, instruction):
        second_nibble = (instruction & 0x0F00)    
        self.registers['V' + str(second_nibble >> 8)] += instruction & 0x00FF

    def op_annn(self, instruction):
        self.registers['Vi'] = instruction & 0x0FFF
    
    def op_dxyn(self, instruction):
        X = (instruction & 0x0F00) 
        Y = (instruction & 0x00F0) 
        N = (instruction & 0x000F)
        
        x_coordinate = self.registers['V' + str(X >> 8)]
        y_coordinate = self.registers['V' + str(Y >> 4)]
        pointer = self.registers['Vi']
        sprite = self.memory[pointer: pointer + N]
        
        self.screen.render(sprite, x_coordinate, y_coordinate, height = N)
        
    def set_current_instruction(self, instruction):
        self.current_instruction = instruction
    
    def fetch_instruction(self, addr):
        byte_a =  self.memory[addr]
        byte_b = self.memory[addr + 1]
        return byte_a << 8 | byte_b
    
    def clear_screen():
        Screen.cls()
    
    def execute(self):
        instruction = self.current_instruction
        first_nibble = (instruction & 0xf000) >> 12
            
        match first_nibble:
            case 0: self.clear_screen
            case 1: self.op_1nnn(instruction)                 
            case 6: self.op_6xnn(instruction)
            case 7: self.op_7xnn(instruction)       
            case 0xA: self.op_annn(instruction)  
            case 0xD: self.op_dxyn(instruction)
                
    

def main() -> None:
    cpu = Cpu()
    Running = True
    frame = 0

    cpu.mem_write(font, 0)

    print("Chip8 emulator start")
    path = 'ibm.ch8'

    rom_obj = open(path, "rb")
    rom_arr = bytearray(rom_obj.read())
    cpu.mem_write(rom_arr, cpu.pc)

    while Running:
        pc = cpu.pc
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key in keyboard:
                    print(event.unicode.lower())                            
    
        current_instruction = cpu.fetch_instruction(pc)
        cpu.set_current_instruction(current_instruction)
        cpu.execute()
        
        if cpu.instruction_is_1nnn == False:
             cpu.set_pc(pc + 2)
        
        cpu.reset_flags()
        
        print(current_instruction, hex(current_instruction))
        print('pc', cpu.pc, cpu.pc - 511)
        print(cpu.registers)

        pygame.display.flip()
    
     
        dt = pygame.time.Clock().tick(60)
        frame += 1        


if __name__ == '__main__':
    main()