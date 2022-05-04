import asyncio
from pysnmp.hlapi.asyncio import *

@asyncio.coroutine
def run():
    snmpEngine = SnmpEngine()
    errorIndication, errorStatus, errorIndex, varBinds = yield from sendNotification(
        snmpEngine,
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('demo.snmplabs.com', 162)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity('1.3.6.1.6.3.1.1.5.2')
        ).addVarBinds(
            ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
            ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
        )
    )

    if errorIndication:
        print(errorIndication)
    snmpEngine.transportDispatcher.closeDispatcher()
    
import socket  
host,port = ('localhost', 5556)
agent= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
    agent.connect((host, port))
    print("agent connecté") 
    asyncio.get_event_loop().run_until_complete(run())
except:
    print("connexion au serveur échouée")
    
