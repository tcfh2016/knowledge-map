import numpy as np
import pickle
from random import gauss

a = [gauss(1.5, 2) for i in range(1000000)]

pkl_file = open('data.pkl', 'wb')
pickle.dump(a, pkl_file)
pkl_file.close()

pkl_file = open('data.pkl', 'rb')
file_content = pickle.load(pkl_file)
print(file_content[:5])
pkl_file.close()
