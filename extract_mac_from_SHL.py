
listofmacs = []
with open('/Users/vinayreddy/Desktop/logs/robson_SHL/StaticHostList.xml', 'r') as fh:
    for line in fh:
        if 'address=' in line:
#            a=line.split('address=')[1].split('/')[0].strip().split('"')[1]

            listofmacs.append(line.split('address=')[1].split('/')[0].strip().split('"')[1])
print(listofmacs)