def get_a(b):
  '''
  Get preimage a from A for f(a) = b where b in B
  '''
    a = 1
    while(1):
        print(F'a:{a}, b{b}')
        x = pow(3,a)%17
        print(F'x:{x}')
        if x == b:
            print(F'The preimage a of b={b} is: {a}')
            return a
        if a > 10000:
            return -1
        a +=1

a = geta(7)
