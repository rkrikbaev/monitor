#!./.venv/bin/python
import psutil
import requests
import time, json, sys

company = sys.argv[1]
unit_name = sys.argv[2]
time_sleep = sys.argv[3]

while True:
        # gives a single float value
        cpu_percent= psutil.cpu_percent()
        cpu_count=psutil.cpu_count()
        cpu_times_per=psutil.cpu_times_percent()
        # gives an object with many fields
        # psutil.virtual_memory()
        # you can convert that object to a dictionary
        virtual_memory= dict(psutil.virtual_memory()._asdict())
        # you can have the percentage of used RAM
        mem_used_percent= psutil.virtual_memory().percent
        # you can calculate percentage of available memory
        mem_avail_percent= psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        mem_total=psutil.virtual_memory().total
        
        payload = json.dumps(
            {
            "cpu_percent": cpu_percent,
            "mem_used_percent":mem_used_percent,
            "mem_total":mem_total,
            "ts": time.time_ns()
            })

        url=f'http://207.154.236.186:9000/rest/api/{company}/{unit_name}'
        
        try:
                r=requests.post(url=url,data=payload)
        except:
                continue
        time.sleep(int(time_sleep))
