import cv2
import zmq
import pickle

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")  # subscribe to all

# Create a resizable window
cv2.namedWindow("Annotated Stream", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Annotated Stream", 1280, 720)  # set desired size

while True:
    data = socket.recv()
    frame = pickle.loads(data)

    # Optional: scale frame to fit the window size (if source is small)
    frame = cv2.resize(frame, (1280, 720))

    cv2.imshow("Annotated Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
