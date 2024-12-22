import pickle

name = 'Мухаммад'
age = 27
lst = ['яблоко', "апельсин", "огурчик", "манты"]

with open('bin.dat', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(lst, file)

with open('bin.dat', 'rb') as file:
    data1 = pickle.load(file)
    data2 = pickle.load(file)
    data3 = pickle.load(file)

print(data1)
print(data2)
print(data3)