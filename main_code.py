# Path to the PDF file


import pdf_reader as pr
import os 
import pandas as pd 
import txt_parser as tp
import numpy as np

entries = os.listdir('uploads')
for x in range(len(entries)):
  entries[x] = 'uploads/'+ entries[x]



def createDF(path):
  df, org, subj = pr.read_pdf(pdf_path=path)
  
  pd.set_option("max_colwidth", None)  
  df = df.rename(columns={0: "Opportunity"})
  
  df["Links"] = df["Opportunity"].map(tp.find_url)
  df["Opportunity"] = df["Opportunity"].map(tp.remove_emoji)
  df["Opportunity"] = df["Opportunity"].map(tp.remove_url)

  print("subject: ", subj)
  df["Opportunity"] = df["Opportunity"].map(lambda x: tp.removeSubject(x, subj=subj))
  df["Opportunity"] = df["Opportunity"].map(tp.removeNonAscii)
  df['Header'] = df["Opportunity"].map(tp.get_cat)

  return df

empty = True

for file in entries:
  df = createDF(file)

  if empty == True:
    data_consolidated = df
    empty = False 
    print("first done")
  else: 
    print("starting second")
    data_consolidated = np.vstack((data_consolidated, df))

data_consolidated = pd.DataFrame(data_consolidated)

data_consolidated.to_csv('Output.csv')