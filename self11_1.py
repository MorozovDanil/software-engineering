def fib(n):
  f_n, f_n1 = 1, 1
  for i in range(n):
      yield f_n
      f_n, f_n1 = f_n1, f_n1 + f_n

n = 321
f_list = list(fib(n))
print(f_list[-1])