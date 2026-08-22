words = input().split()

for i, val in enumerate(words):
    words[i] = val[0].upper()+val[1:]

print(' '.join(words))