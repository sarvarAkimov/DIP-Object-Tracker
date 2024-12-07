import cv2
import time

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[7]

if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create() 
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create() 
if tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create() 
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create() 
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()
if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

def track_object_with_accuracy_and_save_frames(video_source="same_instance.mp4", start_time=2, end_time=4, save_frame_numbers=[50]):
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print("Error: Cannot open video source.")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    if start_time >= duration or end_time > duration or start_time >= end_time:
        print("Error: Invalid start or end time.")
        return

    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read video file.")
        return
    bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Object to Track")
    tracker.init(frame, bbox)

    frame_count = 0
    successful_tracks = 0
    interval_frames = 0
    start_processing_time = time.time()

    saved_frames = set(save_frame_numbers) 
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream.")
            break

        frame_count += 1
        current_time = frame_count / fps

        success, bbox = tracker.update(frame)
        if start_time <= current_time <= end_time:
            interval_frames += 1
            if success:
                successful_tracks += 1

        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        else:
            cv2.putText(frame, "Tracking lost!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if frame_count in saved_frames:
            frame_filename = f"(2)MIL(2)_tracker_frame({frame_count}).png"
            cv2.imwrite(frame_filename, frame)
            print(f"Frame {frame_count} saved as {frame_filename}")
            saved_frames.remove(frame_count) 

        cv2.imshow("CSRT Object Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if interval_frames > 0:
        accuracy = (successful_tracks / interval_frames) * 100
        print(f"Tracking Accuracy from {start_time}s to {end_time}s: {accuracy:.2f}%")
    else:
        print("No frames found in the specified time interval.")

    end_processing_time = time.time()
    processing_time = end_processing_time - start_processing_time
    print(f"Total processing time between {start_time}s and {end_time}s: {processing_time:.2f} seconds.")

    cap.release()
    cv2.destroyAllWindows()

track_object_with_accuracy_and_save_frames("small_instance.mp4", 2, 4, save_frame_numbers=[40, 140])
