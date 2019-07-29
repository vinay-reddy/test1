
from extract_mac_from_SHL import listofmacs

macslist = []
with open('/Users/vinayreddy/Desktop/macs.txt') as fh:
    for line in fh:
        line = line.strip()
        mac = []
        for i in range(0,len(line),2):
            mac.append(line[i:i+2])
        modifiedMac= "-".join(mac).upper()
        macslist.append(modifiedMac)


        # with open('/Users/vinayreddy/Desktop/macs_modified.txt', 'a') as w:
        #     w.write(modifiedMac + '\n')

with open('/Users/vinayreddy/Desktop/test.xml', 'w') as fh2:
    header = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<TipsContents xmlns="http://www.avendasys.com/tipsapiDefs/1.0">
<TipsHeader exportTime="Fri, 05 Jul 2019 18:58:05 UTC" version="6.0"/>
<GuestUsers>'''
    tailer = '''  </GuestUsers>
</TipsContents>'''
    fh2.write(header + '\n')
    for mac in listofmacs:
        fh2.write('''<GuestUser name="%s" password="%s"  startTime="2019-07-05 18:50:32"  sponsorName="admin" sponsorProfile="1" enabled="true" guestType="DEVICE">
             <GuestUserTags tagName="Role ID" tagValue="2"/>''' % (mac, mac))
        fh2.write('<GuestUserTags tagName="Role ID" tagValue="2"/>')
        fh2.write('<GuestUserTags tagName="mac" tagValue="%s"/>' % (mac))
        fh2.write('''<GuestUserTags tagName="mac_auth" tagValue="1"/>
      <GuestUserTags tagName="source" tagValue="mac_create"/>
      <GuestUserTags tagName="do_expire" tagValue="2"/>
      <GuestUserTags tagName="no_portal" tagValue="1"/>
      <GuestUserTags tagName="Create Time" tagValue="2019-07-05 18:50:32"/>
      <GuestUserTags tagName="no_password" tagValue="1"/>
      <GuestUserTags tagName="remote_addr" tagValue="10.205.8.105"/>
      <GuestUserTags tagName="Visitor Name" tagValue="ABM"/>
      <GuestUserTags tagName="expire_postlogin" tagValue="0"/>
      <GuestUserTags tagName="simultaneous_use" tagValue="0"/>
      <GuestUserTags tagName="sponsor_profile_name" tagValue="IT Administrators"/>
    </GuestUser>''' + '\n')
    fh2.write(tailer)



