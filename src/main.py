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
    """
    - Args:
    - Returns:
    """
    prefix, file_list = get_file_list()
    fig = plt.figure(figsize=(30,40), tight_layout=True)
    
    for file_name in file_list:
        i = file_list.index(file_name)
        img = Image.open(prefix + file_name)
        img_crop = img.crop((3300, 1500, 4300, 2500))
        """
        https://qiita.com/nkay/items/d1eb91e33b9d6469ef51#21-figureadd_subplot
        """
        if i == 0:
            ax = fig.add_subplot(3, 2, 1)
        elif i >= 1:
            ax = fig.add_subplot(3, 2, i+1)
        else:
            sys.exit(1)
        ax.set_title(file_name, fontsize=40)
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.imshow(img_crop)
    
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
