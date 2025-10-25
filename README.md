# VT-MFLV
This repo is the official implementation of "VT-MFLV: Vision-Text Multimodal Feature Learning V Network for Medical Image Segmentation"

<img width="527" height="401" alt="frame" src="https://github.com/user-attachments/assets/734b67a2-0bfe-4af1-8387-2d547fbcd0f2" />

## Requirements

Python == 3.7 and install from the ```requirements.txt``` using:
```angular2html
pip install -r requirements.txt
```
Questions about NumPy version conflict. The NumPy version we use is 1.17.5. We can install bert-embedding first, and install NumPy then.

## Usage

### 1. Data Preparation
#### 1.1. QaTa-COV19, MosMedData+ and MoNuSeg Datasets (demo dataset)
The original data can be downloaded in following links:
* QaTa-COV19 Dataset - [Link (Original)](https://www.kaggle.com/datasets/aysendegerli/qatacov19-dataset)

* MosMedData+ Dataset - [Link (Original)](http://medicalsegmentation.com/covid19/) or [Kaggle](https://www.kaggle.com/datasets/maedemaftouni/covid19-ct-scan-lesion-segmentation-dataset)

* MoNuSeG Dataset (demo dataset) - [Link (Original)](https://monuseg.grand-challenge.org/Data/)

* ESO-CT Dataset [1] [2]

[1] Jin, Dakai, et al. "DeepTarget: Gross tumor and clinical target volume segmentation in esophageal cancer radiotherapy." Medical Image Analysis 68 (2021): 101909.

[2] Ye, Xianghua, et al. "Multi-institutional validation of two-streamed deep learning method for automated delineation of esophageal gross tumor volume using planning CT and FDG-PET/CT." Frontiers in Oncology 11 (2022): 785788.

The text annotation of QaTa-COV19 has been released!

  *(Note: The text annotation of QaTa-COV19 train and val datasets [download link](https://1drv.ms/x/s!AihndoV8PhTDkm5jsTw5dX_RpuRr?e=uaZq6W).
  The partition of train set and val set of QaTa-COV19 dataset [download link](https://1drv.ms/u/s!AihndoV8PhTDgt82Do5kj33mUee33g?e=kzWl8y).
  The text annotation of QaTa-COV19 test dataset [download link](https://1drv.ms/x/s!AihndoV8PhTDkj1vvvLt2jDCHqiM?e=954uDF).)*

  ***(Note: The contrastive label is available in the repo.)***
  
***(Note: The text annotation of MosMedData+ train dataset [download link](https://1drv.ms/x/s!AihndoV8PhTDguIIKCRfYB9Z0NL8Dw?e=8rj6rY).
The text annotation of MosMedData+ val dataset [download link](https://1drv.ms/u/s!AihndoV8PhTDguIGtAgZiRQFYfsAjw?e=tqowkJ).
The text annotation of MosMedData+ test dataset [download link](https://1drv.ms/u/s!AihndoV8PhTDguIHdHkwXMxGlgU9Tg?e=PbcllF).)***
  
  *If you use the datasets provided by us, please cite the LViT.*

#### 1.2. Format Preparation

Then prepare the datasets in the following format for easy use of the code:

```angular2html
├── datasets
    ├── QaTa-Covid19
    │   ├── Test_Folder
    |   |   ├── Test_text.xlsx
    │   │   ├── img
    │   │   └── labelcol
    │   ├── Train_Folder
    |   |   ├── Train_text.xlsx
    │   │   ├── img
    │   │   └── labelcol
    │   └── Val_Folder
    |	    ├── Val_text.xlsx
    │       ├── img
    │       └── labelcol
    └── MosMedDataPlus
        ├── Test_Folder
        |   ├── Test_text.xlsx
        │   ├── img
        │   └── labelcol
        ├── Train_Folder
        |   ├── Train_text.xlsx
        │   ├── img
        │   └── labelcol
        └── Val_Folder
            ├── Val_text.xlsx
            ├── img
            └── labelcol
```


### 2. Training

#### 2.1. Pre-training
You can replace LVIT with U-Net for pre training and run:
```angular2html
python train_model.py
```

#### 2.2. Training

You can train to get your own model. It should be noted that using the pre-trained model in the step 2.1 will get better performance or you can simply change the model_name from LViT to LViT_pretrain in config.

```angular2html
python train_model.py
```


### 3. Evaluation

#### Test the Model and Visualize the Segmentation Results
First, change the session name in ```Config.py``` as the training phase. Then run:
```angular2html
python test_model.py
```
You can get the Dice and IoU scores and the visualization results. 
