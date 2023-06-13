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
    user_message = "Type here..." if len(messages) != 0 else "No messages yet"


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
                color: #4267B2;
                outline: 1px solid #4267B2;
                padding: 10px;
                border-radius: 5px;
                margin-top: 20px;
                }

                /* Chat messages */
                .chat-message {
                  margin-bottom: 10px;
                }

                .chat-message .message-content {
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
                }

                 /* Messages list */
                .messages-list {
                  margin-top: 20px;
                  background-color: #e9e9e9;
                  padding: 10px;
                  border-radius: 5px;
                }

                /* Current message and form*/
                .current-container {
                  margin-top: 20px;
                  background-color: #e9e9e9;
                  padding: 10px;
                  border-radius: 5px;
                }

                /* Timestamp */
                .timestamp {
                  font-size: 12px;
                  color: #ECB22E;
                   padding-top: 2px;
                }

                /* Scrollbar */
                ::-webkit-scrollbar {
                    width: 5px;
                }   

                ::-webkit-scrollbar-track { 
                    background-color: #f1f1f1;
                }

                ::-webkit-scrollbar-thumb {
                    background-color: #888;
                }


                ::-webkit-scrollbar-thumb:hover {
                    background: #555;
                }

                @keyframes rainbow {
                 0% { background-color: red; }
                 14% { background-color: orange; }
                 28% { background-color: yellow; }
                 42% { background-color: green; }
                 57% { background-color: blue; }
                 71% { background-color: indigo; }
                 85% { background-color: violet; }
                 100% { background-color: red; }
                 }

                 #current-message {
                 padding: 10px;
                 margin-left: 10px;
                 margin-right: 10px;
                 border-radius: 7px; 
                 border: none;
                 color:  #fff;
                 font-weight: bold;
                 text-shadow: 0px 0px 5px #000;
                 background-image: linear-gradient(to right, rgba(255, 0, 0, 0.3), rgba(255, 165, 0, 0.3), rgba(255, 255, 0, 0.3), rgba(0, 128, 0, 0.3), rgba(0, 0, 255, 0.3), rgba(75, 0, 130, 0.3), rgba(238, 130, 238, 0.3), rgba(255, 0, 0, 0.3));
                 background-size: 100% 100%;
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
                <form class="input-area current-container" action ="/" method= "POST">
                    <input type="text" name='message' placeholder="{{input_message}}">
                    <input type="submit" value="Send">
                </form>
            </div>  </div>  </div>
        </body>
    </html>
    """
    return render_template_string(html, name=name,messages=messages, input_message=user_message) 


if __name__ == "__main__":
    app.run(debug=True)

