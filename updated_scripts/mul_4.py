import pandas as pd
import concurrent.futures
import multiprocessing
import datetime as dt
import re, timeit

start = dt.datetime.now()

f1_ro1 = re.compile(r'.*SessId (.*)')
f2_ro1 = re.compile(r'Service Categorization time = (.*)ms')
f3_ro1 = re.compile(r'.*The request has been categorized into service (.*)')
f4_ro1 = re.compile(r'.*user(.*) in (.*)')
f5_ro1 = re.compile(r'.*= (.*)ms')
f6_ro1 = re.compile(r'eap_peap')
f7_ro1 = re.compile(r'No.of requests in request processing tree: (.*)')
f8_ro1 = re.compile(r'.*user .*, domain (.*)')
f9_ro1 = re.compile(r'.*authenticated successfully')
f10_ro1 = re.compile(r'.*= (.*)ms')
f11_ro1 = re.compile(r'.*= (.*)ms')
f12_ro1 = re.compile(r'.*= (.*)ms')

columns_radius = ['Time', 'drop', 'Thread/RequestNo./SessionID', 'Level','Module', 'Message']
df_radius = pd.read_csv('/Users/vinayreddy/Desktop/logs/jeff_social_login/latest_logs/tmpZCO9pl/PolicyManagerLogs/tips-radius-server/radius.csv', names=columns_radius)
lines_count = df_radius.shape[0]

#s1 = dt.datetime.now()
df_session_lines = df_radius[df_radius['Thread/RequestNo./SessionID'].str.contains(' SessId ')]
session_lines_count = df_session_lines.shape[0]
#print(dt.datetime.now() - s1)

df_service_start=df_radius[df_radius['Message'].str.contains('Starting Service Categorization')]
df_service_time=df_radius[df_radius['Message'].str.contains('Service Categorization time')]
df_service=df_radius[df_radius['Message'].str.contains('The request has been categorized into service')]
df_user_found_in=df_radius[df_radius['Message'].str.contains('found user')]
df_lookup_time=df_radius[df_radius['Message'].str.contains('User lookup time')]
df_dot1x=df_radius[df_radius['Message'].str.contains('rlm_eap_peap: Initiate')]
df_tree_count=df_radius[df_radius['Message'].str.contains('No.of requests in request processing tree')]
df_domain=df_radius[df_radius['Message'].str.contains(' authenticating user ')]
df_usr_auth_time=df_radius[df_radius['Message'].str.contains('User Authentication time')]
df_policy_time=df_radius[df_radius['Message'].str.contains('Policy Evaluation time ')]
df_request_time=df_radius[df_radius['Message'].str.contains('Request processing time')]



#
# with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
#     # df_service_start = executor.submit(df_f1).result()
#     # df_service_time = executor.submit(df_f2).result()
#     # df_service = executor.submit(df_f3).result()
#     # df_user_found_in = executor.submit(df_f4).result()
#     # df_lookup_time = executor.submit(df_f5).result()
#     # df_dot1x = executor.submit(df_f6).result()
#     # df_tree_count = executor.submit(df_f7).result()
#     # df_domain = executor.submit(df_f8).result()
#     # df_usr_auth_time =  executor.submit(df_f9).result()
#     # df_policy_time = executor.submit(df_f10).result()
#     # df_request_time = executor.submit(df_f11).result()
#
#     results = [executor.submit(func).result() for func in [df_f1, df_f2, df_f3, df_f4, df_f5, df_f6, df_f7, df_f8, df_f9, df_f10, df_f11] ]

end = dt.datetime.now()

print(end - start)

