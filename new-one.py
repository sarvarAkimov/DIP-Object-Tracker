import cv2

tracker = cv2.TrackerCSRT_create()

def track_object(video_source=0):
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print("Error: Cannot open video source.")
        return
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read video file or webcam.")
        return
    bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Object to Track")
    tracker.init(frame, bbox)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream.")
            break
        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        else:
            cv2.putText(frame, "Tracking lost!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("CSRT Object Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# track_object(0)

track_object("messi.mp4")
