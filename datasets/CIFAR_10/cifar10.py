from torch.utils.data import Dataset
from torchvision.transforms import Compose


def unpickle(file: str) -> dict:
    """
    数据集解压函数
    :param file: str 数据集路径
    :return: 返回一个字典
    """
    import pickle
    with open(file, 'rb') as fo:
        dict_ = pickle.load(fo, encoding='bytes')
    return dict_


def rmdirs(dir) -> None:
    """
    递归删除文件夹下所有文件
    :param dir: str
    """
    import os
    for f in [os.path.join(dir, simple_name) for simple_name in os.listdir(dir)]:
        if os.path.isfile(f):
            os.remove(f)
        elif os.path.isdir(f):
            rmdirs(f)
    os.rmdir(dir)


def save_image(data: bytes, path: str, label: int, target_file_name: str) -> None:
    """
    保存图片到指定文件
    :param path: 文件夹路径
    :param label: 标签号
    :param data: 数据
    :param target_file_name: 文件名
    """
    import os, numpy as np, PIL.Image as Image
    image = np.reshape(data, (3, 32, 32))
    image_data = image.transpose((1, 2, 0))  # 将原图(x,y,z)转置到新的坐标系(y,z,x)
    file_dir = os.path.join(path, str(label))
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    file = os.path.join(file_dir, target_file_name)
    image = Image.fromarray(image_data.astype(np.uint8), mode="RGB")
    image.save(file, 'png')


def save_all_image(path: str, length: int, data_list: list, label_list: list, file_names: list) -> None:
    """
    保存所有图片
    :param length:
    :param file_names:
    :param label_list:
    :param data_list:
    :param path
    :return:
    """
    for i in range(length):
        save_image(data_list[i], path, label_list[i], file_names[i])


def init(proj_path: str) -> None:
    """
    TODO
    :type proj_path: str
    :return:
    """
    import os

    temp_path: str = os.path.join(proj_path, "datasets", "CIFAR_10", ".temp")

    if not os.path.exists(temp_path):
        os.mkdir(temp_path)
    else:
        rmdirs(temp_path)
        os.mkdir(temp_path)

    train_path = os.path.join(temp_path, "train")
    os.mkdir(train_path)

    test_path = os.path.join(temp_path, "test")
    os.mkdir(test_path)

    data_file_path: str = os.path.join(proj_path, "datasets", "CIFAR_10", "data_batch")
    data: dict = unpickle(data_file_path)
    data_labels = data[b'labels']
    data_names = [str(name, 'utf-8') for name in data[b'filenames']]
    data_list = data[b'data']
    save_all_image(train_path, len(data_list), data_list, data_labels, data_names)

    test_file_path: str = os.path.join(proj_path, "datasets", "CIFAR_10", "test_batch")
    test: dict = unpickle(test_file_path)
    test_labels = test[b'labels']
    test_names = [str(name, 'utf-8') for name in test[b'filenames']]
    test_list = test[b'data']
    save_all_image(test_path, len(test_list), test_list, test_labels, test_names)


class CIFAR10(Dataset):
    def __init__(self, proj_path: str, compose: Compose = None):
        """
        CIFAR10数据集对象，其中包括10,000张图片，每张图片附带有一个标签。
        :param proj_path (str) 项目目录
        :param compose (Compose) 指定的图像操作方式
        """

    def __getitem__(self, item):
        """
        TODO
        :param item:
        :return:
        """

    def __len__(self):
        """
        TODO
        :return:
        """


if __name__ == '__main__':
    # TODO delete
    init("/Media/E/Programing/PyCharm/deep-learning")
