from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    name = 'You yourself'
    html = """
    <html>
        <head>
            <title>My Personal Chat</title>
            <style>
                /* Chat container */
                .chat-container {
                  width: 100%;
                  max-width: 600px;
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
                        <p>User message content goes here</p>
                    </div>
                </div>
                <div class="chat-message bot-message">
                    <div class="message-content">
                        <p>Bot message content goes here</p>
                    </div>
                </div>
                <div class="input-area">
                    <input type="text" placeholder="Type your message...">
                    <input type="submit" value="Send">
                </div>
            </div>
        </body>
    </html>
    """
    return render_template_string(html, name=name)

if __name__ == "__main__":
    app.run()


