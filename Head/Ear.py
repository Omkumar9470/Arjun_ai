import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init

init(autoreset=True)


def Trans_hindi_to_english(txt):
    try:
        english_txt = translate(txt, to_language="en")
        return english_txt

    except Exception as e:
        print(Fore.RED + f"Translation error: {e}")
        return txt


def listen():

    recognizer = sr.Recognizer()


    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = 300

    recognizer.pause_threshold = 1.5
    recognizer.non_speaking_duration = 1

    with sr.Microphone() as source:

        print(Fore.LIGHTBLUE_EX + "I am Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                audio = recognizer.listen(source)

                print(Fore.LIGHTGREEN_EX +"Got it, Recognizing...")

                # Convert speech → text
                recognized_txt = recognizer.recognize_google(audio).lower()
                print(Fore.BLUE + "Recognized: " + recognized_txt)

                translated_txt = Trans_hindi_to_english(recognized_txt)

                print(Fore.BLUE + "Mr Om: " + translated_txt)

                return translated_txt

            except sr.UnknownValueError:
                print(Fore.RED + "Could not understand what you said.")
                continue


            except sr.RequestError as e:
                print(Fore.RED + f"Speech recognition error: {e}")
                return ""


if __name__ == "__main__":
    listen()

