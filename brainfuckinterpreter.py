from mod import Mod
code = input('Enter BF code here: ')
tape = [Mod(0, 256)]
pointerloc = 0
codepos = 0
stack = []


def interpret(code, tape, pointerloc, codepos, stack):
    currcode = code[codepos]
    currtape = tape[pointerloc]
    if currcode == '>':
        pointerloc += 1
    elif currcode == '<':
        pointerloc -= 1
    elif currcode == '+':
        tape[pointerloc] += 1
    elif currcode == '-':
        tape[pointerloc] -= 1
    elif currcode == '.':
        print(chr(int(currtape)), end='')
    elif currcode == ',':
        tape[pointerloc] = ord(input('input '))
    elif currcode == '[':
        if tape[pointerloc]:
            stack.append(codepos)
        else:
            newloc = codepos + 1
            level = 1
            while True:
                if code[newloc] == '[':
                    level += 1
                elif code[newloc] == ']':
                    level -= 1
                if not level:
                    break
                newloc += 1
            codepos = newloc
    elif currcode == ']':
        if currtape != 0:
            codepos = stack[-1]
        else:
            stack.pop()
    pointerloc, tape = tapecheck(pointerloc, tape)
    codepos += 1
    return tape, pointerloc, codepos, stack


def tapecheck(pointerloc, tape):
    if pointerloc >= len(tape):
        tape.append(Mod(0, 256))
    if pointerloc == -1:
        tape.insert(0, Mod(0, 256))
        pointerloc += 1
    return pointerloc, tape


while codepos < len(code):
    tape, pointerloc, codepos, stack = interpret(
        code, tape, pointerloc, codepos, stack)
