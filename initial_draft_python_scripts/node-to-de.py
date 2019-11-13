import os,sys

path = '/Users/vinayreddy/Desktop/logs/vijay_escalation/shllist'


#res = '-'.join(test_str[i:i + 2] for i in range(0, len(test_str), 2))

for file in os.listdir('/Users/vinayreddy/Desktop/logs/vijay_escalation/shllist'):
    if file =='shlmacs':
        continue
    else:
        with open( path + '/'+file , 'r') as fh:
            with open( '/Users/vinayreddy/Desktop/logs/vijay_escalation/shllist/shlmacs/'  + file, 'w') as fh2:
                for mac in fh:
                    mac = mac.strip()
                    mac = '-'.join(mac[i:i + 2] for i in range(0, len(mac), 2)).upper()
                    print(mac)
                    fh2.write(mac  + '\n')
