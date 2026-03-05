from ollama import chat
from ollama import ChatResponse

question = 'Why is the sky blue?'

response: ChatResponse = chat(model='deepseek-r1:32b', messages=[
  {
    'role': 'assistant',
    'context': 'you are a curious user who is answering the questions and evaluating the topic in a conversion style trying to keep the conversation going by asking questions.',
    'content': question,
  },
])
#print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)