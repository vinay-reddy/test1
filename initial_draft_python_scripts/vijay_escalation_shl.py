
# fh2 = open('/Users/vinayreddy/Desktop/logs/vijay_escalation/truncatedmacs', 'w')
# with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
#     for mac in fh:
#         mac = mac.strip()[:6] + '\n'
#         fh2.write(mac)
#
# fh2.close()

import pprint
import operator

macs_oui_list = []
count = {}
#fh2 = open('/Users/vinayreddy/Desktop/logs/vijay_escalation/truncatedmacs', 'w')
with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
    for mac in fh:
        mac = mac.strip()[:6]
        macs_oui_list.append(mac)

for mac_oui in macs_oui_list:
    count.setdefault(mac_oui, 0)
    count[mac_oui] = count[mac_oui] + 1

sorted_d = sorted(count.items(), key=operator.itemgetter(1), reverse= True)

pprint.pprint(sorted_d)

#fh2.close()

# function to display the macs that are present when mac_oui is passed

def macs(mac_oui):
    with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
        for mac in fh:
            if mac_oui in mac:
                mac = mac.strip()
                print(mac)

#macs('0c5415')

#function to display split the macs at nth location and print the macs count.

# def splitter(location):
#
#     macs_oui_list = []
#     count = {}
#     with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
#         for mac in fh:
#             mac = mac.strip()[:location]
#             macs_oui_list.append(mac)
#
#     for mac_oui in macs_oui_list:
#         count.setdefault(mac_oui, 0)
#         count[mac_oui] = count[mac_oui] + 1
#     sorted_d = sorted(count.items(), key=operator.itemgetter(1), reverse= True)
#
#     pprint.pprint(sorted_d)
