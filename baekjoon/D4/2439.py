N = int(input())
star = ""
for i in range(1,N+1):
    for k in range(1,N-i+1):
        star += " "
    for j in range(1,i+1):
        star += "*"
    print(star)
    star =""