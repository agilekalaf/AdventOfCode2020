list = [0,1,2,3,4,5,6,7,8,9,10]

a = 0
b = 1
c = 2
x = (list[a],list[b],list[c])
print(sum(x))

print(len(list))

for a in list:
  while b < len(list):
    while c < len(list):
      if(x == 5261):
        print(list[a], list[b], list[c], "hit")
        break
      else:
        print(list[a],list[b],list[c])
        c += 1
    c = 2
    b += 1
  a += 1
  b = 1