english_sentences = [
    {"text": "When my time comes \nForget the wrong that I’ve done.",
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
        "level": 1}

def filter_out_sentences_by_level():
    level = user.get("level")
    filtered_sentences = []
    for sentence in english_sentences:
        if type(sentence) == dict:
            if level == int(sentence["level"]):
                filtered_sentences.append(sentence)
        else:
            continue
    return filtered_sentences

def filter_out_sentences_by_input_word(input_word):
    sentences_filtered_by_level = filter_out_sentences_by_level()
    message = ""
    if filter_out_sentences_by_level():
        for sentence in sentences_filtered_by_level:
            if input_word.lower() in sentence.get("text").lower():
                message = message + sentence.get("text") + "\n*****\n"
        if message:
            print(message)
        else:
            print(f"Sorry, there are no sentences with a word '{input_word}'")
    else:
        print(f"Sorry, there are no sentences for your level")
    return message


filter_out_sentences_by_input_word("the")
