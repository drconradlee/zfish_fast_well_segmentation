from tqdm import tqdm
import numpy as np

a = []
for i in tqdm(np.arange(100)):
    a.append(i)
    