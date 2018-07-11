import helper_functions

def checkflags(a,b,s):
	if(a>=1 and b==0):
		print("Please Enter a Name for your",s)
	else:
		print("Please Enter a",s,"first.")


#strings
x = "I did not understand. Please Re-enter your query."

#initialization
print("Welcome to DMoD. Please Enter your query.")
print("Press s to stop.")

q = input(">>>").lower()


#data storage
pname = []
tname = {}
tbl = []
cname = {}
clm = []

#flags
pf = 0 
pnf = 0
tf = 0
tnf = 0
cf = 0
cnf = 0
yf = 0


while q!='s':

	try:
		
		#cheching for newproject intent and asking user for a name.
		if helper_functions.checkforproject(q):
			pf += 1
			checkflags(pf,pnf,'Project')
			pvar = input(">>>")
			while pvar=="":
				print("Please Enter a proper name : ")
				pvar = input(">>>")
			if pvar in pname:
				print("Project already exists.")
			else:
				pname.append(pvar)

		#checking for newtable intent and prompting user for a project
		#to add that table to.
		elif helper_functions.checkfortable(q):
			if(pf==0):
				print("Create a project first.")
			else:
				tf += 1
				#input name of project
				px = input("Please enter the name of the project to add a table to.\nLeave empty to use last created project.\n>>>")
				if(px==""): #for last project entered.
					checkflags(tf,tnf,'Table')
					tvar = input(">>>")
					if pname[-1] not in tname.keys():
						tname[pname[-1]] = []
					if tvar in tname[pname[-1]]:
						print("Table already exists, please try a new name.")
					else:
						tname[pname[-1]].append(tvar)
				else: #by name of project to enter new table
					if px in pname:
						checkflags(tf,tnf,'Table')
						tvar = input(">>>")
						if px not in tname.keys():
							tname[px] = []
						if tvar in tname[px]:
							print("Table already exists, please try a new name.")
						else:
							tname[px].append(tvar)
					else:
						print("Project not found. Please enter again.")
				tbl.append(tvar)	
					
		#checking for newcolumn intent and prompting user for a project and a table
		#to add that column to.
		elif helper_functions.checkforcolumn(q):
			if(pf==0):
				print("Create a project first.")
			elif(tf==0):
				print("Create a table first.")
			else:
				cf += 1
				#input name of project
				tx = input("Please enter the name of the table to add a column to.\nLeave empty to use last created table.\n>>>")
				if tx=="" :
					#entering data to last created table
					checkflags(cf,cnf,'Column')
					cx = helper_functions.enternonempty()
					if tbl[-1] not in cname.keys():
						cname[tbl[-1]] = []
					if cx in cname[tbl[-1]]:
						print("Column already exists")
					else:
						cname[tbl[-1]].append(cx)

				elif tx in tbl :
					checkflags(cf,cnf,'Column')
					cx = helper_functions.enternonempty()
					if tx not in cname.keys():
						cname[tx] = []
					if cx in cname[tx]:
						print("Column already exists")
					else:
						cname[tx].append(cx)
				else:
					print("Table not Found.")	
				clm.append(cx)

		#check for desc
		elif (q=="desc"):
			helper_functions.desc(pname,tname,cname,pf,tf,cf)
			print("Column Data :",clm,"\nTable Data :",tbl)


		#I daid not understand your command.	
		else:
			print(x)

	#I did not understand your command.		
	except:
		print(x)

	q = input(">>>").lower()



helper_functions.desc(pname,tname,cname,pf,tf,cf)
print("Column Data :",clm,"\nTable Data :",tbl)
