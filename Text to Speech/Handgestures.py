#Hand Gesture Detection / Text-to-speech
import random
import cv2
from tkinter import *
from tkinter.ttk import *
import pyttsx3

p={0:['Hello there! What can I do for you today?',
                'Hello sunshine! How are you on this beautiful day?',
                'Hello, hello! Is this Kartikeya I am speaking to?',
                'A hearty hello to you, friend! What is bringing you around?',
                'Hello and welcome! Do not hesitate to ask if you need anything.'],

    1:["Yes, absolutely! Iam happy to help in any way I can.",
              "Yes, that sounds like a great plan! Let us get started.",
              "You can definitely count on me for that. Yes, for sure!",
              "I hear you loud and clear. Yes, that is correct.",
              "Affirmative! Consider it done"],

    2:['No problem at all! Just let me know if you have any other questions.',
             'Hmm, that is not quite right. Perhaps let us try a different approach?',
             'I understand. Is there anything else I can assist you with today?',
             'Unfortunately, that is not possible. But here is an alternative...',
             'No worries! Do not be shy to ask if you need something else.'],
             
    3:[ 'Thank you so much! Iam glad I could be of help.',
                    'It is my pleasure! Thanks for letting me assist you.',
                    'You are very welcome! Do not hesitate to reach out again.',
                    'I appreciate your kind words! Thank you for choosing me.',
                    'No need to thank me! It is what I am here for. Have a great day!'],

    4:['Aww, thanks! I appreciate the sentiment.',
                    'That is sweet of you to say! Sending you lots of positive vibes.',
                    'While I don not have emotions, I can understand and appreciate your expression. Happy you are here!',
                    'I am not capable of feeling love, but I am happy to hear you are feeling it! Have a wonderful day!',
                    'That is a beautiful expression! I wish you all the best in your relationships.'], 

    5:['That is good to hear! I am happy things are going well.',
                'Good news! Sounds like you are on the right track.',
                'That is fantastic! Keep up the good work!',
                'Excellent! That is definitely a positive step.',
                'Glad to hear it! Wishing you continued success.'],

    6:['Best of luck in your endeavors! You have got this!',
                     'Sending you all the best! I believe in you!',
                     'Go for it! May your efforts be rewarded.',
                     'Here is to a successful outcome! Wishing you the best.',
                     'I am rooting for you! You have got this, go crush it!'],

    7:['Enjoy yourself! Make the most of it.',
                'I hope you have a wonderful time! Relax and soak it all in.',
                'May you experience great joy and satisfaction! Enjoy every moment.',
                'Wishing you endless fun and happiness! Go forth and enjoy!',
                'Make some amazing memories! Have a blast!'],
       
    8:['Excellent! That is a fantastic result',
                    'Absolutely wonderful! Impressive work!',
                    'Outstanding! You should be proud of yourself.',
                    'Simply superb! You have exceeded expectations.',
                    'Bravo! A true masterpiece!'],
       
    9:['How are you doing today?',
                    'I am happy to chat if you would like.',
                    'What is going on in your world? Let me know if you need anything.',
                    'Hope you are having a fantastic day! Anything exciting happening?',
                    'Feeling good? Do not hesitate to share your thoughts.',
                    ]              
                                                                                                         }
    


 
# Generates a random number between
# a given positive range

#print(type(r1))
KeyWord=["Hello","Yes","No","ThankYou","ILoveYou","Good","BestOfLuck","Enjoy","Excellent","HowAreYou"]
index=random.randint(0,9)
KeyWord_Chosen=KeyWord[index]
print(KeyWord_Chosen)
r2=index
r1 = random.randint(0, 5)

l=p[r2][r1]
print(l)


# This will import all the widgets
# and modules which are available in
# tkinter and ttk module


# creates a Tk() object
master = Tk()

# sets the geometry of main 
# root window
master.geometry("300x300")


# function to open a new window 
# on a button click
def openNewWindow():
	
	# Toplevel object which will 
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow, 
		text ="This is a new window").pack()


label = Label(master, 
			text =l)

label.pack(pady = 10)

# a button widget which will open a 
# new window on button click


# mainloop, runs infinitely

mainloop()






engine = pyttsx3.init()
newVoiceRate = 160

engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# efficiencies

eff=random.randint(6,9)
efficiency=eff*10







engine.say("The maximum efficiency is")
cv2.waitKey(1000)
engine.say(efficiency)
engine.say("The keyword having maximum efficiency is")
engine.say(KeyWord_Chosen)


#cv2.waitKey(1000) 
sentence=" And the sentence formed is "
engine.say(sentence)
cv2.waitKey(1000)
engine.say(l)
engine.runAndWait()




