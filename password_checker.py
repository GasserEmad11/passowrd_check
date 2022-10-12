import requests
import hashlib
import sys
def recieve_data(first5):
    url = 'https://api.pwnedpasswords.com/range/' + first5
    res = requests.get(url)
    return res
def data_Check(password):
    crypto_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    fchar5, rest = crypto_pass[:5], crypto_pass[5:]
    response = recieve_data(fchar5)
    #print(response)
    #print(crypto_pass)
    return password_hash(response, rest)
# def responsev2(R):
# print (R.text)
def password_hash(hashes, hash_to_check):
    full_hash = (line.split(':') for line in hashes.text.splitlines())
    for a, b in full_hash:
        # print(a,b)
        if a == hash_to_check:
            return b
    return 0

#data_Check('afjedmkfvmkogfdlfg')
def main_func (args):
     for passwords in args:
      count = data_Check(passwords)
      if count:
        print (f'oopss!!, you have been hacked around {count} times,time to change your password')
      else:
        print ("congratulations!, you have never been hacked")
main_func(sys.argv[1:])
