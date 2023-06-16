import pyttsx3

vt = pyttsx3.init()

v = int(input("Enter the voice tone of your Friend: \n0-Male\n1-Female : "))
while v > 1:
    v = int(input("Tone should be male(0) or female(1) : "))

# rate
rate = vt.getProperty("rate")
vt.setProperty('rate', 150)

# voice
voices = vt.getProperty("voices")
vt.setProperty("voice", voices[v].id)


def speak(text):
    print("Speaking....")
    vt.say(text)
    vt.runAndWait()


x = input("Enter Your Name: ")
txt = f"Hello {x}, I am your Virtual Friend I will repeat after you"
speak(txt)
while True:
    txt = input("What should i say: ")
    txt = txt.lower()
    if txt == "bye":
        print("Thank You")
        vt.say("Thank you,nice meeting you")
        vt.runAndWait()
        break
    else:
        speak(txt)
