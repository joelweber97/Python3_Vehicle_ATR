from bs4 import BeautifulSoup
import wget
import os

#works for the top_2016 html file and associated jp2 imagery

with open('./top_2016.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    links = []
    for a in soup.find_all('a', class_="ant-btn ant-btn-link", href=True):
        links.append(a['href'])

    #print(links)
    print('success')
    links2 = []
    for i in links:
        if 'nc-cir.zip' in i:
            links2.append(i)
    print(len(links2))

    links3 = links2[:2]
    count = 1
    output_dir = r'G:/top_images'
    for i in links2:
        print(count)
        print(i)
        name = i.split('/')[-1]
        print(name)
        output_file = os.path.join(output_dir, name)
        print(output_file, output_dir)
        count += 1
        if os.path.exists(output_file):
            pass
        else:
            wget.download(i, output_file)
        


'''
#works for the naip_2020 html file and associated sid imagery

with open('naip_2020.html', 'r') as f:
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

    output_dir = './full_images'
    for i in links2:
        #print(i)
        name = i.split('/')[-1]
        print(name)
        print(os.path.join(output_dir, name))
        wget.download(i, os.path.join(output_dir, name))

'''
