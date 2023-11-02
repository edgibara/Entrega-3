import hashlib as hb
input=open("input.txt","r")
user_file=open("password.txt","r")
hash_input=hb.sha256()
text_input=input.readline()
pswd_hash=user_file.readline()
text_input=text_input.encode("UTF-8")
hash_input.update(text_input)
if hash_input.hexdigest()==pswd_hash:
    print("O hash da senha salva é",pswd_hash,".\n")
    print("A senha fornecida pelo usuário coincide.")
    valid_paswd:bool=1
else:
    print("O hash da senha salva é",pswd_hash,".\n")
    print("A senha fornecida pelo usuário não coincidiu com aquela salva.")
    valid_paswd:bool=0
input.close()
user_file.close()
