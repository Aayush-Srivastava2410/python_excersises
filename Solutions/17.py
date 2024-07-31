def factors(x):
    factors = []
    for i in range(1, x+1):
        if x%i == 0:
            factors.append(i)
        else:pass
    
    return factors

for i in range(0, 101):
    if factors(i) == []:
        print(i)
    else: pass
