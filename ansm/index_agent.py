import pandas as pd


def get_indices():
    data = pd.read_excel(r'../read_data/Template_Input_Output.xlsx', header=None, sheet_name='SearchStrategy')

    search_strings = data.loc[7:9][19].values
    date_from = str(data.loc[2:3][1].values[0]).split(" ")[0]
    date_to = str(data.loc[2:3][1].values[1]).split(" ")[0]

    return (search_strings, date_from, date_to)

data = get_indices()
print(data)