import cv2
import os


def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])


def video2frames(input_file, output_dir):
    v = cv2.VideoCapture(input_file)
    print("video {} FPS: {}".format(input_file, v.get(cv2.CAP_PROP_FPS)))
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


if __name__ == "__main__":
    input_file = './testdata/v1.mp4'
    output_dir = "./testdata/v1-frames-tmp"
    video2frames(input_file, output_dir)
