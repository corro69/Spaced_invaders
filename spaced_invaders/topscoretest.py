import pickle
import os

x = 100

topscore_save = int(x)
pickle_out = open("topscore.dat","wb")
pickle.dump(topscore_save, pickle_out)
pickle_out.close()

#topscore_save.remove()

#pickle_in = open("topscore.dat", "rb")
#topscore_save = pickle.load(pickle_in)

print(topscore_save)
#print(topscore_save[1])