def convertToInt(myStr):
    myStrInt=[ord(c) for c in myStr]
    return myStrInt
def xor(a, b):
    return a ^ b
def generator(k):
    if (len(k)<5 or len(k)>256):
        print ("you need to write key between 5 and 256")
        return 
    S=[]
    for i in range(0,256):
        S.append(i)
    j=0
    key=convertToInt(k)
    for i in range(0,256):
        j=(j+S[i]+key[i % len(key)])% 256
        S [i],S[j] =S[j],S[i]
    return S
def convertMessageRc4(cle ,mess):
    i=0
    j=0
    EncMess=[]
    S=generator(cle)
    messInt=convertToInt(mess)
    for charMess in messInt:
        i=(i + 1)% 256
        j=(j + S[i])%256
        S[i] , S[j] = S[j] ,S[i]
        octecChif = S[ ( S[i] + S[j] ) % 256]
        result = octecChif ^ charMess
        EncMess.append(result)
    arrChar=[]
    str=""
    for m in EncMess:
        arrChar.append(chr(m))
    str=''.join(arrChar)
    return str




# theKey=input("Enter the to key to code with Rc4 :")
# mess=input("Enter the message :")
# cipherText=convertMessageRc4(theKey,mess)

# # print ("The cipher text ",cipherText)

# # print ("the dechiffrement is ",convertMessageRc4(theKey,cipherText))









         