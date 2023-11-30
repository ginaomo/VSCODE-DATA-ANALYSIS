import streamlit as st 
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from sklearn.preprocessing import LabelEncoder
matplotlib.use('Agg')

# creating fnction to handle actions
def main():
    activities=['EDA','Visualisation','Prediction'] # select whatever you want to do
    choice=st.sidebar.selectbox("what do yo want to do?",activities)
    if choice =="EDA":
        st.subheader("Exploratory Data Analysis")
        data=st.file_uploader("upload dataset",type=["csv","xlsx"])
        
        if data is not None:
            st.success("Data uploaded successfully")
            df = pd.read_csv(data)
            st.dataframe(df.head())
            st.write("Rows and columns are", df.shape)
            
    elif choice == "Visualisation":
        st.subheader("Visualisation")
        data = st.file_uploader("Upload dataset", type=["csv","xlsx"])
        if data is not None:
            st.success("Data uploaded successfully")
            df = pd.read_csv(data)
            st.dataframe(df.head())
            st.write(sns.countplot(df, x=df["division"]))
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
    elif choice == "Prediction":
            st.subheader("Prediction")
            df = pd.read_csv("heights_weights.csv")
            # st.dataframe(df.head())
            #Dividing my data into X and y variables
            x=df.iloc[:,0:-1]
            y=df.iloc[:,-1]
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
            model = KNeighborsClassifier()
            model.fit(x_train,y_train)
            y_predict = model.predict(x_test)
            # st.write("Accuracy Score:", accuracy_score(y_test,y_predict))
            height = st.number_input("Enter your height in cm")
            weight = st.number_input("Enter your weight in lb")
            if st.button("Predict"):
                result = model.predict([[height,weight]])
                if result == 1:
                    st.success("You are Female")
                else:
                    st.success("You are Male")
    else:
        st.subheader("Welcome to Tech365")
        st.subheader("Select an option on the left to get started")
        

main()

