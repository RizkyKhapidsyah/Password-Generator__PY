import random
from string import digits, punctuation, ascii_letters

panjang = 20
simbol = ascii_letters + digits + punctuation
acak_secara_aman = random.SystemRandom()
kata_sandi = "".join(acak_secara_aman.choice(simbol)
                    for i in range(panjang))

print('==================')
print('Password Generator')
print('==================')
print('Password Anda  = ' + kata_sandi)
