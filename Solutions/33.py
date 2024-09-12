n = int(input('Number:'))

ed = od =''

while(n>0):
    ld = n%10
    if ld%2==0:
        ed=ed+str(ld)
    else:
        od=od+str(ld)
    n=n//10

print(od+ed)