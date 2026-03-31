import speech_recognition as sr

r = sr.Recognizer()
spoken_texts = []

while True:
    try:
        with sr.Microphone() as source:
            print("Say the trigger word ('snow') to start...")
            r.adjust_for_ambient_noise(source, duration=0.3)

            # Listen for trigger word
            audio = r.listen(source, timeout=5)  # auto stops on silence
            text = r.recognize_google(audio).lower()
            print("Heard:", text)

            if "exit" in text:
                print("Exiting program...")
                break

            if "snow" in text:
                print("Trigger detected! Listening for your prompt...")

                # Listen for the actual prompt (auto-stop when user stops speaking)
                audio_prompt = r.listen(source, timeout=5, phrase_time_limit=10)
                prompt_text = r.recognize_google(audio_prompt).lower()
                print("You said:", prompt_text)
                spoken_texts.append(prompt_text)
                break  # Exit after capturing one prompt for testing

    except sr.WaitTimeoutError:
        continue

    except sr.UnknownValueError:
        print("Could not understand audio")
        continue

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        continue

    except KeyboardInterrupt:
        print("Program terminated by user")
        break

print("Captured prompts:", spoken_texts)