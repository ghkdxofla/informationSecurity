
# coding: utf-8

# In[9]:

class MathTool:
    #Extended euclid algorithm
    def eea(self, a, b):
        

        A = [1, 0, a]
        B = [0, 1, b]
        T = [0, 0, 0]
        while 1:
            if B[2] == 0:
                # no inverse
                return 0
            if B[2] == 1:
                #found inverse
                return B[1]
            q = A[2] // B[2]
            T = [A[0] - (q * B[0]), A[1] - (q * B[1]), A[2] - (q * B[2])]
            A = B
            B = T    
    #GCD
    def gcd(self, a, b):
        while b != 0:
            temp = a % b
            a = b
            b = temp
        return abs(self.a)
    
    #Square and Multiplication
    def squAndMul(self, b, e, m):
        binExp = []
        while e != 0:
            binExp.append(e % 2)
            e = e // 2

        result = 1
        binExp.reverse()
        for i in binExp:
            if i == 0:
                result = (result * result) % m
            else:
                result = (result * result * b) % m
        return result
    #Prime Factorization
    def primeFac(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors


# In[2]:

class RSA:
    def __init__(self, c, e, p, q):
        self.c = c
        self.e = e
        self.p = p
        self.q = q
        
    def decrypt(self):
        #n은 prime factorization을 통해 p, q 구한다
        mt = MathTool()
        pi_n = (self.p - 1) * (self.q - 1)
        d = mt.eea(pi_n, self.e)
        if d<0:
            d = d + pi_n
        #decrypt
        m = mt.squAndMul(self.c, d, (self.p * self.q))
        return m


# In[3]:

class ElGamal:
    
    def __init__(self, Ya, a, q, c1, c2):
        self.Ya = Ya
        self.a = a
        self.q = q
        self.c1 = c1
        self.c2 = c2
        
    def find_Xa(self):
        mt = MathTool()
        Xa = 1
        original = mt.squAndMul(self.a, Xa, self.q)
        findKey = mt.squAndMul(self.a, Xa, self.q)
        while self.Ya!=findKey:
            findKey= (findKey * original) % self.q
            Xa += 1
            
        return Xa
    def decrypt(self, Xa):
        mt = MathTool()
        #recover K

        #self.Ya = self.a**Xa % self.q
        #K = c1**Xa % q
        k = mt.squAndMul(self.c1, Xa, self.q)
        
        k_inv = mt.eea(self.q, k)
        m = self.c2 * k_inv % self.q
        return m
        
        
    

"""
# In[4]:

#Prime Factorization
import time
start = time.time()
print(MathTool().primeFac(18444164967047483891))
end = (time.time() - start) / 60
print(end)
#[4294404461, 4294929631]




# In[10]:

#Answer for problem 1
rsa = RSA(21, 29, 4294404461, 4294929631)
rsa.decrypt()


# In[11]:

#Sample test1
rsa = RSA(3540, 29, 4294404461, 4294929631)
rsa.decrypt()


# In[12]:

#Sample test2
rsa = RSA(173, 29, 4294404461, 4294929631)
rsa.decrypt()


# In[16]:

#ElGamal Xa
import time
elg = ElGamal(22, 43, 1605333871, 187341129, 881954783)
start = time.time()
print(elg.find_Xa())
end = (time.time() - start) / 60
print(end)


# In[13]:

#Answer for problem 2
elg = ElGamal(22, 43, 1605333871, 187341129, 881954783)
elg.decrypt(1463159957)


# In[14]:

#Sample test1
elg = ElGamal(22, 43, 1605333871, 187341129, 50696994)
elg.decrypt(1463159957)


# In[15]:

#Sample test2
elg = ElGamal(22, 43, 1605333871, 187341129, 1212049520)
elg.decrypt(1463159957)


# In[ ]:
"""
if __name__ == '__main__':
    import time
    start = time.time()
    prime = MathTool().primeFac(18444164967047483891)
    print("Prime Factorization n. result is p = {0}, q = {1}".format(prime[0], prime[1]))
    end = (time.time() - start) / 60
    print("time for calculation(second) : {0}".format(end))
    
    rsa = RSA(21, 29, prime[0], prime[1])
    print("problem 1 answer : {0}".format(rsa.decrypt()))
    
    elg = ElGamal(22, 43, 1605333871, 187341129, 881954783)
    start = time.time()
    Xa = elg.find_Xa()
    print("ElGamal Xa : {0}".format(Xa))
    end = (time.time() - start) / 60
    print("time for calculation(second) : {0}".format(end))
    print("problem 2 answer : {0}".format(elg.decrypt(Xa)))

    input()

