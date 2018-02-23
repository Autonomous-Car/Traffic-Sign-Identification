# coding:utf-8
import json
import urllib
import cv2


def getImage(latitude=["40.1153915"], longitude=["-88.2332863"], heading=["270"], pitch=["0"],submit=""):
    latitude=float(latitude[0])
    longitude=float(longitude[0])
    heading=float(heading[0])
    pitch=float(pitch[0])

    if not (latitude >= -90 and
            latitude <= 90 and
            longitude > -180 and
            longitude <= 180 and
            heading >= 0 and
            heading < 360):
        return ""

    urlprefix = "https://maps.googleapis.com/maps/api/streetview?"
    heading %= 360
    params = {
        "size": "640x640",
        "location": "{0},{1}".format(latitude, longitude),
        "heading": heading,
        "pitch": pitch,
        "key": "AIzaSyBbQhzYbyV4csCYjf74KQUetJFMCPLIR6A"
    }
    filename = "{loc}-{hdg}-{pit}.jpg".format(**{
        "loc": "{0},{1}".format(latitude, longitude),
        "hdg": heading,
        "pit": pitch
    })
    url = urlprefix + urllib.urlencode(params)
    a = urllib.urlopen(url).read()
    fileprefix = "static/pictures/"
    if __name__ != '__main__':
        fileprefix = "TrafficSignIdentification/" + fileprefix
    with open(fileprefix + filename, "wb") as file:
        file.write(a)
        file.close()
    return filename

def stopSign(filename):
    print filename
    pic = cv2.imread(filename)
    print(pic)



if __name__ == '__main__':
    stopSign(getImage())

