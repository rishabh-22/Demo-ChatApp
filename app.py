from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/chat')
def chat():
    username = request.args.get('username')
    # room = request.args.get('room')

    if username:
        return render_template('chat.html', username=username)
    else:
        return redirect(url_for('home'))


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info(f"{data['username']} has sent message to the room: {data['message']}")
    socketio.emit('receive_message', data)


@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info(f"{data['username']} has joined the room")
    join_room('ocean')  # ocean is the room name
    socketio.emit('join_room_announcement', data)


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info(f"{data['username']} has left the room")
    leave_room('ocean')  # ocean is the room name
    socketio.emit('leave_room_announcement', data)


if __name__ == '__main__':
    socketio.run(app)
