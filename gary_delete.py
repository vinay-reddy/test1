

import re, csv




regexobj=re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3}) ')

regexobj2 = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w{3,}) (\w+) (\w+) (\d+) .* duration: ([\d.]+) .*?: (.*)', re.DOTALL) #good perfectly working one.
string = ''
listoflines = []
with open('/var/lib/pgsql/data/pg_log/postgresql-Thu.log', 'r') as fh:
    firstPatternFound = None
    secondPatternFound = None
    for line in fh.readlines():
        b = regexobj.search(line)
        if b is not None and firstPatternFound is None:
            firstPatternFound =1
            string = string + line
        elif b is None and firstPatternFound == 1:
            string = string + line
        elif b is not None and firstPatternFound == 1:
            listoflines.append(string)
            string = ''
            string = string + line



with open('queries.csv', 'w') as fh2:
    outputwriter = csv.writer(fh2)
    for item in listoflines:
        if 'duration:' in item:
            #             print(item)
            c = regexobj2.search(item)
            outputwriter.writerow(c.groups())
        #             print(list(c.groups()))
        else:
            continue





