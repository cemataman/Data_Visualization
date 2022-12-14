import pandas as pd
import numpy as np
import copy

import warnings
import logging
logging.captureWarnings(True)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

### Dataframe display settings
desired_width=520
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

### Import data from the excel file
df = pd.read_excel('/Users/cem_ataman/Desktop/conceptioncomments.xlsx')

# Modify topic names in columns
df['a'] = 'topic ' + df['a'].astype(str)

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


### Add the unique values (topics) as children into the dataframe
for val in unique_values:
    new_row = copy.deepcopy(new_df.iloc[0,:])
    new_dict = new_row.to_dict()
    for x,y in new_dict.items():
        if x == 'branch':
            new_dict.update({'branch':val})
        else: new_dict.update({x:''})
    new_df = new_df.append(new_dict, ignore_index=True)
    new_df['root'].replace('', ' ', inplace=True)
    new_df.dropna(subset=['root'], inplace=True)

new_df.to_excel('Sunburst_Data.xlsx')
print(new_df)