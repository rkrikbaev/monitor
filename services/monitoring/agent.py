#!./.venv/bin/python
import psutil
import requests
import time, json, sys


def ping(url):

        try:    
                elapsed_total_seconds = requests.get(url).elapsed.total_seconds()
                return  elapsed_total_seconds
        except:
                return -1

def checkIfProcessRunning(processName='beam.smp'):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if pinfo.get('name'):
                if processName.lower() in pinfo.get('name', 'noname').lower() :
                        listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects

def sendMessage(text):
        pass

def _get_cpu_percent(pid):
        """Get CPU percent used by process.
        """
        return psutil.Process(pid).cpu_percent()

def main(list_of_processes, url, time_sleep):

        while True:

                # by process
                by_process = []  
                for pname in list_of_processes:
                        if checkIfProcessRunning(pname[0])==False:
                                sendMessage(text='Process down: {pname[1]} is down!')
                        else:
                                processes = findProcessIdByName(pname[0])
                                for item in processes:
                                        if item.get('pid'):
                                                pid = item.get('pid')
                                                by_process.append(
                                                        {
                                                                pname[1]:_get_cpu_percent(pid)
                                                        })
                # total values
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
                elapsed_total_seconds = ping(url)
                
                payload = json.dumps(
                {
                "cpu_percent": int(cpu_percent),
                "mem_used_percent": int(mem_used_percent),
                "ts": time.time_ns(),
                "delay": int(elapsed_total_seconds*1000),
                "by_process": by_process
                })

                url=f'http://monitor.faceplate.io:9000/rest/api/asset/update?company={company}&asset={asset}'
                
                try:
                        r=requests.post(url=url,data=payload)
                        print(payload)
                except:
                        pass
                time.sleep(int(time_sleep))

if __name__ == "__main__":


        try:
                company = sys.argv[1]
                asset = sys.argv[2]
                time_sleep = sys.argv[3]
        except:
                company = 'test_company'
                asset = 'test_line'
                time_sleep = 10

        list_of_processes = [('beam.smp','faceplate'), ('firefox','browser')]
        url = f'http://{company}.faceplate.io:9000/fp/runtime'

        main(list_of_processes, url, time_sleep)