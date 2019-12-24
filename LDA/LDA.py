from scipy.io import arff
import pandas as pd
PATH='./LDA/'

# dataset from https://archive.ics.uci.edu/ml/datasets/EEG+Eye+State#
data_fn="EEG_Dataset.arff"
data = arff.loadarff(PATH+data_fn)
df=pd.DataFrame(data[0])

