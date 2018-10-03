def access_list(f):
	file=open("f")
	b=[]
	for line in file:
		line=line.strip()
		for i in line.split():
			if i=="global_access" or i=="fw-management_access_in":
				b.append(line)
	return list
read="running-config.cfg"
print(access_list(read))
