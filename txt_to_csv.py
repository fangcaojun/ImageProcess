import numpy as np  
import pandas as pd  
  
txt = np.loadtxt('/home/fangcaojun/Documents/Python/other/ImageProcess/VOC2007/ImageSets/Main/17.txt')  
txtDF = pd.DataFrame(txt)  
txtDF.to_csv('train.csv',index=False) 