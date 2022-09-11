from operator import index
import sys, os, glob
import pprint
from PIL import Image
import matplotlib.pyplot as plt

def get_file_list():
    """
    - Args:
    - Returns:
    """
    # file_list = glob.glob(os.path.join("..", "data", "*"))
    prefix = "../data/Morning_glory_"
    file_list = [
        "original_x4.jpg",
        "realesr-animevideov3-x4.jpg",
        "realesrgan-x4plus.jpg",
        "realesrgan-x4plus-anime.jpg",
        "waifu2x(CUnet)(noise_scale)(Level0)(x4.000000).jpg"
    ]
    pprint.pprint(file_list)
    return prefix, file_list


def create_graph():
    prefix, file_list = get_file_list()

    n_data = len(file_list) # 表示するデータ数
    # fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(20,20))
    fig = plt.figure(figsize=(30,40), tight_layout=True)

    # fig.suptitle("Comparison of illustration images upscaled by Real-ESRGAN, waifu2x", fontsize=48)

    for file_name in file_list:
        i = file_list.index(file_name)
        img = Image.open(prefix + file_name)
        img_crop = img.crop((3300, 1500, 4300, 2500))
        """
        nrows，ncols，indexは位置と大きさを決めるパラメータで、整数を入れる。台紙Figureを、縦nrows分割・横ncols分割したうちのindex番目の位置に配置されたAxesが返される。グラフを1つしか作らないときは(1, 1, 1)で良い。
        """
        if i == 0:
            ax = fig.add_subplot(3, 2, 1)
        elif i == 1:
            ax = fig.add_subplot(3, 2, 3)
        elif i == 2:
            ax = fig.add_subplot(3, 2, 4)
        elif i == 3:
            ax = fig.add_subplot(3, 2, 5)
        elif i == 4:
            ax = fig.add_subplot(3, 2, 6)
        else:
            sys.exit(1)
        ax.set_title(file_name, fontsize=40)
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.imshow(img_crop)

    # ax = fig.add_subplot(3, 2, 2)
    # ax.text(0.2, 0.5, "Comparison of\nillustration images\nupscaled by Real-ESRGAN, waifu2x", fontsize=60, color="black", bbox=(dict(boxstyle="round", fc="white")))
    # ax.axes.xaxis.set_visible(False)
    # ax.axes.yaxis.set_visible(False)

    
    fig.savefig("../data/comparison.jpg")


def main():
    """
    - Args:
    - Returns:
    """
    # get_file_list()
    create_graph()


if __name__ == '__main__':
    main()
