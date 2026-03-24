import os
for file in os.listdir():
    if os.path.isfile(file):
        os.remove(file)

outputmonth = dataframe.iloc[0,0]
outputmonth

listofagencyall = list(dataframe['Agency #'].unique())
listofagencysel = listofagencyall[:]
listofagencysel

dfg3 = dataframe.copy()

dfg3['Open Stock'] = dfg3['Open Stock'].astype(int)
dfg3['Oil Production'] = dfg3['Oil Production'].astype(int)
dfg3['Oil Other'] = dfg3['Oil Other'].astype(int)
dfg3['Oil Sales'] = dfg3['Oil Sales'].astype(int)
dfg3['Close Stock'] = dfg3['Close Stock'].astype(int)
dfg3['Gas Production'] = dfg3['Gas Production'].astype(int)
dfg3['Gas Lease Use'] = dfg3['Gas Lease Use'].astype(int)
dfg3['Gas Sales'] = dfg3['Gas Sales'].astype(int)
dfg3['Water Production'] = dfg3['Water Production'].astype(int)
dfg3['Gas Sales BTU'] = dfg3['Gas Sales BTU'].astype(int)
dfg3['Injection Volume'] = dfg3['Injection Volume'].astype(int)



 
 

for i in listofagencysel: 

    dftest1 = dfg3[dfg3['Agency #']==i] 

     

    ## PART A 

    xxy = dftest1.copy().reset_index() 

    xxa = xxy.copy() 

    xxa['H1'] = 'LA' 


    xxa['OGOR'] = (pd.to_numeric(xxa.index)+1).astype(str).str.zfill(4) 

 
 

    xxa['O'] = 'A' 

    xxa['LETTER NAME'] = xxa['Well Name(s)'].str.extract('(\D+)') 

    xxa['WAPITI OPERATING LLC'] = xxa['Well Name(s)'].str.extract('(.\d.*)') 

    xxa['11'] = '' 

    xxa['12'] = '' 

    xxa = xxa[['H1', 'OGOR', 'O', 'API #', 'Prod Int', 'WAPITI OPERATING LLC', 'Well Status', 'Days Produced', 'Oil Production', 'Gas Production', 'Water Production', 'Injection Volume', '12']] 

     

    ## PART B 

     

    xxb = pd.DataFrame(columns = ['H1', 'OGOR', 'O', 'API #', 'Prod Int', 'WAPITI OPERATING LLC', 'Well Status', 'Days Produced', 'Oil Production', 'Gas Production', 'Water Production', 'Injection Volume', '12'],  

                       index=range(4)) #SO 4 AS DEFAULT,... HOW TO REMOVE?  TRY 1 AND TEST T1 ON 78433 

 
 

    xxb['H1'] = 'LB' 

     



     

    xxb['O'] = 'A' 

 
 

    xxb.iat[-4,3]='17' 

    xxb.iat[-3,3]='10' 

    xxb.iat[-2,3]='01' 

    xxb.iat[-1,3]='20' 



     

    xxb.iat[0, 10] = dftest1['Water Production'].sum() 

    xxb.iat[1, 8] = dftest1['Oil Production'].sum() 

    xxb.iat[2, 7] = dftest1['Gas Sales BTU'].sum() 

    xxb.iat[2, 9] = dftest1['Gas Sales'].sum() 

    xxb.iat[3, 9] = dftest1['Gas Lease Use'].sum() 

     



    xxb = xxb.loc[~(xxb==0).any(axis=1)]

     

    xxb['OGOR'] = (2001 + np.arange(len(xxb))).astype(str) 

   

    xxb = xxb.fillna('') 

     

    ## PART C  

    xxc = pd.DataFrame(columns = ['H1', 'OGOR', 'O', 'API #', 'Prod Int', 'WAPITI OPERATING LLC', 'Well Status', 'Days Produced', 'Oil Production', 'Gas Production', 'Water Production', 'Injection Volume', '12'], index=range(3)) 

    xxc['H1'] = 'LC' 

    xxc['OGOR'] = '3001' 

    xxc['O'] = 'A' 



    xxc.iat[0,3] = dftest1.iloc[0, -1] 

    

     


    dftestgrav = dftest1.copy() 

    dftestgrav['Oil Gravity'] = dftestgrav['Oil Gravity'].replace(0, np.nan) 

    xxc.iat[0, 6] = str(round(10*dftestgrav['Oil Gravity'].sum(),0))[:-2] 


     

    xxc.iat[0, 7] = dftest1['Open Stock'].sum() 

    xxc.iat[0, 8] = dftest1['Oil Production'].sum() 

    xxc.iat[0, 9] = dftest1['Oil Sales'].sum() 

     


     

    xxc.iat[0, 12] = dftest1['Close Stock'].sum() 

     

     

     

    xxc.iat[1, 0] = 'T1' 

     


    xxc.iat[1, 1] = len(pd.concat([xxa, xxb]))+1 

    xxc.iat[1, 2] = 'CHARLIE NYE' 

    xxc.iat[1, 3] = '7133658546' 

    xxc.iat[1, 5] = dt.date.today().strftime(format=('%m%d%Y')).zfill(6)

    xxc.iat[2, 0] = 'TR' 

    xxc.iat[2, 1] = '1' 

    xxc.iat[2, 2] = '' 

    xxc = xxc.fillna('') 

     

 
 

     



    xxy = pd.concat([xxa, xxb, xxc]) 

    col_name_1 = ['H1', 'OGOR', 'O', dftest1.iat[0,0][5:7]+dftest1.iat[0,0][:4], 'K4006', 'WAPITI OPERATING LLC', '', "".join(re.split("[^a-zA-Z]*", dftest1.iat[0,3])), dftest1.iat[0,1], dftest1.iat[0,2], '', '', ''] 

    xxy.columns = col_name_1 

     

    xxy.to_csv(f"{i}_{outputmonth}.csv", index=False) 

     

 from os import walk
from pathlib import PurePath
for path, subdirs, files in walk('.'):
    for name in files:
        print(PurePath(path, name))


filenames = os.listdir('/hex')
with open('hex.csv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)