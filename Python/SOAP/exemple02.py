# This exemple will parse the content of xml_to_parse2 by using the ElementTree library
# The atributes are a dict

# Source : https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

tree = ET.parse('xml_to_parse2.xml')
# if you don't want to get it from a file you can also fetch it from a string using:
# root = ET.fromstring("string_with_xml_content")

root = tree.getroot()
print(root)

print('# New print :')
print(root.tag)
# will print:
'''data'''

print('# New print :')
print(root.attrib)
# will print:
'''{}'''
# as the 'data' tag contains dictionaries and not atributes.

print('# New print :')
for child in root:
    print(child.tag, child.attrib)
# will print:
'''
country {'name': 'Liechtenstein', 'test_atribute1': 'test01'}
country {'name': 'Singapore'}
country {'name': 'Panama', 'unique_atribute': 'test02'}
'''
#we ask here to print all children Tags of "ROOT" and the TAG atributes

print('# New print :')
print(root[0][1].text)
# will print:
'''
2008
'''

print('# New print :')
print(root[0][3].text)
# will print:
'''
This is a test text inside a tag
'''

print('# New print :')
print(root[0].attrib)
# will print:
'''
{'name': 'Liechtenstein', 'test_atribute1': 'test01'}
'''

print('# New print :')
print(root[0].attrib['test_atribute1'])
# will print:
'''
test01
'''

# This will loop inside all tags also inside each child and child of child.
print('# New print :')
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
# will print:
'''
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}
'''

# When we loop over an element we can get its atributes value with "country.get('test_atribute1')"
# Or we can loop over its children and find a particular element with : country.find('rank'). Here ca can acess its atribute of text.
print('# New print :')
for country in root.findall('country'):
    rank = country.find('rank').text #Element.find() finds the first child with a particular tag, and Element.text accesses the element’s text content.
    name = country.get('name') #Element.get() accesses the element’s attributes
    special = country.get('test_atribute1')
    print(name, rank, special)
# will print:
'''
Liechtenstein 1 test01
Singapore 4 None
Panama 68 None
'''

print('# New print :')
for country in root.findall('country'):
    neighbor = country.find('neighbor')
    #name = country.get('name') #Element.get() accesses the element’s attributes
    #special = country.get('test_atribute1')
    print(neighbor.attrib, neighbor.attrib['direction'], neighbor.attrib['name'], neighbor.text )
# will print:
'''
{'name': 'Austria', 'direction': 'E'} E Austria This is a test text inside a tag
{'name': 'Malaysia', 'direction': 'N'} N Malaysia None
{'name': 'Costa Rica', 'direction': 'W'} W Costa Rica None
'''