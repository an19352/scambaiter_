import os
import openai
from secret import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY # os.getenv("OPENAI_API_KEY")

def gen_text1(prompt):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  res = completion.choices[0].message.content
  return res
  # print(res)


def gen_text2(prompt):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  res = completion.choices[0].message.content
  return res
  # print(res)


# gen_text2("Hello")