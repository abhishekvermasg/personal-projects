import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

# https://medium.com/@deeptechtalker/meditation-a-guide-to-unlocking-inner-peace-and-fulfillment-e979299fbffa

os.environ['OPENAI_API_KEY'] = "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"

llm = OpenAI(temperature=.7)
template = \
"""

Keyword: {text}

You are the best blog writer in the world. Given a keyword, you can generate the perfect blog structure.
Return the structure in JSON format.

The JSON structure includes the following keys:
title: string \\ title of the blog
subtitle: string \\ subtitle of the blog
sections: array of sections. each section has keys: title and key points.

"""

prompt_template = PromptTemplate(input_variables=["text"], template=template)
answer_chain = LLMChain(llm=llm, prompt=prompt_template)
answer = answer_chain.run("meditation")
print(answer)

import json

x = json.loads(answer)

template = \
"""

You are the best blog writer in the world.

Given this structure of the article: {structure}

Let's write section with {title} and the following key points:
{keypoints}


"""

prompt_template = PromptTemplate(input_variables=["structure", "title", "keypoints"], template=template)
answer_chain = LLMChain(llm=llm, prompt=prompt_template)

final_article = f"{x['title']}\n\n{x['subtitle']}\n\n"

for section in x["sections"]:
  section_answer = answer_chain.predict(structure=answer, title=section['title'], keypoints=section['keyPoints'])
  print(section_answer)
  final_article += section_answer
  final_article += "\n"
