opcodes = {"add": "00000", "sub": "00001", "mov1": "00010", "mov2": "00011", "ld": "00100", "st": "00101",
           "mul": "00110", "div": "00111", "rs": "01000", "ls": "01001",
           "xor": "01010", "or": "01011", "and": "01100", "not": "01101", "cmp": "01110", "jmp": "01111",
           "jlt": "11100", "jgt": "11101", "je": "11111", "hlt": "11010"}
opcodes2 = {value: key for key, value in opcodes.items()}
regs = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
        "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
regs2 = {value: key for key, value in regs.items()}
stmtTypes = {"add": "A", "sub": "A", "mov1": "B", "mov2": "C", "ld": "D", "st": "D", "mul": "A", "div": "C", "rs": "B",
             "ls": "B", "xor": "A", "or": "A", "and": "A", "not": "C", "cmp": "C", "jmp": "E", "jlt": "E", "jgt": "E",
             "je": "E", "hlt": "F"}
stmtTypes2 = {value: key for key, value in stmtTypes.items()}
unusedSpace = {"A": "00", "B": "", "C": "00000",
               "D": "", "E": "0000", "F": "00000000000"}
unusedSpace2 = {value: key for key, value in unusedSpace.items()}
regdic = {'000': 0, '001': 0, '010': 0, '011': 0, "100": 0, "101": 0, '110': 0, "111": 0}
def execute(inputs):
    PC,check=0,0
    initialpc=0
    while check == 0 and PC < 127:
        n = str(inputs[PC])
        regdic['111'] = 0
        a = n[0:5]
        if opcodes2[a] not in ['jgt','je','jmp','jlt']:
            if opcodes2[a] == 'add':
                regdic[n[7:10]] = regdic[n[10:13]] + regdic[n[13:16]]
                if regdic[n[7:10]]>15:
                    regdic[n[7:10]]=0
            elif opcodes2[a] == 'sub':
                if regdic[n[10:13]] < regdic[n[13:16]]:
                    regdic[n[7:10]] = 0
                    regdic['111'] = 8
                else:
                    regdic[n[7:10]] = regdic[n[10:13]] - regdic[n[13:16]]
            elif opcodes2[a] == 'mul':
                regdic[n[7:10]] = regdic[n[10:13]] * regdic[n[13:16]]
            elif opcodes2[a] == 'or':
                regdic[n[7:10]] = regdic[n[10:13]] | regdic[n[13:16]]
            elif opcodes2[a] == 'xor':
                regdic[n[7:10]] = regdic[n[10:13]] ^ regdic[n[13:16]]
            elif opcodes2[a] == 'and':
                regdic[n[7:10]] = regdic[n[10:13]] * regdic[n[13:16]]
                regdic[n[7:10]] = regdic[n[10:13]] & regdic[n[13:16]]
            elif opcodes2[a] == 'mov1':
                regdic[n[6:9]] = int((n[9:16]), 2)
            elif opcodes2[a] == 'rs':
                regdic[n[6:9]] = regdic[n[6:9]] >> int([n[9:16]], 2)
            elif opcodes2[a] == 'ls':
                regdic[n[6:9]] = regdic[n[6:9]] << int(regdic[n[9:16]], 2)
            elif opcodes2[a] == 'mov2':
                regdic[n[10:13]] = regdic[n[13:16]]
            elif opcodes2[a] == 'div':
                if regdic[n[13:16]] == 0:
                    regdic['000'] = 0
                    regdic['001'] = 0
                    regdic['111'] = 8
                else:
                    regdic['000'] = regdic[n[10:13]] // regdic[n[13:16]]
                    regdic['001'] = regdic[n[10:13]] % regdic[n[13:16]]
            elif opcodes2[a] == 'not':
                regdic[n[10:13]] = ~regdic[n[13:16]]
            elif opcodes2[a] == 'cmp':
                if regdic[n[10:13]] > regdic[n[13:16]]:
                    regdic['111'] = 2
                elif regdic[n[10:13]] < regdic[n[13:16]]:
                    regdic['111'] = 4
                else:
                    regdic['111'] = 1
            elif opcodes2[a] == 'ld':
                regdic[n[6:9]] = int([n[9:16]], 2)
            elif opcodes2[a] == 'hlt':
                check = 1
            print((bin(initialpc)[2:]).zfill(7), end="        ")
            print((bin(regdic['000'])[2:]).zfill(16), end=" ")
            print((bin(regdic['001'])[2:]).zfill(16), end=" ")
            print((bin(regdic['010'])[2:]).zfill(16), end=" ")
            print((bin(regdic['011'])[2:]).zfill(16), end=" ")
            print((bin(regdic['100'])[2:]).zfill(16), end=" ")
            print((bin(regdic['101'])[2:]).zfill(16), end=" ")
            print((bin(regdic['110'])[2:]).zfill(16), end=" ")
            print((bin(regdic['111'])[2:]).zfill(16))
            PC = PC + 1
            initialpc+=1
        else:
            PC+=1
inputs=[]
check2=0
while check2==0:
    x=input()
    inputs.append(x)
    if x[0:5]=='11010':
        check2=1
execute(inputs)
for elm in inputs:
    print(elm)
count = 128 - len(inputs)
for i in range(0, count):
    print('0000000000000000')
def run_test(input_file, output_file):
    with open(input_file, 'r') as file:
        input_data = file.read().splitlines()
    with open(output_file, 'r') as file:
        expected_output = file.read().splitlines()
    output = execute(input_data)
    if output == expected_output:
        print(f"Test Passed: {input_file}")
    else:
        print(f"Test Failed: {input_file}")