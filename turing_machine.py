# files
TAPE = open("tape.txt", "r")
ALF = open("alfabet.txt", "r")
COMMANDS = open("commands.txt", "r")
RESULT = open("result.txt", "w")

# function
def readByChar(filename):
    text = filename.read()
    array = [text[i] for i in range(len(text))]
    return array

def findCommand(q, cell, com, alf):
    for i in com:
        if (q == int(i[0])) and (cell == i[1]) and (checkAlf(cell, alf)):
            return i
    return "error"

def executeCommand(com, q, tape, cell_num):
    flag = True
    if com[2] == ">":
        q = int(com[3])
        tape[cell_num] = com[4]
        cell_num += 1 if com[5] == "R" else -1
    else:
        flag = False
    return q, tape, cell_num, flag

def writeRes(resFile, tape, cell_num, q, iter, com, back_tape, back_cell_num):
    resFile.write(str(iter) + ".\n")
    resFile.write("".join(back_tape) + "\n")
    resFile.write(" " * (back_cell_num) + "^" + "\n")
    resFile.write(com + "\n")
    resFile.write("".join(tape) + "\n")
    resFile.write(" " * (cell_num) + "^" + "\n\n")

def checkError(com):
    if com == "error":
        print("Error! Emergency stop of the program")

def checkAlf(c, alf):
    return (c == "_") or (c in alf)


if __name__ == "__main__":
    # program
    # start settings
    tape = readByChar(TAPE)
    alf = readByChar(ALF)
    com = [line.strip() for line in COMMANDS]
    q = 0
    cell_num = 0
    iter = 0
    flag = True

    # start MT
    print("Start MT")
    while flag:
        command = findCommand(q, tape[cell_num], com, alf)
        back_tape = tape.copy()
        back_cell_num = cell_num
        checkError(command)
        q, tape, cell_num, flag = executeCommand(command, q, tape, cell_num)
        iter += 1
        writeRes(RESULT, tape, cell_num, q, iter, command, back_tape, back_cell_num)
    print("Program end")
