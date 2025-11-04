import cv2
import os
import time
import numpy as np
import sys

# Hide cursor (for smoother visuals)
def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

# Show cursor back
def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def rgb_to_ansi(r, g, b):
    """Return ANSI escape code for RGB color."""
    return f"\033[38;2;{r};{g};{b}m"

def convert_frame_to_ascii(frame, width=80):
    """
    Convert a frame to colorized ASCII art.
    Uses downscaling and brightness mapping for efficiency.
    """
    ascii_chars = " .:-=+*#%@"

    height = int(frame.shape[0] * width / frame.shape[1] / 2)
    height = max(1, height)

    # Resize for speed
    frame = cv2.resize(frame, (width, height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ascii_lines = []
    for y in range(height):
        line = []
        for x in range(width):
            b, g, r = frame[y, x]
            brightness = gray[y, x] / 255.0
            char = ascii_chars[int(brightness * (len(ascii_chars) - 1))]
            line.append(f"{rgb_to_ansi(r, g, b)}{char}")
        ascii_lines.append("".join(line) + "\033[0m")
    return "\n".join(ascii_lines)

def play_video_in_terminal(video_path, width=80, fps=0):
    if not os.path.exists(video_path):
        print(f"❌ File '{video_path}' not found.")
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1.0 / (fps or video_fps or 24)

    hide_cursor()
    sys.stdout.write("\033[2J")  # clear once

    try:
        prev_time = time.time()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_art = convert_frame_to_ascii(frame, width)

            # Move cursor to top-left only (don’t clear screen)
            sys.stdout.write("\033[H")
            sys.stdout.write(ascii_art)
            sys.stdout.flush()

            # precise frame pacing
            now = time.time()
            elapsed = now - prev_time
            if elapsed < frame_delay:
                time.sleep(frame_delay - elapsed)
            prev_time = now

    except KeyboardInterrupt:
        print("\n⏹️ Playback stopped.")
    finally:
        show_cursor()
        sys.stdout.write("\033[0m")
        cap.release()


if __name__ == "__main__":
    video_path = input("📂 Enter full path to video file: ").strip()
    if not os.path.exists(video_path):
        print("❌ File not found.")
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
