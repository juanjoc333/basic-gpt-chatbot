import openai
from dotenv import dotenv_values

import argparse

config = dotenv_values(".env")
openai.api_key = config.get("OPENAI_API_KEY")


def bold_red_text(text):
    BOLD_RED = "\033[91;1m"  # 91 for red, 1 for bold
    RESET = "\033[0m"
    return BOLD_RED + text + RESET


def bold_blue_text(text):
    BOLD_BLUE = "\033[94;1m"  # 94 for blue, 1 for bold
    RESET = "\033[0m"
    return BOLD_BLUE + text + RESET


def main():
    parser = argparse.ArgumentParser(description="Chat with GPT-3")
    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the personality of the chatbot",
        default="a pirate",
    )

    args = parser.parse_args()
    personality = args.personality

    system_prompt = f"You are a conversational chatbot. You are a {personality}."

    messages_list = []

    while True:
        try:
            user_input = input(bold_blue_text("You: "))
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

            print(bold_red_text("Assistant: "), response.choices[0].message.content)
            messages_list.append(
                {"role": "assistant", "content": response.choices[0].message.to_dict()}
            )

        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
