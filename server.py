from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Received message:", message)
        print("Timestamp:", timestamp)
        messages.append(message)

    name = 'You yourself'
    user_message = request.form.get("message", "")


    html = """
   <!DOCTYPE html>
        <head>
            <title>My Personal Chat</title>
            <style>
                /* Chat container */
                .chat-container {
                  width: 100%;
                  max-width: 800px;
                  margin: 0 auto;
                  padding: 20px;
                  background-color: #f7f7f7;
                  border: 1px solid #ccc;
                  border-radius: 5px;
                }

                /* Chat messages */
                .chat-message {
                  margin-bottom: 10px;
                }

                .chat-message .message-content {
                  background-color: #fff;
                  padding: 10px;
                  border-radius: 5px;
                }

                .chat-message .message-content p {
                  margin: 0;
                }

                /* User message */
                .user-message .message-content {
                  background-color: #337ab7;
                  color: #fff;
                }

                /* Bot message */
                .bot-message .message-content {
                  background-color: #5cb85c;
                  color: #fff;
                }

                /* Input area */
                .input-area {
                  margin-top: 20px;
                }

                .input-area input[type="text"] {
                  width: 100%;
                  padding: 10px;
                  border: 1px solid #ccc;
                  border-radius: 5px;
                  font-size: 16px;
                }

                .input-area input[type="submit"] {
                  margin-top: 10px;
                  padding: 10px;
                  background-color: #337ab7;
                  color: #fff;
                  border: none;
                  border-radius: 5px;
                  cursor: pointer;
                  font-size: 16px;
                }
            </style>
        </head>
        <body>
            <div class="chat-container">
                <div class="chat-message user-message">
                    <div class="message-content">
                        <p>{{message}}</p>
                    </div>
                </div>
                <div class="chat-message bot-message">
                    <div class="message-content">
                        <p>Bot message content goes here</p>
                    </div>
                </div>
                <form class="input-area" action ="/" method= "POST">
                    <input type="text" name='message' placeholder="Type your message...">
                    <input type="submit" value="Send">
                </form>
            </div>
        </body>
    </html>
    """
    return render_template_string(html, name=name, message=user_message) 


if __name__ == "__main__":
    app.run(debug=True)


