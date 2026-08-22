words = input("Enter a sentence: ").split()

longest_word = ''

for i in words:
    if len(i)>len(longest_word):
        longest_word=i

print(longest_word)