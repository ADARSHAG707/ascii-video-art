# 🎬 ASCII Video Art in Terminal

After a long time away from Python, I wanted to build something creative — so I made a **real-time colorized ASCII video player** that runs directly in your **terminal** 🧠✨

It reads any video and converts it into colorful ASCII art using **OpenCV**, **NumPy**, and **ANSI escape codes** — giving your terminal a cinematic glow-up!

---

## 🚀 Features

- 🎨 **Colorized ASCII rendering** — full RGB mapped to ANSI colors  
- ⚡ **Smooth playback** with minimal flicker using cursor control  
- 🧩 **Customizable width & FPS** — fits any terminal size  
- 🪶 **Lightweight & portable** — runs entirely in Python  

---

## 🧠 How It Works

1. Each frame of the video is captured via OpenCV  
2. Pixels are converted to ASCII characters based on brightness  
3. Each character’s color is mapped using its RGB values  
4. Frames are drawn in-place using ANSI cursor repositioning for smooth animation  

---

## 📦 Installation

Make sure you have **Python 3.10+** installed.

Then install dependencies:-

bash
pip install opencv-python numpy

▶️ Usage

Run the script:

python ascii_video_art.py

Then provide:

    📂 Full path to your video file (e.g. C:\Users\ADARSH\Downloads\video.mp4)

    📏 Width of your terminal (default: 120)

    🎞️ FPS (default uses video FPS)

I wanted to push the idea further with color, performance, and interactivity.
📁 Repository Contents

ascii-video-art/
│
├── ascii_video_art.py    # Main program file
├── README.md             # You’re here!
└── aura farmer.mp4      # (optional demo video)

🌐 Connect

💼 Author: Adarsh AG
