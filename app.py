from flask import Flask, Response, jsonify, render_template
import cv2

app = Flask(__name__)

# Video source: Use 0 for the default webcam
video_source = 0  # Set to 1 or higher if you have multiple cameras

cap = cv2.VideoCapture(video_source)
if not cap.isOpened():
    raise ValueError(f"Cannot open webcam with index {video_source}")

object_count = 0


def object_detection():
    global object_count
    background_subtractor = cv2.createBackgroundSubtractorMOG2()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Cannot read frame from webcam.")
            break

        # Apply background subtraction and find contours
        mask = background_subtractor.apply(frame)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frame_object_count = 0  # Count objects in the current frame
        for contour in contours:
            if cv2.contourArea(contour) > 1000:  # Filter small objects
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame_object_count += 1

        object_count = frame_object_count  # Update global object count

        # Encode the frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            print("Failed to encode frame.")
            break

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    cap.release()


@app.route('/video_feed')
def video_feed():
    """Video feed route."""
    return Response(object_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_count')
def get_count():
    """Object count route."""
    return jsonify({"count": object_count})


@app.route('/')
def index():
    """Index route displaying the video feed and object count."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

