#Operator    meaning         Desc
#1.and       Logical AND    True only if the both operands are true
#2.or        Logical OR     True if at least one of the operands is True
#3.not       Logical NOT    True if the operand is False and vice-versa

t,t1,f,f1=True,True,False,False

print(t and f)
print(t and t)
print(f and f)


print(t or f)
print(t or t)
print(f or f)

print(not t)
print(not f)
