orig_word = input('Enter a word: ')
word = orig_word.lower()

palindrome = True
for i in range(len(word)//2):
    if word[i] != word[-1 - i]:
        palindrome = False
        break