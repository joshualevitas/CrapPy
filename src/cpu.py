# class definition for cpu
# 8 registers

memory_max = 1 << 16

class CPU:
    def __init__(self):

        self.memory = [0] * memory_max # 65536 bytes of memory
        self.registers = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0,
            "R4": 0,
            "R5": 0,
            "R6": 0,
            "R7": 0,
            "RPC": 0,
            "RCOND": 0,
            "RCOUNT": 0
        }

        self.flags = {
            "FL_POS": 1 << 0,
            "FL_ZRO": 1 << 1, 
            "FL_NEG": 1 << 2
        }


    def set_flags(self, val):
        if val < 0:
            self.registers["RCOND"] += self.flags["FL_NEG"]
        elif val == 0:
            self.registers["RCOND"] += self.flags["FL_ZRO"]
        else:
            self.registers["RCOND"] += self.flags["FL_POS"]


    #op codes
    def op_add(self, reg_a, reg_b, c):
        if type(c) == int:
            self.registers[reg_a] = self.registers[reg_b] + c
        else:
            self.registers[reg_a] = self.registers[reg_b] + self.registers[c]
        
        self.set_flags(self.registers[reg_a])

    
    def op_and(self, reg_a, reg_b, c):
        if type(c) == int:
            self.registers[reg_a] = self.registers[reg_b] & c
        else:
            self.registers[reg_a] = self.registers[reg_b] & self.registers[c]

        self.set_flags(self.registers[reg_a])

    def op_not(self, reg_a, reg_b):
        self.registers[reg_a] = ~self.registers[reg_b]
        self.set_flags(self.registers[reg_a])

    #idk if this is right
    def op_br(self, flag, offset):
        if self.registers["RCOND"] & flag:
            self.registers["RPC"] += offset

    def op_jmp(self, reg_a):
        self.registers["RPC"] = self.registers[reg_a]

    def op_jsr(self, reg_a):
        self.registers["R7"] = self.registers["RPC"]
        self.registers["RPC"] = self.registers[reg_a]

    def op_ld(self, reg_a, address):
        self.registers[reg_a] = self.memory[address]
        self.set_flags(self.registers[reg_a])

    def op_ldi(self, reg_a, address):
        self.registers[reg_a] = self.memory[self.memory[address]]
        self.set_flags(self.registers[reg_a])
        

    def op_ldr(self, reg_a, reg_b, offset):
        self.registers[reg_a] = self.memory[self.registers[reg_b] + offset]
        self.set_flags(self.registers[reg_a])

    def op_lea(self, reg_a, offset):
        self.registers[reg_a] = self.registers["RPC"] + offset
        self.set_flags(self.registers[reg_a])

    def op_st(self, reg_a, address):
        self.memory[address] = self.registers[reg_a]

    def op_sti(self, reg_a, address):
        self.memory[self.memory[address]] = self.registers[reg_a]

    def op_str(self, reg_a, reg_b, offset):
        self.memory[self.registers[reg_b] + offset] = self.registers[reg_a]

    def op_trap(self, address):
        self.registers["R7"] = self.registers["RPC"]
        self.registers["RPC"] = address

    def op_res(self):
        pass

    def op_rti(self):
        pass