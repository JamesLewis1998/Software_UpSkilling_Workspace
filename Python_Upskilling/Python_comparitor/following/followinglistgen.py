from bs4 import BeautifulSoup as BS
import os
import json


print("Current directory:", os.getcwd())

if os.path.exists('following_reformatted.html'):
    with open('following_reformatted.html', "r") as f:
        data = f.read()
else:
    print("Not found!")


with open('Python_Upskilling/Python_comparitor/following/following_reformatted.html', 'r', encoding='utf-8') as followingshtml:
    html_cont = followingshtml.read()
# Read HTML content from a file

# Parse the HTML content
soup = BS(html_cont, 'html.parser')

# Define empty followings list 
followingslist = []

# Extract text from all tags
followings = soup.find_all('div', class_='_a6-p')
for following in followings:
    paragraphs = following.find_all('a')  # Find all <p> tags within each <div class='content'>
    for p in paragraphs:
        print(p.get_text())
        followingslist.append(p.get_text())

followingslist.sort()

print(len(followingslist))
print(followingslist)

##      with open("Python_Upskilling/Python_comparitor/following/following_python_list.json", "w") as outfile:
##          json.dump(followingslist, outfile, indent=4)