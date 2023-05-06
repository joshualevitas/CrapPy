from cpu import CPU

def run(program):
    cpu = CPU()
    with open(program, 'r') as f:
        line = f.readline()
        execute(cpu, line)
    
    print(cpu.registers)



def execute(cpu, line):
    line = line.split()
    if line[0] == "LOAD":
        cpu.op_ld(line[1], int(line[2], 2))
    return


        

run("test_program")
# with open("test_program", 'r') as f:
#     line = f.readline()
#     print(int(line.split()[-1]))






    