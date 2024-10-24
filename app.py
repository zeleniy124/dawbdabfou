from flask import Flask, request, jsonify,render_template
import os
import requests
import openai
from openai import OpenAI

session = requests.Session()
proxies = {
    'http': 'http://rih1tw6hn5-corp.mobile.res-country-DE-hold-session-session-671ad2af72487:scFmtRPJyIvx5c4X@93.190.142.57:9999',
    'https': 'https://rih1tw6hn5-corp.mobile.res-country-DE-hold-session-session-671ad2af72487:scFmtRPJyIvx5c4X@93.190.142.57:9999'
}
session.proxies.update(proxies)

# Step 2: Override OpenAI's default session with your custom session
openai.requestssession = session



client = OpenAI(
    api_key = "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",
)

application = Flask(__name__)

# Set your OpenAI API key

@application.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    try:
        # Make a request to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can use GPT-4 if needed
            messages=[
                {"role": "system", "content": "You are Peter Griffin from Family Guy. Respond as Peter with humor and a trolling tone.. Yo, limiting your reply to one sentence."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=50,  # Adjust token limit for shorter responses
            temperature=0.9  # Higher temperature for more creative and humorous responses
        )

        reply = response.choices[0].message.content
        return jsonify({'reply': reply.strip()})  # Strip any extra whitespace

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(host="0.0.0.0")
