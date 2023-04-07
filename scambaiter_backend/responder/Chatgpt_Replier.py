import os
import openai
from secret import OPENAI_API_KEY
# from secret import CONTENT

openai.api_key = OPENAI_API_KEY # os.getenv("OPENAI_API_KEY")

def gen_text1(prompt):
  prompt = "Reply without any signature :" + prompt
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a dull person and gullible person who is easy to persuade. You want to share information. Do not call them a scam. Keep conversation going. Ask follow-up questions. Do not give any personal information. Greet them in the start."},
      {"role": "user", "content": prompt}
    ],
    temperature = 0.2,
    top_p = 0.2
  )
  res = completion.choices[0].message.content
  return res
  # print(res)


def gen_text2(prompt):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  res = completion.choices[0].message.content
  return res
  # print(res)


# print(gen_text1(CONTENT))