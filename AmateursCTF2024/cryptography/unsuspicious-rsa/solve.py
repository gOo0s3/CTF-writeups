from Crypto.Util.number import inverse, long_to_bytes, isPrime
from math import isqrt, factorial

def nextPrime(p, n):
    p += (n - p) % n
    p += 1
    iters = 0
    while not isPrime(p):
        p += n
    return p

N = 172391551927761576067659307357620721422739678820495774305873584621252712399496576196263035396006999836369799931266873378023097609967946749267124740589901094349829053978388042817025552765214268699484300142561454883219890142913389461801693414623922253012031301348707811702687094437054617108593289186399175149061
e = 65537
c = 128185847052386409377183184214572579042527531775256727031562496105460578259228314918798269412725873626743107842431605023962700973103340370786679287012472752872015208333991822872782385473020628386447897357839507808287989016150724816091476582807745318701830009449343823207792128099226593723498556813015444306241

q = nextPrime(isqrt(N), factorial(90))
p = N//q

assert N == p*q, "wrong p or wrong q"

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,N)

print(long_to_bytes(m).decode())