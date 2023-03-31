import openai
import config
openai.api_key = config.OPENAI_API_KEY


def openAIQuery(query):
    response = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': query},
  ],
  temperature = 0  
)

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['message']['content']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'

    return answer