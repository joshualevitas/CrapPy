#write assembly parser

def ass_splitter(program):
    with open(program, 'r') as p:
        lines = p.readlines()  
        return [line.strip("\n").split() for line in lines]  
    


allowed_functions = ["ADD",
                     "NOT",
                     "BR",
                     "JMP",
                     "JSR",
                     "LD",
                     "LDI",
                     "LDR",
                     "LEA",
                     "ST",
                     "STI",
                     "STR",
                     "TRAP",
                     "RES",
                     "RTI"]






def ass_parser(program):
    try:
        lines = ass_splitter(program)

    except Exception as e:
        print(e)


