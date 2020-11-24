def rec(x: int):
    if not isinstance(x, int):
        print(f'{x} MUST be integer')
        return
    
    if x == 0:
        print(f'{x} is equal to 0')
        return
    else:
        print(f'{x} ...')
        rec(x - 1)

rec(4)
rec('4')

def power(n: int, p: int):
    if not isinstance(n, int) or not isinstance(p, int):
        print(f'The arguments {n} and {p} MUST be integer')
        return
    
    if p == 0: return 1
    return n * power(n, p - 1)

print(power(1, 0))
print(power(1, 1))
print(power(2, 2))
print(power(2, 3))
print(power(2, 6))

def fact(n: int):
    if not isinstance(n, int):
        print(f'{n} MUST be integer')
        return
    
    if n == 0: return 1
    return n * fact(n - 1)

print(fact(5))

def efun(num):
  if num==0:
    return 1
  else:
    return num * efun(num-2)

print(efun(8))