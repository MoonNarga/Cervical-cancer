from matplotlib.pyplot import pause
import paddle.vision.datasets as s
import time
a = s.Cifar10()
for i in range(10):
    d = a[i][0]
    d.show()
    print(a[i][1])
    time.sleep(3)
    d.close()
    
