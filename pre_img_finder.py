from functools import partial

def power_mod_function(base, mod, x):
    return (base ** x) % mod


def get_a(b):
    '''
    Get preimage a from A for f(a) = b where b in B
    '''
    a = 1
    while(1):
        # print(F'a:{a}, b{b}')
        x = pow(3, a) % 17
        # print(F'x:{x}')
        if x == b:
            return a
        if a > 10000:
            return -1
        a += 1

def get_a_parametric(b, base, mod):
    '''
    Get preimage a from A for f(a) = b where b in B
    '''
    a = 1
    while(1):
        # print(F'a:{a}, b{b}')
        x = pow(base, a) % mod
        # print(F'x:{x}')
        if x == b:
            return a
        if a > 10000:
            return -1
        a += 1


def get_a_dynamic(b, func):
    '''
    Get preimage a from A for f(a) = b where b in B by using a passed in function
    '''
    for a in range(10001):
        if func(a) == b:
            return a
    return -1


def main():
    b = 7
    a = get_a(7)
    print(F'The preimage a of b={b} is: {a}')
    a = get_a_parametric(7, 3, 17)
    print(F'Again, the preimage a of b={b} is: {a}')
    a = get_a_dynamic(7, partial(power_mod_function, 3, 17))
    print(F'Again, the preimage a of b={b} is: {a}')


if __name__ == '__main__':
    main()
