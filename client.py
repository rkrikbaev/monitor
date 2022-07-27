#!./.venv/bin/python
import psutil
import requests
import time, json, sys

# # gives a single float value
# psutil.cpu_percent()
# # gives an object with many fields
# psutil.virtual_memory()
# # you can convert that object to a dictionary 
# dict(psutil.virtual_memory()._asdict())
# # you can have the percentage of used RAM
# psutil.virtual_memory().percent
# 79.2
# # you can calculate percentage of available memory
# psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
# 20.8

company = sys.argv[1]
unit_name = sys.argv[2]
time_sleep = sys.argv[3]

while True:
        # gives a single float value
        cpu_percent= psutil.cpu_percent()
        cpu_count=psutil.cpu_count()
        cpu_times_per=psutil.cpu_times_percent()
        # gives an object with many fields
        psutil.virtual_memory()
        # you can convert that object to a dictionary
        virtual_memory= dict(psutil.virtual_memory()._asdict())
        # you can have the percentage of used RAM
        mem_used_percent= psutil.virtual_memory().percent
        # you can calculate percentage of available memory
        mem_avail_per= psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        mem_total=psutil.virtual_memory().total
        
        payload = json.dumps(
            {
            "cpu_percent": cpu_percent, 
            "mem_used_percent":mem_used_percent,
            "mem_avail_percent":mem_avail_per,
            "mem_total":mem_total
            })

        url=f'http://207.154.236.186:9000/rest/api/{company}/{unit_name}'
        
        try:
                print(payload)
                r=requests.post(url=url,data=payload)
                print(r.status_code)
        except Exception as exc:
                print(exc)
        
        time.sleep(int(time_sleep))
