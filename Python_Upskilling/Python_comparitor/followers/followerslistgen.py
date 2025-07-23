from bs4 import BeautifulSoup as BS
import os
import json

print("Current directory:", os.getcwd())

if os.path.exists('followers_reformatted.html'):
    with open('followers_reformatted.html', "r") as f:
        data = f.read()
else:
    print("Not found!")


with open('Python_Upskilling/Python_comparitor/followers/followers_reformatted.html', 'r', encoding='utf-8') as followershtml:
    html_cont = followershtml.read()
# Read HTML content from a file

# Parse the HTML content
soup = BS(html_cont, 'html.parser')

# Define empty followers list 
followerslist = []

# Extract text from all tags
followers = soup.find_all('div', class_='_a6-p')
for follower in followers:
    paragraphs = follower.find_all('a')  # Find all <p> tags within each <div class='content'>
    for p in paragraphs:
        print(p.get_text())
        followerslist.append(p.get_text())

followerslist.sort()

print(len(followerslist))
print(followerslist)

##        with open("Python_Upskilling/Python_comparitor/followers/followers_python_list.json", "w") as outfile:
##            json.dump(followerslist, outfile, indent=4)