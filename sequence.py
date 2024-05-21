#List


# students = ['musa','ibramim','abdullahi','muhammad']

# state = ['kano','kaduna','kogi','kwara','jigawa','lagos']

# state.extend(students)
# state.remove('kogi')
# state.pop(0)
# state[1] = 'imo'
# state[2:6]=['edo','bauchi','jos','ondo']

# state.append('sokoto')
# state.insert(2,'zamfara')

# print(state)

# print(len(state))
# print(type(state))

# print(state[0])
# print(state[1])
# print(state[2:4])

# tuple

# region = ('kano','kaduna','kogi','kwara','jigawa','lagos')

# print(region)


# set

zone = {'kano','kaduna','kogi','kwara','jigawa','lagos'}
names = ['musa','ibramim','abdullahi','muhammad']

zone.add('katsina')
zone.update(names)
print(zone)


#Dictionary

munzaly = {
    'name' : 'munzali',
    'school': 'maaun',
    'hostel': 'nabayan school',
    'department': 'computer science',
    'favourite color': 'blue',
    'level':300,
    'wife':'amina'
    }
x = munzaly.get('department')
x = munzaly.keys()
x = munzaly.values()

# print(munzaly['name'])
# print(len(munzaly))
# print(type(munzaly))
