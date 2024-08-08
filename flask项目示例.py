app = Flask(__name__)

# 替换为你的 OpenAI API 密钥
openai.api_key = '你的api密钥'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",  # 使用合适的模型
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    ) 



对应的html    index.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat with GPT-4</title>
</head>
<body>
    <h1>Chat with GPT-4</h1>
    <input type="text" id="user-input" placeholder="Enter your message here">
    <button id="send-button">Send</button>
    <div id="response"></div>

    <script>
        document.getElementById('send-button').addEventListener('click', function() {
            const userMessage = document.getElementById('user-input').value;
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({message: userMessage})
            })
            .then(response => response.json())
            .then(data => {
                const responseDiv = document.getElementById('response');
                if (data.error) {
                    responseDiv.textContent = `Error: ${data.error}`;
                } else {
                    responseDiv.textContent = `Assistant: ${data.message}`;
                }
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>





    
    assistant_message = response.choices[0].message['content'].strip()
    return jsonify({"message": assistant_message})

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)  # 使用不同的端口以避免冲突






