import pandas as pd

data = [
    ['Alex', 20, 1050],
    ['Bob', 52, 1400],
    ['Cat', 23, 1690]
]

df = pd.DataFrame(data, columns=['name', 'age', 'salary'])

print(df)