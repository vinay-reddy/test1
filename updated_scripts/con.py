
import concurrent.futures
import tarfile
import datetime as dt

start_time = dt.datetime.now()

file_list = []
#


with tarfile.open('/Users/vinayreddy/Desktop/logs/jeff_social_login/cppm-logs-2019-9-27-17-6-46.tar.gz', 'r')  as to:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [ executor.submit(to.extract(file)) for file in to.getnames()]
        print(results)

end_time1 = dt.datetime.now()

print('Time taken to extract = ', end_time1 - start_time)