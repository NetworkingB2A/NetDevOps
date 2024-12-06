# Import modules
import sys
from helper import *

import yaml
import json

import xml.etree.ElementTree as ET

import xml.dom.minidom as MD

# Main function
if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print("DevNet")


    #########################################
    #              Procedure 2              #
    #########################################
    print('##################')
    print('###### YAML ######')
    print('##################')

    # Open the user.yaml file as read only
    with open("user.yaml", "r") as stream:

        # Load the stream using safe_load
        user_yaml = yaml.safe_load(stream)
    

    # Print the object type
    print("Type of user_yaml variable:")
    print(type(user_yaml))

    print('----------------------')

    # Iterate over the keys of the user_yaml and print them
    print('Keys in user_yaml:')

    for key in user_yaml:
        print(key)

    print('----------------------')

    # Create a new instance of class User
    user = User()

    # Assign values from the user_yaml to the object user    
    user.id = user_yaml.get('id')
    user.first_name = user_yaml.get('first_name')
    user.last_name = user_yaml.get('last_name')
    user.birth_Date = user_yaml.get('birth_date')
    user.address = user_yaml.get('address')
    user.score = user_yaml.get('score')
    
    # Print the user object
    print('User object:')
    print(user)


    #########################################
    #              Procedure 3              #
    #########################################
    print('##################')
    print('###### JSON ######')
    print('##################')

    # Create JSON structure from the user object
    user_json = json.dumps(user, default = serializeUser)
    
    # Print the created JSON structure
    print('Print user_json:')
    print(user_json)


    print('----------------------')

    # Create JSON structure with indents and sorted keys
    print('JSON with indents and sorted keys')
    print(json.dumps(user, sort_keys = True, indent = 4, default=serializeUser))


    #########################################
    #              Procedure 4              #
    #########################################
    print('######################')
    print('# XML - Element Tree #')
    print('######################')

    # Parse the user.xml file
    tree = ET.parse("user.xml")

    # Get the root element
    root = tree.getroot()

    # Print the tags
    print('Tags in the XML:')
    for element in root:
        print(element.tag)
    print('----------------------')

    # Print the value of id tag
    print('id tag value:')
    print(root.find("id").text)

    print('----------------------')

    # Find all elements with the tag address in root
    addresses = root.findall("address")

    # Print the adresses in the xml
    print('Addresses:')
    for address in addresses:
        print(address)
        print("Address:")
        for element in address:
            print(f"{element.tag} : { element.text}")


    print('----------------------')
    
    # Print the elements in root with their tags and values
    print('Print the structure')   
    for element in root.iter():
        print(f"{element.tag} : {element.text}")

    # Parsing XML files with MiniDOM 
    print('######################')
    print('### XML - MiniDOM ####')
    print('######################')

    # Parse the user.xml file
    dom = MD.parse("user.xml")

    # Print the tags
    for node in dom.childNodes:
        printTags(node.childNodes)


    print('----------------------')    

    # Accessing element value
    print('Accessing element value')
    idElements = dom.getElementsByTagName("id")
    print(idElements)
    elementId = idElements.item(0)
    print(elementId.childNodes)
    idValue = elementId.firstChild
    print(idValue)
    print('----------------------')

    # Print elements from the DOM with tag name 'address'
    print('Addresses:')
    for i in dom.getElementsByTagName("address"):
        printNodes(i.childNodes)

    print('----------------------')

    # Print the entire structure with printNodes
    print('The structure:')
    for i in dom.childNodes:
        printNodes(i.childNodes)


    #########################################
    #              Procedure 5              #
    #########################################
    print('######################')
    print('#   Use Namespaces   #')
    print('######################')

    # Parse the user.xml file
    itemTree = ET.parse("item.xml")


    # Get the root element
    itemRoot = itemTree.getroot()

    # Define namespaces
    namespaces = {
        "a": "https://www.example.com/network",
        "b": "https://www.example.com/furniture"
    }
    

    # Set table as the root element
    elementsInNSa = itemRoot.findall('a:table', namespaces)
    elementsInNSb = itemRoot.findall('b:table', namespaces)

    # Elements in NS a
    print('Elements in NS a:')
    for element in elementsInNSa:
        for item in element.iter():
            print(f"{item.tag}: {item.text}")

    print('----------------------')

    # Elements in NS b
    print('Elements in NS b:')
    for element in list(elementsInNSb[0]): 
        print(f"{element.tag}: {element.text}")