import pandas as pd

# read the text file
with open('data.txt', 'r') as file:
    text_data = [line.strip().split()[0] for line in file.readlines()]

# read the Excel sheet
excel_data = pd.read_excel('data.xlsx', header=None)

# get the first row of the Excel sheet
excel_row = list(excel_data.iloc[0])

# convert the first row of the Excel sheet to a string type
excel_row = [str(item) for item in excel_row]

# compare the data
text_file_diff = set(text_data) - set(excel_row)
excel_diff = excel_data.drop(0, axis=0).loc[:, ~excel_data.iloc[0].isna()]
excel_diff.columns = excel_row
excel_diff = excel_diff[~excel_diff.index.isin(text_data)]
common_data = set(text_data).intersection(set(excel_row))

# print the differences
print("The following data is in the Excel sheet but not in the text file:")
print(excel_diff.to_string(index=False))

print("\nThe following data is in the text file but not in the Excel sheet:")
for item in text_file_diff:
    print(item)

print("\nThe following data is common to both the text file and the Excel sheet:")
for item in common_data:
    print(item)
