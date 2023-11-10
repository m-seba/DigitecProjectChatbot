# UserStory#11
import datetime

def ermittelZeit():
    currentTime = datetime.datetime.now()
    currentTimeinString = currentTime.strftime("%H:%M:%S")
    return currentTimeinString

known_answers = {
    "ostfalia": [
        "0. Wie viele Studierende hat die Ostfalia?",
        "1. Wie viele Standorte hat die Ostfalia?",
        "2. Wo befindet sich das Hauptgebäude der Ostfalia?",
        "3. Wann sind die Öffnungszeiten der Ostfalia?"
    ],
    "wintersemester": [
        "0. Welche Studiengänge werden im Wintersemester an der Ostfalia angeboten?",
        "1. Gibt es besondere Veranstaltungen während des Wintersemesters an der Ostfalia?",
        "2. Wie unterstützt die Ostfalia ihre Studierenden im Wintersemester?",
        "3. Welche Aktivitäten plant die Studentenvereinigung für das kommende Wintersemester an der Ostfalia?"
    ],
    "lan": [
        "0. What types of devices are typically connected to a LAN, and how do they interact?",
        "1. What are the main advantages of implementing a LAN in a small to medium-sized business environment?",
        "2. What is a LAN, and how does it differ from other types of networks?",
        "3. How do LANs facilitate the sharing of data, devices, and resources within a limited geographic area?"
    ],
}

answer11 = {"ostfalia": ["0.cerca 150000","1. 4 standort ","2.wolfenuttel","3. 8:00 am - 17:00 pm"],
            "wintersemester": ["0.digital tech -informatik -rechts - managment","1. yes","2.ccc","3.ccc"],
            "lan": [" 0.all types printer desktop smartphones ","1. faster commnication more productivity ","2.ccc","3.ccc"]
            }

print( "Hello")
print( "How can I help you?")

user_question = input("Type a keyword: ").lower()
    
if user_question in known_answers:
    question_variants = known_answers[user_question]
    print( question_variants)
    
    user_question2 = int(input("Enter the question number: ")) 

    if user_question2 < len(known_answers[user_question]):  #length of elements in set
        print(answer11[user_question][user_question2])
    else:
        print( "Invalid index")
else:
    print("can you write again?")