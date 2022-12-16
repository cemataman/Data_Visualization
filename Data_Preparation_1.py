import pandas as pd
df = pd.read_excel("/Users/cem_ataman/Desktop/conceptioncomments.xlsx")

'''
df["Victim's age"] = pd.to_numeric(df["Victim's age"], errors='coerce').fillna(0).astype(np.int64)
df.rename(columns={'Fleeing (Source: WaPo)': 'Fleeing'}, inplace=True)

df = df[df["State"].isin(['NY', 'CA', 'TX'])]
df = df[df["Victim's race"].isin(["White", "Black", "Hispanic", "Asian"])]
'''

def check_if_cell(row):
    return row and type(row) == str

# creating a dictionary with an empty list to store main arguments
cdict = {"main": []}

#for k in range(len(df["Contribution ID"]))

for j in range(len(df["Comment ID"])):
    cid = df["Comment ID"][j]
    if not check_if_cell(df["Comment Subject"][j]):
        cdict["main"].append(cid) #, df["created (UTC)"][j])
    cdict[cid] = []
    for i in range(len(df["Comment Subject"])):
        subject = df["Comment Subject"][i]
        if check_if_cell(subject):
            sid = subject.split(" ")[-1]
            if int(cid) == int(sid):
                cdict[cid].append(df["Comment ID"][i]) # df["created (UTC)"][i])

cdict = {k: v for k, v in cdict.items() if v}
print(cdict)

# cdict is the output