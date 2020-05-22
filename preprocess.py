import numpy as np
import os
#import tensorflow as tf
import unicodedata
import re
import numpy as np
def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    w = re.sub(r"[^a-zA-Z?.!,]+", " ", w)
    w = w.rstrip().strip()
    w = '<start> ' + w + ' <end>'
    return w

ds_path='/home/al/Downloads/lines/lines-a'
csv_path="/home/al/Desktop/nnfl final/nds-a"
i=0
nds=np.array([])
for e  in 'a':
    print(2600000*i)
    for f  in 'a':
        if e+f=='pg':
            break
        ds = np.loadtxt(ds_path+e+f,delimiter='\n',dtype='str',encoding='bytes')
        nds=np.array(list( map(preprocess_sentence,ds)))
        np.savetxt(csv_path+e+f+".csv",nds,delimiter="\t",fmt='%s')
    i+=1
print('\n\n\n\ndone')
