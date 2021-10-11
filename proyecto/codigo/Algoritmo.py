import pandas as pd
import glob
import numpy as np
import math
from PIL import Image
import os
import os.path

path = r'..\csv\enfermo_csv'  # aqui va el path de los csv
all_files = glob.glob(path + "/*.csv")
def resize_nerghbor(src_data, dst_height, dst_width):
      ori_height, ori_width = src_data.shape
      ratio_height = ori_height / dst_height
      ratio_width = ori_width / dst_width
      dst_data = np.zeros((dst_height, dst_width), np.uint8)

      for y in range(dst_height):
          for x in range(dst_width):
              x_ori = int(x * ratio_width)
              y_ori = int(y * ratio_height)          #Redondeo
              dst_data[y, x] = src_data[y_ori, x_ori]
      return dst_data
i=1
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)

    #l=np.asarray(df)
    l=np.array(df)
    print(l)
          
    c=l.shape[0]
    d=l.shape[1]
    n = resize_nerghbor(l,c-90,d-90)
    
    dataf=pd.DataFrame(n) 
    
    tes=str(i)
    p="data"+tes+".csv"
    i+=1
    s=dataf.to_csv("results\\" + p)
    
    
'''
            Autores
    Miguel Ángel Chacón López
    Luisa María García Salazar
'''
    

