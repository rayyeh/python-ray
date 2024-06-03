filein = "D:\SL37.out"
fileout = "D:\SL37.csv"
file1 = open(filein,"r")
file2 = open(fileout,"w+")
count = 0

def is_empty(string):
	return not string.strip()

for line in file1.readlines():
        count = count+1
        #print(count)
        #print(line)
        idx1 = line.index('Flds')
        data=line[0:12]+','+line[idx1+5:]
        data1=data.replace("'","")
        data2=data1.replace(')','')

        #print(data2.split(','))  
        rptname = data2.split(',')[1]
        #print(rptname)
        if rptname.strip():
            file2.write(data2)

file1.close()
file2.close()
