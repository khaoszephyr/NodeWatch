# NodeWatch

Nodewatch is a home-lab computer vision and security analytics platform designed to run on local hardware using Python, OpenCV, and YOLO.

The project begins as a simple camera capture system and will gradually evolve into a full detection, event logging, analysis, and security research platform.

## Current Status ##
**Phase 1 Complete - Changes Implemented:**
* Configurable camera source
* VideoStream abstraction layer
* Live webcam feed
* FPS overlay
* Timestamp overlay
* Snapshot capture
* Camera health monitoring
* Git/GitHub integration

**Phase 2.1 Complete - Changes Implemented:**
* YOLOv8 object detection integration
* Real-time object classification
* Bounding box rendering
* Detection overlay integration
* Obbject detection running at approximately 24-25 FPS
* Confidence scores display
  
**Phase 2 - In Progress**
* Detection confidence treshold filtering
* Detection event generation
* Snapshot capture on detection
* Detection cooldown logic
* Object satistics and counters
* Detection logging framework
  
## Project Roadmap ##
**Phase 1** - Camera Capture Layer \
**Phase 2** - YOLO Object Detection \
**Phase 3** - Detection Storage & Event Logging \
**Phase 4** - Object Tracking & Correlaton \
**Phase 5** - FastAPI Backend \
**Phase 6** - Dashboard & Analytics \
**Phase 7** - Dataset Collection & Model Training \
**Phase 8+** - Security Analytics, SIEM Integration, and Adversarial Testing 

## Requirements ##
Python 3.10+ \
Install dependencies: \
pip install -r requirements.txt

## Long-Term Goal ##
Create a LAN-only computer vision platform capable of collecting, analyzing, and visualizing detection events while serving as a cybersecutity, machine learning, and software engineering learning project. NodeWatch is being developed incrementally, with each phase building upon the previous one. Features are validated in isolation before being integrated into the larger platform to maintain reliability and simplify troubleshooting.
