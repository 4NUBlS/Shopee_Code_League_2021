# import botnoi as bn
import pandas as pd

det = pd.read_csv('titanic.csv')

print('Poor-People :',
        det[(det['Survived'] == 1)
            & (det['Fare'] <= 7.91)
        ].count()['Survived']
    )

print('Nomal-People :',
        det[(det['Survived'] == 1)
            & (det['Fare'] > 7.91)
            & (det['Fare'] < 31)
        ].count()['Survived']
    )

print('Rich-People :',
        det[(det['Survived'] == 1)
            & (det['Fare'] >= 31)
        ].count()['Survived']
    )