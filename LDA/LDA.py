from scipy.io import arff
import pandas as pd


# dataset from https://archive.ics.uci.edu/ml/datasets/EEG+Eye+State#
data_fn="./LDA/EEG_Dataset.arff"
data = arff.loadarff(data_fn)
df=pd.DataFrame(data[0])

