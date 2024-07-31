x = input('Char')
# Here I will assume that you enter a single character :D

if x.lower() in 'aeiou':
    print('Vowel')
elif x.lower() in 'bcdfghjklmnpqrstvwxyz':
    print('Consonant')
else:
    print('Special character')

