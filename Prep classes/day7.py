
# # Find unique numbers exercise
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# unique = []
#
# my_list.sort()
#
# for i in range(len(my_list)-1):
#    if my_list[i] != my_list[i + 1]:
#        unique.append(my_list[i])
#
# if my_list[-2] != my_list[-1]:
#     unique.append(my_list[-1])
# else:
#     pass
#
# print('The list with unique elements only:')
# print(unique)
#
# ##but better:
# ##
# if __name__ == '__main__':
#     my_list = [1,2,4,4,1,4,2,6,2,9]
#     finish_list = []
#
#     for i in my_list:
#         if i not in finish_list:
#             finish_list.append(i)
#
# print(finish_list)

# EMPTY = "-"
# ROOK = "ROOK"
# board = []
#
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
#
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
#
# print(board)
# my_list = [0, 1, 2, 3]
# x=1
# for elem in my_list:
#     x *=elem
#     print(x)

# i=0
# while i<=3:
#     i+=2
#     print("*")

# var = 1
# while var<10:
# #    var += 1
# #    if var%2==0:
# #        continue
#     print("*")
#     var = var << 1

# t=[[3-i for i in range (3)] for j in range (3)]
# s=0
# for i in range (3):
#     s += t[i][i]
# print (s)

# a = 1
# b = 0
# c = a & b
# d = a | b
# e= a ^ b
# print (c+d+e)

# my_list = [[0, 1, 2, 3] for i in range (2)]
# print(my_list[2][0])

# my_list = [1, 2, 3, 4]
#
# print(my_list[-3:-2])

for i in range (1):
    print("*")
else:
    print("*")