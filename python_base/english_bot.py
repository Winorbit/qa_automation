#Домашка на функции
#Вариант для level инвалид + опускать значение без ключа

english_sentences_damaged = [{"text": "When my time comes \n Forget the wrong that I’ve done.", "level": 1},
                             "In a hole in the ground there lived a hobbit.",
                             {"text": "The sky the port was the color of television, tuned to a dead channel.",
                              "level": "4"}, {"text": "I love the smell of napalm in the morning.", "level": 0},
                             {"text": "The man in black fled across the desert, and the gunslinger followed.",
                              "level": 0}, {"text": "The Consul watched as Kassad raised the death wand.", "level": 1},
                             {"text": "If you want to make enemies, try to change something.", "level": 2}, {
                                 "text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
                                 "level": 1}, {
                                 "text": "I learned very early the difference between knowing the name of something and knowing something.",
                                 "level": 2}]

user = {"username": "Darya", "level": 1}

input_word = "The"
input_word = input_word.upper()
UserName = user.get("username")

filtered = []


def validate_input_data(raw_list):
    for sentence in english_sentences_damaged:
        if type(sentence) == str:
            continue
        if user.get("level") == int(sentence.get("level")):
            if input_word in sentence.get("text").upper():
                filtered.append(sentence.get("text"))


validate_input_data(english_sentences_damaged)


def create_and_send_message(filtered_list):
    if len(filtered) == 0:
        print(f"Sorry {UserName}, no sentences found")
    if len(filtered) == 1:
        print(f"Your sentence is: {filtered[0]}")
    else:
        message = ("\n*****\n".join(filtered))
        print(message)


create_and_send_message(filtered)
