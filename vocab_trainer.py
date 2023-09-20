import os
import json
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

# https://medium.com/@deeptechtalker/meditation-a-guide-to-unlocking-inner-peace-and-fulfillment-e979299fbffa

os.environ['OPENAI_API_KEY'] = "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"

llm = OpenAI(temperature=.7)

template = \
"""
you are a chatbot that teaches vocabulary. you first ask a probing word, if the 
user says i know this word you progress to a rarer word. you also provide a 
mnemonic to remember the word. 

you are to return it in a JSON only with the following keys:
word
part of speech
definition
example
mnemonic

"""

memory = []
words = []
word_dict = set()

greeting = """
Hi, I am VocabBot. I will ask you few questions to judge where you fall \
on the vocab coolness meter. Here are my 4 options:\n
1. I know this word\n
2. I don't know this word\n
3. Start\n
4. End\n
5. Next\n
Use these options to interact with me from now on.
"""

memory.append(greeting)

print(greeting)
print()

def generate_latest_word():
  words.append(json.loads(llm.predict(template)))
  word_dict.add(words[-1]['word'])
  return

def return_latest_word():
  return words[-1]['word']

def return_latest_word():
  return "\n".join([k + ": " + v for k, v in words[-1].items()]) + "\n"

def introduce_word():
  print(f"Do you know the meaning of {words[-1]['word']}")

while True:
  temp = int(input().strip())
  if temp == 5: temp = 1
  if temp == 1:
    print("Great let's move on.\n")
    generate_latest_word()
    introduce_word()
  elif temp == 2:
    print("Let me get the details of the word for you then.\n")
    print(return_latest_word())
  elif temp == 3:
    print("Welcome to Vocab Chat\n")
    generate_latest_word()
    introduce_word()
  elif temp == 4:
    break