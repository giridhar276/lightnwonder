
import psutil

print(psutil.cpu_percent())

print(psutil.swap_memory())

print(psutil.virtual_memory())

print(psutil.disk_usage("C:\\"))    # windows
#print(psutil.disk_usage("/usr/bin")) # linux

print(psutil.disk_partitions())

print(psutil.net_connections())