import json

mylist = [1,2,3]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print('List :', json.dumps(mylist))
# print('Type :', type(json.dumps(mylist)))
print('Matrix :', json.dumps(matrix, indent=2))