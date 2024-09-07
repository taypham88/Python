
v1 = 9
v2 = 9
carry = 0

val = v1 + v2 + carry
carry = val // 10
val = val % 10

print(val, carry)