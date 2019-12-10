# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Nikhil Krishnan
# Roll Number: 2018248
# Section: B
# Group: 1
# Date:18/10/18



def binon2 (binary):
#Necessary for binon1()
	if len(binary) == 4 :
		return binary
	if len(binary) == 3 :
		return "0"+binary
	if len(binary) == 2 :
		return "0"+"0"+binary
	if len(binary) == 1 :
		return "0"+"0"+"0"+binary
def binon1(n): 
#Necessary for binon()
	if int(n) == 0:
		return "0"
	if int(n)//2 == 0:
		return "1"
	else:
		binary = str(binon1(int(n)//2))+str(int(n)%2)
	return binary
def binon(n):
#Returns binary of a number
#Eg binon("13") - 1101
#Eg binon("2") - 0010
	return binon2(binon1(n))
def ppap(numVar,List):
#Used in lob
	for i in range (len (List)):
		List[i][0:int(numVar)] = List[i][-int(numVar):]
		List[i][int(numVar):] = "-"
	if len (List[0]) != 4:
		for i in range (len (List)):
			for k in range (3-int(numVar)):
				List[i].append("-")
	return List
def lob(numVar,stringIn): 
#Returns a list of binary, here a list of minterm and dontcare 
#only if input is entered in the correct format. 
#Eg lob1 ("3","(1,3,7) d (0,2,5)") - [['0','0','1','-'],['0','1','1','-'],['1','1','1','-'],['0','0','0','-'],['0','1','0','-'],['1','0','1','-']]
#Eg lob1 ("4","(0,1,2,13,14) d -") - [['0','0','0','0'],['0','0','0','1'],['0','0','1','0'],['1','1','0','1'],['1','1','1','0']]
#Eg lob1 ("2","(0,1,2,3) d -") - [['0','0','-','-'],['0','1','-','-'],['1','0','-','-'],['1','1','-','-']]
	indexd = stringIn.index('d')
	stringInd = stringIn
	stringIn = stringIn.split('d')
	minterms = stringIn[0]
	minterms = minterms[1:-2]
	minterms = minterms.split(',')
	binmin = list(map(binon, minterms))
	emptylist1 = []
	for i in range(len(binmin)):
		emptylist1.append([])
	for i in range (len (binmin)) :
		for k in range(4):
			emptylist1[i].append (binmin[i][k])
	if stringInd[indexd+2] != '-' :
		dontcare = stringIn[1]
		dontcare = dontcare[2:-1]
		dontcare = dontcare.split(',')
		bindc = list(map(binon, dontcare))
		emptylist2 = []
		for i in range(len(bindc)):
			emptylist2.append([])
		for i in range (len (bindc)) :
			for k in range(4):
				emptylist2[i].append (bindc[i][k])
		for i in range (len (emptylist2)):
			emptylist1.append(emptylist2[i])
		if (int(numVar) == 1) or (int(numVar) == 2) or (int(numVar) == 3) :
			emptylist1 = ppap(numVar,emptylist1)
			return [emptylist1,emptylist2]
		else:
			return [emptylist1,emptylist2]
	else:
		if (int(numVar) == 1) or (int(numVar) == 2) or (int(numVar) == 3) :
			emptylist1 = ppap(numVar,emptylist1)
			return [emptylist1]
		else:
			return [emptylist1]
def fa (li): 
#Returns the answer in the form strings of individual minterms.
#Eg fa (["0","-","1","0"]) - w'yz'
	dictw = {"-":"","0":"w\'","1":"w"}
	dictx = {"-":"","0":"x\'","1":"x"}
	dicty = {"-":"","0":"y\'","1":"y"}
	dictz = {"-":"","0":"z\'","1":"z"}
	answer = dictw[li[0]]+dictx[li[1]]+dicty[li[2]]+dictz[li[3]]
	if answer == "":
		return "1"
	else:
		return answer	
def simplify(List):
	emptylist1 = []
	endlist = []
	while List != []:
		for i in range (len (List)):
			for k in range(len (List)):
				count = 0
				for j in range(4):
					if List[i][j] == List[k][j] :
						count = count + 1
				if count == 3:
					emptylist1.append([List[i],List[k]])
		#I have made pairs of minterms which differ only at one position and appended them to emptylist1.
		if emptylist1 != [] :
			for i in range (len (List)):
				count = 0
				for j in range (len (emptylist1)):
					for k in range (2):
						if List[i] == emptylist1[j][k] :
							count = count + 1
				if count == 0 :
					endlist.append(List[i])
		else :
			for i in List:
				endlist.append(i)
			List = []
		#I have made list of minterms not used in the previous list. THIS ALSO HAS THE DON'T CARES. They are in endlist.
		if emptylist1 != [] :
			emptylist69 = []
			for i in range (len (emptylist1)):
				for j in range (4):
					if emptylist1[i][0][j] != emptylist1[i][1][j] :				
						a = list(emptylist1[i][0])
						b = list(emptylist1[i][1])
						a[j] = "-" 
						b[j] = "-"
						emptylist69.append([a,b])
			emptylist2 = []
			for i in range (len (emptylist69)):
				emptylist2.append(emptylist69[i][0])
			emptylist3 = []
			for i in emptylist2:
				if i not in emptylist3:
					emptylist3.append(i)
		#I have now replaced the common position with "-" and reduced the list by transferring elements to emptylist3 and removed the duplicates.
			List = emptylist3
			emptylist1 = []
	return endlist
def minFunc(numVar, stringIn):
	if stringIn[:2] == "()":
		return "0"
	else:
		if len (lob (numVar,stringIn)) == 1 :
			List = lob (numVar,stringIn)[0]
			emptylist1 = []
			endlist = []
			endlist = simplify (List)
			stringOut = list(map(fa,endlist)) 
			stringOut.sort(reverse=True)
			t =""
			for i in range (len(stringOut)):
				t = t+stringOut[i]+"+"
			stringOut = t[:-1]
			return stringOut
		else:		
			bindc = simplify (lob (numVar,stringIn)[1])
			List = lob (numVar,stringIn)[0]
			emptylist1 = []
			endlist = []
			endlist = simplify (List)
			for i in bindc :
				if i in endlist:
					endlist.remove(i)
			stringOut = list(map(fa,endlist)) 
			stringOut.sort(reverse=True)
			t =""
			for i in range (len(stringOut)):
				t = t+stringOut[i]+"+"
			stringOut = t[:-1]
			return stringOut 


