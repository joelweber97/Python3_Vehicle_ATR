import zipfile
import os

def un_zipFiles(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                outpath = os.path.join(path, 'unzipped')
                zip_file.extract(names,outpath)
            zip_file.close() 


un_zipFiles('/Users/joelweber/github/Python3_Vehicle_ATR/full_images')