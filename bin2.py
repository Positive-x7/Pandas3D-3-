# import pickle

# lst_names = ['Дени', "Мансур", "Мухаммад", "Тамерлан", "Сафия", "Сайфулла", 'Иса', "Муса"]

# with open('bin2.dat', 'wb') as file:
#     pickle.dump(len(lst_names), file)
#     for name in lst_names:
#         pickle.dump(name, file)

# with open('bin2.dat', 'rb') as file:
#     length = pickle.load(file)
#     for i in range(length):
#         print(pickle.load(file))


lst = []

lst.append('Амирхан')
lst.append(555)
lst.insert('Мустафа', 0)
print(lst)