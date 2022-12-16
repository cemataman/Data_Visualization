import pandas as pd
df = pd.read_excel("//Users/cem_ataman/Dropbox/Research/Collaborations/Hamburg Group/Participation Data/Drupal 8 (2020-21)/41. Magistrale Wandsbek/conceptioncomments.xlsx")

def check_if_cell(row):
    return row and type(row) == str

# creating a dictionary with an empty list to store main arguments
cdict = {"main": []}

for j in range(len(df["Comment ID"])):
    cid = df["Comment ID"][j]
    if not check_if_cell(df["Comment Subject"][j]):
        cdict["main"].append((cid, df["created (UTC)"][j], df["Comment Text"][j]))
    cdict[cid] = []
    for i in range(len(df["Comment Subject"])):
        subject = df["Comment Subject"][i]
        if check_if_cell(subject):
            sid = subject.split(" ")[-1]
            if int(cid) == int(sid):
                cdict[cid].append((df["Comment ID"][i], df["created (UTC)"][i], df["Comment Text"][i]))

cdict = {k: v for k, v in cdict.items() if v}
print(cdict)

# cdict is the output