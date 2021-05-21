#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the libraries
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input
from sklearn.model_selection import train_test_split

#from google.colab import files
#uploaded = files.upload()

D0_0 = 'https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/0%2C0.csv'
D0_12='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/0%2C12.csv'
D0_18='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/0%2C18.csv'
D0_24='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/0%2C24.csv'
D0_6='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/0%2C6.csv'
D12_0='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C0.csv'
D12_12='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C12.csv'
D12_15='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C15.csv'
D12_18='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C18.csv'
D12_21='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C21.csv'
D12_24='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C24.csv'
D12_3='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C3.csv'
D12_6='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C6.csv'
D12_9='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/12%2C9.csv'
D15_15='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/15%2C15.csv'
D15_21='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/15%2C21.csv'
D15_3='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/15%2C3.csv'
D15_9='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/15%2C9.csv'
D18_0='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/18%2C0.csv'
D18_12='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/18%2C12.csv'
D18_18='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/18%2C18.csv'
D18_24='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/18%2C24.csv'
D18_6='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/18%2C6.csv'
D3_0='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C0.csv'
D3_12='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C12.csv'
D3_15='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C15.csv'
D3_18='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C18.csv'
D3_21='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C21.csv'
D3_24='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C24.csv'
D3_3='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C3.csv'
D3_6='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C6.csv'
D3_9='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/3%2C9.csv'
D6_0='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C0.csv'
D6_12='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C12.csv'
D6_15='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C15.csv'
D6_18='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C18.csv'
D6_21='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C21.csv'
D6_24='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C24.csv'
D6_3='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C3.csv'
D6_6='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C6.csv'
D6_9='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/6%2C9.csv'
D9_0='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C0.csv'
D9_12='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C12.csv'
D9_15='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C15.csv'
D9_18='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C18.csv'
D9_21='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C21.csv'
D9_24='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C24.csv'
D9_3='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C3.csv'
D9_6='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C6.csv'
D9_9='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/9%2C9.csv'
Dnot='https://raw.githubusercontent.com/frankbastidas/WHC2021Datas/master/positionsTouchedData/noTouch.csv'
# 51 datasets

#df1 = pd.read_csv(url)

# Importing the Boston Housing dataset
#from sklearn.datasets import load_boston


# In[3]:


