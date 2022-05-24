import psutil
import platform
import socket
import os
import time
import datetime

def GetTimeStmp():
    return time.mktime(datetime.datetime.now().timetuple())

def GetOSInfo():
    os = platform.system()
    versionInfo = platform.version()
    version = versionInfo.split('.')
    bitInfo = platform.machine()
    bit = 32
    if '64' in bitInfo:
        bit = 64
    elif '86' in bit:
        bit = 32
    return os, version[0], bit

def GetHostName():
    return socket.gethostname()

def GetMachineModel():
    if psutil.WINDOWS:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DESCRIPTION\System\BIOS')
        value, tmp = winreg.QueryValueEx(key, "SystemVersion")
        return value
    else:
        return 'Mac ' + socket.gethostname()

def GetMacAddress():
    wifi_mac = ''
    ehternet_mac = ''
    if psutil.WINDOWS:
        result = os.popen('getmac')
        strRead = result.read()
        lst = strRead.splitlines()
        if len(lst) > 4:
            ehternet_mac = lst[3].split(" ")[0]
            wifi_mac = lst[4].split(" ")[0]
        elif len(lst) > 3:
            ehternet_mac = lst[3].split(" ")[0]
    else:
        for name, info in psutil.net_if_addrs().items():
            if 'en0' in name:
                for addr in info:
                    if 18 == addr.family:
                        wifi_mac = addr.address
            if 'Ethernet' in name:
                for addr in info:
                    if -1 == addr.family:
                        ehternet_mac = addr.address
    return 'internet Mac：'+ehternet_mac+'\n'+'Wifi Mac：'+wifi_mac

class GetCpuInfo:
    def name():
        cpu_info = str(platform.processor())
        return cpu_info
    def count():
        cpu_info = '核心数：'+str(psutil.cpu_count(logical=False))+'核心'
        return cpu_info
    def thread():
        cpu_info = '线程数：'+str(psutil.cpu_count())+'线程'
        return cpu_info
    def freq():
        cpu_info = 'CPU频率：'+str(psutil.cpu_freq()[2] / 1000)+'GHz'
        return cpu_info

def GetCpuPercent():
    return psutil.cpu_percent()

def GetTotalMemory():
    return '总共'+ str(round(psutil.virtual_memory().total //1000000000))+'GB'

def GetBatteryRemaining():
    battery_remaining = ''
    if psutil.sensors_battery():
        battery_remaining = psutil.sensors_battery().percent
    return battery_remaining

def GetProcessRunInfo(process_name: list):
    cpu_percent = 0
    memory_usage = 0
    for process in psutil.process_iter():
        try:
            if process.name() in process_list:
                cpu_percent += process.cpu_percent()
                memory_usage += process.memory_info().rss
        except (psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return cpu_percent, memory_usage

print(GetMacAddress())