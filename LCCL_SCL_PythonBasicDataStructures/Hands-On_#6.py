def report(s):
    d = dict()
    s = s.lower().split()
    print(s)
    for word in s:
        key = word[0].upper()


report('''Someday I'll wish upon a star''')
