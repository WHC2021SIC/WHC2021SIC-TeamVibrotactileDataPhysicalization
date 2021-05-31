import tensorflow as tf

# Restore model
print(tf.__version__)
loaded_model = tf.keras.models.load_model('./xyForcePlate/')


# In[58]:


# Run predict with restored model
#predictions = loaded_model.predict(norm_test_X)