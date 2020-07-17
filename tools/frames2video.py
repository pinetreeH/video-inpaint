import cv2
import os
import time


def frames2video(input_frame_dir, output_file, fps, frame_width, frame_height):
    frames = os.listdir(input_frame_dir)
    frames.sort(key=lambda x:int(x[:-4]))

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
    print("output file is {}".format(output_file))


if __name__ == "__main__":
    input_frame_dir = './testdata/v1-frames'
    output_file = "./testdata/v1-frames-2video" + str(int(time.time())) + ".avi"
    fps = 25
    frame_width = 636
    frame_height = 360
    frames2video(input_frame_dir, output_file, fps, frame_width, frame_height)
