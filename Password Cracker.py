import hashlib

flag = 0
print("="*50)
print("\tPassword Cracker Using Python")
print("="*50)
paas_hash = input("enter your md5 hash : ")
wordlist = input("enter your file name : ")

try:
    paas_hash = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in paas_hash:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == paas_hash:
        print("password found")
        print("password is " + word)
        flag = 1
        break
if flag == 0:
    print("password/passphrase is not in the list")