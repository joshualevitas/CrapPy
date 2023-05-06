from cpu import *

cpu = CPU()
cpu.memory[0] = 0b00000001
cpu.memory[1] = -0b00000001
cpu.op_ld("R0", 0)
assert cpu.registers["R0"] == 1

cpu.op_ldi("R0", 0)
assert cpu.registers["RCOND"] == 4


