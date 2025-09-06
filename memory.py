class Memory():
    def __init__(self):
        # data defined in bytes
        self.memory = bytearray(4096)        
        self.pointer = 0
    
    # Methods of writing to the memory    
    def write(self, address, buffer:bytearray):
        # write the buffer to the memory at the address        
        self.pointer = address
        for i, byte in enumerate(buffer):
            self.memory[self.pointer + i] = byte
            
        self.pointer += len(buffer) 
    
    
    # Methods to reading memory
    def read_all(self):
        print(self.memory)
        
    def show_mem(self):
        for byte in self.memory:
            print(byte)

