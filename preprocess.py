import numpy as np
import os
#import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import unicodedata
import re
import numpy as np
import time

'''
notes
*******************
*taking top k words out of n will reduce chances of words like names entering the vocabulary

'''
###functions
# Converts the unicode file to ascii
def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ." 
    # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)
    
    w = w.rstrip().strip()
    
    # adding a start and an end token to the sentence
    # so that the model know when to start and stop predicting.
    w = '[CLS] ' + w + '[SEP]'
    return w



###code
ds_path='/home/al/Downloads/lines/lines-a'
csv_path="/home/al/Desktop/nnflproj/nds2/nds-a"
i=0
nds=np.array([])

for e  in 'abcdefghijklmnopqrstuvwxyz':
    print(2600000*i)
    for f  in 'abcdefghijklmnopqrstuvwxyz':
        
        if e+f=='pg':
            break
        
    
        ds = np.loadtxt(ds_path+e+f,delimiter='\n',dtype='str',encoding='bytes')
        nds=np.array(list( map(preprocess_sentence,ds)))
        np.savetxt(csv_path+e+f+".tsv",nds,delimiter="\t",fmt='%s')
    i+=1
print('done')


print('\n\n\n\ndone')
