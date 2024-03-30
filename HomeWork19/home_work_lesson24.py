from xml.etree import ElementTree

class BreakfastMenu:
    def __init__(self, path):
        self.path = path
        self.tree = ElementTree.parse(path)
        self.root = self.tree.getroot()

    def xml_to_string(self):
        return ElementTree.tostring(self.root, encoding='utf-8').decode('utf-8')

    def string_to_xml(self, xml_string):
        self.root = ElementTree.fromstring(xml_string)
        self.tree = ElementTree.ElementTree(self.root)

    def add_custom_tag(self, tag, value):
        custom_tag = ElementTree.Element(tag)
        custom_tag.text = value
        self.root.append(custom_tag)

    def remove_custom_tag(self, tag):
        for elem in self.root.findall(tag):
            self.root.remove(elem)

    def get_elements_with_parameters(self, parameter):
        elements = []
        for food in self.root.iter('food'):
            if parameter in food.attrib:
                elements.append(food.attrib[parameter])
        return elements

# Пример использования класса

# Создание экземпляра класса BreakfastMenu
menu = BreakfastMenu('example.xml')

# Преобразование XML в строку
xml_string = menu.xml_to_string()
print("XML в строке:")
print(type(xml_string))

# Добавление кастомного тега
menu.add_custom_tag('custom_tag', 'Custom Value')

# Удаление кастомного тега
menu.remove_custom_tag('custom_tag')

# Получение элементов с параметром
elements_with_parameters = menu.get_elements_with_parameters('waffle_name')
print("Элементы с параметром 'waffle_name':")
print(elements_with_parameters)
