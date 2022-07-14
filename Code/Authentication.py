from ast import literal_eval
import hashlib 
import math
import random

class Data:
	def __init__(self,ID,Hash):
		self.ID=ID
		self.Hash=Hash

class Data2:
	def __init__(self,encryptedData,KsCipered):
		self.encryptedData=encryptedData
		self.KsCipered=KsCipered

class KEY:
	def __init__(self,publicKey,privateKey):
		self.publicKey=publicKey
		self.privateKey=privateKey

class KEY2:
	def __init__(self,publicKey):
		self.publicKey=publicKey

def ReadText(txtFile):
	file = open(txtFile,"r")
	text=''
	for x in file:
		text += x
	file.close()
	return text

def HashTheText(contentOfTxt):
	hashedText = hashlib.sha256(contentOfTxt.encode())
	return hashedText.hexdigest()

def HexadecimalToBinary(hexadecimalString):
	res = "{0:08b}".format(int(hexadecimalString,16))
	return res

def BinaryToDecimal(number):
	decNum = int(number,2)
	return decNum

def SumUpBinary(binaryString):
	sum = 0
	for x in binaryString:
		sum += int(x)
	return sum

def GeneratePrimes(x,y):
	primeNumberList = []
	for n in range(x,y):
		isPrime =True
		for num in range(2,n):
			if n % num == 0:
				isPrime = False
		if isPrime:
			primeNumberList.append(n)
	primeNumberList.remove(1)
	return primeNumberList

def GcdCalculator(bigON,n,primeNumberList):
	gcdFlag = True
	while(gcdFlag):
		e = primeNumberList[random.randint(1,len(primeNumberList)-1)]
		#print("e : " , e)
		#print("e's prime number list : " , primeNumberList)
		if(e < n and e > 2 and math.gcd(int(e),int(bigON)) == 1):
			#print("e's last prime number list : " , primeNumberList)
			return e
		else :
			primeNumberList.remove(e)

def ModCalculator(bigON , n , e , primeNumberList):
	tempPrimeNumbers =[]
	modFlag = True
	while(modFlag):
		d = primeNumberList[random.randint(1,len(primeNumberList)-1)]
		#print("d : " , d)
		#print("d's prime number list : " , primeNumberList)
		if(d < bigON and d > 2 and (int(e)*int(d))%int(bigON) == 1):
			for x in tempPrimeNumbers:
				#print("x:",x)
				primeNumberList.append(x)
			#print("d's last prime number list : " , primeNumberList)
			return d
		else :
			tempPrimeNumbers.append(d)
			primeNumberList.remove(d)

def KeyGenerator(KEY , primeNumberList):
	randomPrime1 = primeNumberList[random.randint(0,len(primeNumberList)-1)]
	#print("prime number list " , primeNumberList)
	primeNumberList.remove(randomPrime1)
	print("random prime number 1 : " , randomPrime1)
	#print("prime number list " , primeNumberList)
	randomPrime2 = primeNumberList[random.randint(0,len(primeNumberList)-1)]
	print("random prime number 2 : " , randomPrime2)
	primeNumberList.append(randomPrime1)
	n = randomPrime1 * randomPrime2
	print("n : " , n)
	bigON = (randomPrime1-1) * (randomPrime2-1)
	print(f"Big O = {bigON}")
	e=GcdCalculator(bigON , n , primeNumberList)
	print("e : " , e)
	d=ModCalculator(bigON , n , e , primeNumberList)
	print("d : " , d)
	KEY.publicKey = [e,n]
	KEY.privateKey = [d,n]

def SRR(text,iteration):
	text = list(text)
	for x in range(iteration):
		first = 0
		second =0
		for z in range(len(text)):
			if(z == 0):
				first = text[z]
				second = text[z+1]
				text[z+1] = first
				first = second
			elif(z == len(text)-1):
				text[0] = first
			else:
				second = text[z+1]
				text[z+1] = first
				first = second
	return text

def GenerateKS():
	flag = True
	count=0
	newRandomKS = ""
	randomKS = random.randint(1000000000,9000000000)
	randomKS = bin(randomKS)[2:]
	while(flag):
		add = randomKS[count]
		newRandomKS = newRandomKS+add
		#print("new random ks" ,newRandomKS)
		count +=1
		if(count>=10):
			flag = False
			return newRandomKS

def DataEncryption(Data,Ks):
	hashedData = HashTheText(Data.ID)
	#print("hashed data ",hashedData)
	binaryData = HexadecimalToBinary(hashedData)
	#print("binary data : " , binaryData)
	sumOfBinaryData = SumUpBinary(binaryData)
	#print("sum of binary data: " , sumOfBinaryData)
	#print(Data.Hash)
	totalSum=sumOfBinaryData+Data.Hash
	#print(totalSum)
	binaryTotalSum = bin(totalSum)[2:]
	#print(binaryTotalSum)
	finalData = ""
	for x in range(len(binaryTotalSum)):
		#print(binaryData)
		#print(Ks)
		acd = binaryTotalSum[x] != Ks[x]
		if(acd == False):
			#print("1 eklendi")
			finalData = finalData+"1"
		else:
			#print("0 eklendi")
			finalData = finalData+"0"
	return finalData



