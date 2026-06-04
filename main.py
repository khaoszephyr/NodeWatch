import cv2
import yaml
import time
import os
from datetime import datetime

from capture.stream import VideoStream

def load_settings(path="config/settings.yaml"):
    with open(path, 'r') as file:
        return  yaml.safe_load(file)

def draw_overlay(frame, fps, camera_status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cv2.putText(
        frame, 
        f"FPS: {fps:.0f}", 
        (10, 30), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.8, 
        (0, 255, 0), 
        2,
    )

    cv2.putText(
        frame,
        timestamp,
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Status: {camera_status}",
        (10, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
    )

    return frame

def save_snapshot(frame, folder="storage/snapshots"):
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"snapshot_{timestamp}.jpg"
    path = os.path.join(folder, filename)

    cv2.imwrite(path, frame)
    print(f"Snapshot saved: {path}")

def main():
    settings = load_settings()
    camera_settings = settings['camera']

    stream = VideoStream(
        source=camera_settings['source'],
        width=camera_settings['width'],
        height=camera_settings['height'],
        fps=camera_settings['fps']
    ).start()

    print("NodeWatch Phase 1 started.")
    print("Press 'q' to quit.")

    prev_time = time.time()
    fps = 0.0
    display_fps = 0.0
    fps_update_interval = 1.0
    last_fps_update = time.time()
    failed_frame_count = 0
    camera_status = "Healthy"

    try:

        while True:
            frame = stream.read()

            if frame is None:
                failed_frame_count += 1
                camera_status = "Error 01: Frame read failed."

                print(f"Error 01: Failed to read frame. Count: {failed_frame_count}")

                if failed_frame_count >= 10:
                    print("Error 02: Too many failed frames. Exiting.")
                break

                continue
            else:
                failed_frame_count = 0
                camera_status = "Healthy"

            current_time = time.time()
            elapsed_time = current_time - prev_time

            if elapsed_time > 0:
                current_fps = 1.0 / elapsed_time

                if fps == 0.0:
                    fps = current_fps
                else:
                    fps = (fps * 0.95) + (current_fps * 0.05)

            prev_time = current_time

            if current_time - last_fps_update >= fps_update_interval:
                display_fps = round(fps)
                last_fps_update = current_time

            frame = draw_overlay(frame, display_fps, camera_status)

            cv2.imshow("NodeWatch Camera Feed", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                print("Exiting NodeWatch Phase 1.")
                break
            
            if key == ord('s'):
                print("Saving snapshot...")
                save_snapshot(frame)
                print("Snapshot saved.")

    finally:
        stream.stop()
        cv2.destroyAllWindows()
        print("Camera stopped.")       

if __name__ == "__main__":
    main()