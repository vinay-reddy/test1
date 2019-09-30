import re, sys


reg_obj = re.compile(r'^\[[\d/]+')
pattern_found = None
string = ''
line_list = []
with open('/Users/vinayreddy/Desktop/study/cluster_join/radius-portal-script/log.wb-NS_LAB', 'r') as fh:
    for line in fh:
        a = reg_obj.search(line)
        if a is not None and pattern_found is None:
            string = string + line
            pattern_found = 1
        elif a is None and pattern_found == 1:
            string = string + line
            line_list.append(string)
            string = ''
            pattern_found = None



for item in line_list:
    a= re.split("\s\s", item)[0] + re.split("\s\s", item)[1]
    b = a.split(',')
    #c = [ item for item in b if '[' in item item.strip('[') elif ']' in item item.strip(']') ]
   # c = [item.strip('[')  if '[' in item  else item.strip(']') if ']'  in item  else item for item in b]
    print()
    print(a)
    print()
    print('printing splitted item 0 and item 1 with , :',b)
    print()
    print('printing item 0 :', re.split("\s\s", item)[0])
    print('printing item 1 :',re.split("\s\s", item)[1])
    print('printing item 2 :',re.split("\s\s", item)[2])
    sys.exit()