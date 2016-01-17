
# coding: utf-8

# In[51]:

import pandas as pd
import numpy as np

data = pd.read_csv(open('profile.csv'))
print(data)
print(data.columns)

#converting to numpy array
numbofpts=data.as_matrix([data.columns])
numbofpts[:,2]

#finding avg age
numbofpts[:,2].mean()

avg_open=numbofpts[:,4].mean()
avg_con=numbofpts[:,5].mean()
avg_ext=numbofpts[:,6].mean()
avg_agr=numbofpts[:,7].mean()
avg_neu=numbofpts[:,8].mean()
gender_ratio=numbofpts[:,3].mean()
print("ratio")
print(gender_ratio)
if gender_ratio>0.5:
    gender=1
else:
    gender=0

print(gender)

output_data=data
del output_data['age']
output_data.insert(2, 'age','25-34')
output_data['gender']=gender
output_data['ope']=avg_open
output_data['con']=avg_con
output_data['ext']=avg_ext
output_data['agr']=avg_agr
output_data['neu']=avg_neu
output_data

