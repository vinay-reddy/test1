
import pandas as pd

#csv file generation

fh2 = open('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/log/httpd/http_csv.csv', 'w')


with open('/Users/vinayreddy/Desktop/logs/Gary/logs_march5/tmpVYKaK3/SystemLogs/var/log/httpd/ssl_access_log.1', 'r') as fh:
    for line in fh:
        line = line.strip()
        a = line.split()
        #        print(len(a),  a)

        #        print(a[0],a[3].split('[')[1], a[5].split('"')[1], a[6], a[7].split('"')[0], a[-1], sep=',')

        fh2.write(a[0] + ',' + a[3].split('[')[1]+','+ a[5].split('"')[1] + ',' + a[-1].split('µ')[0] +',' + a[6]+','+ a[7].split('"')[0] + '\n')

fh2.close()

pd.options.display.max_rows = 1200
pd.options.display.max_colwidth = 1000

# to-do: load from pandas

columns = ['IP address','Date and Time','HTTP Methods', 'Time taken', 'URL', 'HTTP']

pandas_load = pd.read_csv('/Users/vinayreddy/Desktop/logs/gregory-server-performance/tmp8AqQtA/SystemLogs/var/log/httpd/http_csv.csv', names= columns, header= None)

print(pandas_load)

print(pandas_load['Time taken'].dtype)

b = pandas_load.sort_values(by=['Time taken'], ascending=False)

series = b['URL']


c = series.value_counts(sort=True).to_frame()
print(c[:30])


ip_series = b['IP address'].value_counts(sort=True).to_frame()

# print(ip_series.columns)
ip_series.reset_index(inplace=True)
print(ip_series.columns)
ip_series_count = ip_series.rename(columns={'index': 'IP address', 'IP address': 'Count'})
print(ip_series_count)
#
# print(b)

# function with parameter as IP address and returns all the http requests done by that IP.

# def http_requests_per_ip(ip_address):
#     req_per_ip = b.loc[b['IP address'] == ip_address]
#     return req_per_ip
#
# req_per_ip =http_requests_per_ip('10.147.243.37')
# print(req_per_ip)