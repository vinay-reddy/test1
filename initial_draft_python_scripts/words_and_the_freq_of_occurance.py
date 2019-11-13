
from collections import Counter
import pprint

counter = Counter()
with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/policy-server/policy-server.log.0', 'r') as fh_read:
    for line in fh_read:
        words=line.split()
#        print(words)
        counter.update(words)
pprint.pprint(counter)