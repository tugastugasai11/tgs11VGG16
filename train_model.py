import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1. Persiapkan Dataset
train_dir = 'data/train'
test_dir = 'data/test'

train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

# Menggunakan class_mode='categorical' karena ada 3 kelas (Adidas, Converse, Nike)
train_data = train_datagen.flow_from_directory(train_dir, target_size=(224, 224), batch_size=32, class_mode='categorical')
test_data = test_datagen.flow_from_directory(test_dir, target_size=(224, 224), batch_size=32, class_mode='categorical')

# 2. Load Model VGG16 Pretrained
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Membekukan layer agar tidak di-train ulang
for layer in base_model.layers:
    layer.trainable = False

# 3. Tambahkan Layer Klasifikasi Baru
model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax') # Output 3 kelas
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 4. Latih Model
print("Memulai pelatihan model...")
model.fit(train_data, validation_data=test_data, epochs=10)

# 5. Simpan Model
model.save('model_sepatu_vgg16.h5')
print("Model berhasil disimpan sebagai 'model_sepatu_vgg16.h5'")