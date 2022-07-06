# import sage library
#coding:utf-8
from sage.all_cmdline import *
import socket

# sagemath high level variables
_sage_const_42 = Integer(42)
_sage_const_27 = Integer(27)
_sage_const_1026 = Integer(1026)
_sage_const_150000 = Integer(150000)
_sage_const_10000 = Integer(10000)
_sage_const_1 = Integer(1)
_sage_const_2 = Integer(2)
_sage_const_0 = Integer(0)

# dghv var
var_lambda = _sage_const_42
rho = _sage_const_27
eta = _sage_const_1026
gamma = _sage_const_150000
tau = _sage_const_10000
alpha = _sage_const_1
rho1 = rho + alpha


def keyGen():
    " keyGen "
    p = random_prime(_sage_const_2 ** (eta+_sage_const_1),
                     proof=False, lbound=_sage_const_2 ** eta)

    init_val = _sage_const_0
    se = initial_seed()
    set_random_seed(se)
    list_chi = [ZZ.random_element(_sage_const_2 ** gamma) for i in range(tau)]
    list_xi = [ZZ.random_element(
        (_sage_const_2 ** (var_lambda+eta))//p) for i in range(tau)]
    list_r = [ZZ.random_element(-_sage_const_2 ** rho +
                                _sage_const_1, _sage_const_2 ** rho) for i in range(tau)]
    list_delta = [init_val for i in range(tau)]
    for i in range(tau):
        list_delta[i] = (list_chi[i] % p) + list_xi[i] * p - list_r[i]

    q0 = ZZ.random_element(_sage_const_2 ** gamma // p)
    x0 = q0 * p

    pk = [se, x0, list_delta]
    sk = p

    return pk, sk


def encrypt(pk, m):
    " encrypt "
    c = m

    x0 = pk[_sage_const_1]
    se = pk[_sage_const_0]
    set_random_seed(se)
    list_chi = [ZZ.random_element(_sage_const_2 ** gamma) for i in range(tau)]
    for i in range(tau):
        b_i = ZZ.random_element(_sage_const_2 ** alpha)  # TODO
        x_i = list_chi[i] - pk[_sage_const_2][i]
        c = (c + _sage_const_2 * b_i * x_i) % x0

    r = ZZ.random_element(-_sage_const_2 ** rho1 +
                          _sage_const_1, _sage_const_2 ** rho1)
    c = (c + _sage_const_2 * r) % x0

    # print c
    return c


"""
def evaluate(pk, c, c_list):
"""


def decrypt(sk, c):
    return (c % sk) % _sage_const_2


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    
    
    pk, sk = keyGen()
    m0 = _sage_const_0
    c0 = encrypt(pk, m0)
    m0_dec = decrypt(sk, c0)
    m1 = _sage_const_1
    c1 = encrypt(pk, m1)
    m1_dec = decrypt(sk, c1)

    #print("m0_dec == m0:", m0_dec == m0)
    #print("m1_dec == m1:", m1_dec == m1)

    #print("dec(enc(0) + enc(0)) =", decrypt(sk, c0 + c0))
    #print("dec(enc(0) + enc(1)) =", decrypt(sk, c0 + c1))
    #print("dec(enc(1) + enc(0)) =", decrypt(sk, c1 + c0))
    #print("dec(enc(1) + enc(1)) =", decrypt(sk, c1 + c1))

    #print("dec(enc(0) * enc(0)) =", decrypt(sk, c0 * c0))
    #print("dec(enc(0) * enc(1)) =", decrypt(sk, c0 * c1))
    #print("dec(enc(1) * enc(0)) =", decrypt(sk, c1 * c0))
    #print("dec(enc(1) * enc(1)) =", decrypt(sk, c1 * c1))

    #print("dec(enc(1) * enc(1)) + enc(0) * (enc(1) + enc(1)) =",
         # decrypt(sk, c1 * c1 + c0 * (c1 + c1)))
    #print("dec(enc(0) * enc(1)) + enc(0) * (enc(1) + enc(1)) =",
          #decrypt(sk, c0 * c1 + c0 * (c1 + c1)))
    #print("dec((enc(0) * enc(1) + enc(1) + enc(0)) * enc(1) * enc(0) * ",
          #"(enc(1) + enc(1))) =",
          #decrypt(sk, (c0 * c1 + c1 + c0) * c1 * c0 * (c1 + c1)))
    msg = s.recv(50)
    print("Le serveur a envoyé : "+msg.decode("utf-8"))# recevoir un message de puis le serveur
    s.send(b"Bonjour Mr serveur!") # envoi de message vers le serveur

if __name__ == "__main__":
    main()
