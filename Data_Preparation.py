# import pandas as pd
# df = pd.read_excel("/Users/cem_ataman/Desktop/conceptioncomments.xlsx")
#
# '''
# df["Victim's age"] = pd.to_numeric(df["Victim's age"], errors='coerce').fillna(0).astype(np.int64)
# df.rename(columns={'Fleeing (Source: WaPo)': 'Fleeing'}, inplace=True)
#
# df = df[df["State"].isin(['NY', 'CA', 'TX'])]
# df = df[df["Victim's race"].isin(["White", "Black", "Hispanic", "Asian"])]
#
# '''
#
# def check_if_cell(row):
#     return row and type(row) == str
#
# # creating a dictionary with an empty list to store main arguments
# cdict = {"main": []}
#
# #for k in range(len(df["Contribution ID"]))
#
#
#
# for j in range(len(df["Comment ID"])):
#     cid = df["Comment ID"][j]
#     if not check_if_cell(df["Comment Subject"][j]):
#         cdict["main"].append(cid) #, df["created (UTC)"][j])
#     cdict[cid] = []
#     for i in range(len(df["Comment Subject"])):
#         subject = df["Comment Subject"][i]
#         if check_if_cell(subject):
#             sid = subject.split(" ")[-1]
#             if int(cid) == int(sid):
#                 cdict[cid].append(df["Comment ID"][i]) # df["created (UTC)"][i])
#
# cdict = {k: v for k, v in cdict.items() if v}
# print(cdict)
#
# # cdict is the output

import plotly.express as px
import pandas as pd
import copy

### Import data from the excel file
df = pd.read_excel('/Users/cem_ataman/Desktop/conceptioncomments.xlsx')

#### CREATING A DATAFRAME WITH PARENT AND CHILD COLUMNS ####

new_df = pd.DataFrame()
unique_values = []

for i in range(len(df.iloc[:,0])):

    # take the topic numbers as unique values
    if df['a'].to_list()[i] not in unique_values:
        unique_values.append(df['a'].to_list()[i])

    # filter out the comments with no replies and turn each row to an object with the information under columns
    if df['branch'].to_list()[i] in df['root'].to_list() or (str(df['root'].to_list()[i]) != " " and str(df['root'].to_list()[i]) != "nan"):
        row = df.iloc[i,:]
        new_row = copy.deepcopy(row)

        #turn each row into a dictionary (column names: keys, rows: values)
        new_dict = new_row.to_dict()

        #locate topic numbers as parents under root
        if str(row['root']) == "nan":
            new_dict.update({'root': row['a']})

        new_df = new_df.append(new_dict, ignore_index=True)
print(new_df)

### Add the unique values (topic numbers) as children into the dataframe
for val in unique_list:
    new_row = copy.deepcopy(new_df.iloc[0,:])
    new_dict = new_row.to_dict()
    for x,y in new_dict.items():
        if x == 'branch':
            new_dict.update({'branch':val})
        else: new_dict.update({x:''})
    new_df = new_df.append(new_dict, ignore_index=True)

new_df.to_excel('kate2.xlsx')
