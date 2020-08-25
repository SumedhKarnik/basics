#! /usr/bin/python3
import random

#recurssive calls
def fib(n):
    fib.ct += 1

    if n <= 1:
        return 1

    return fib(n-1) + fib(n-2)

#memoization
def fib_memo(n):
    if n in fib_memo.mem:
        return fib_memo.mem[n]

    fib_memo.ct += 1
    
    if n <= 1:
        out = 1
    else:
        out = fib_memo(n-1) + fib_memo(n-2)

    fib_memo.mem[n] = out
    return out 
    
#additive sequence
def fib_seq(n, b1, b2):
    fib_seq.ct += 1

    if n == 0:
        return b1
    
    ret = fib_seq (n-1, b2, b1+b2)
    b1, b2 = b2, ret

    return ret

#bottom-up (iterative)
def fib_bu(n):
    ret = b1 = 0
    b2 = 1

    for i in range(n):
        ret = b1 + b2
        b1, b2 = b2, ret

    return ret
    

def main():
    num = random.randint(3, 30)

    fib.ct = 0
    print(f"Recurrsive fib of {num} is {fib(num)} in {fib.ct} iterations")

    fib_memo.ct = 0
    fib_memo.mem = {}
    print(f"  Memoized fib of {num} is {fib_memo(num)} in {fib_memo.ct} iterations")

    fib_seq.ct = 0
    print(f"  Sequence fib of {num} is {fib_seq(num,1,1)} in {fib_seq.ct} iterations")

    print(f" Iterative fib of {num} is {fib_bu(num)} in {num} iterations")
    

if __name__ == "__main__":
    main()
