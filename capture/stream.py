import cv2

class VideoStream:
    def __init__(self, source=0, width=1280, height=720, fps=30):
        self.source = source
        self.width = width
        self.height = height
        self.fps = fps
        self.capture = None

    def start(self):
        self.capture = cv2.VideoCapture(self.source)

        if not self.capture.isOpened():
            raise RuntimeError(f"Failed to open video stream from source: {self.source}")
        
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.capture.set(cv2.CAP_PROP_FPS, self.fps)

        return self 
    
    def read(self):
        if self.capture is None:
            raise RuntimeError("Camera has not been started.")
        
        success, frame = self.capture.read()

        if not success: 
            return None
        
        return frame
    
    def stop(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None