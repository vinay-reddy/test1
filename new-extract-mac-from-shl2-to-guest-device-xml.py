
import re
import pandas as pd
import numpy as np
import csv


regexobj = re.compile(r'"(.*?)"')


listofmacs = []
fh_writecsv = open('/Users/vinayreddy/Desktop/logs/robson_SHL/des_mac.csv', 'w')
csv_output = csv.writer(fh_writecsv)
with open('/Users/vinayreddy/Desktop/logs/robson_SHL/StaticHostList2.xml', 'r') as fh:

    for line in fh:
        if ('address=' and 'Member description=') in line:
            #            print(line.strip())
            #            a=line.split('address=')[1].split('/')[0].strip().split('"')[1]
            b = regexobj.findall(line)
            print(b)
            csv_output.writerow(b)

            #listofmacs.append(line.split('address=')[1].split('/')[0].strip().split('"')[1])
#print(listofmacs)

fh_writecsv.close()
pd.options.display.max_rows = 1200
print("max columns: ", pd.options.display.max_columns)
print(pd.options.display.max_rows)

df = pd.read_csv('/Users/vinayreddy/Desktop/logs/robson_SHL/des_mac.csv', header=None, names = ['description', 'mac'],skip_blank_lines=True)

print(df)
mac_count = df.index.max()


with open('/Users/vinayreddy/Desktop/test2.xml', 'w') as fh3:
    header = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<TipsContents xmlns="http://www.avendasys.com/tipsapiDefs/1.0">
<TipsHeader exportTime="Fri, 05 Jul 2019 18:58:05 UTC" version="6.0"/>
<GuestUsers>'''
    tailer = '''</GuestUsers>
</TipsContents>'''
    fh3.write(header + '\n')
    j = 700
    for i in range(699, mac_count + 1):
        j = j + 1
        fh3.write('''<GuestUser name="%s" password="%s"  startTime="2019-07-05 18:50:32"  sponsorName="admin" sponsorProfile="1" enabled="true" guestType="DEVICE">''' % (df.iloc[i]['mac'].upper(), df.iloc[i]['mac'].upper()) + '\n')
        fh3.write('<GuestUserTags tagName="Role ID" tagValue="6"/>' + '\n')
        fh3.write('<GuestUserTags tagName="notes" tagValue="%s"/>' % (df.iloc[i]['description']) + '\n')
        fh3.write('<GuestUserTags tagName="mac" tagValue="%s"/>' % (df.iloc[i]['mac'].upper()) + '\n')
        fh3.write('''<GuestUserTags tagName="mac_auth" tagValue="1"/>
      <GuestUserTags tagName="source" tagValue="mac_create"/>
      <GuestUserTags tagName="do_expire" tagValue="2"/>
      <GuestUserTags tagName="no_portal" tagValue="1"/>
      <GuestUserTags tagName="Create Time" tagValue="2019-07-05 18:50:32"/>
      <GuestUserTags tagName="no_password" tagValue="1"/>
      <GuestUserTags tagName="remote_addr" tagValue="10.205.8.105"/>
      <GuestUserTags tagName="Visitor Name" tagValue="%s"/>
      <GuestUserTags tagName="expire_postlogin" tagValue="0"/>
      <GuestUserTags tagName="simultaneous_use" tagValue="0"/>
      <GuestUserTags tagName="sponsor_profile_name" tagValue="IT Administrators"/>
    </GuestUser>''' % (df.iloc[i]['mac'].upper()) + '\n')
    fh3.write(tailer)

fh3.close()
