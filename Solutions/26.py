inputs = []

while True:
    x=input('Input:')
    if x == "show":
        print(inputs)
    elif x=='exit': exit()
    else:
        inputs.append(x)