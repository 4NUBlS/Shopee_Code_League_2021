def translate(word):
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'ay'
    else:
        for i, char in enumerate(word):
            if char in 'aeiouy':
                return word[i:] + word[:i] + 'ay'

    return word + 'ay'

s = 'i love the eleqance of python'
for word in s.split():
    print(translate(word))