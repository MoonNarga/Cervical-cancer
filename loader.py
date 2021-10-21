import paddle
from dataset import MyDataset

BATCH_SIZE = 64
BATCH_NUM = 20

# 测试定义的数据集
custom_dataset = MyDataset()

print('=============custom dataset=============')
for data, label in custom_dataset:
    data.show()
    label.show()
    break

# train_loader = paddle.io.DataLoader(custom_dataset, batch_size=BATCH_SIZE, shuffle=True)
# # 如果要加载内置数据集，将 custom_dataset 换为 train_dataset 即可
# for batch_id, data in enumerate(train_loader()):
#     x_data = data[0]
#     y_data = data[1]

#     print(x_data.shape)
#     print(y_data.shape)
#     break