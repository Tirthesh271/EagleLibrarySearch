import xml.etree.ElementTree as ET
import os
=======

def findComponent(filePath, file):
    tree = ET.parse(filePath)
    root = tree.getroot()

    # Find component from description
    for i in root.iter('package'):
        try:
            if inp.lower() in i.attrib['name'].lower() or inp.lower() in str(i[0].text).lower():
                print("Component is ",i.attrib['name'], "\nLibrary is ",file)
        except:pass

    for i in root.iter('package3d'):
        try:
            if inp.lower() in i.attrib['name'].lower() or inp.lower() in str(i[0].text).lower():
                print("Component is ",i.attrib['name'], "\nLibrary is ",file)
        except:pass

    for i in root.iter('deviceset'):
        try:
            if inp.lower() in i.attrib['name'].lower() or inp.lower() in str(i[0].text).lower():
                print("Component is ",i.attrib['name'], "\nLibrary is ",file)
        except:pass
#user = input('Enter Username')
user ='tirthesh'#testing
path =str()
path = r"C:\Users" + "\\" + user + "\AppData\Roaming\Eagle\lbr"
print(path)

inp = input('Enter element to find: ')
#inp = 'ultrasonic'#testing

print("Main Library Directory:")
for rootdir, subdirs, files in os.walk(path):
    for file in files:
        if file.endswith('.lbr'):
            filePath = os.path.join(rootdir, file)
            findComponent(filePath, file)

print("Documents/Library:\n")
path =r"C:\Users"+"\\"+user+r"\Documents\EAGLE\libraries"
for rootdir, subdirs, files in os.walk(path):
    for file in files:
        if file.endswith('.lbr'):
            filePath = os.path.join(rootdir, file)
            try:
                findComponent(filePath,file)
            except:pass
=======
#Find component from description
for i in root.iter('package'):
    if inp.lower() in i.attrib['name'].lower() or inp.lower() in str(i[0].text).lower():
        print(i.attrib['name'])
