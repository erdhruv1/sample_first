s = "hello   world  lol"
a = ' '.join(map(lambda s: s[0].upper()+s[1:] if len(s) > 0 else '', s.split(' ')))
print(a)
# newStr = ""
# for i in range(len(a)):
#     if i==0:
#         newStr = a[i].capitalize()
#     else:
#         newStr = newStr + ' ' + a[i].capitalize()
#
# print(newStr)