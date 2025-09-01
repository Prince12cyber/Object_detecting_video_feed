# Object Detection Video Feed

A Flask-based web application that performs real-time object detection using your webcam and displays the video feed along with the detected object count in a browser.

## Features
- **Live Video Feed:** Streams webcam video to your browser.
- **Object Detection:** Uses OpenCV's background subtraction to detect moving objects.
- **Object Count:** Displays the number of detected objects, updated in real time.
- **Modern UI:** Simple, responsive interface with live updates.

## Demo
![Demo Screenshot](demo_screenshot.png)

## Getting Started

### Prerequisites
- Python 3.7+
- pip
- Webcam

### Installation
1. **Clone the repository:**
   ```powershell
   git clone https://github.com/Prince12cyber/Object_detecting_video_feed.git
   cd Object_detecting_video_feed
   ```
2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install flask opencv-python
   ```

### Running the Application
1. **Start the Flask server:**
   ```powershell
   python .venv/app.py
   ```
2. **Open your browser:**
   Navigate to `http://127.0.0.1:5000/` to view the live video feed and object count.

## Project Structure
```
.venv/
├── app.py               # Main Flask application
├── static/
│   ├── styles.css       # CSS for UI
│   └── script.js        # JS for live object count
├── templates/
│   └── index.html       # Main HTML page
```

## How It Works
- **app.py:**
  - Captures video from your webcam using OpenCV.
  - Applies background subtraction to detect moving objects.
  - Draws bounding boxes around detected objects.
  - Streams the processed video to the browser.
  - Provides an API endpoint (`/get_count`) for the current object count.
- **index.html:**
  - Displays the video feed and object count.
  - Uses JavaScript to fetch and update the object count every second.
- **styles.css:**
  - Styles the UI for a clean, modern look.
- **script.js:**
  - Periodically fetches the object count from the server and updates the UI.

## Customization
- **Change Video Source:**
  - Edit `video_source` in `app.py` to use a different camera index.
- **Adjust Detection Sensitivity:**
  - Modify the contour area threshold in `app.py` (`cv2.contourArea(contour) > 1000`).

## Troubleshooting
- **Webcam Not Detected:**
  - Ensure your webcam is connected and not used by another application.
  - Try changing the `video_source` index in `app.py`.
- **Dependencies Issues:**
  - Make sure you installed all required packages in your virtual environment.

## License
This project is licensed under the MIT License.

## Author
Prince12cyber
