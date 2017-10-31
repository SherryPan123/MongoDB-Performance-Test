#coidng=utf-8

import os

import xml.etree.ElementTree as ET



filepath=r'E:\all_data'

os.chdir(filepath)

files=os.listdir(filepath)


for file in files:
    (filename,filetail)=os.path.splitext(file)
    if filename[-4:]=='exif':
        os.rename(file,filename+'.xml')

files=os.listdir(filepath)


for file in files:
    if file.endswith('xml'):
        try:
            writeText=''
            tree=ET.parse(file)
            root=tree.getroot()
            camera='Camera: '
            photo=root.iter('photo')
            exif=root.iter('exif')

            for p in photo:
                camera=camera+p.get('camera')+'\n'

            writeText=writeText+camera


            for e in exif:
                labellist=e.get('label')
                labellist=labellist.split('\n')
                for label in labellist:
                    if e.get('label')==label:
                        child=e.getchildren()[0]
                        temp = label + ': ' + child.text + '\n'
                        writeText=writeText+temp
                print writeText
            (filename, filetail) = os.path.splitext(file)
            savename=filename[0:len(filename)-4]+'_geo.txt'
            f=open(savename,'w')
            f.writelines(writeText)
            f.close()



        except Exception as e:
            print e
        finally:
            print 'done'


