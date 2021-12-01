import pandas as pd
import os
import numpy as np
train_name = []
test_name = []
val_name = []
img_path = '/Users/Dong/Desktop/dataPath_new/data'
for root, dirs, filenames in os.walk(img_path):
    for filename in filenames:
        if '.jpg' in filename:
            if 'train' in root:
                train_name.append(filename)
            elif 'test' in root:
                test_name.append(filename)
            elif 'val' in root:
                val_name.append(filename)
            else:
                print("there is something wrong", filename)
        else:
            pass
        # print("it is not a jpg file.", filename)


train_name = np.array(train_name)
test_name = np.array(test_name)
val_name = np.array(val_name)

train_name_reshape = train_name.T
test_name_reshape = test_name.T
val_name_reshape = val_name.T

train_name_csv = pd.DataFrame(train_name_reshape)
test_name_csv  = pd.DataFrame(test_name_reshape)
val_name_csv   = pd.DataFrame(val_name_reshape)

train_name_csv.to_csv('/Users/Dong/Desktop/dataPath_new/data/train_name.csv')
test_name_csv .to_csv('/Users/Dong/Desktop/dataPath_new/data/test_name.csv')
val_name_csv  .to_csv('/Users/Dong/Desktop/dataPath_new/data/val_name.csv')


