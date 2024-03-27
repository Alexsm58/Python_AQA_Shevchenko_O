import xml.etree.ElementTree as ET


class XMLProcessor:
    def __init__(self, file_path):
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

    def xml_to_string(self):
        return ET.tostring(self.root, encoding='unicode')

    def string_to_xml(self, xml_string):
        self.root = ET.fromstring(xml_string)

    def add_custom_tag(self, tag_name, attributes=None):
        new_tag = ET.Element(tag_name, attrib=attributes)
        self.root.append(new_tag)

    def remove_custom_tag(self, tag_name):
        for child in self.root.findall('.//' + tag_name):
            self.root.remove(child)

    def get_elements_with_attributes(self, tag_name, attributes):
        elements = self.root.findall('.//' + tag_name)
        filtered_elements = []
        for element in elements:
            element_attributes = element.attrib
            if all(attr in element_attributes.items() for attr in attributes.items()):
                filtered_elements.append(element)
        return filtered_elements


# Приклад використання класу з файлом example.xml:
file_path = "example.xml"
xml_processor = XMLProcessor(file_path)

# Перегон XML в рядок
xml_as_string = xml_processor.xml_to_string()
print("XML як рядок:")
print(xml_as_string)

# Додавання кастомного тегу
xml_processor.add_custom_tag('custom_tag', {'attribute': 'value'})
print("\nXML з доданим кастомним тегом:")
print(xml_processor.xml_to_string())

# Видалення кастомного тегу
xml_processor.remove_custom_tag('custom_tag')
print("\nXML з видаленим кастомним тегом:")
print(xml_processor.xml_to_string())

# Отримання елементів з параметрами
filtered_elements = xml_processor.get_elements_with_attributes('food', {'name': 'Belgian Waffles'})
print("\nЕлементи з параметрами:")
for element in filtered_elements:
    print(ET.tostring(element, encoding='unicode'))
