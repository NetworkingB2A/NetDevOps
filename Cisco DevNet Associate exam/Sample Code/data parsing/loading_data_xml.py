import xml.etree.ElementTree as ET

# Load the XML file

tree = ET.parse("data_load.xml")

root = tree.getroot()

print(dir(tree))


print(ET.tostring(root, encoding='unicode', method='xml'))

print(root.attrib)
for child in root:
    for subchild in child:
        print(subchild.tag, subchild.attrib)

for child in root.find("Devices"):
    print(child.tag, child.attrib.get("name"))