d0_0 = pd.read_csv(D0_0,header=None).transpose()
d0_0['x']=0; d0_0['y']=0
d0_12 = pd.read_csv(D0_12,header=None).transpose()
d0_12['x']=0; d0_12['y']=12
d0_18 = pd.read_csv(D0_18,header=None).transpose()
d0_18['x']=0; d0_18['y']=18
d0_24 = pd.read_csv(D0_24,header=None).transpose()
d0_24['x']=0; d0_24['y']=24
d0_6 = pd.read_csv(D0_6,header=None).transpose()
d0_6['x']=0; d0_6['y']=6
d12_0 = pd.read_csv(D12_0,header=None).transpose()
d12_0['x']=12; d12_0['y']=0
d12_12 = pd.read_csv(D12_12,header=None).transpose()
d12_12['x']=12; d12_12['y']=12
d12_15 = pd.read_csv(D12_15,header=None).transpose()
d12_15['x']=12; d12_15['y']=15
d12_18 = pd.read_csv(D12_18,header=None).transpose()
d12_18['x']=12; d12_18['y']=18
d12_21 = pd.read_csv(D12_21,header=None).transpose()
d12_21['x']=12; d12_21['y']=21
d12_24 = pd.read_csv(D12_24,header=None).transpose()
d12_24['x']=12; d12_24['y']=24
d12_3 = pd.read_csv(D12_3,header=None).transpose()
d12_3['x']=12; d12_3['y']=3
d12_6 = pd.read_csv(D12_6,header=None).transpose()
d12_6['x']=12; d12_6['y']=6
d12_9 = pd.read_csv(D12_9,header=None).transpose()
d12_9['x']=12; d12_9['y']=9
d15_15 = pd.read_csv(D15_15,header=None).transpose()
d15_15['x']=15; d15_15['y']=15
d15_21 = pd.read_csv(D15_21,header=None).transpose()
d15_21['x']=15; d15_21['y']=21
d15_3 = pd.read_csv(D15_3,header=None).transpose()
d15_3['x']=15; d15_3['y']=3
d15_9 = pd.read_csv(D15_9,header=None).transpose()
d15_9['x']=15; d15_9['y']=9
d18_0 = pd.read_csv(D18_0,header=None).transpose()
d18_0['x']=18; d18_0['y']=0
d18_12 = pd.read_csv(D18_12,header=None).transpose()
d18_12['x']=18; d18_12['y']=12
d18_18 = pd.read_csv(D18_18,header=None).transpose()
d18_18['x']=18; d18_18['y']=18
d18_24 = pd.read_csv(D18_24,header=None).transpose()
d18_24['x']=18; d18_24['y']=24
d18_6 = pd.read_csv(D18_6,header=None).transpose()
d18_6['x']=18; d18_6['y']=6
d3_0 = pd.read_csv(D3_0,header=None).transpose()
d3_0['x']=3; d3_0['y']=0
d3_12 = pd.read_csv(D3_12,header=None).transpose()
d3_12['x']=3; d3_12['y']=12
d3_15 = pd.read_csv(D3_15,header=None).transpose()
d3_15['x']=3; d3_15['y']=15
d3_18 = pd.read_csv(D3_18,header=None).transpose()
d3_18['x']=3; d3_18['y']=18
d3_21 = pd.read_csv(D3_21,header=None).transpose()
d3_21['x']=3; d3_21['y']=21
d3_24 = pd.read_csv(D3_24,header=None).transpose()
d3_24['x']=3; d3_24['y']=24
d3_3 = pd.read_csv(D3_3,header=None).transpose()
d3_3['x']=3; d3_3['y']=3
d3_6 = pd.read_csv(D3_6,header=None).transpose()
d3_6['x']=3; d3_6['y']=6
d3_9 = pd.read_csv(D3_9,header=None).transpose()
d3_9['x']=3; d3_9['y']=9
d6_0 = pd.read_csv(D6_0,header=None).transpose()
d6_0['x']=6; d6_0['y']=0
d6_12 = pd.read_csv(D6_12,header=None).transpose()
d6_12['x']=6; d6_12['y']=12
d6_15 = pd.read_csv(D6_15,header=None).transpose()
d6_15['x']=6; d6_15['y']=15
d6_18 = pd.read_csv(D6_18,header=None).transpose()
d6_18['x']=6; d6_18['y']=18
d6_21 = pd.read_csv(D6_21,header=None).transpose()
d6_21['x']=6; d6_21['y']=21
d6_24 = pd.read_csv(D6_24,header=None).transpose()
d6_24['x']=6; d6_24['y']=24
d6_3 = pd.read_csv(D6_3,header=None).transpose()
d6_3['x']=6; d6_3['y']=3
d6_6 = pd.read_csv(D6_6,header=None).transpose()
d6_6['x']=6; d6_6['y']=6
d6_9 = pd.read_csv(D6_9,header=None).transpose()
d6_9['x']=6; d6_9['y']=9
d9_0 = pd.read_csv(D9_0,header=None).transpose()
d9_0['x']=9; d9_0['y']=0
d9_12 = pd.read_csv(D9_12,header=None).transpose()
d9_12['x']=9; d9_12['y']=12
d9_15 = pd.read_csv(D9_15,header=None).transpose()
d9_15['x']=9; d9_15['y']=15
d9_18 = pd.read_csv(D9_18,header=None).transpose()
d9_18['x']=9; d9_18['y']=18
d9_21 = pd.read_csv(D9_21,header=None).transpose()
d9_21['x']=9; d9_21['y']=21
d9_24 = pd.read_csv(D9_24,header=None).transpose()
d9_24['x']=9; d9_24['y']=24
d9_3 = pd.read_csv(D9_3,header=None).transpose()
d9_3['x']=9; d9_3['y']=3
d9_6 = pd.read_csv(D9_6,header=None).transpose()
d9_6['x']=9; d9_6['y']=6
d9_9 = pd.read_csv(D9_9,header=None).transpose()
d9_9['x']=9; d9_9['y']=9
dnot = pd.read_csv(Dnot,header=None).transpose()
dnot['x']=-1; dnot['y']=-1


# In[4]:


datasRaw = np.concatenate([d0_0 ,d0_12 ,d0_18 ,d0_24 ,d0_6 ,d12_0 ,d12_12 ,d12_15 ,
                        d12_18 ,d12_21 ,d12_24 ,d12_3 ,d12_6 ,d12_9 ,d15_15 ,d15_21 ,
                        d15_3 ,d15_9 ,d18_0 ,d18_12 ,d18_18 ,d18_24 ,d18_6 ,d3_0 ,
                        d3_12 ,d3_15 ,d3_18 ,d3_21 ,d3_24,d3_3 ,d3_6 ,d3_9 ,
                        d6_0 ,d6_12 ,d6_15 ,d6_18 ,d6_21 ,d6_24 ,d6_3 ,d6_6 ,
                        d6_9 ,d9_0 ,d9_12 ,d9_15 ,d9_18 ,d9_21 ,d9_24 ,d9_3 ,
                        d9_6 ,d9_9 ])
