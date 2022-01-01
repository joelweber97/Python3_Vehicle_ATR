from bs4 import BeautifulSoup
import wget
import os

with open('html.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    links = []
    for a in soup.find_all('a', class_="ant-btn ant-btn-link", href=True):
        links.append(a['href'])

    #print(links)
    print('success')
    links2 = []
    for i in links:
        if 'nc.zip' in i:
            links2.append(i)
    
    links3 = links2[:1]
    #print(links3)


    output_dir = './full_images'
    for i in links3:
        #print(i)
        name = i.split('/')[-1]
        print(name)
        print(os.path.join(output_dir, name))
        wget.download(i, os.path.join(output_dir, name))