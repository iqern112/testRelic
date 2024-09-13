from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import pandas as pd
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Store JMeter data temporarily
jmeter_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/requirements', methods=['GET', 'POST'])
def requirements():
    if request.method == 'POST':
        # Capture requirements from form and filter data (logic to be added)
        pass
    return render_template('requirements.html')

@app.route('/results')
def results():
    return render_template('results.html')

@socketio.on('connect_jmeter')
def connect_jmeter():
    global jmeter_data
    while True:
        # Simulate reading data from JMeter in real time
        data = {
            'timestamp': time.time(),
            'response_time': 100 + 10,  # Simulated response time
        }
        jmeter_data.append(data)
        emit('jmeter_data', data)
        socketio.sleep(1)

@socketio.on('upload_file')
def handle_file(data):
    global jmeter_data
    # Parse uploaded file data from JMeter
    df = pd.read_csv(data)
    jmeter_data = df.to_dict(orient='records')
    emit('file_uploaded', {'status': 'success'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

