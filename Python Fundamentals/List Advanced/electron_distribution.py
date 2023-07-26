def electron_addition(electrons):
    atom_shell = []
    index = 1
    while True:
        if electrons <= 0:
            break
        current_number_of_electrons = 2 * index ** 2
        if current_number_of_electrons <= electrons:
            atom_shell.append(current_number_of_electrons)
        else:
            atom_shell.append(electrons)
            electrons = 0
        electrons -= current_number_of_electrons
        index += 1
    return atom_shell


number_of_electrons = int(input())

print(electron_addition(number_of_electrons))
