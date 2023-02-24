# Follow the instructions in the tab to the right
# Write your mad libs program here

# importing the text to speech library

# introduction

# importing the text to speech library
import gtts

# introduction

print("Welcome to the Mad Libs game!!")

print("**** ***** ***** ******")

# prompting the user to enter words
name = input("Enter your first name: ")
country = input("Enter a country: ")
movie = input("Enter your favorite movie: ")
color = input("Enter your favorite color: ")
city = input("Enter your favorite city: ")
food = input("Enter your favorite food: ")

# the complete story with the users words using fstring
print("----*****-------")
story =f"Hey {name},You're obsessed with the color {color} {movie} is your favorite movie and you won't have a problem rewatching it.\nYou can easily live in the bustling city of {city} and you've been dreaming of visiting {country}, or maybe you already have.Eating {food} is what makes your day better, I see why that's one of your favorite foods!"

print(story)

# convrting text to speech
print("\033[0;30;46mPlease read the description")
def tts():
    counter = 0
    while True:
        counter += 1
        text = str(story)
        language = str(input("\033[0;34;40mLanguage: "))
        name = str(input("\033[0;35;40mFile Name: "))
        if language == "Af" or language == "af" or language == "Afrikaans" or language == "afrikaans":
            language = "af"
        elif language == "Ar" or language == "ar" or language == "Arabic" or language == "arabic":
            language = "ar"
        elif language == "Bg" or language == "bg" or language == "Bulgarian" or language == "bulgarian":
            language = "bg"
        elif language == "Bn" or language == "bn" or language == "Bengali" or language == "bengali":
            language = "bn"
        elif language == "Bs" or language == "bs" or language == "Bosnian" or language == "bosnian":
            language = "bs"
        elif language == "Ca" or language == "ca" or language == "Catalan" or language == "catalan":
            language = "ca"
        elif language == "Cs" or language == "cs" or language == "Czech" or language == "czech":
            language = "cs"
        elif language == "Cy" or language == "cy" or language == "Welsh" or language == "welsh":
            language = "cy"
        elif language == "Da" or language == "da" or language == "Danish" or language == "danish":
            language = "da"
        elif language == "De" or language == "de" or language == "German" or language == "german":
            language = "de"
        elif language == "El" or language == "el" or language == "Greek" or language == "greek":
            language = "el"
        elif language == "En" or language == "en" or language == "English" or language == "english":
            language = "en"
        elif language == "Eo" or language == "eo" or language == "Esperanto" or language == "esperanto":
            language = "eo"
        elif language == "Es" or language == "Es" or language == "Spanish" or language == "spanish":
            language = "es"
        elif language == "Et" or language == "et" or language == "Estonian" or language == "estonian":
            language = "et"
        elif language == "Fi" or language == "fi" or language == "Finnish" or language == "finnish":
            language = "fi"
        elif language == "Fr" or language == "fr" or language == "French" or language == "french":
            language = "fr"
        elif language == "Gu" or language == "gu" or language == "Gujarati" or language =="gujarati":
            language = "gu"
        elif language == "Hi" or language == "hi" or language == "Hindi" or language == "hindi":
            language = "hi"
        elif language == "Hr" or language == "hr" or language == "Croatian" or language == "croatian":
            language = "hr"
        elif language == "Hu" or language == "hu" or language == "Hungarian" or language == "hungarian":
            language = "hu"
        elif language == "Hy" or language == "hu" or language == "Armenian" or language == "armenian":
            language = "hy"
        elif language == "Id" or language == "id" or language == "Indonesian" or language == "indonesian":
            language = "id"
        elif language == "Is" or language == "is" or language == "Icelandic" or language == "icelandic":
            language = "is"
        elif language == "It" or language == "it" or language == "Italian" or language == "italian":
            language = "it"
        elif language == "Ja" or language == "ja" or language == "Japanese" or language == "japanese":
            language = "ja"
        elif language == "Jw" or language == "jw" or language == "Javanese" or language == "javanese":
            language = "jw"
        elif language == "Km" or language == "km" or language == "Khmer" or language == "khmer":
            language = "km"
        elif language == "Kn" or language == "kn" or language == "Kannada" or language == "kannada":
            language = "kn"
        elif language == "Ko" or language == "ko" or language == "Korean" or language == "korean":
            language = "ko"
        elif language == "La" or language == "la" or language == "Latin" or language == "latin":
            language = "la"
        elif language == "Lv" or language == "lv" or language == "Latvian" or language == "latvian":
            language = "lv"
        elif language == "Mk" or language == "mk" or language == "Macedonian" or language == "macedonian":
            language = "mk"
        elif language == "Ml" or language == "ml" or language == "Malayalam" or language == "malayalam":
            language = "ml"
        elif language == "Mr" or language == "mr" or language == "Marathi" or language == "marathi":
            language = "mr"
        elif language == "My" or language == "my" or language == "Myanmar" or language == "myanmar" or language == "burmese" or language == "Burmese":
            language = "my"
        elif language == "Ne" or language == "ne" or language == "Nepali" or language == "nepali":
            language = "ne"
        elif language == "Nl" or language == "nl" or language == "Dutch" or language == "dutch":
            language = "nl"
        elif language == "No" or language == "no" or language == "Norwegian" or language == "norwegian":
            language = "no"
        elif language == "Pl" or language == "pl" or language == "Polish" or language == "polish":
            language = "pl"
        elif language == "Pt" or language == "pt" or language == "Portuguese" or language == "portuguese":
            language = "pt"
        elif language == "Ro" or language == "ro" or language == "Romanian" or language == "romanian":
            language = "ro"
        elif language == "Ru" or language == "ru" or language == "Russian" or language == "russian":
            language = "ru"
        elif language == "Si" or language == "si" or language == "Sinhala" or language == "sinhala":
            language = "si"
        elif language == "Sk" or language == "sk" or language == "Slovak" or language == "slovak":
            language = "sk"
        elif language == "Sq" or language == "sq" or language == "Albanian" or language == "albanian":
            language = "sq"
        elif language == "Sr" or language == "sr" or language == "Serbian" or language == "serbian":
            language = "sr"
        elif language == "Su" or language == "su" or language == "Sundanese" or language == "sundanese":
            language = "su"
        elif language == "Sv" or language == "sv" or language == "Swedish" or language == "swedish":
            language = "sv"
        elif language == "Sw" or language == "sw" or language == "Swahili" or language == "swahili":
            language = "sw"
        elif language == "Ta" or language == "ta" or language == "Tamil" or language == "tamil":
            language = "ta"
        elif language == "Te" or language == "te" or language == "Telugu" or language == "telugu":
            language = "te"
        elif language == "Th" or language == "th" or language == "Thai" or language == "thai":
            language = "th"
        elif language == "Tl" or language == "tl" or language == "Filipino" or language == "filipino":
            language = "tl"
        elif language == "Tr" or language == "tr" or language == "Turkish" or language == "turkish":
            language = "tr"
        elif language == "Uk" or language == "uk" or language == "Ukrainian" or language == "ukrainian":
            language = "uk"
        elif language == "Ur" or language == "ur" or language == "Urdu" or language == "urdu":
            language = "ur"
        elif language == "Vi" or language == "vi" or language == "Vietnamese" or language == "vietnamese":
            language = "vi"
        elif language == "Zh-CN" or language == "zh-CN" or language == "Chinese" or language == "chinese":
            language = "zh-CN"
        elif language == "Zh-TW" or language == "zh-TW" or language == "Taiwan" or language == "taiwan":
            language = "zh-TW"
        elif language == "Zh" or language == "zh" or language == "Mandarin" or language == "mandarin":
            language = "zh"
        else:
            print("Sorry, no such language found.")
        gtts.gTTS(text,lang=language).save(str(counter).zfill(2)+" "+str(name)+".mp3")
        print("\033[0;32;40mFile saved as: " + str(counter).zfill(2)+" "+str(name)+".mp3"+"\n")
try:
    tts()
except:
    print("\033[0;31;40mPlease try again")
    tts()
