# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:30:34 2020

@author: Geetu
"""
"""
In this one I added a score and made it say the score.
After asking a question, it deletes it from the list
Note: The list,not the dict
It also has an option of "quit". If you say quit it says"Have a nice day."
"Your score is" and then the score.
Very happy!
"""
score = 0
import pygame
(width,height) = (500,500)
screen = pygame.display.set_mode((width,height))
title = pygame.display.set_caption('Test 1')
pygame.display.flip()
Image = pygame.image.load("alexascreen2.jpg")
screen.blit(Image,(0,0))
pygame.display.update()
pygame.font.init()
white = (255,255,255)
font = pygame.font.Font('freesansbold.ttf',22)
#text = font.render('Hello',True,white)
#screen.blit(text,(250,250))
#pygame.display.update()
answer = "a"
dict1 = {"What is the capital of India?":"delhi",
             "Which country is known as 'The Hexagon'?":"france",
             "What is Jupiter's biggest moon?":"ganymede",
            "Where did the art of origami come from?":"japan",
             "Who wrote the Harry Potter series ?":"jk rowling"}

import speech_recognition as Athena
AudioIn = Athena.Recognizer()
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty(rate,125)
engine.say("Say 'quiz' for question")
engine.runAndWait()
with Athena.Microphone() as source:
  while answer != "quit":
    a = AudioIn.listen(source)
    answer=AudioIn.recognize_google(a)
    answer = answer.lower()
    if answer == "quiz":
        engine.say("Quiz time! Ready?")
        engine.runAndWait()
        import random
        question = random.choice(list(dict1))
        def textmessage(text,x,y):
           message = font.render(text,True,white)
           screen.blit(message,(x,y))
           pygame.display.update()
        textmessage(question,10,250)
        engine.say(question)
        engine.runAndWait()
        a = AudioIn.listen(source)
        answer=AudioIn.recognize_google(a)
        answer = answer.lower()
        true_answer = dict1.get(question)
        if answer == true_answer:
            textmessage("Correct!",10,280)
            engine.say("Correct")
            engine.runAndWait()
            textmessage("You said "+answer,10,300)
            engine.say("You said"+answer)
            engine.runAndWait()
            Image = pygame.image.load("alexascreen2.jpg")
            screen.blit(Image,(0,0))
            score = score+1
        elif answer == "quit":
            textmessage("Have a nice day",10,280)
            engine.say("Have a nice day")
            engine.runAndWait()
            textmessage("Your score is ",10,300)
            textmessage(str(score),10,320)
            engine.say("Your score is ")
            engine.say(score)
            engine.runAndWait()
            Image = pygame.image.load("alexascreen2.jpg")
            screen.blit(Image,(0,0))
        else:
            textmessage("Wrong!",10,280)
            engine.say("Wrong")
            engine.runAndWait()
            textmessage("You said "+answer,10,300)
            engine.say("You said"+answer)
            engine.runAndWait()
            Image = pygame.image.load("alexascreen2.jpg")
            screen.blit(Image,(0,0))
        del(dict1[question])
        length = len(dict1.keys())
        if length == 0 :
                textmessage("Hurray! Done",10,300)
                engine.say("Hurray! done")
                engine.runAndWait()
                textmessage("Have a nice day",10,350)
                engine.say("Have a nice day")
                engine.runAndWait()
                textmessage("Your score is :",10,360)
                textmessage(str(score),10,370)
                engine.say("Your score is :")
                engine.runAndWait()
                engine.say(score)
                engine.runAndWait()
                break
            

#while answer != "quit":
while True:
  for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
pygame.quit()