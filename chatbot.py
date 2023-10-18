import openai
from dotenv import dotenv_values

import argparse

config = dotenv_values(".env")
openai.api_key = config.get("OPENAI_API_KEY")


def main():
    parser = argparse.ArgumentParser(description="Chat with GPT-3")
    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the personality of the chatbot",
        default="A chatbot that can chat about anything",
    )

    args = parser.parse_args()
    personality = args.personality

    system_prompt = f"You are a conversational chatbot. You are a {personality}."

    messages_list = []

    while True:
        try:
            user_input = input("You: ")
            messages_list.append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_input,
                    },
                ],
            )

            print("Assistant:", response.choices[0].message.content)
            messages_list.append(
                {"role": "assistant", "content": response.choices[0].message.to_dict()}
            )

        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
