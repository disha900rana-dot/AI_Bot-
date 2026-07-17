from anthropic import Anthropic

client = Anthropic(
    api_key="YOUR_API_KEY"  # Replace with your actual API key
)

messages = []

def completion(user_message):
    global messages

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=messages
    )

    assistant_reply = response.content[0].text

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    print(f"Jarvis: {assistant_reply}")


if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis. How may I help you?\n")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("Jarvis: Goodbye!")
            break

        completion(question)