def decodePair(a,b,dictdecode):
    dictdecode[a]=b

def decodeString(stringIn,dictdecode):
    decodedString=''
    for i in stringIn:
        if i in dictdecode:
            decodedString+=dictdecode[i]
        else:
            decodedString+=i
    return decodedString

dict_decode={}            
print("Enter the string you want to decode: ")
codedString=input()
while True:
    print("write a pair:")
    a=input()
    b=input()
    decodePair(a,b,dict_decode)
    decodedString=decodeString(codedString,dict_decode)
    print(decodedString)
