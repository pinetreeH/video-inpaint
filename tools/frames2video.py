import cv2
import os
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--frame_dir", type=str, default=None)
parser.add_argument("--fps", type=int, default=25)
parser.add_argument("--frame_width", type=int, default=100)
parser.add_argument("--frame_height", type=int, default=100)
parser.add_argument("--video_dir", type=str, default=None)

args = parser.parse_args()


def frames2video(input_frame_dir, output_file, fps, frame_width, frame_height):
    print("input_frame_dir: {} ".format(input_frame_dir))
    print("output video file is {}".format(output_file))
    print("fps is {}".format(fps))
    print("frame_width is {}".format(frame_width))
    print("frame_height is {}".format(frame_height))

    frames = os.listdir(input_frame_dir)
    frames.sort(key=lambda x: int(x[:-4]))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
    count = 0
    for frame in frames:
        count = count + 1
        file = os.path.join(input_frame_dir, frame)
        img = cv2.imread(file)
        video.write(img)

    video.release()
    print("read {} frames ".format(count))


def main():
    if not os.path.exists(args.frame_dir):
        print("frame dir not exists: {}".format(args.frame_dir))
        return

    if not os.path.exists(args.video_dir):
        print("create video dir: {}".format(args.video_dir))
        os.mkdir(args.frame_dir)

    output_file = os.path.join(args.video_dir, str(int(time.time())) + ".avi")
    frames2video(args.frame_dir, output_file, args.fps, args.frame_width, args.frame_height)


if __name__ == "__main__":
    main()
