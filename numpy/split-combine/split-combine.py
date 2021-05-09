import numpy as np

cheq = np.zeros((8,8))
cheq[::2,::2] = 1
cheq[1::2,1::2] = 1
print(cheq)

cheq_split = np.split(cheq, 2)
print(cheq_split[0])
print(cheq_split[1])

cheq = np.concatenate(cheq_split)
print(cheq)


cheq_split = np.split(cheq, 2, axis=1)
print(cheq_split[0])
print(cheq_split[1])

cheq = np.concatenate(cheq_split, axis=1)
print(cheq)
