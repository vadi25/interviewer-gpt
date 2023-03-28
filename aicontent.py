import openai
import config
openai.api_key = config.OPENAI_API_KEY


def openAIQuery(query):
    response = openai.Completion.create(
      engine="gpt-3.5-turbo",
      prompt=query,
      temperature=0.9,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0.25)

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'

    return answer