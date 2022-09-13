import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

import os, PIL

import numpy as np
np.random.seed(1)

import tensorflow as tf
tf.random.set_seed(1)
import pathlib
data_dir = '/Users/chubingnan/Dev/github/arc0035/Recognition-of-eye-state-based-on-Vgg16/Eye_dataset'
data_dir = pathlib.Path(data_dir)
print(data_dir)

image_count = len(list(data_dir.glob('*/*')))
print('图片总数为:', image_count)

# 参数准备
batch_size = 8
img_height = 224
img_width = 224

# 数据集-训练集
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    seed=12,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

# 数据集-测试集
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    seed = 12,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

class_names = train_ds.class_names
print(class_names)
class_names = val_ds.class_names
print(class_names)

# plt.figure(figsize=(10,5))
# plt.suptitle('Data Visualization')
#
# for images, labels in train_ds.take(1):
#     for i in range(8):
#         ax = plt.subplot(2, 4, i+1)
#         plt.imshow(images[i].numpy().astype('uint8'))
#         plt.title(class_names[labels[i]])
#         plt.savefig('pic1.jpg', dpi=600)
#         plt.axis('off')

for images_batch, labels_batch in train_ds:
    print(images_batch.shape)
    print(labels_batch.shape)
    break

# config data set
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(AUTOTUNE)

# vgg-16
model = tf.keras.applications.VGG16()
model.summary()

initial_learning_rate = 1e-4
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps = 20,
    decay_rate = 0.96,
    staircase = True
)
optimizer = tf.keras.optimizers.Adam(learning_rate = lr_schedule)

model.compile(
    optimizer = optimizer,
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

epochs = 10
history = model.fit(
    train_ds,
    validation_data= val_ds,
    epochs = epochs
)

