import wmi

# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[0]

for things in nic_configs:
    print things

# IP address, subnetmask and gateway values should be unicode objects
ip = u'192.168.0.11'
subnetmask = u'255.255.255.0'
gateway = u'192.168.0.1'

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
print nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
print nic.SetGateways(DefaultIPGateway=[gateway])

for things in nic_configs:
    print things
    
# Enable DHCP
print nic.EnableDHCP()

print nic.Description

print nic.DHCPEnabled
print nic.DNSHostName

print nic.IPAddress[0]
print nic.IPSubnet[0]

    