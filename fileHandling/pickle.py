import pickle

lst = ['a','b','c','d']
with open("file.txt","wb") as f:
    pickle.dump(lst, f)