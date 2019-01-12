def INBOX():
	global flag
	global R
	try:
		R = inputBox.pop(0)
	except:
		print('INPUTBOX IS EMPTY!')
		flag = 1
	return

def OUTBOX():
	global flag
	global R
	if R == outputBox[0]:
		outputBox.pop(0)
		if not outputBox:
			print('CONGRETULATION!')
			flag = 1
	else:
		print('NO, I WANT',str(outputBox[0]),'BUT YOU GIVE ME',str(R))
		flag = 1
	R = None
	return

# def JUMP(res,):
# 	global flag
# 	global R

def ADD(num):
	global flag
	global floor
	global R
	R += floor[num]
	return

def SUB(num):
	global flag
	global floor
	global R
	R -= floor[num]
	return

def BUMPADD(num):
	global flag
	global floor
	global R
	floor[num] += 1
	R = floor[num]
	return

def BUMPSUB(num):
	global flag
	global floor
	global R
	floor[num] -= 1
	R = floor[num]
	return


def COPYFROM(num):
	global flag
	global R
	global floor
	try:
		R = floor[num]
	except:
		print("FLOOR IS EMPTY!")
		flag = 1
	return

def COPYTO(num):
	global flag
	global R
	global floor
	try:
		floor[num] = R
	except:
		print("FLOOR IS EMPTY!")
		flag = 1
	return

def END():
	global flag
	global R
	flag = 1
	return

R = None
# inputBox = [4, 5, 9, 2, 6, 3, 8, 1, 7, 0]
# outputBox = [1, 2, 3, 4, 5, 6, 7, 8, 9]
inputBox = [3,-3,0]
outputBox = [3,2,1,0,-3,-2,-1,0,0]
flag = 0
floor = [None,None,None]
# floor = [0,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
def main():
	global floor
	global flag
	codeFlag = 0
	codeList = [line[:-1] for line in open('mycode.txt')]
	# print(codeList)
	print("THE FLOOR IS:")
	for i,j in zip(range(1,len(floor)+1),floor):
		print(i,j)
	print("===============================")
	if input("READY?(y/n)") == 'y':
		pass
	else:
		print("bye")
		return
	step = 0
	codelen = len(codeList) - 1 
	while not flag:
		step += 1
		code = codeList[codeFlag]
		# print(code,'R:',R,'floor:',floor)
		codeFlag += 1
		if code == "INBOX":
			INBOX()
		elif code == "OUTBOX":
			OUTBOX()
		elif code == "END":
			END()
		elif code.startswith("JUMP"):
			# JUMP(int(code.split()[-1]), codeFlag)
			if '[' in code:
				codeFlag = floor[int(code.split()[-1][1:-1]) - 1]
			else:
				codeFlag = int(code.split()[-1]) - 1
		elif code.startswith("COPYFROM"):
			if '[' in code:
				COPYFROM(floor[int(code.split()[-1][1:-1]) - 1])
			else:
				COPYFROM(int(code.split()[-1]))
		elif code.startswith("COPYTO"):
			if '[' in code:
				COPYTO(floor[int(code.split()[-1][1:-1]) - 1])
			else:
				COPYTO(int(code.split()[-1]))
		elif code.startswith("BUMPSUB"):
			if '[' in code:
				BUMPSUB(floor[int(code.split()[-1][1:-1]) - 1])
			else:
				BUMPSUB(int(code.split()[-1]))
		elif code.startswith("BUMPADD"):
			if '[' in code:
				BUMPADD(floor[int(code.split()[-1][1:-1]) - 1])
			else:
				BUMPADD(int(code.split()[-1]))
		elif code.startswith("JZ"):
			if R == 0:
				if '[' in code:
					codeFlag = floor[int(code.split()[-1][1:-1]) - 1]
				else:
					codeFlag = int(code.split()[-1]) - 1
				# codeFlag = int(code.split()[-1])
		elif code.startswith("JN"):
			if R < 0:
				if '[' in code:
					codeFlag = floor[int(code.split()[-1][1:-1]) - 1]
				else:
					codeFlag = int(code.split()[-1]) - 1
		elif code.startswith("ADD"):
			if '[' in code:
				ADD(floor[int(code.split()[-1][1:-1]) - 1])
			else:
				ADD(int(code.split()[-1]))
		elif code.startswith("SUB"):
			if '[' in code:
				SUB(floor[int(code.split()[-1][1:-1]) - 1])
			else:
				SUB(int(code.split()[-1]))

	if outputBox:
		print('OUTPUT WRONG!')
	else:
		print("step:",step)
		print("codelen:",codelen)


main()		
