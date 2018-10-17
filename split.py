property_transfer_xml = '''
<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento'; 
//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento'; 
//urn:multiCall/sessionId['?']</con:targetPath>'''

sourcePath = property_transfer_xml.split('sourcePath')[1].split('<')[0][1:]
targetPath = property_transfer_xml.split('targetPath')[1].split('<')[0][1:]

print(type(property_transfer_xml))
print(len(sourcePath))
print(len(targetPath))

#print(list(set(property_transfer_xml[0])))
#print(list(set(property_transfer_xml[1])))
#print(list(set(property_transfer_xml[2])))
#print(list(set(property_transfer_xml[3])))
#print(list(set(property_transfer_xml[4])))
#print(list(set(property_transfer_xml[5])))
#print(list(set(property_transfer_xml[6])))
#print(list(set(property_transfer_xml[7])))
#print(list(set(property_transfer_xml[8])))
#print(list(set(property_transfer_xml[9])))       
#print(list(set(property_transfer_xml[10])))      

print(sourcePath)
print(targetPath)