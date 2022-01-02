import zipfile
import os

def un_zipFiles(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                print(names)
                outpath = os.path.join(path, 'unzipped')
                zip_file.extract(names,outpath)
            zip_file.close() 
            os.remove(os.path.join(path, file))


un_zipFiles('G:/top_images/test')