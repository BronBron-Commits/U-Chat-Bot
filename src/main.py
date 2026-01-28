from tts import speak

def main():
    print("U-Chat-Bot ready (type 'quit' to exit)")
    while True:
        user = input(">>> ").strip()
        if user in ("quit", "exit"):
            break

        response = f"You said: {user}"
        print(response)
        speak(response)

if __name__ == "__main__":
    main()
