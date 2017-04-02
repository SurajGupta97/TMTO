import random
from random import randrange
from bisect import bisect_left
import operator
from cipher import Cipher
from math import log
from Crypto.Cipher import AES
def binary_search(a, x):
	lo = 0
	hi = len(a)   
	pos = bisect_left(a, x, lo, hi) 
	return (pos if pos != hi and a[pos] == x else -1)

def iterate(cipher,m,t,PlainText,CipherText,N):
	for tab in range(1,t+1):
		sp=random.sample(range(1,N),m)
		# sp = range(1,m+1)	
		cip=Cipher(cipher,PlainText,int(log(N,2)),128)

		table=[]
		ep = random.sample(range(1,N),m)
		for i in range(m):
			xi=sp[i]
			print xi,
			for j in range(t):
				xi=cip.f(xi)
				print xi,
			print
			ep[i]=xi
			table.append((sp[i],ep[i]))

		table.sort(key=operator.itemgetter(1))
		print table

		strow = [x[0] for x in table]
		endrow = [x[1] for x in table]

		flag=False
		print "[*] ciphertext:",CipherText
		yi=cip.R(CipherText)
		print "[*] yi:",yi,
		asdf = yi
		for k in range(t):
			asdf = cip.f(asdf)
			print asdf,
		print
		for i in range(t):
			temp=binary_search(endrow,yi)
			if temp!=-1:
				print i
				print temp
				te = strow[temp]
				for j in range(t-1-i):
					te=cip.f(te)
				if cip.f(te) == cip.R(CipherText):
					asd = hex(te).replace("0x", "").replace("L", "")
					asd = '0'*((2*(128/8)-len(asd))) + asd
					asd = asd.decode("hex")

					dfg = hex(PlainText).replace("0x", "").replace("L", "")
					dfg = '0'*(2*(128/8)-len(dfg)) + dfg
					dfg = dfg.decode("hex")

					ct = int((cip.aes_encrypt(asd, dfg)).encode("hex"), 16)
					if ct==CipherText:
						flag=True
				kooy = te
				break
			else:
				yi=cip.f(yi)

		if flag==True:
			return (flag,kooy)

	return (False, "bekar code hai mera!")

if __name__ == "__main__":
	N = 256
	m =	6
	t = 6
	pt = 12
	key = randrange(N)

	key = hex(key).replace("0x", "").replace("L", "")
	key = '0'*((2*(128/8)-len(key))) + key
	key = key.decode("hex")

	plaintext = hex(pt).replace("0x", "").replace("L", "")
	plaintext = '0'*(2*(128/8)-len(plaintext)) + plaintext
	plaintext = plaintext.decode("hex")

	aes = AES.new(key, AES.MODE_CBC, '0'*16)
	ciphertext = aes.encrypt(plaintext)
	ciphertext = int(ciphertext.encode("hex"), 16)

	print "[*] ciphertext212", ciphertext

	_, key =  iterate("AES",m,t,pt,ciphertext,N)
	print key	

	key = hex(key).replace("0x", "").replace("L", "")
	key = '0'*((2*(128/8)-len(key))) + key
	key = key.decode("hex")

	c = Cipher("AES", plaintext, 8, 128)
	plaintext = hex(pt).replace("0x", "").replace("L", "")
	plaintext = '0'*(2*(128/8)-len(plaintext)) + plaintext
	plaintext = plaintext.decode("hex")

	ct =  c.aes_encrypt(key, plaintext, True)
	print int(ct.encode("hex"), 16)

	# print c.f(3, True)
	# print c.f(2, True)