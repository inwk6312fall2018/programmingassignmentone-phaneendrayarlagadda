file=open('running-config.cfg')
file1=open('result.txt','w+')
for line in file:
  line=line.strip(string.punctuation + string.whitespace)
  line=str(line.split())
  if(line[0]=='security-level'):
    line[1]='10'
    file1.write(str(line[1]))
    if(len(line)>=4):
      if(line[2][0:3]=='192' or line[2][0:3]=='172'):
        output1=line[2][4:]
        del line[2]
        output2='10.'+output1
        line.insert(2,output2)
      file1.write(str(line))
    file1.write(str(line))
