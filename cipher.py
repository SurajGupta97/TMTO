from Crypto.Cipher import DES
import random

class Cipher:
	def __init__(self, cipher="DES", r, plaintext=1, keylen=56, msglen=64):
		self.cipher = cipher
		self.keylen = keylen
		self.msglen = msglen
		self.r = r
		self.permute = random.sample(range(0, msglen), keylen)

	def f(self, key):
		
		# Convert key and plaintext to string
		key = hex(key).replace("0x", "").replace("L", "")
		key = '0'*(16-len(key)) + key
		key = key.decode("hex")

		plaintext = hex(plaintext).replace("0x", "").replace("L", "")
		plaintext = '0'*(2*(self.msglen/8)-len(plaintext)) + plaintext
		plaintext = plaintext.decode("hex")

		# Encryption code
		if self.cipher=="DES":
			des = DES.new(key, DES.MODE_CBC)
			cphr = des.encrypt(plaintext)
		else:
			cphr = "12345678"

		cphr = self.R(int(cphr.encode("hex"), 16))
		return cphr

	def R(self, cipher):
		cipher = bin(cipher).replace("0b", "")
		cipher = '0'*(self.msglen-len(cipher)) + cipher
		cipher = [cipher[i] for i in self.permute]
		cipher = ''.join(cipher)
		return int(cipher, 2)