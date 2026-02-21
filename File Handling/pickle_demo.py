import pickle

data = [1,2,3,4,5,6]

with open("pickle.pkl","wb") as f:
    pickle.dump(data,f)


with open("pickle.pkl","rb") as f:
    x = pickle.load(f)

print(x)