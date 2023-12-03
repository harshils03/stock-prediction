
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt



#tcs
data1=pd.read_csv('C:\\Users\\harsh\\Desktop\\tcs.csv')
# print(data)
a1 = data1['Close'].values

scaler1 = MinMaxScaler(feature_range=(0, 1))
scaled_data1 = scaler1.fit_transform(a1.reshape(-1, 1))
# print(scaled_data1)

sequence_length1 = 10  # Length of each input sequence
sequences1 = []
for i in range(len(scaled_data1) - sequence_length1):
    sequence1 = scaled_data1[i:i+sequence_length1]
    sequences1.append(sequence1)

sequences1 = np.array(sequences1)
# print(sequences1)   

X1 = sequences1[:, :-1]
y1 = sequences1[:, -1]

X1 = X1.reshape(X1.shape[0], X1.shape[1], 1)

model1 = Sequential()
model1.add(LSTM(50, input_shape=(X1.shape[1], 1)))
model1.add(Dense(1))

model1.compile(optimizer='adam', loss='mse')

model1.fit(X1, y1, epochs=10, batch_size=32)

predicted_data1 = model1.predict(X1)

predicted_data1 = scaler1.inverse_transform(predicted_data1)
actual_data1 = scaler1.inverse_transform(y1.reshape(-1, 1))





#itc
data2=pd.read_csv('C:\\Users\\harsh\\Desktop\\itc.csv')
# print(data)
a2 = data2['Close'].values

scaler2 = MinMaxScaler(feature_range=(0, 1))
scaled_data2 = scaler2.fit_transform(a2.reshape(-1, 1))
# print(scaled_data2)

sequence_length2 = 10  # Length of each input sequence
sequences2 = []
for i in range(len(scaled_data2) - sequence_length2):
    sequence2 = scaled_data2[i:i+sequence_length2]
    sequences2.append(sequence2)

sequences2 = np.array(sequences2)
# print(sequences1)   

X2 = sequences2[:, :-1]
y2 = sequences2[:, -1]

X2 = X2.reshape(X2.shape[0], X2.shape[1], 1)

model2 = Sequential()
model2.add(LSTM(50, input_shape=(X2.shape[1], 1)))
model2.add(Dense(1))

model2.compile(optimizer='adam', loss='mse')

model2.fit(X2, y2, epochs=10, batch_size=32)

predicted_data2 = model2.predict(X2)

predicted_data2 = scaler2.inverse_transform(predicted_data2)
actual_data2 = scaler2.inverse_transform(y2.reshape(-1, 1))




#infosys

data3=pd.read_csv('C:\\Users\\harsh\\Desktop\\infosys.csv')
# print(data3)

a3 = data3['Close'].values
# print(a3)

scaler3 = MinMaxScaler(feature_range=(0, 1))
scaled_data3 = scaler3.fit_transform(a3.reshape(-1, 1))
# print(scaled_data3)

sequence_length3 = 10  # Length of each input sequence
sequences3 = []
for i in range(len(scaled_data3) - sequence_length3):
    sequence3 = scaled_data3[i:i+sequence_length3]
    sequences3.append(sequence3)

sequences3 = np.array(sequences3)
# sequences3

X3 = sequences3[:, :-1]
y3 = sequences3[:, -1]

X3 = X3.reshape(X3.shape[0], X3.shape[1], 1)

model3 = Sequential()
model3.add(LSTM(50, input_shape=(X3.shape[1], 1)))
model3.add(Dense(1))

model3.compile(optimizer='adam', loss='mse')

model3.fit(X3, y3, epochs=10, batch_size=32)

predicted_data3 = model3.predict(X3)

predicted_data3 = scaler3.inverse_transform(predicted_data3)
actual_data3 = scaler3.inverse_transform(y3.reshape(-1, 1))




#hdfc
data4=pd.read_csv('C:\\Users\\harsh\\Desktop\\hdfc.csv')
# print(data4)

a4 = data4['Close'].values
# print(a4)

scaler4 = MinMaxScaler(feature_range=(0, 1))
scaled_data4 = scaler4.fit_transform(a4.reshape(-1, 1))
# print(scaled_data4)

sequence_length4 = 10  # Length of each input sequence
sequences4 = []
for i in range(len(scaled_data4) - sequence_length4):
    sequence4 = scaled_data4[i:i+sequence_length4]
    sequences4.append(sequence4)

sequences4 = np.array(sequences4)
sequences4

X4 = sequences4[:, :-1]
y4 = sequences4[:, -1]

X4 = X4.reshape(X4.shape[0], X4.shape[1], 1)

model4 = Sequential()
model4.add(LSTM(50, input_shape=(X4.shape[1], 1)))
model4.add(Dense(1))

