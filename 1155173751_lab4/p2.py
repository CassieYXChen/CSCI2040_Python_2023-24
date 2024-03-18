from functools import reduce

vehicle_dict = {
"Sedan": 1500,
"SUV": 2000,
"Pickup": 3000,
"Minivan": 1600,
"Van": 2400,
"Semi": 13600,
"Bicycle": 7,
"Motorcycle": 110,
}

fruit = [{"apple": 10, "pear": 20, "banana": 30, "strawberry": 50},
{"apple": 12, "pear": 5, "banana": 20, "strawberry": 5},
{"apple": 15, "pear": 26, "banana": 32, "strawberry": 8}]

list1 = list(map(lambda x: 2 ** x, range(1, 12)))
list2 = list(map(lambda x: x % 3, range(1, 12)))
list3 = [x for x in range(1, 20) if x % 2 == 1]
list4 = [x for x in range(1, 20) if x in [y**2 for y in range(1, int(x**0.5)+1)]]
list5 = [x if x >= 0 else 0 for x in range(-5, 6) ]
list6 = [i.upper() for i in vehicle_dict.keys() if vehicle_dict[i] < 2500]
list7 = [' '.join([f'{i}*{j}={i*j}' for j in range(1, i+1)]) for i in range(1, 10)]
dict1 = reduce(lambda x, y: {key: float(x.get(key, 0)) + float(y[key]) for key in x.keys()}, fruit)
