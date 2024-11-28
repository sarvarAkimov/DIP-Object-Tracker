# Object Tracking with OpenCV CSRT Tracker  

This project demonstrates object tracking using OpenCV's **CSRT Tracker**, known for its high accuracy and robustness in challenging scenarios like object overlaps, unpredictable movements, and changes in object shape or size.  


---


[VIDEO JOURNALING LINK](https://drive.google.com/file/d/1VE3Hqa44SU2fx5g_u5cWeP9m2yxCmoco/view?usp=sharing)

## Features  

- **Real-Time Tracking**: Track objects live through a webcam.  
- **Video File Support**: Analyze pre-recorded videos for object tracking.  
- **Versatile Trackers**: Compare the CSRT tracker with other trackers like MOSSE, KCF, and MIL.  

---

## How CSRT Works  

The **CSRT tracker** uses advanced techniques like spatial reliability maps and feature extraction to focus on stable object regions, ensuring precision even in complex conditions. It adapts dynamically to changes in object size or occlusion.  

---

## How to Use  

1. **Real-Time Tracking**: Track objects live via webcam.  
2. **Video Analysis**: Track objects in pre-recorded videos.  
3. **Custom Trackers**: Switch between different OpenCV trackers for comparison.  

---

## File Structure  
```
project/ 
├── CSRT_tracker.py # Main script for tracking 
├── football.clip.mp4 # Optional sample video 
├── README.md # Documentation 
├── requirements.txt # Dependencies list
```
---

## Prerequisites  

- Python 3.7+  
- OpenCV 4.x+  

Install dependencies using the `requirements.txt` file.  

---

## License  

This project is licensed under the MIT License.  

---  

**Explore object tracking effortlessly!**  
