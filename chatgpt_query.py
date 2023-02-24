#used to directly query ChatGPT

import openai
import argparse

openai.api_key = "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"

def query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )
    return response.choices[0].text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make queries to the OpenAI API.")
    parser.add_argument("prompt", help="The prompt to send to the OpenAI API.")
    args = parser.parse_args()

    response = query(args.prompt)
    print(response)
