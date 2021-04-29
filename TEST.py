# def solution(V):
#     x = y = 0
#     if V[0][0] == V[1][0]:
#         x = V[2][0]
#     elif V[0][0] == V[2][0]:
#         x = V[1][0]
#     else:
#         x = V[0][0]
#
#     if V[0][1] == V[1][1]:
#         y = V[2][1]
#     elif V[0][1] == V[2][1]:
#         y = V[1][1]
#     else:
#         y = V[0][1]
#     return [x, y]
#
# print(solution([[1,4],[3,4],[3,10]]))
# print(solution([[1,1],[2,2],[1,2]]))
#
#
#
# def solution(V):
#     checkX = {}
#     checkY = {}
#     for i in range(len(V)):
#         if V[i][0] in checkX:
#             checkX[V[i][0]] += 1
#         else:
#             checkX[V[i][0]] = 1
#         if V[i][1] in checkY:
#             checkY[V[i][1]] += 1
#         else:
#             checkY[V[i][1]] = 1
#
#     result = [0,0]
#     for i in checkX:
#         if checkX[i] % 2 != 0:
#             result[0] = i
#     for i in checkY:
#         if checkY[i] % 2 != 0:
#             result[1] = i
#     return result
# print(solution([[1,4],[3,4],[3,10]]))
# print(solution([[1,1],[2,2],[1,2]]))
#
# def solution(V):
#     resultX = []
#     resultY = []
#     for i in range(len(V)):
#         if V[i][0] not in resultX:
#             resultX.append(V[i][0])
#         else:
#             for j in range(len(resultX)):
#                 if V[i][0] == resultX[j]:
#                     del resultX[j]
#                     break
#         if V[i][1] not in resultY:
#             resultY.append(V[i][1])
#         else:
#             for j in range(len(resultY)):
#                 if V[i][1] == resultY[j]:
#                     del resultY[j]
#                     break
#
#     return resultX+resultY
#
# print(solution([[1,4],[3,4],[3,10]]))
# print(solution([[1,1],[2,2],[1,2]]))

# a = "abc"
# for i in range(len(a)):
#     if i == 1:
#         a = a[:i]+"f"+a[i:]
# print(a)

# cat = """
# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
# """


