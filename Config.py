# -*- coding: utf-8 -*-
import os
import torch
import time
import ml_collections

## PARAMETERS OF THE MODEL
save_model = True
tensorboard = True
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
use_cuda = torch.cuda.is_available()
seed = 666
os.environ['PYTHONHASHSEED'] = str(seed)

cosineLR = True  # Use cosineLR or not
n_channels = 3
n_labels = 1  # MoNuSeg & Covid19
epochs = 2000
img_size = 224
print_frequency = 1
save_frequency = 5000
vis_frequency = 10
early_stopping_patience = 200 # 50 ljq100

pretrain = False
task_name = 'MoNuSeg' 
# task_name = 'Covid19'
learning_rate = 1e-4  # MoNuSeg: 1e-3, Covid19: 3e-4, ljq: 5e-5,1e-5,5e-6
batch_size = 4  # For LViT-T, 2 is better than 4

model_name = 'LViT'
# model_name = 'LViT_pretrain'

train_dataset = './datasets/' + task_name + '/Train_Folder/'
val_dataset = './datasets/' + task_name + '/Val_Folder/'
test_dataset = './datasets/' + task_name + '/Test_Folder/'
task_dataset = './datasets/' + task_name + '/Train_Folder/'
session_name = 'Test_session' + '_' + time.strftime('%m.%d_%Hh%M')
save_path = task_name + '/' + model_name + '/' + session_name + '/'
model_path = save_path + 'models/'
tensorboard_folder = save_path + 'tensorboard_logs/'
logger_path = save_path + session_name + ".log"
visualize_path = save_path + 'visualize_val/'
test_session = 'Test_session_11.22_15h39'  # ljq add this line

##########################################################################
# CTrans configs
##########################################################################
def get_CTranS_config():
    config = ml_collections.ConfigDict()
    config.transformer = ml_collections.ConfigDict()  # 确保 transformer 字段被初始化
    config.KV_size = 960
    config.transformer.num_heads = 8  # 定义 transformer 中的 attention heads
    config.transformer.num_layers = 4  # 定义 transformer 的层数
    config.expand_ratio = 4  # MLP 扩展比率
    config.transformer.embeddings_dropout_rate = 0.1
    config.transformer.attention_dropout_rate = 0.1
    config.transformer.dropout_rate = 0
    config.patch_sizes = [16, 8, 4, 2]
    config.base_channel = 64  # U-Net 的基本通道
    config.n_classes = 1
    return config


# used in testing phase, copy the session name in training phase
# test_session = "Test_session_05.23_14h19"  # dice=79.98, IoU=66.83
