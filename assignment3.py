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

def reverse(a, b):
    k = b + 1
    l=[]
    for num in range(a, k):
        l.append(num)
    return l


print(reverse(-10, -1))





