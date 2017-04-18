from Crypto.Cipher import DES, AES
import random

class Cipher:
	def __init__(self, cipher="DES",plaintext=1, keylen=56, msglen=64, IV='00000000'):
		self.cipher = cipher
		self.plaintext = plaintext
		self.keylen = keylen
		self.msglen = msglen
		self.permute = random.sample(range(0, msglen), keylen)
		# print self.permute
		# self.permute = [0,1,2,3,4,5,6,7]
		self.iv = IV
		# print "[*] Params passed to Cipher class:"
		# print "[*] plaintext: ", plaintext
		# print "[*] keylen: ", keylen
		# print "[*] msglen: ", msglen


	def f(self, key, display=False):
		
		# Convert key and plaintext to string
		key = hex(key).replace("0x", "").replace("L", "")
		key = '0'*((2*(self.msglen/8)-len(key))) + key
		key = key.decode("hex")

		plaintext = hex(self.plaintext).replace("0x", "").replace("L", "")
		plaintext = '0'*(2*(self.msglen/8)-len(plaintext)) + plaintext
		plaintext = plaintext.decode("hex")

		# if display:
		# 	print "[*] key: ", key.encode("hex")
		# 	print "[*] plaintext:" , plaintext.encode("hex")

		# Encryption code
		if self.cipher=="DES":
			cphr = self.des_encrypt(key, plaintext)
		else:
			cphr = self.aes_encrypt(key, plaintext)

		cphr = self.R(int(cphr.encode("hex"), 16))
		return cphr

	def R(self, cipher):
		cipher = bin(cipher).replace("0b", "")
		cipher = '0'*(self.msglen-len(cipher)) + cipher
		cipher = [cipher[i] for i in self.permute]
		cipher = ''.join(cipher)
		# print "[*] cipher:",cipher
		return int(cipher, 2)

	def des_encrypt(self, key, plaintext, display=False):
		# if display:
		# 	print "[*] plaintext: ", plaintext.encode("hex")
		# 	print "[*] key: ", key.encode("hex")
		des = DES.new(key, DES.MODE_CBC, self.iv)
		cphr = des.encrypt(plaintext)
		return cphr

	def aes_encrypt(self, key, plaintext, display=False):
		# if display:
		# 	print "[*] plaintext: ", plaintext.encode("hex")
		# 	print "[*] key: ", key.encode("hex")
		aes = AES.new(key, AES.MODE_CBC, '0'*16)
		cphr = aes.encrypt(plaintext)
		return cphr