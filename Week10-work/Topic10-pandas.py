import pandas as pd

listData = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 70],
    ['Mark', 'math', 57],
    ['Mark', 'programming', 70],
    ['John', 'programming', 61],
]

df = pd.DataFrame(listData, columns = ['Name', 'Subject', 'Grade'])

print(df.head(3))

path = "./data/"
csv_filename = path + "grades.csv"
df.to_csv(csv_filename)

excel_filename = path + "grades.xlsx"
df.to_excel(excel_filename, index=False, sheet_name='data')

with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name='summary')

mean = df.describe().loc['mean', 'Grade']
print(mean)

