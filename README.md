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

- Python 3.x
- Install required Python packages:
  ```bash
  pip install pyshark pandas flask flask-cors nest_asyncio
