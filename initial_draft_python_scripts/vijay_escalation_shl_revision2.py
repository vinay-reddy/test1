
# fh2 = open('/Users/vinayreddy/Desktop/logs/vijay_escalation/truncatedmacs', 'w')
# with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
#     for mac in fh:
#         mac = mac.strip()[:6] + '\n'
#         fh2.write(mac)
#
# fh2.close()

import pprint
import operator
#
# macs_oui_list = []
# count = {}
# #fh2 = open('/Users/vinayreddy/Desktop/logs/vijay_escalation/truncatedmacs', 'w')
# with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
#     for mac in fh:
#         mac = mac.strip()[:6]
#         macs_oui_list.append(mac)
#
# for mac_oui in macs_oui_list:
#     count.setdefault(mac_oui, 0)
#     count[mac_oui] = count[mac_oui] + 1
#
# sorted_d = sorted(count.items(), key=operator.itemgetter(1), reverse= True)
#
# pprint.pprint(sorted_d)
#
# #fh2.close()
#
# # function to display the macs that are present when mac_oui is passed
#
# def macs(mac_oui):
#     with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
#         for mac in fh:
#             if mac_oui in mac:
#                 mac = mac.strip()
#                 print(mac)
#
# macs('0c5415')

#function to  split the macs at nth location and print the macs count.

def splitter(location):

    macs_oui_list = []
    count = {}
    with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
        for mac in fh:
            mac = mac.strip()[:location]
            macs_oui_list.append(mac)

    for mac_oui in macs_oui_list:
        count.setdefault(mac_oui, 0)
        count[mac_oui] = count[mac_oui] + 1
    sorted_d = sorted(count.items(), key=operator.itemgetter(1), reverse= True)
    return sorted_d

#    pprint.pprint(sorted_d)

mac_dict=splitter(6)
pprint.pprint(mac_dict)

#function to display split the macs at nth location and print the macs count.
#0c5415

def splitter_per_oui(oui,location):

    macs_oui_list = []
    count = {}
    with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
        for mac in fh:
            if oui in mac:
                mac = mac.strip()[:location]
                macs_oui_list.append(mac)

    for mac_oui in macs_oui_list:
        count.setdefault(mac_oui, 0)
        count[mac_oui] = count[mac_oui] + 1
    sorted_d = sorted(count.items(), key=operator.itemgetter(1), reverse= True)

#    pprint.pprint(sorted_d)
    return sorted_d

# function to display the macs that are present when mac_oui is passed

def macs(mac_oui):
    with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
        for mac in fh:
            if mac_oui in mac:
                mac = mac.strip()
                print(mac)

# mac_dict=splitter_per_oui('0c5415e', 8)
#
# pprint.pprint(mac_dict)
# to display the mac_oui and
for key,value in mac_dict:
    splitted_oui=splitter_per_oui(key, 6)
    #print(key + ' :', splitted_oui)
    with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/shllist/' + key , 'w') as fh2:
        with open('/Users/vinayreddy/Desktop/logs/vijay_escalation/macs', 'r') as fh:
            for mac in fh:
                if key in mac:
                    mac = mac.strip() + '\n'
                    fh2.write(mac)



