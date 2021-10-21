import paddle
from paddle.io import Dataset
import os
from PIL import Image

IMAGE_SIZE = (1440, 1080)
CLASS_NUM = 2

class MyDataset(Dataset):
    """
    步骤一：继承paddle.io.Dataset类
    """
    def __init__(self):
        """
        步骤二：实现构造函数，定义数据集大小
        """
        super(MyDataset, self).__init__()
        self.num_samples = 0
        self.train_images = []
        self.train_labels = []
        path = "E:/iodine" 
        for root, dirs, files in os.walk(path):
            for subdir in dirs:
                if (subdir != "iodine"):
                    self.train_images.append(Image.open(os.path.join(root, subdir, "img.png")))
                    self.train_labels.append(Image.open(os.path.join(root, subdir, "label.png")))
                    self.num_samples += 1

    def __getitem__(self, index):
        """
        步骤三：实现__getitem__方法，定义指定index时如何获取数据，并返回单条数据（训练数据，对应的标签）
        """
        
        data = self.train_images[index]
        label = self.train_labels[index]

        return data, label

    def __len__(self):
        """
        步骤四：实现__len__方法，返回数据集总数目
        """
        return self.num_samples