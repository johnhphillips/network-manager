import sys  
import wmi

if __name__ == "__main__":  
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

    if len(colNicConfigs) < 1:
        print "Can not get network configuration"
        exit()

    objNicConfig = colNicConfigs[0]

    ip = ['192.168.1.100']
    subnet = ['255.255.255.0']
    gateway = ['192.168.1.1']
    gatewayCostMetrics = [1]
    dnsServers = ['192.168.1.2','192.168.1.3']

    val = objNicConfig.EnableStatic(IPAddress = ip, SubnetMask = subnet)
    print val
    val = objNicConfig.SetGateways(DefaultIPGateway = gateway, GatewayCostMetric = gatewayCostMetrics)
    print val
    val = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder = dnsServers)
    print val

    print 'ip: ', ', '.join(objNicConfig.IPAddress)