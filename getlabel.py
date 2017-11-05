import main

import os

import xml.etree.ElementTree as ET


def parseinfo(xmlname,filename):
    try:

        labelfile = open('label.txt')
        labels = labelfile.readlines()

        writeText = ''
        f=open(xmlname)
        tree = ET.parse(f)
        root = tree.getroot()
        camera = 'Camera: '
        photoid = 'Photo ID: '
        photo = root.iter('photo')
        exif = root.iter('exif')

        for p in photo:
            camera = camera + p.get('camera') + '\n'
            photoid = photoid + p.get('id') + '\n'

        writeText = writeText + photoid + camera

        for e in exif:
            for label in labels:
                if e.get('label') == label.strip():
                    child = e.getchildren()[0]
                    temp = label.strip() + ': ' + child.text + '\n'
                    writeText = writeText + temp



        f = open(filename)
        tree = ET.parse(f)
        root = tree.getroot()
        photoid = 'Photo ID: '
        photo = root.iter('photo')
        title = root.iter('title')
        owner = root.iter('owner')
        UserID = 'User ID: '

        for user in owner:
            UserID = UserID + user.get('nsid') + '\n'
        writeText = writeText + UserID

        IsFavotite = 'IsFavorite: '
        SaveLevel = 'Save_Level: '
        Rotation = 'Rotation: '

        for p in photo:
            IsFavotite = IsFavotite + p.get('isfavorite') + '\n'
            SaveLevel = SaveLevel + p.get('safety_level') + '\n'
            Rotation = Rotation + p.get('rotation') + '\n'

        writeText = writeText + IsFavotite + SaveLevel + Rotation

        visibility = root.iter('visibility')
        IsFamily = 'IsFamily: '
        IsFriend = 'IsFriend: '
        IsPublic = 'IsPublic: '

        for v in visibility:
            IsFamily = IsFamily + v.get('isfamily') + '\n'
            IsFriend = IsFriend + v.get('isfriend') + '\n'
            IsPublic = IsPublic + v.get('ispublic') + '\n'

        writeText = writeText + IsFamily + IsFriend + IsPublic

        URL = 'URL: '

        address = root.iter('url')

        for a in address:
            URL = URL + a.text + '\n'

        writeText = writeText + URL

        location = root.iter('location')
        Site = 'Location: Country: '
        Latitude = 'Latitude: '
        Longitude = 'Longitude: '

        for l in location:
            Latitude = Latitude + str(l.get('latitude')) + '\n'
            Longitude = Longitude + str(l.get('longitude')) + '\n'

            child = l.getchildren()
            Site = Site + child[0].text + ', Region: ' + child[1].text + ', County: ' + child[2].text + ',' \
                                                                                                        ' Neighbourhood: ' + \
                   child[3].text + '\n'

        dates = root.iter('dates')
        ReleaseTime = 'ReleaseTime: '

        for d in dates:
            ReleaseTime = ReleaseTime + d.get('taken') + '\n'

        writeText = writeText + ReleaseTime

        cancomment = 'CanComment: '
        comment = 'commnent: '
        haspeople = 'haspeople: '

        candownload = 'CanDownload: '
        canshare = 'CanShare: '
        canprint = 'CanPrint: '
        canblog = 'CanBlog: '

        temp = root.iter('editability')

        for t in temp:
            cancomment = cancomment + t.get('cancomment') + '\n'

        writeText = writeText + cancomment

        temp = root.iter('usage')

        for t in temp:
            canshare = canshare + t.get('canshare') + '\n'
            canprint = canprint + t.get('canprint') + '\n'
            canblog = canblog + t.get('canblog') + '\n'
            candownload = candownload + t.get('candownload') + '\n'

        writeText = writeText + candownload + canshare + canprint + canblog

        temp = root.iter('comments')

        for t in temp:
            comment = comment + t.text + '\n'

        writeText = writeText + comment

        temp = root.iter('people')

        for t in temp:
            haspeople = haspeople + t.get('haspeople') + '\n'

        writeText = writeText + haspeople

        writeText = writeText + Longitude + Latitude + Site


        # f = open('temp.txt', 'w')

        writeText = writeText + UserID
        UserName = 'UserName: '
        RealName = 'RealName: '
        iconsever = 'iconserver: '
        temp = root.iter('owner')

        for user in temp:
            UserName = UserName + user.get('username') + '\n'
            RealName = RealName + user.get('realname') + '\n'
            iconsever = iconsever + user.get('iconserver') + '\n'
        writeText = writeText + UserName + RealName + Site + iconsever


        print (writeText)



        f = open('temp.txt', 'a')
        f.writelines(writeText)
        f.close()


    except Exception as e:
        print(e)
    finally:
        print('Done')











parseinfo('8396784221_exif.xml','29126181995_info.txt')
















