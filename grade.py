import ollama
import os

prompt_intro="""
You are a world class editor. You specialize in helping writers clarify their writing without changing their meaning or voice.

Instructions:
- Take the Wikipedia article below and suggest three edits that would most improve the clarity of the article.
- If there are no improvements to be made, please state that.
- Do not include any discussion or explanation of your edits.
- Do not include any preamble or conclusion.
- Only respond with the suggested edits, nothing else.
- Do not change the meaning or voice of the article.
- Do not change the order or structure of the article.
- Do not add or remove any information.
- Do not ask questions or request clarification.
- Provide the new text and the original text.
- Do not provide a description of what is being changed.
- Focus only on the words and not the formatting or special formatting characters.
"""

# For each file in ./data:
# read the file into a string then call ollama.generate on the contents of the file

# For each file in ./data:
# read the file into a string then call ollama.generate on the contents of the file
# then write the response to a file in ./responses

for f in os.listdir('./data'):
  with open(f'./data/{f}', 'r') as file:
    text = file.read()
    response = ollama.generate(
      model='llama3',
      prompt=f"{prompt_intro}\n\n```\n{text}\n```",
      stream=False
    )
    with open(f'./responses/{f}', 'w') as response_file:
      response_file.write(response['response'])



# response = ollama.generate(
#   model='llama3',
#   prompt="Why is the sky blue?",
#   stream=False
# )

# # print(response)

# print(response['response'])