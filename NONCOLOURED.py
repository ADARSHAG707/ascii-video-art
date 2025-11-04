import cv2
import os
import time
import numpy as np
import sys

def convert_frame_to_ascii(frame, width=80):
    """
    Convert a frame to ASCII art using brightness levels.
    """
    ascii_chars = " .:-=+*#%@"

    height = int(frame.shape[0] * width / frame.shape[1] / 2)
    height = max(1, height)

    resized_frame = cv2.resize(frame, (width, height))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    normalized = gray_frame / 255.0
    ascii_frame = ""
    for row in normalized:
        ascii_frame += "".join(ascii_chars[int(pixel * (len(ascii_chars) - 1))] for pixel in row)
        ascii_frame += "\n"
    return ascii_frame


def play_video_in_terminal(video_path, width=80, fps=0):
    """
    Play a video as ASCII art in terminal (static, no scrolling).
    """
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file '{video_path}' not found.")
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1.0 / (video_fps if fps == 0 and video_fps > 0 else fps or 30)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_art = convert_frame_to_ascii(frame, width)

            # Move cursor to top-left without clearing screen fully
            sys.stdout.write("\033[H\033[J")  # clear + reset cursor
            sys.stdout.write(ascii_art)
            sys.stdout.flush()

            time.sleep(frame_delay)

    except KeyboardInterrupt:
        print("\n⏹️ Playback interrupted by user.")
    finally:
        cap.release()


if __name__ == "__main__":
    video_path = input("📂 Enter the full path to your video file: ").strip()
    if not os.path.exists(video_path):
        print("❌ File not found. Please check your path.")
        sys.exit(1)

    try:
        width = int(input("📏 Enter terminal width (default 80): ") or "80")
    except ValueError:
        width = 80

    try:
        fps = int(input("🎞️ Enter FPS (default uses video FPS): ") or "0")
    except ValueError:
        fps = 0

    play_video_in_terminal(video_path, width, fps)
