import pandas as pd

food1 = {'ID': [1, 2, 3, 4, 5, 6], 'Name': ["corn ", "mango", "graph", "orange", "pine apple", "carrot"],
         'price': [14, 15, 16, 17, 18, 19]}

food2 = {'ID': [1, 2, 3, 4, 5, 6], 'Name': ["apple ", "mango", "graph", "orange", "pine apple", "carrot"],
         'price': [14, 15, 16, 17, 18, 19]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = pd.merge(table1, table2, on="ID")

print(fusion)
