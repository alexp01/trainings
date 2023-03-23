#https://www.studytonight.com/python-howtos/how-to-read-xml-file-in-python#:~:text=a%20single%20tree.-,Example%20Read%20XML%20File%20in%20Python,XML%20file%20using%20getroot()%20.
#https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
#https://linuxhint.com/parse_xml_python_beautifulsoup/

from bs4 import BeautifulSoup

with open('xml_to_parse.xml', 'r') as f:
    data = f.read()

# Passing the stored data inside the beautifulsoup parser
bs_data = BeautifulSoup(data, 'xml')

# Will search everywhere for tags with a specific name.
all_genre_atributes = bs_data.find_all('genre')
print('# New print :')
print(all_genre_atributes)
# Will print:
'''[<genre>Computer</genre>, <genre>Fantasy</genre>, <genre>Fantasy</genre>, <genre>Fantasy</genre>, <genre>Fantasy</genre>, <genre>Romance</genre>, <genre>Romance</genre>, <genre>Horror</genre>, <genre>Science Fiction</genre>, <genre>Computer</genre>, <genre>Computer</genre>, <genre>Computer</genre>]'''


# Will search everywhere for tags with a specific name.
# As this tag contains children it will display all
all_books = bs_data.find_all('book')
print('# New print :')
#print(all_books) # this will print all Tags 'book' with each content also.
print(all_books[2]) # will only print the third one in the list
# Will print:
'''
   <book id="bk103" test="2">
      <author> test5="value5" test6="value6">Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology
      society in England, the young survivors lay the
      foundation for a new society.</description>
	  This is a random text for bk103
   </book>
'''

# Will get the first encounter of a specific tag.
b_genre = bs_data.find('price')
print('# New print :')
print(b_genre)
# Will print:
'''
<price>44.95</price>
'''

b_name = bs_data.find('book', {'test':'0'})
print('# New print :')
print(b_name)
# Will print:
'''
<book id="bk101" test="0">
<author> test1="value1" test2="value2"&gt;Gambardella, Matthew</author>
<title>XML Developer's Guide</title>
<genre>Computer</genre>
<price>44.95</price>
<publish_date>2000-10-01</publish_date>
<description>An in-depth look at creating applications
      with XML.</description>
'''



