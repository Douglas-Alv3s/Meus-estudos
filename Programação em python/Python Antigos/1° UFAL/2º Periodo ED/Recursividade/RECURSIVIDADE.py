
def fat(n):
    if n == 0:
        return 1
    else:
        return n*fat(n-1)

fatorial = fat(5)

print(fatorial)

# 5*4! = 4*3*2*1
# 4*3! = 3*2*1
# 3*2! = 2*1 
# 1*1! = 1

