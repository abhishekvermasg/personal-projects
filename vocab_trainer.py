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

# Output

# Hi, I am VocabBot. I will ask you few questions to judge where you fall on the vocab coolness meter. Here are my 4 options:

# 1. I know this word

# 2. I don't know this word

# 3. Start

# 4. End

# 5. Next

# Use these options to interact with me from now on.


# 3
# Welcome to Vocab Chat

# Do you know the meaning of prodigy
# 1
# Great let's move on.

# Do you know the meaning of Ubiquitous
# 1
# Great let's move on.

# Do you know the meaning of ameliorate
# 1
# Great let's move on.

# Do you know the meaning of jejune
# 2
# Let me get the details of the word for you then.

# word: jejune
# part of speech: adjective
# definition: lacking in interest or excitement; dull
# example: He gave a jejune presentation that failed to capture the audience's attention.
# mnemonic: Jejune rhymes with 'June', a month that can be quite boring compared to others in the year.

# 5
# Great let's move on.

# Do you know the meaning of defenestrate
# 1
# Great let's move on.

# Do you know the meaning of Lugubrious
# 1
# Great let's move on.

# Do you know the meaning of abscond
# 1
# Great let's move on.

# Do you know the meaning of extemporaneous
# 2
# Let me get the details of the word for you then.

# word: extemporaneous
# part_of_speech: adjective
# definition: done without preparation; impromptu; spontaneous
# example: He gave an extemporaneous speech at the award ceremony.
# mnemonic: EXTemporaneous (EXTRA + temporary) - something done without preparation in an extra, temporary way.

# 1
# Great let's move on.

# Do you know the meaning of insouciance
# 2
# Let me get the details of the word for you then.

# word: insouciance
# part_of_speech: noun
# definition: the attitude of being unconcerned; indifference
# example: He had an air of insouciance when asked about his future plans.
# mnemonic: The word 'insouciance' contains the word 'souciance' which can remind you of 'caution' - the opposite of insouciance.