
def task1():
	filein=open("running-config.cfg") #opening the file runnig_config
	list= []                      #creating an empty list
	for line in filein:
		line=line.strip()              #getting rid of white spaces
		line=line.split()              #this will create a list 
		if(line[0] ==  "interface"): #checks if the 1st word is iterface
			list.append(line[1])  #assigning the  next  item  
	print(list)
task1()