model4.compile(optimizer='adam', loss='mse')

model4.fit(X4, y4, epochs=10, batch_size=32)

predicted_data4 = model4.predict(X4)

predicted_data4 = scaler4.inverse_transform(predicted_data4)
actual_data4 = scaler4.inverse_transform(y4.reshape(-1, 1))





#reliance
data5=pd.read_csv('C:\\Users\\harsh\\Desktop\\reliance.csv')
# print(data5)

a5 = data5['Close'].values
# print(a5)

scaler5 = MinMaxScaler(feature_range=(0, 1))
scaled_data5 = scaler5.fit_transform(a5.reshape(-1, 1))
# print(scaled_data5)

sequence_length5 = 10  # Length of each input sequence
sequences5 = []
for i in range(len(scaled_data5) - sequence_length5):
    sequence5 = scaled_data5[i:i+sequence_length5]
    sequences5.append(sequence5)

sequences5 = np.array(sequences5)
sequences5

X5 = sequences5[:, :-1]
y5 = sequences5[:, -1]

X5 = X5.reshape(X5.shape[0], X5.shape[1], 1)

model5 = Sequential()
model5.add(LSTM(50, input_shape=(X5.shape[1], 1)))
model5.add(Dense(1))

model5.compile(optimizer='adam', loss='mse')

model5.fit(X5, y5, epochs=10, batch_size=32)

predicted_data5 = model5.predict(X5)

predicted_data5 = scaler5.inverse_transform(predicted_data5)
actual_data5 = scaler5.inverse_transform(y5.reshape(-1, 1))












import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def show_warning():
    messagebox.showwarning("Warning","Select a company.")

def display_plot():
    selected_option = dropdown3.get()
    
    if selected_option == "ITC":
        plt.figure(figsize=(10, 6))
        plt.plot(actual_data2, label='Actual Data')
        plt.plot(predicted_data2, label='Predicted Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Actual vs. Predicted Data')
        plt.legend()
        plt.show()

    elif selected_option == "Tata Consultancy Services":
        plt.figure(figsize=(10, 6))
        plt.plot(actual_data1, label='Actual Data')
        plt.plot(predicted_data1, label='Predicted Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Actual vs. Predicted Data')
        plt.legend()
        plt.show()

    elif selected_option == "Infosys":
        plt.figure(figsize=(10, 6))
        plt.plot(actual_data3, label='Actual Data')
        plt.plot(predicted_data3, label='Predicted Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Actual vs. Predicted Data')
        plt.legend()
        plt.show()

    elif selected_option == "HDFC Bank":
        plt.figure(figsize=(10, 6))
        plt.plot(actual_data4, label='Actual Data')
        plt.plot(predicted_data4, label='Predicted Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Actual vs. Predicted Data')
        plt.legend()
        plt.show()

    elif selected_option == "Reliance Industries":
        plt.figure(figsize=(10, 6))
        plt.plot(actual_data5, label='Actual Data')
        plt.plot(predicted_data5, label='Predicted Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Actual vs. Predicted Data')
        plt.legend()
        plt.show()

    else:
        show_warning()
    
    canvas = FigureCanvasTkAgg(plt.gcf(), master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("stock analysis")

bg_image = Image.open("bg1.png") 
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)
bg_label.pack(fill="both", expand=True)

plot_window = tk.Toplevel(root)
plot_window.title("Plot Window")

options1 = ["United States","Canada","UK","China","India"]
selected_option1 = tk.StringVar()  
options2 = ["Large Cap","Mid Cap","Small Cap"]
selected_option2 = tk.StringVar()
options3 = ["ITC","Tata Consultancy Services","Infosys","HDFC Bank","Reliance Industries"]
selected_option = tk.StringVar()

placeholder_text = "Select country"
selected_option1 = tk.StringVar(value=placeholder_text)
placeholder_text = "Select capital"
selected_option2 = tk.StringVar(value=placeholder_text)
placeholder_text = "Select company"
selected_option3 = tk.StringVar(value=placeholder_text)

dropdown1 = ttk.Combobox(root, textvariable=selected_option1, values=options1)
dropdown1.place(relx=0.1, rely=0.1)
dropdown2 = ttk.Combobox(root, values=options2,textvariable=selected_option2)
dropdown2.place(relx=0.1, rely=0.2)
dropdown3 = ttk.Combobox(root, values=options3,textvariable=selected_option3)
dropdown3.place(relx=0.1, rely=0.3)

plot_button = tk.Button(root, text="Display Plot", width=15, height=3, command=display_plot)
plot_button.place(relx=0.5, rely=0.5)

root.mainloop()

