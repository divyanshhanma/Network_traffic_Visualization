import pyshark
import nest_asyncio
import pandas as pd
from flask import Flask, jsonify, render_template
from flask_cors import CORS  # Import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Apply nest_asyncio (if using Jupyter or similar environments)
nest_asyncio.apply()

# Function to capture network traffic
def capture_traffic(interface='Wi-Fi', packet_count=100):
    try:
        # Capture live packets
        capture = pyshark.LiveCapture(interface=interface)
        packets = []

        # Capture network traffic
        for packet in capture.sniff_continuously(packet_count=packet_count):
            packet_info = {
                'time': float(packet.sniff_time.timestamp()),
                'protocol': packet.highest_layer,
                'length': int(packet.length)
            }
            packets.append(packet_info)

        # Return DataFrame of packet information
        return pd.DataFrame(packets)

    except Exception as e:
        print(f"Error capturing traffic: {e}")
        return pd.DataFrame()

# Route to capture traffic and return data as JSON
@app.route('/api/capture')
def capture_and_send():
    print("Received request to capture traffic")  # Debugging output
    df = capture_traffic(interface='Wi-Fi', packet_count=100)

    if df.empty:
        print("No packets captured.")  # Debugging output
        return jsonify({'error': 'No data captured, check network interface or permissions'}), 400

    # Convert timestamp to readable time format
    df['time'] = df['time'].astype(float)  # Ensure it's float

    # Compute throughput (bytes per second)
    df['time_diff'] = df['time'].diff().fillna(1)  # Time difference between packets (fill first with 1)
    df['throughput'] = df['length'] / df['time_diff'].replace(0, 1)  # Avoid division by zero

    # Prepare the data for frontend
    data = {
        'time': df['time'].tolist(),  # This should be in seconds
        'length': df['length'].tolist(),
        'protocol': df['protocol'].tolist(),
        'throughput': df['throughput'].tolist()  # Pass throughput data to frontend
    }

    print("Captured data:", data)  # Debugging output
    return jsonify(data)

# Main route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
