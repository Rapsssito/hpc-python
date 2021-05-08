import numpy as np

rand = np.random.rand(4,4)

print(rand)
print(rand[1])
print(rand[:,2])
rand[:2,:2] = 0.21
print(rand)


cheq = np.zeros((8,8))
cheq[::2,::2] = 1
cheq[1::2,1::2] = 1
print(cheq)
