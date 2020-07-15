from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

# <h1> its a header tag
# <p> is a paragraf tag

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_h1_tag(): # find function is checking for tags like <body>, <h1>
    h1_tag = simple_soup.find('h1') # find is just giving 1 found element, the first
    return h1_tag.string # string is a property of h1_tag objects

def find_all_li_tags():
    list_items = simple_soup.find_all('li') # find is just giving 1 found element, the first
    return list_items # string is a property of h1_tag objects

def find_paragraf_tag_with_subtitle():
    subtitle_tag = simple_soup.find('p', {"class": "subtitle"}) # find function has as an argument, a Dict where you can put the arguments that you want to match in your html tag
    return subtitle_tag.string

def find_the_other_paragraph():
    list_of_paragraph = simple_soup.find_all('p')
    other_paragraph = [p for p in list_of_paragraph if 'subtitle' not in p.attrs.get('class', [])]
    # instead of p.attrs.get('class' you can do p.attrs['class']). As atributes are seend as Dict by python. But if there is no class element in that Dict, you get a KeyError.
    # i added a second argument to the get function, as whitout it it will return None in case there is no class argument in the html tag
    # and if the get fct returns None you can not do : if 'subtitle' not in None. It can not compare something with None.
    # thats why i return an empty list in case the get does not find such an ergument called 'class'
    return other_paragraph[0].string

print(find_h1_tag())
print(find_all_li_tags())

list_of_li = find_all_li_tags()
#list_of_li = [str(item)[4:-5] for item in list_of_li] # its not the easier way to fetch just the string content
list_of_li = [e.string for e in list_of_li] # this is easier as its using the string property of the list_of_li object
print(list_of_li)

print(find_paragraf_tag_with_subtitle())

print(find_the_other_paragraph())