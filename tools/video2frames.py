import cv2
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--raw_video", type=str, default=None)
parser.add_argument("--frame_dir", type=str, default=None)
args = parser.parse_args()


def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])


def video2frames(input_file, output_dir):
    v = cv2.VideoCapture(input_file)
    print("video: {}".format(input_file))
    print("video FPS: {}".format(v.get(cv2.CAP_PROP_FPS)))
    print("video frame count: {}".format(v.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("video frame width: {}".format(v.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print("video frame height: {}".format(v.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("video frame fourcc: {}".format(decode_fourcc(v.get(cv2.CAP_PROP_FOURCC))))
    print("video frame format: {}".format(v.get(cv2.CAP_PROP_FORMAT)))

    success = True
    num = 0
    while success:
        success, frame = v.read()
        if not success:
            print("write {} frames ".format(num))
            break
        num = num + 1
        output_file_path = os.path.join(output_dir, str(num) + ".jpg")
        cv2.imwrite(output_file_path, frame)

    print("video2frames done")


def main():
    if not os.path.exists(args.raw_video):
        print("raw video file not exists!")
        return

    if os.path.exists(args.frame_dir):
        print("delete dir: {}".format(args.frame_dir))
        shutil.rmtree(args.frame_dir)
    print("output dir [frame dir]: {}".format(args.frame_dir))
    os.mkdir(args.frame_dir)

    video2frames(args.raw_video, args.frame_dir)


if __name__ == "__main__":
    main()
