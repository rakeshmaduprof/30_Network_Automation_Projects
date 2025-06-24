from easysnmp import Session

def snmp_get(ip, community, oid):
    try:
        session = Session(hostname=ip, community=community, version=2)
        result = session.get(oid)
        return result.value
    except Exception as e:
        return f"Error: {e}"

def get_device_stats(ip, community):
    stats = {
        "uptime": snmp_get(ip, community, '1.3.6.1.2.1.1.3.0'),       # SysUpTime
        "interfaces": snmp_get(ip, community, '1.3.6.1.2.1.2.1.0'),   # IfNumber
        "cpu": snmp_get(ip, community, '1.3.6.1.4.1.9.2.1.57.0') # You can add real OID here for CPU if available
    }
    return stats
