import pandas as pd

Employee = {'ID': [1, 2, 3, 4, 5, 6], 'Name': ["Vamsi", "John", "Maxwell", "Markram", "Klashen", "Gurbaz"],
            'Hourly salary': [14, 15, 16, 17, 18, 19]}

table1 = pd.DataFrame(Employee)

print(table1.head(1))  # prints from the first record

print(table1.tail(1))  # prints from the last record
