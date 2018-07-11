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
MainJSON = {}
clm = []

#flags
pf = 0 
pnf = 0
tf = 0
tnf = 0
cf = 0
cnf = 0
yf = 0



#main runner
while q!='s':

	try:
		
		#cheching for newproject intent and asking user for a name.
		if helper_functions.checkforproject(q):
			pf += 1
			checkflags(pf,pnf,'Project')
			pvar = helper_functions.enternonempty()
			if pvar in pname:
				print("Project already exists.")
			else:
				pname.append(pvar)
			if pvar not in MainJSON.keys():
				MainJSON[pvar] = {}
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
					tvar = helper_functions.enternonempty()
					if pname[-1] not in MainJSON.keys():
						MainJSON[pname[-1]] = {}
					if tvar in MainJSON[pname[-1]].keys():
						print("Table already exists, please try a new name.")
					else:
						MainJSON[pname[-1]][tvar] = {}
				else: #by name of project to enter new table
					if px in pname:
						checkflags(tf,tnf,'Table')
						tvar = helper_functions.enternonempty()
						if px not in MainJSON.keys():
							MainJSON[px] = {}
						if tvar in MainJSON[px].keys():
							print("Table already exists, please try a new name.")
						else:
							MainJSON[px][tvar] = {}
					else:
						print("Project not found. Please enter again.")
				tbl.append(tvar)	
					
		#checking for newcolumn intent and prompting user for a project and a table
		#to add that column to. This also creates the main JSON.
		elif helper_functions.checkforcolumn(q):
			if(pf==0):
				print("Create a project first.")
			elif(tf==0):
				print("Create a table first.")
			else:
				cf += 1
				#input name of project
				px = input("Please enter the name of the project to add a column to.\nLeave empty to use last created project.\n>>>")
				try:
					if px=="": 
						px = pname[-1]
					print("The Tables available are : ",MainJSON[px].keys())
					#input name of table

					print("Please enter the name of the table to add a column to.\n>>>")
					tx = helper_functions.enternonempty()

					#last created table in last created/entered project. making JSON.
					"""if tx==""  :
						checkflags(cf,cnf,'Column')
						cx = helper_functions.enternonempty()
						if px not in MainJSON.keys():
							MainJSON[px] = {}
						if cx in MainJSON[px][-1]:
							print("Column already exists")
						else:
							MainJSON[px][-1].append(cx)"""

					#table entered. Making JSON.
					if tx in MainJSON[px].keys() :
						checkflags(cf,cnf,'Column')
						cx = helper_functions.enternonempty()
						if tx not in MainJSON[px].keys():
							MainJSON[px] = {}
						if cx in MainJSON[px][tx].keys():
							print("Column already exists")
						else:
							MainJSON[px][tx][cx] = {}
					else:
						print("Table not Found.")	
					"""DONE UPTO HERE"""

					clm.append(cx)
				except:
					print("No Tables available.")
				

		#check for desc
		elif (q=="desc"):
			helper_functions.desc(pname,MainJSON,pf,tf,cf)
			print("Column Data :",clm,"\nTable Data :",tbl)

		elif helper_functions.checkforhi(q):
			print("Hi there! Welcome to Dmod.\nPlease do keep your queries short and simple.")

		#I did not understand your command.	
		else:
			print(x)

	#I did not understand your command.		
	except:
		print(x)

	q = input(">>>").lower()


helper_functions.desc(pname,MainJSON,pf,tf,cf)
print("Column Data :",clm,"\nTable Data :",tbl)
print("Encoded Json is : \n",helper_functions.encode_json(MainJSON))