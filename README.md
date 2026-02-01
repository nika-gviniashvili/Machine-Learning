
About this project:

In this project, the main goal was to analyze network traffic data and detect DDoS attacks using a Convolutional Neural Network (CNN).
Usually, network traffic analysis is done by applying machine learning algorithms directly to numerical features. 
In this scenario, a different approach was taken: the network traffic data was first converted into images, and these images were then used as input for a CNN model.
This approach was chosen because CNNs are especially good at learning patterns from images. 
By transforming network traffic features into image form, the CNN can learn relationships between features, instead of treating each feature separately. This makes it possible to apply image-based deep learning techniques to network traffic data.

The idea of converting network data into images is based on representing numerical feature vectors as two-dimensional matrices.
In this project, each network flow contains 80 numeric features. These features are reshaped into an 8 × 10 matrix, and the matrix is saved as a grayscale image.
Each pixel in the image represents one normalized network feature, and the brightness of the pixel corresponds to the feature value.

Although these images may look like random noise to a human eye, they still preserve important relationships between features. 
CNNs are able to learn from these pixel-level patterns, even if the images do not contain clear visual shapes.

About the Dataset:

The dataset used in this project is a network traffic dataset in CSV format: Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
The dataset was obtained from Kaggle.com:
Link:https://www.kaggle.com/datasets/ishasingh03/friday-workinghours-afternoon-ddos

Each row in the dataset represents a single network flow, while each column represents a network feature, such as packet counts, packet lengths, flow duration, and timing statistics.
The dataset also includes a label column, which indicates whether the traffic is benign or ddos.

Program Workflow:
The program consists of two main steps:

Converting network traffic data from CSV format into images,
Training a convolutional neural network using the generated images.

Step 1: Converting Network Data into Images
Data Preprocessing

First, the CSV file is loaded using Python code.
The label column is converted to lowercase and mapped as follows:

benign → 0
ddos → 1

Only numeric features are kept for further processing. Non-numeric columns such as IP addresses, timestamps, and flow identifiers are removed because they cannot be directly used in numerical computations.
Some network features contain infinite or invalid values, which usually occur because of division by zero in traffic calculations. These values are handled, and rows containing invalid data are removed to prevent errors during normalization.
After cleaning, all numeric features are normalized to the range 0, 1 using MinMaxScaler. This step ensures that all features contribute equally to the learning process.

Note: To reduce execution time after running the code and to simplify experimentation, the number of processed network flows is limited to 1000 samples.

Image Generation:

After preprocessing, one row in the CSV corresponds to one image; 

Images are saved according to their label in the following folders:

dataset/benign
dataset/malware

Step 2: CNN Model Training

The generated images are used as input for the CNN model.
Images are loaded directly from the dataset directory using ImageDataGenerator, where folder names are automatically interpreted as class labels.

The dataset is automatically split into:

80% training data and 20% validation data.


About CNN Architecture:

A simple CNN architecture is used in this project:

one convolutional layer to extract feature patterns, 
one max-pooling layer to reduce spatial dimensions,
one flatten layer,
Two dense layers for classification.

The output layer uses a sigmoid activation function to classify traffic as benign or DDoS.

The model is trained for 5 epochs and saved after training.
During training, the CNN achieved high accuracy on both training and validation data, which shows that the model was able to learn meaningful patterns from the image-based representation of network traffic.

Conclusion

In this project, network traffic data was successfully converted from CSV format into grayscale images and used to train a convolutional neural network for DDoS detection. 
Converting network features into images made it possible to apply CNNs, which are effective at learning spatial relationships between features. 
The image size was selected based on the number of available features, and the dataset size was limited to reduce execution time. 

This project shows that representing network traffic as images is a practical and effective approach for network attack detection.
