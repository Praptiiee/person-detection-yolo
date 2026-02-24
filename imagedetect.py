from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolo11n.pt")
print( model.names)
# Find "person" class ID dynamically
person_class_id = next(
    k for k, v in model.names.items() if v == "person"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame, classes=[person_class_id], conf=0.6)

    person_count = len(results[0].boxes) if results[0].boxes is not None else 0

    annotated_frame = results[0].plot()

    cv2.putText(
        annotated_frame,
        f"Persons detected: {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Person Counter", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