#**************************************************Encryption
text = ReadText("personalInformation")
#print("text : " , text)
hashedText = HashTheText(text)
#print("hashed Text : " , hashedText)
binaryText = HexadecimalToBinary(hashedText)
#print("binary Text : " , binaryText)
#decimalText = BinaryToDecimal(binaryText)
#print("decimal Text : ", decimalText)
sumOfBinary = SumUpBinary(binaryText)
print("sum of binary : " , sumOfBinary)
primeNumberList = GeneratePrimes(1,200)
#print("prime number list" , primeNumberList)
keyDST= KEY("null" , "null")
keySRC= KEY("null" , "null")
#**************************************************Çalışan örnekten gelen sayılar

keyDST.publicKey = [29,46]
keyDST.privateKey = [19,46]
keySRC.publicKey = [89,291]
keySRC.privateKey = [41,291]
"""
KeyGenerator(keyDST,primeNumberList)
print("SRC")
KeyGenerator(keySRC,primeNumberList)
#print("KeyDST public 0 : " , keyDST.publicKey[0])
#print("KeyDST public 1 : " , keyDST.publicKey[1])
#print("KeyDST private 0 : " , keyDST.privateKey[0])
#print("KeyDST private 1 : " , keyDST.privateKey[1])
#print("KeySRC public 0 : " , keySRC.publicKey[0])
#print("KeySRC public 1 : " , keySRC.publicKey[1])
#print("KeySRC private 0 : " , keySRC.privateKey[0])
#print("KeySRC private 1 : " , keySRC.privateKey[1])
#**************************************************SRR denemesi
#tex = "atakan"
#ttt = SRR(tex,2)
#print(ttt)
#**************************************************Private ve public key in çalışması
#num1 = sumOfBinary ** int(keyDST.publicKey[0])
#ciper = int(num1)%int(keyDST.publicKey[1])
#print(f"ciper : {ciper}")
#num2 = int(ciper) ** int(keyDST.privateKey[0])
#message = int(num2)%int(keyDST.privateKey[1])
#print(f"message : {message}")
"""
#**************************************************SRR kullanılan private encryption
#num2 = sumOfBinary ** int(keySRC.privateKey[0])
#ciper = int(num2)%int(keySRC.privateKey[1])
#print(ciper)
#binar = bin(ciper)[2:]
#print(binar)
#binar = SRR(binar,5)
#print(binar)
#**************************************************K_H
keyK_H = KEY2("null")
firstDSTPublic = keyDST.publicKey[0]
firstDSTPublic = bin(firstDSTPublic)[2:]
sumFirstDSTPublic=SumUpBinary(firstDSTPublic)
#print(sumFirstDSTPublic)
secondDSTPublic = keyDST.publicKey[1]
secondDSTPublic = bin(secondDSTPublic)[2:]
sumSecondtDSTPublic=SumUpBinary(secondDSTPublic)
#print(sumSecondtDSTPublic)
number1 = sumFirstDSTPublic ** int(keySRC.privateKey[0])
ciper1 = int(number1)%int(keySRC.privateKey[1])
#print(f"ciper1 : {ciper1}")
number2 = sumSecondtDSTPublic ** int(keySRC.privateKey[0])
ciper2 = int(number2)%int(keySRC.privateKey[1])
#print(f"ciper2 : {ciper2}")
keyK_H.publicKey = [ciper1 , ciper2]
#print(keyK_H.publicKey[0] )
#print(keyK_H.publicKey[1] )
actualText = sumOfBinary ** int(keyK_H.publicKey[0])
actualCiper = int(actualText)%int(keyK_H.publicKey[1])
print(f"actualCiper : {actualCiper}")
actualText1= actualCiper ** int(keyK_H.publicKey[0])
actualCiper1 = int(actualText1)%int(keyK_H.publicKey[1])
print("Actual ciper 1 : ",actualCiper1)
Ks = GenerateKS()
print("KS :" , Ks)
Data = Data(text , actualCiper)
#print(Data.ID )
#print(Data.Hash)
encryptedData = DataEncryption(Data,Ks)
print("encryptedData : " , encryptedData)
KsSumUp = SumUpBinary(Ks)
print("Ks sum Up : " ,KsSumUp)
number3 = KsSumUp ** int(keyDST.publicKey[0])
KsCipered = int(number3)%int(keyDST.publicKey[1])
print("KsCipered : " ,KsCipered)
finalData=Data2(encryptedData,KsCipered)
print("Final Data's encrypted data " ,finalData.encryptedData)
print("Final Data's KsCipered " , finalData.KsCipered)

#**************************************************Dencryption
ciperedKs = finalData.KsCipered
number4 = ciperedKs ** int(keyDST.privateKey[0])
decryptedKs = int(number4)%int(keyDST.privateKey[1])
print("decrypted Ks : " ,decryptedKs)































