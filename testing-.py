
#
# fh2.write("<GuestUser name= "%s" password= "%s" startTime="2019-07-05 18:50:32" expiryTime="2020-07-04 18:50:32" sponsorName="admin" sponsorProfile="1" enabled="true" guestType="DEVICE">
#                                                                                                                                                                                         <GuestUserTags tagName="Role ID" tagValue="2"/>")
# fh2.write("<GuestUserTags tagName="Role ID" tagValue="2"/>")
# fh2.write("<GuestUserTags tagName="mac" tagValue="mac"/>")

mac = 'AA-BB-CC-DD-EE-FF'

with open('/Users/vinayreddy/Desktop/testing2.txt', 'w') as fh:
    fh.write('''<GuestUser name="%s" password="%s"  startTime="2019-07-05 18:50:32" expiryTime="2020-07-04 18:50:32" sponsorName="admin" sponsorProfile="1" enabled="true" guestType="DEVICE">
             <GuestUserTags tagName="Role ID" tagValue="2"/>''' % (mac, mac))
