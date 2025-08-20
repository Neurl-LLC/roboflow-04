import os
import cv2
import zmq
import pickle
from dotenv import load_dotenv
from inference import InferencePipeline

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")  # publish frames on port 5555

load_dotenv() # Load Environment Variables

def my_sink(result, video_frame):
    if result.get("label_visualization"):
        frame = result["label_visualization"].numpy_image
        # Serialize with pickle (could also use JPEG encode for speed)
        data = pickle.dumps(frame)
        socket.send(data)

    print("Worked!", result)

pipeline = InferencePipeline.init_with_workflow(
    api_key=os.environ["ROBOFLOW_API_KEY"],
    workspace_name=os.environ["WORKSPACE_NAME"],
    workflow_id=os.environ["WORKFLOW_ID"],
    video_reference=os.environ["VIDEO_REFERENCE"],
    max_fps=30,
    on_prediction=my_sink
)

pipeline.start()
pipeline.join()

