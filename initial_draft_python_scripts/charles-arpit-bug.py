
import pandas as pd
import csv

columns = ['radius_accounting_log_insert', 'id', 'user_name', 'nas_ip_address', 'nas_port', 'nas_port_type', 'calling_station_id', 'called_station_id', 'framed_ip_address', 'service_type', 'acct_status_type', 'acct_delay_time', 'acct_input_octets', 'acct_output_octets', 'acct_input_packets', 'acct_output_packets', 'acct_session_id', 'acct_authentic', 'acct_session_time', 'acct_terminate_cause', 'timestamp']



df = pd.read_csv('/Users/vinayreddy/Desktop/logs/charles-fdb/tmpO2glHJ/PolicyManagerLogs/var/avenda/tips/fdb/RadiusAccountingLog/RadiusAccountingLog.2019-10-18_15.fdb', header = None, names = columns)
df = df.reset_index()
b = df[['id', 'acct_status_type', 'timestamp']]
c = b[b.duplicated()]

c = c.groupby('id')
d = c.first()
print(d)
e = c.get_group('R050a538e-03-5daa1276')
#print(e)
# df = df.groupby('timestamp')
#
#
# a = df.first()
#