datasRaw.shape  # 51*5000 = 255000


# In[5]:


datasFull=pd.DataFrame.from_dict(datasRaw)
datasFull.columns=["F0","F1","F2","F3","x","y"]
datasFull.head()


# In[6]:


dataTrain, dataTest = train_test_split(datasFull, test_size=0.2)
dataTrain, dataVal = train_test_split(dataTrain, test_size=0.2)


# In[7]:


dataTrain.head()


# In[8]:


# Helper functions
def norm(x):
    return (x - train_stats['mean']) / train_stats['std']

def format_output(data):
    y1 = data.pop('x')
    y1 = np.array(y1)
    y2 = data.pop('y')
    y2 = np.array(y2)
    return y1, y2


# In[33]:


print(train_stats['mean'])
print(train_stats['std'])


# In[9]:


# Get X and Y as the 2 outputs and format them as np arrays
train_stats = dataTrain.describe()
train_stats.pop('x')
train_stats.pop('y')
train_stats = train_stats.transpose()
train_Y = format_output(dataTrain)
test_Y = format_output(dataTest)
val_Y = format_output(dataVal)


# In[10]:


# Normalize the training and test data
norm_train_X = np.array(norm(dataTrain))
norm_test_X = np.array(norm(dataTest))
norm_val_X = np.array(norm(dataVal))


# In[11]:


def build_model():
    # Define model layers.
    input_layer = Input(shape=(len(dataTrain .columns),))
    first_dense = Dense(units='128', activation='relu')(input_layer)
    # Y1 output will be fed from the first dense
    y1_output = Dense(units='1', name='x_output')(first_dense)

    second_dense = Dense(units='128', activation='relu')(first_dense)
    # Y2 output will be fed from the second dense
    y2_output = Dense(units='1', name='y_output')(second_dense)

    # Define the model with the input layer and a list of output layers
    model = Model(inputs=input_layer, outputs=[y1_output, y2_output])

    return model


# In[13]:


model = build_model()

# Specify the optimizer, and compile the model with loss functions for both outputs
optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)
model.compile(optimizer=optimizer,
              loss={'x_output': 'mse', 'y_output': 'mse'},
              metrics={'x_output': tf.keras.metrics.RootMeanSquaredError(),
                       'y_output': tf.keras.metrics.RootMeanSquaredError()})


# In[15]:


# Train the model for 200 epochs
history = model.fit(norm_train_X, train_Y,
                    epochs=200, validation_data=(norm_test_X, test_Y))


# In[16]:


# Test the model and print loss and rmse for both outputs
loss, Y1_loss, Y2_loss, Y1_rmse, Y2_rmse = model.evaluate(x=norm_val_X, y=val_Y)

print()
print(f'loss: {loss}')
print(f'x_loss: {Y1_loss}')
print(f'y_loss: {Y2_loss}')
print(f'x_rmse: {Y1_rmse}')
print(f'y_rmse: {Y2_rmse}')


# In[17]:


def plot_diff(y_true, y_pred, title=''):
    plt.scatter(y_true, y_pred)
    plt.title(title)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.axis('equal')
    plt.axis('square')
    plt.xlim(plt.xlim())
    plt.ylim(plt.ylim())
    plt.plot([-100, 100], [-100, 100])
    plt.show()


def plot_metrics(metric_name, title, ylim=5):
    plt.title(title)
    plt.ylim(0, ylim)
    plt.plot(history.history[metric_name], color='blue', label=metric_name)
    plt.plot(history.history['val_' + metric_name], color='green', label='val_' + metric_name)
    plt.show()


# In[18]:


# Run predict
Y_pred = model.predict(norm_test_X)
price_pred = Y_pred[0]
ptratio_pred = Y_pred[1]

plot_diff(test_Y[0], Y_pred[0], title='x')
plot_diff(test_Y[1], Y_pred[1], title='y')


# In[39]:


# Plot RMSE
plot_metrics(metric_name='x_output_root_mean_squared_error', title='x RMSE', ylim=7)
plot_metrics(metric_name='y_output_root_mean_squared_error', title='y RMSE', ylim=7)


# In[20]:


# Save model
model.save('./xyForcePlate/', save_format='tf')


# In[21]:


# Restore model
loaded_model = tf.keras.models.load_model('./xyForcePlate/')


# In[58]:


# Run predict with restored model
predictions = loaded_model.predict(norm_test_X)
x_pred = predictions[0]
y_pred = predictions[1]


# In[57]:


norm_test_X.shape


# In[53]:


norm_test_X[0]


# In[65]:


print(y_pred)


# In[66]:


print(test_Y[1])


# ################################################################################
