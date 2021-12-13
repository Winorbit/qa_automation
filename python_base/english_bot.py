english_sentences = [
    {"text": "When my time comes \n Forget the wrong that I’ve done.",
     "level": 1},
    {"text": "In a hole in the ground there lived a hobbit.",
     "level": 2},
    {"text": "The sky the port was the color of television, tuned to a dead channel.",
     "level": 1},
    {"text": "I love the smell of napalm in the morning.",
     "level": 0},
    {"text": "The man in black fled across the desert, and the gunslinger followed.",
     "level": 0},
    {"text": "The Consul watched as Kassad raised the death wand.",
     "level": 1},
    {"text": "If you want to make enemies, try to change something.",
     "level": 2},
    {"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
     "level": 1},
    {"text": "I learned very early the difference between knowing the name of something and knowing something.",
     "level": 2}
]
user = {"username": "Kate",
        "level": 2}

input_word = "The"
input_word = input_word.upper()
message = ""
for sentence in english_sentences:
    if user.get("level") == sentence.get("level"):
        if input_word in sentence.get("text").upper():
            message = message + sentence.get("text") + "\n*****\n"
if not message:
    print("Sorry,There are no sentences.")
else:
    print(user["username"] + ", Your sentence:\n" + message)

###############################################
english_sentences_damaged = [
    {"text": "When my time comes \n Forget the wrong that I’ve done.",
     "level": 1},
    "In a hole in the ground there lived a hobbit.",
    {"text": "The sky the port was the color of television, tuned to a dead channel.",
     "level": "4"},
    {"text": "I love the smell of napalm in the morning.",
     "level": 0},
    {"text": "The man in black fled across the desert, and the gunslinger followed.",
     "level": 0},
    {"text": "The Consul watched as Kassad raised the death wand.",
     "level": 1},
    {"text": "If you want to make enemies, try to change something.",
     "level": 2},
    {"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
     "level": 1},
    {"text": "I learned very early the difference between knowing the name of something and knowing something.",
     "level": 2}
]
user = {"username": "Sveta",
        "level": 1}

input_word = input().upper()
message = ""

for sentence in english_sentences_damaged:
    if type(sentence) == dict:
        if type("level") != int:
            sentence["level"] = int(sentence.get("level"))
        if user.get("level") == sentence.get("level"): 
            if input_word in sentence.get("text").upper():
                message = message + sentence.get("text")+"\n*****\n"
if not message:
	print("Sorry, There are no sentences")
else: 
	print(user["username"] + ", Your sentence:" + "\n*****\n" + message)  
