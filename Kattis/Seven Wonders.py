input_ = input()

print(input_.count('T') ** 2 +
      input_.count('G') ** 2 +
      input_.count('C') ** 2 +
      7 * (min(input_.count('T'), input_.count('G'), input_.count('C'))))
