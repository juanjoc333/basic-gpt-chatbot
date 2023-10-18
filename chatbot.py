import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config.get("OPENAI_API_KEY")

messages_list = []

while True:
    try:
        user_input = input("You: ")
        messages_list.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
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
