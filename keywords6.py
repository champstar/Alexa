# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:44:12 2020

@author: Geetu
"""
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty(rate,125)

dict1 = {"nebula":"A cloud of gas and dust in space;It forms new stars ",
         "astronomy":"The study of celestial objects such as stars,planets etc and phenonema that originate outside the Earth's atmosphere"
         ,"nicolaus copernicus":"proposed a heliocentric system, that is the idea that the Sun was at the centre and not the Earth.",
         "galileo galilei":"resurfaced heliocentricity, and discovered four of Jupiters moons - Io Europa Ganymede Callisto",
         "heliocentrism":"the idea that the Sun was at the centre and not the Earth.",
         "andromeda galaxy":"considered the Milky Way's twin galaxy",
        "variable stars":"any star whose brightness fluctuates as seen from Earth",
        "halley's comet":"A comet which can be seen once every 74 years, discovered by Edmond Halley",
        "constellations":"A constellation is an area on the celestial sphere in which a group of stars forms an imaginary outline or pattern. First noted by Babylonians.",
        "supermoon":"A point in time when the moon is closer to Earth. The moon appears larger than usual."}
engine.say("Dictionary of Astronomy")
engine.say("Enter a phrase or word")
engine.runAndWait()
keyword = input("Enter a phrase/word:")
keyword = keyword.lower()
if keyword in dict1:
    print(dict1.get(keyword))
    engine.say(keyword)
    engine.say(dict1.get(keyword))
    engine.runAndWait()