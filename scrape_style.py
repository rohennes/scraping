import bs4
import urllib.request
import random
import os
import webbrowser
import re
websites = ['https://redhat-documentation.github.io/supplementary-style-guide/']
# source = urllib.request.urlopen('https://www.york.com/').read()
# soup = bs.BeautifulSoup(source,'lxml')

#nav = soup.nav

#print(nav)

#for url in nav.find_all('a'):
#   print(url.get('href'))



def get_nav_bar(websites):
	sections_list = []
	for website in websites:
		source = urllib.request.urlopen(website).read()
		soup = bs4.BeautifulSoup(source,'lxml')
		mydivs = soup.find_all("div", {"class": "sect3"})
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("The sect3 content is the following:")
		for section in mydivs:
			sections_list.append(section)
		list_length = len(sections_list)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("There are ", list_length, "sections in the list.")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		random_num = random.randint(5,list_length)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("The random numnber is ", random_num)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		#print (sections_list[random_num])
		snippet = str(sections_list[random_num])

		pattern = "images\/yes\.png"
		yes_link = "https://redhat-documentation.github.io/supplementary-style-guide/images/yes.png"
		new_snippet = re.sub(pattern,yes_link,snippet)

		pattern = "images\/no\.png"
		no_link = "https://redhat-documentation.github.io/supplementary-style-guide/images/no.png"
		
		new_snippet = re.sub(pattern,no_link,new_snippet)
		#print(new_snippet)
		html = new_snippet
		path = os.path.abspath('temp.html')
		print(path)
		url = 'file:/' + path

		#with open(path, 'w') as f:
		#    f.write(html)
		#webbrowser.open(path)
		print(url)

get_nav_bar(websites)



# html = '<html> ...  generated html string ...</html>'
# path = os.path.abspath('.temp.html')
# url = 'file://' + path

# with open(path, 'w') as f:
#     f.write(html)
# webbrowser.open(url)
#print(nav)


#body = soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)