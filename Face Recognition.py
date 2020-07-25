import tensorflow.keras
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import cv2


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('test_photo.jpg')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
# i did some changes
print ("Compatibility ratio with models :")
print("  flash || spaderman")
prediction = model.predict(data)
#print(np.argmax(prediction[0]))
#max_index = np.argmax(predictions[0])

reselt=str(prediction)
removed = reselt.replace("[", "")
removed1 = removed.replace("]", "")

data = removed1.split(" ") 
if (data[0]>data[1]):
    print("he's flash")
   
    im=Image.open('test_photo.jpg');
    d = ImageDraw.Draw(im)
    d.text((30,30), "flash", fill=(0,255,255))
    im.show()


    #--------------------

elif (data[0]<data[1]):
    print("he's spaderman")
    im=Image.open('test_photo.jpg');
    d = ImageDraw.Draw(im)
    d.text((30,30), "spaderman", fill=(0,255,255))
    im.show()




