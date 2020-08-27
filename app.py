from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room
from word_tags import make_tags_from_sentence


app = Flask(__name__)
app.secret_key = "8530297024358329"
socketio = SocketIO(app)

users = []
# messages = []
user_db = set()


@app.route('/', methods=["POST", "GET"])
def home():
    if 'user' in session and session['user'] in users:
        return "Please continue your session from a single browser window.", 403
        # return redirect(url_for('chat'))
    if request.method == 'POST':
        user = request.form.get('username')
        if user in user_db:
            message = 'Please use a different username, someone with that username already exists in the room.'
            return render_template("index.html", message=message)
        session['user'] = user
        user_db.add(user)
        return redirect(url_for('chat'))
    return render_template("index.html")


@app.route('/chat', methods=["POST", "GET"])
def chat():
    username = ''
    if 'user' in session and session['user'] not in users:
        username = session['user']
    if username:
        return render_template('chat.html', username=username, users=users)
    else:
        return redirect(url_for('home'))


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info(f"{data['username']} has sent message to the room: {data['message']}")
    if data['message'][0] == '|':
        msg = make_tags_from_sentence(data['message'][1:])
        data['username'] = "System"
        data['message'] = "Here's the breakdown of your sentence" + str(msg)
        data['created_at'] = ''
        socketio.emit('receive_message', data)
    else:
        data['created_at'] = '['+datetime.now().strftime("%d %b, %H:%M")+']'
        # messages.append(data)
        # print(messages)
        socketio.emit('receive_message', data)


@socketio.on('join_room')
def handle_join_room_event(data):
    if data['username'] == session['user'] and data['username'] in users:
        return "Please continue your session from a single browser window.", 403
    app.logger.info(f"{data['username']} has joined the room")
    users.append(data['username'])
    join_room('ocean')  # ocean is the room name
    socketio.emit('join_room_announcement', data)


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info(f"{data['username']} has left the room")
    users.remove(data['username'])
    leave_room('ocean')  # ocean is the room name
    socketio.emit('leave_room_announcement', data)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
