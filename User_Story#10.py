# UserStory#10
import datetime
import random

def ermittelZeit():
    currentTime = datetime.datetime.now()
    currentTimeinString = currentTime.strftime("%H:%M:%S")
    return currentTimeinString


known_answers = {
    "wie viele standorte hat die ostfalia?": ["Die Ostfalia hat mehrere Standorte: jeweils in Wolfsburg, Wölfenbüttel, Braunschweig und Salzgitter", "Wolfsburg, Wölfenbüttel, Braunschweig und Salzgitter", "In Nidersachsen: Wolfsburg, Wölfenbüttel, Braunschweig und Salzgitter"],
    "wie viele studierende hat die ostfalia?": ["Die Ostfalia Hochschule hat zur Zeit rund 15.000 Studierende", "15.000 Studenten", "zur Zeit ungefähr 15.000"],
    "wer sind die ansprechpersonen im digitec bereich?": ["Ansprechpersonen sind z.B. Verena Barby", "Frau Verena Barby", "Miss Verena Barby"]
}


print(ermittelZeit(), "Hello")
print(ermittelZeit(), "How can I help you?")

asked_questions = set()  # set()function = the elements in a set list are unordered, so it will appear in a random order



while True:
    user_question = input("Ask me something: ").lower()

    if user_question == "bye":
        break

    if user_question in asked_questions:
        print(ermittelZeit(), "This question has already been asked. Please ask another question.")
        continue

    if user_question in known_answers:
        random_response = random.choice(known_answers[user_question])   #selects a random element from the set list
        print(ermittelZeit(), random_response)

        asked_questions.add(user_question)  #aktuelle user_question wird zu asked_questions hinzugefügt. Dies geschieht um Duplikate zu vermeiden

    else:
        print("I'm not sure how to answer that question.")

print("Goodbye! Thanks for using the program.")
