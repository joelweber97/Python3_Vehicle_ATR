#!/usr/bin/env python
# coding: utf-8

# CNN can be trained for single class of data as well, here we need to understand 2 aspects of it.
# 
# 1. Simple way is : you take single class and randomly mix of many other classes label data and train in CNN
# 2. Auto encoder way: Train your single set of images (make sure dataset cover very high variance), then now in prediction time: pass images to autoencoder and check reconstruction error. If reconstruction error high: they say “my single class NOT found in this image”, if it’s in manageable range, then say “my single class FOUND”

# ### simple cnn way

# In[1]:

import cv2
import tensorflow as tf


# In[2]:



import numpy as np
import glob
import tensorflow as tf
import tensorflow
from tensorflow.keras import datasets, layers, models

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
#from tensorflow.keras.utils import np_utils
from tensorflow.keras import utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# In[28]:


'''
im = cv2.imread('./image_chips2/clipped_image_254.png')
#im2 = Image.open('./image_chips/clipped_image_1.tif.png')


print(im.shape)



cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()




image_files = glob.glob('./image_chips2/*.png')
#print(image_files)'''


# In[3]:


vehicle_images = glob.glob('./vehicle_chips2/*/*.png')
len(vehicle_images)


# In[4]:


vehicle_labels = np.ones(shape = (3271, 1)).astype('uint8')
vehicle_labels.shape


# In[5]:


tree_images = glob.glob('./tree_chips2/*/*.png')
len(tree_images)


# In[6]:


tree_labels = np.zeros(shape = (1925,1)).astype('uint8')
tree_labels.shape


# In[7]:


vehicles = []
for i in vehicle_images:
    data = cv2.imread(i)
    vehicles.append(data)
vehicles = np.array(vehicles)


# In[8]:


vehicles = vehicles/255.


# In[9]:


trees = []
for t in tree_images:
    data = cv2.imread(t)
    trees.append(data)
    
trees = np.array(trees)


# In[10]:


trees = trees/255.


# In[ ]:





# In[11]:


images = np.append(vehicles, trees, axis = 0)
images.shape


# In[12]:


labels = np.append(vehicle_labels, tree_labels, axis = 0)
labels.shape


# In[ ]:





# In[ ]:





# In[13]:


X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.8, random_state=42)


# In[ ]:





# In[ ]:





# In[14]:


model = models.Sequential()
model.add(layers.Conv2D(24, (3, 3), activation='relu', input_shape=(24, 24, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(48, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(48, (3, 3), activation='relu'))


# In[ ]:





# In[15]:


model.summary()


# In[ ]:





# In[16]:


callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5)


# In[ ]:





# In[17]:


model.add(layers.Flatten())
model.add(layers.Dense(48, activation='relu'))
model.add(layers.Dense(2))


# In[ ]:





# In[18]:


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


# In[ ]:





# In[19]:


model.fit(X_train, y_train, epochs = 100, batch_size = 2, callbacks=[callback])


# In[20]:


print(tf.__version__)


# In[21]:


print(tensorflow.python.platform.build_info.build.build_info())


# In[ ]:





# In[80]:


y_pred = model.predict(X_test)


# In[81]:


y_pred


# In[82]:


guess = np.argmax(y_pred, axis = 1)
guess = guess.reshape((len(y_test)), 1)
guess


# In[ ]:





# In[83]:


y_test


# In[ ]:





# In[84]:


results = confusion_matrix(y_test, guess)


# In[85]:


results


# ![Screen%20Shot%202022-01-09%20at%206.49.09%20PM.png](attachment:Screen%20Shot%202022-01-09%20at%206.49.09%20PM.png)

# In[86]:


'''        
    
    
                            Actual Values
                            0     1
            
                        0  1530.  2. 
                
predicted values        1  7.     2618.  




'''


# In[ ]:





# In[87]:


print(classification_report(y_test, guess))


# In[ ]:





# In[88]:


combined = np.concatenate((y_test, guess), axis = 1)
combined


# In[ ]:





# ### Autoencoder way

# In[ ]:




