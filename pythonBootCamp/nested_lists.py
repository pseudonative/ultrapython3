# coords=[[10.423,9.123], [37.212,-14.092], [21.367,32.572]]

# for loc in coords:
#     for coord in loc:
#         print(coord)


board=[[num for num in range(1,4)] for val in range(1,4)]
print(board)
print([["X" if num%2!=0 else "O" for num in range(1,4)] for val in range(1,4)])


[
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,8,9],
]
answer=[[i for i in range(0,10)] for num in range(0,8)]
print(answer)