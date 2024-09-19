import pandas as pd

#! charger le fichier CSV depuis le lien
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

print(titanic_df)