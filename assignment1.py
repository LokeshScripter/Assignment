

string = str(input("please write a scentence to be displayed : "))
even_index = []
p = len(string)
for i in range(p):
    if i % 2 == 0 :
        even_index += string[i]
print(even_index)








