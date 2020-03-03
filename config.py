"""
配置文件
"""
from num_sequence import NumSequence
import torch

device= torch.device("cpu")
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

train_batchsize = 256
test_batch_size = 500


ns = NumSequence()
max_len = 10
