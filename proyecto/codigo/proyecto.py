import pandas as pd
import glob

path=r'C:\Users\Pc\Desktop\Proyecto\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv' #aqui va el path de los csv
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    
frame = pd.concat(li, axis=0, ignore_index=True)

