from ncclient import manager

conn = manager.connect(host="192.168.56.101", port=830, username="cisco", password="cisco123!",
                        hostkey_verify=False, device_params={'name': 'csr'})
                    
config_hostname = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname>Apellido1-Apellido2</hostname>
 </native>
</config>"""
conn.edit_config(target='running', config=config_hostname)

config_loop = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>11</name>
    <ip><address><primary><address>11.11.11.11</address><mask>255.255.255.255</mask></primary></address></ip>
   </Loopback>
  </interface>
 </native>
</config>"""
conn.edit_config(target='running', config=config_loop)
print("Cambios aplicados")