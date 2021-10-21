import paddle
from paddle.io import Dataset
import os
from PIL import Image

IMAGE_SIZE = (1440, 1080)
CLASS_NUM = 2

class IodineDataset(Dataset):
    """
    步骤一：继承paddle.io.Dataset类
    """
    def __init__(self):
        """
        步骤二：实现构造函数，定义数据集大小
        """
        super(IodineDataset, self).__init__()
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

class AceticDataset(Dataset):
    """
    步骤一：继承paddle.io.Dataset类
    """
    def __init__(self):
        """
        步骤二：实现构造函数，定义数据集大小
        """
        super(AceticDataset, self).__init__()
        self.num_samples = 0
        self.train_images_0100 = []
        self.train_images_0130 = []
        self.train_images_0200 = []
        self.train_images_0230 = []
        self.train_labels_0100 = []
        self.train_labels_0130 = []
        self.train_labels_0200 = []
        self.train_labels_0230 = []
        path = "E:/acetic" 
        for root, dirs, files in os.walk(path):
            for subdir in dirs:
                if (subdir != "acetic" and subdir != "0100" and subdir != "0130" and subdir != "0200" and subdir != "0230"):
                    self.train_images_0100.append(Image.open(os.path.join(root, subdir, "0100/img.png")))
                    self.train_images_0130.append(Image.open(os.path.join(root, subdir, "0130/img.png")))
                    self.train_images_0200.append(Image.open(os.path.join(root, subdir, "0200/img.png")))
                    self.train_images_0230.append(Image.open(os.path.join(root, subdir, "0230/img.png")))
                    self.train_labels_0100.append(Image.open(os.path.join(root, subdir, "0100/label.png")))
                    self.train_labels_0130.append(Image.open(os.path.join(root, subdir, "0130/label.png")))
                    self.train_labels_0200.append(Image.open(os.path.join(root, subdir, "0200/label.png")))
                    self.train_labels_0230.append(Image.open(os.path.join(root, subdir, "0230/label.png")))
                    self.num_samples += 1

    def __getitem__(self, index):
        """
        步骤三：实现__getitem__方法，定义指定index时如何获取数据，并返回单条数据（训练数据，对应的标签）
        """
        
        data = [self.train_images_0100[index], self.train_images_0130[index], self.train_images_0200[index], self.train_images_0230[index]]
        label = [self.train_labels_0100[index], self.train_labels_0130[index], self.train_labels_0200[index], self.train_labels_0230[index]]

        return data, label

    def __len__(self):
        """
        步骤四：实现__len__方法，返回数据集总数目
        """
        return self.num_samples