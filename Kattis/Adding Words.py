import fileinput

variables, switch = {}, {}

for i in fileinput.input():
    command = i.split()

    if command[0] == 'def':
        # command[1] is a word
        # command[2] is an integer

        # remove old definition
        if command[1] in variables:
            old_value = variables[command[1]]
            del switch[old_value]

        # add new things to dict
        variables[command[1]] = int(command[2])
        switch[int(command[2])] = command[1]

    if command[0] == 'calc':
        calc_var = command[1::2]
        operator = command[2::2]

        in_dict = True
        for j in calc_var:
            in_dict = j in variables

        if in_dict:
            result = variables[calc_var[0]]

            for j in range(len(calc_var) - 1):
                if operator[j] == '-':
                    result -= variables[calc_var[j + 1]]
                if operator[j] == '+':
                    result += variables[calc_var[j + 1]]

            if result not in switch:
                in_dict = False

        # output
        for i in command[1:]:
            print(i, end=' ')
        if in_dict:
            print(switch[result])
        else:
            print('unknown')

    if command[0] == 'clear':
        variables.clear()
        switch.clear()

# sample test case
# def foo 3
# calc foo + bar =
# def bar 7
# def programming 10
# calc foo + bar =
# def is 4
# def fun 8
# calc programming - is + fun =
# def fun 1
# calc programming - is + fun =
# clear
