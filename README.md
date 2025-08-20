# How to Use Your Existing Cameras for AI (Fast, Easy, No New Hardware)

Think you need brand-new cameras to run modern computer vision? Think again.
Whether it’s a CCTV setup, a workshop camera, or even your smartphone, your **current hardware is all you need**.

All you need to do is stream video frames from your existing camera into a [Roboflow Workflow](https://roboflow.com/workflows/build) (via RTSP or similar protocols), then apply any of the latest computer vision models that Roboflow offers.

---

## Usage

1. **Clone this repository:**

   ```sh
   git clone https://github.com/Neurl-LLC/roboflow-04.git
   cd roboflow-04
   ```

2. **Create a [workflow](https://roboflow.com/workflows/build)** on Roboflow, or simply clone [this example workflow](https://app.roboflow.com/workflows/embed/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3JrZmxvd0lkIjoiWWpmeHFpdmlqYURidEdGeWN4c3oiLCJ3b3Jrc3BhY2VJZCI6IjlkV1VvSGNHd0pXSmtFZG5IY09tUUQzclA0dzEiLCJ1c2VySWQiOiI5ZFdVb0hjR3dKV0prRWRuSGNPbVFEM3JQNHcxIiwiaWF0IjoxNzU1NjEwMTUyfQ.pFq83Whfg7GG7lLyvkcAhXNeLkhR7pnah5vpSfH3aFw).

3. **Create a `.env` file** with the following environment variables:

   ```ini
   ROBOFLOW_API_KEY="YOUR_ROBOFLOW_API_KEY"
   WORKSPACE_NAME="YOUR_WORKSPACE_NAME"
   WORKFLOW_ID="YOUR_WORKFLOW_ID"
   VIDEO_REFERENCE="YOUR_RTSP_LINK"
   ```

4. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the producer script** (handles inference):

   ```sh
   python producer.py
   ```

6. **Run the consumer script** (handles display):

   ```sh
   python consumer.py
   ```

---

## Simulating an IP Camera

Don’t have an IP camera handy? No problem. You can simulate one using [MediaMTX](https://github.com/bluenviron/mediamtx/) and [FFmpeg](https://ffmpeg.org/).

1. [Install MediaMTX](https://github.com/bluenviron/mediamtx/?tab=readme-ov-file#installation) and [download FFmpeg](https://www.ffmpeg.org/download.html).

2. Start the MediaMTX server:

   ```sh
   ./mediamtx
   ```

3. Stream a sample video to the MediaMTX server with FFmpeg:

   ```sh
   ffmpeg -re -stream_loop -1 -i Street_Walk.mp4 -c copy -f rtsp rtsp://127.0.0.1:8554/mystream
   ```

This makes the sample video available at:

```
rtsp://127.0.0.1:8554/mystream
```

Use this RTSP link as your `VIDEO_REFERENCE` in the `.env` file.

---

✅ That’s it. You now have AI-powered computer vision running on your existing cameras with no new hardware required.

