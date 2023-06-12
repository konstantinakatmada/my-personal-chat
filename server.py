from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

messages = []


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messages.append((message,timestamp))
    
    name = 'You yourself'
    user_message = messages[-1][0] if len(messages) != 0 else "No messages yet"


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

                h2.title {
                background-color: #f7f7f7;
                color: #333;
                padding: 10px;
                border-radius: 5px;
                margin-top: 20px;
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

                 /* Messages list */
                .messages-list {
                  margin-top: 20px;
                  background-color: #e9e9e9;
                  padding: 10px;
                  border-radius: 5px;
                }

                /* Timestamp */
                .timestamp {
                  font-size: 12px;
                  color: #999;
                  margin-top: 5px;
                }
            </style>
        </head>
        <body> 
            <div class="chat-container">
            <div class="messages-list">
                    <h2 class="title">Scroll up for previous messages</h2>
                    <ul style="list-style-type: none; padding: 0; margin:0;">
                        {% for msg,ts in messages %}
                        <li class="chat-message user-message">
                        <div class="message-content">
                        <p>{{ msg }}</p>
                        <p class="timestamp">{{ ts}}</p>
                        </div>
                        </li>
                        {% endfor %}
                    </ul>
                </div>  
                <div class="chat-message user-message">
                    <div class="message-content">
                        <p>{{ message }}</p>
                        <p class="timestamp">{{ timestamp }}</p>
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
    print("Messages:", messages)
    return render_template_string(html, name=name, message=user_message, messages=messages) 


if __name__ == "__main__":
    app.run(debug=True)

