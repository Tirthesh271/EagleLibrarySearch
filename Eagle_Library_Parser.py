import xml.etree.ElementTree as ET
from pathlib import Path

user = input('Enter Username')
data =''
data =r"C:\Users"+"\\"+user+r"\Documents\EAGLE\libraries\usb_con-update.lbr"
print(data)
tree = ET.parse(data)
root = tree.getroot()

inp = input('Enter element to find: ')

#Find component from description
for i in root.iter('package'):
    if inp.lower() in i.attrib['name'].lower() or inp.lower() in str(i[0].text).lower():
        print(i.attrib['name'])