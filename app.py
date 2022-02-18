
from netmiko import  ConnectHandler

device = ConnectHandler(device_type='mikrotik', ip='192.168.88.10',username='admin',password='password')
output = device.send_command('show version')
print(output)
device.disconnect()