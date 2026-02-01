from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

DATASET_DIR = "dataset" #Directory where generated images where saved
IMG_H = 8
IMG_W = 10
EPOCHS = 5

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_H, IMG_W),
    color_mode="grayscale",
    class_mode="binary",
    subset="training"
)

val_data = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_H, IMG_W),
    color_mode="grayscale",
    class_mode="binary",
    subset="validation"
)

# CNN

model = Sequential([
    Conv2D(8, (3,3), activation="relu", input_shape=(IMG_H, IMG_W, 1)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# model training


model.fit(train_data, epochs=EPOCHS, validation_data=val_data)

model.save("cnn_model.h5")
print("It worked, Assignment is done!")
