import users
import comment
import camera
import photo

import xml.etree.ElementTree as ET

# return a photo
aPhoto = photo.Photo()

def parseinfo(Id):
    try:
        labelfile = open('label.txt')
        labels = labelfile.readlines()
        xmlname = Id + '_exif.xml'
        filename = Id + '_info.txt'
        f=open(xmlname)
        tree = ET.parse(f)
        root = tree.getroot()
        exif = root.iter('exif')

        for p in root.iter('photo'):
            aPhoto.addPair('photoID', p.get('id'))
            cm = camera.Camera(p.get('camera'))
            aPhoto.setCamera(cm)
        for e in exif:
            for label in labels:
                if e.get('label') == label.strip():
                    child = e.getchildren()[0]
                    key = label.strip().replace(" ", "_").replace("-", "_")
                    value = child.text
                    aPhoto.addPair(key, value)

        f = open(filename)
        tree = ET.parse(f)
        root = tree.getroot()
        for v in root.iter('title'):
            aPhoto.addPair('title', v.text)
        owner = users.User()
        for us in root.iter('owner'):
            owner.addPair('nsid', us.get('nsid'))
            owner.addPair('username', us.get('username'))
            owner.addPair('realname', us.get('realname'))
            owner.addPair('location', us.get('location'))
            owner.addPair('iconserver', us.get('iconserver'))
        aPhoto.setOwner(owner)

        for p in root.iter('photo'):
            aPhoto.addPair('isFavorite', p.get('isfavorite'))
            aPhoto.addPair('safetyLevel', p.get('safety_level'))
            aPhoto.addPair('rotation', p.get('rotation'))

        visibility = root.iter('visibility')
        for v in visibility:
            aPhoto.addPair('isFamily', v.get('isfamily'))
            aPhoto.addPair('isFriend', v.get('isfriend'))
            aPhoto.addPair('isPublic', v.get('ispublic'))
        for a in root.iter('url'):
            aPhoto.addPair('url', a.text)
        for l in root.iter('location'):
            aPhoto.addPair('latitude', l.get('latitude'))
            aPhoto.addPair('longitude', l.get('longitude'))
            child = l.getchildren()
            aPhoto.addPair('country', child[0].text)
            aPhoto.addPair('region', child[1].text)
            aPhoto.addPair('county', child[2].text)
            aPhoto.addPair('neighbourhood', child[3].text)
        for d in root.iter('dates'):
            aPhoto.addPair('releaseTime', d.get('longitude'))
        for t in root.iter('editability'):
            aPhoto.addPair('canComment', t.get('cancomment'))
        for t in root.iter('usage'):
            aPhoto.addPair('canShare', t.get('canshare'))
            aPhoto.addPair('canPrint', t.get('canprint'))
            aPhoto.addPair('canBlog', t.get('canblog'))
            aPhoto.addPair('canDownload', t.get('candownload'))
        comments = comment.Comment()
        for t in root.iter('comments'):
            comments.addPair('text',t.text)
        aPhoto.setComment(comments)
        aPhoto.printPhoto()

    except Exception as e:
        print(e)
    finally:
        print('Done')

# call the function 'parseinfo'
parseinfo('8396784221')
















