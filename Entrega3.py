import hashlib as hb


input=open("input.txt","r")
user_file=open("password.txt","r")
hash_input=hb.sha256()
text_input=input.readline()
pswd_hash=user_file.readline()
text_input=text_input.encode("UTF-8")
hash_input.update(text_input)
input.close()
user_file.close()

def test():
    assert hash_input.hexdigest()==pswd_hash