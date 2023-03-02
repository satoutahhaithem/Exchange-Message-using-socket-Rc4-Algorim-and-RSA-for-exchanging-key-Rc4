import random
import math


def generate_large_prime():
    """
    Generates a random prime number between 100 and 1000 (inclusive).
    """
    while True:
        num = random.randint(100, 256)
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return num
# generating the the two prime number 
p=generate_large_prime()
q=generate_large_prime()
# print("The p is ",p," The q is ",q)
# the first part of our public key
n=p*q
# calculate phi_n (q-1)*(p-1)
phi_n=(q-1)*(p-1)
# we choose number 1<e<ph_n such gcd(e,ph_n)=1
def get_second_part_public_key(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if math.gcd(e, phi_n) == 1:
            return e

e = get_second_part_public_key(phi_n)
# print ("The public key first part is ",n," the second part ",e)
def inverse_modulaire(a,m):
    for i in range (1,m):
        if ( a * i) % m ==1:
            return i
    return None
d=inverse_modulaire(e,phi_n)
# print ("the private key ",d)

def convertToInt(myStr):
    myStrInt=[ord(c) for c in myStr]
    return myStrInt

def convertToStr(myStrInt):
    myStr=[chr(c) for c in myStrInt]
    return myStr

def appendArrayStr(arrStr):
    return ''.join(arrStr)

def encrypt(m, e, n):
    EncryptedArray=[]
    messageConvertedToInt=convertToInt(m)
    for i in messageConvertedToInt:
        EncryptedArray.append(pow(i, e, n))
    return EncryptedArray
def decrypt(c, d, n):
    plainInt=[]
    for i in c :
        plainInt.append(pow(i, d, n))
    plainText=''.join(convertToStr(plainInt))
    return plainText
def arrayIntToFullText(arrayInt):
    arrayCipherText=convertToStr(arrayInt)
    cipherText=appendArrayStr(arrayCipherText)
    return cipherText



# message = input("Enter a message to transfer ")
# messageInt=convertToInt(message)
# print ("the message int is ",messageInt)
# cipherInt = encrypt("TheMessage", e, n)
# print ("the cypher Int",cipherInt)




# plainInt = decrypt(cipherInt, d, n)
# print("the plain Int",plainInt)
# plainText=''.join(convertToStr(plainInt))
# print ("the plain text is ",decrypt(cipherInt,d,n))


# exec(open('Rc4.py').read()) 




