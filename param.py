base=int(input("Enter base: "))
res=int(input("Enter NUM value: "))
print(" base: %d  RESULT: %d"%( base ,res))

num = 1
power =0

while num < res:
    num *= base
    power += 1

print("POWER IS:", power)   
