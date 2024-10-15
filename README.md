# Network Traffic Visualization

This project is a **real-time network traffic analysis tool** built using Python, Flask, PyShark, and JavaScript with Chart.js. It captures live network packets, processes them to compute relevant metrics such as packet size, protocol distribution, and throughput, and visualizes the data in an intuitive web interface.

## Features

- **Real-time network traffic capture**: Captures live packets using `PyShark`.
- **Packet size and protocol analysis**: Displays packet lengths and protocols used in real-time.
- **Throughput calculation**: Computes network throughput in bytes per second.
- **Interactive data visualization**: Line charts and pie charts visualize network behavior using `Chart.js`.
- **Cross-Origin Resource Sharing (CORS)** enabled for API access.

## Technologies Used

- **Backend**:
  - Python
  - Flask
  - PyShark (for packet capture)
  - Pandas (for data processing)
  - Flask-CORS (for enabling CORS)

- **Frontend**:
  - HTML/CSS
  - JavaScript (ES6)
  - Chart.js (for data visualization)

## Installation and Setup

### Prerequisites

1. **Python 3.x**: Ensure that Python is installed.
2. **Wireshark**: PyShark requires Wireshark’s **tshark** utility for packet capture.

   - **Install Wireshark**:
     - **Windows**: Download and install Wireshark from [Wireshark Official Site](https://www.wireshark.org/download.html). Make sure to select "Install `tshark`" during installation.
     - **Linux**:
       ```bash
       sudo apt-get update
       sudo apt-get install wireshark
       sudo usermod -aG wireshark $(whoami)
       ```
       - You may need to log out and back in to apply the changes.

     - **macOS** (with Homebrew):
       ```bash
       brew install wireshark
       ```

3. **Python Libraries**: Install required Python packages:
   ```bash
   pip install pyshark pandas flask flask-cors nest_asyncio
