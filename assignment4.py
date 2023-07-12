# path = "C:/Users/lgowda/Desktop/ASI.txt"
# file = open(path, "r")
# text = file.readlines()
# new_file_output= open("new file","w")
# for line in text:
#
#     if line.strip() == "5.FIVE":
#         continue
#     new_file_output.write(line)

# def filter(l):
#     p = []
#     for char in l:
#         if type(char) != str:
#             p.append(char)
#     return p
#
# def duplicater(l):
#     new = ""
#     output = ""
#     for char in l:
#
#         if char != new:
#             print("(")
#         elif char == new:
#             print(")")
#         new = char
#
#
# j = "appaa"
#
# print(duplicater(j), end="")

# def reverse(a, b):
#     k = b + 1
#     l=[]
#     for num in range(a, k):
#         l.append(num)
#     return l
#
#
# print(reverse(-10, -1))
# data = [0, 9, 2, 3]
#
#
# def maximum(data):
#     l = 0
#     for num in data:
#         if num > l:
#             l = num
#     print(l)
#
#
# def greet(func):
#
#     def wrapper():
#         print("im first")
#         k = func()
#
#         print("im last")
#         return k
#     return wrapper()
#
#
#
#

def calculate_maximum(data):
    l = 0
    for num in data:
        if num > l:
            l = num
    return l


@pytest.mark.new
@pytest.mark.parametrize((("data","po","ho"),"j"), [((1, 3,5),7), ((1, 6, 9),7), (1, 7, 8), (1,6,8)])
def test_maximum(data):
    assert calculate_maximum(data) == max(data), "failed"