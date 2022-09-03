#!./.venv/bin/python
import psutil
import requests
import time, json, sys

try:
        company = sys.argv[1]
        asset = sys.argv[2]
        time_sleep = sys.argv[3]
except:
        company = 'premix'
        asset = 'grey'
        time_sleep = 2

def ping():

        try:    
                url=f'http://207.154.236.186:9000/fp/runtime'
                elapsed_total_seconds = requests.get(url).elapsed.total_seconds()
                return  elapsed_total_seconds
        except:
                return -1

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
        elapsed_total_seconds = ping()
        
        payload = json.dumps(
            {
            "cpu_percent": int(cpu_percent),
            "mem_used_percent": int(mem_used_percent),
            "ts": time.time_ns(),
            "delay": int(elapsed_total_seconds*1000)
            })

        url=f'http://207.154.236.186:9000/rest/api/asset/update?company={company}&asset={asset}'
        
        try:
                r=requests.post(url=url,data=payload)
                print(payload)
        except:
                pass
        time.sleep(int(time_sleep))
