from flask import Flask, render_template, request ,jsonify
import config
import aicontent


def page_not_found(e):
  return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_voice_input', methods=['POST'])
def process_voice_input():
    transcript = request.json['transcript']
    print('Voice input received:', transcript)

    query = "Act as Interview GPT. Interview GPT is an AI specialized in answering job interview questions, you will be given a question and the expected result is an answer. The question is the following:  {}".format(transcript)

    # Process the transcript using the OpenAI Python package
    openAIAnswerUnformatted = aicontent.openAIQuery(query)
    gpt_response = openAIAnswerUnformatted
    # For now, let's return a dummy response
    # gpt_response = 'This is a dummy GPT response for: ' + transcript

    return jsonify(response=gpt_response)

if __name__ == '__main__':
  app.run( ssl_context=('cert.pem', 'key.pem'),host='0.0.0.0', port='8885', debug=True)