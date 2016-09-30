''' 
This is an example demonstrating how to use the MMM Speaker class with the 
Customizable Robot Face Module. Here, the robot will say computer science
jokes compiled from the following links at timed intervals:

#http://www.devtopics.com/best-programming-jokes/
#http://www.hongkiat.com/blog/programming-jokes/
#http://www.ducksters.com/jokes/computer.php
#http://stackoverflow.com/questions/234075/what-is-your-best-programmer-joke 
'''

# Import all libraries
from MMM_Speaker import Speaker   #Make sure you have pyOSC installed! https://pypi.python.org/pypi/pyOSC
import time
import sys

# Create a speaker:
speaker = Speaker();

#Create a list of jokes:
jokes = ["In order to understand recursion, you must first understand recursion", 
 "",
 "A guy walks into a bar and asks for 1.014 root beers.",
 "The bartender says, I will have to charge you extra, that is a root beer float.",
 "So the guy says In that case, better make it a double.",
 "",
 "An S E O Expert walks into a bar, pub, public house, inn, restaurant, club.",
 "",
 "There are ten kinds of people in this world.",
 "Those who understand binary, and those who don't.",
 "",
 "Why did the programmer quit his job?",
 "Because he didn't get arrays.",
 "",
 "There is no place like 1 2 7 dot 0 dot 0 dot 1.",
 "",
 "I would tell you a U D P joke, but you might not get it.",
 "",
 "Knock knock.",
 "Race condition.",
 "Who is there?",
 "",
 "Why do programmers always confuse Halloween with Christmas?",
 "Because Oct 31 equals Dec 25.",
 "",
 "The generation of random numbers is too important to be left to chance.",
 "",
 "What do you call 8 Hobbits?",
 "A Hobbite.",
 "",
 "What is the object oriented way to get rich?",
 "Inheritance.",
 "", 
 "There are ten kinds of people in this world.",
 "Those who understand ternary, those who don't, and those who thought this was a binary joke.",
 "",
 "What is a Computer Scientist's favourite hangout place?",
 "Foo Bar.",
 "",
 "What do computers and air conditioners have in common?",
 "They both become useless when you open Windows.",
 "",
 "The word algorithm was coined to recognise Al Gore's contribution to computer science.",
 "",
 "A computer scientist can't get out of the shower,",
 "because the shampoo bottle said lather, rinse, repeat.",
 "",
 "What did the spider do on the computer?",
 "Made a website!",
 "",
 "How many programmers does it take to change a lightbulb?",
 "None, that's a hardware problem.",
 "",
 "When your hammer is C plus plus, everything begins to look like a thumb.",
 "",
 "Unix is user friendly.",
 "It's just very particular who its friends are.",
 "",
 "A Foo walks into a Bar, takes a look around, and says Hello World.",
 "",
 "Why don't jokes work in octal?",
 "Because 7 10 11.",
 "",
 "Don't anthropomorphize computers.", 
 "They hate that.",
 "",
 "Two bytes meet. The first asks, Are you ill?",
 "The second byte replies, No, just feeling a bit off.",
 "",
 "Two threads walk into a bar.",
 "The barkeeper says, I want don't any conditions race like time last!",
 "",
 "Old C programmers never die, they're just cast into void.",
 "",
 "If you listen to a UNIX shell, can you hear the C?",
 "",
 "If Java is the answer, the question must have been really verbose.",
 "",
 "Why doesn't C plus plus have a garbage collector?",
 "Because there would be nothing left!",
 "",
 "Why do Assembly programmers wear scuba diving gear?",
 "Because they work below C level.",
 "",
 "In theory, there ought to be no difference between theory and practice. In practice, there is.",
 "",
 "Why do Java programmers wear glasses?",
 "Because they don't C Sharp.",
 "",
 "Why do we need to comment our code?",
 "If it was hard to write, it should be hard to understand.",
 "",
 "Ah, you think syntax is your ally?",
 "You merely adopted the syntax. I was born in it.",
 "",
 "Hardware is the part of the computer you can kick.",
 "",
 "An optimist person will say that the glass is half-full.",
 "A pessimist person will say that the glass is half-empty.",
 "A programmer will say that the glass is twice as large as necessary.",
 "",
 "What is the definition of programmer?",
 "Programmer: a machine that turns coffee into code.",
 "",
 "Why did Microsoft name their search engine Bing?",
 "B Because I It's N Not G Google.",
 "",
 ]

joke = 0;
 
# Tell jokes in an infinite loop:
while(True):
  text = jokes[joke]
  speaker.speak(text)
  print(text)
  joke = joke + 1
  if(len(text) > 0):
    time.sleep(8.0)
  else:
    time.sleep(5.0)
  if(joke >= len(jokes)):
    joke = 0
