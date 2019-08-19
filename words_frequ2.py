
from collections import Counter
import pprint
import re

exclude_words = ['-', 'Req', '[main]', 'rlm_policy:', 'are', 'of', 'RadiusServer.Radius', 'The', 'from', '=', 'rlm_service:', '[Th', 'SessId', '(80)' ]
counter = Counter()
reg_obj = re.compile(r'\d{4}-\d{2}-\d{2}')

with open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/PolicyManagerLogs/tips-radius-server/radius.log.0', 'r') as fh_read:
    for line in fh_read:
        words=line.split()
        # for word in words:
        #     if word in exclude_words:
        #         words.remove(word)
        # #        print(words)
        counter.update(words)
counter = counter
pprint.pprint(counter.most_common(25))