from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
root = tree.getroot()
for food in root:
    print(root)

decoded_to_str = ElementTree.tostring(root).decode()
print(type(decoded_to_str))

changes = decoded_to_str.replace('<calories>950</calories>', '<calories>50</calories>')
encoded_res = ElementTree.fromstring(changes)
print(type(encoded_res))
food_five = encoded_res[4]
for parameter in food_five:
    if parameter.tag == 'calories':
        print(parameter.text, parameter.attrib['waffle_name'])