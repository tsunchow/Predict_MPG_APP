import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image

#from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
#from sklearn.impute import SimpleImputer

#from sklearn.pipeline import Pipeline
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.compose import ColumnTransformer
import warnings
warnings.filterwarnings('ignore')



acc_ix, wt_ix, hpower_ix, cyl_ix = 4, 3, 2, 0

##custom class inheriting the BaseEstimator and TransformerMixin
class CustomAttrAdder(BaseEstimator, TransformerMixin):
    def __init__(self, acc_and_power=True):
        self.acc_and_power = acc_and_power  # new optional variable
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X):
        wt_and_cyl = X[:, wt_ix] * X[:, cyl_ix] # required new variable
        if self.acc_and_power:
            acc_and_power = X[:, acc_ix] * X[:, hpower_ix]
            return np.c_[X, acc_and_power, wt_and_cyl] # returns a 2D array
        
        return np.c_[X, wt_and_cyl]
    
def predict_mpg_web1(config,regressor):
    
    if type(config)==dict:
        df=pd.DataFrame(config)
    else:
        df=config 

# Note the model is in the form of pipeline_m, including both transforms and the estimator
# The config is with Origin already in country code
    y_pred=regressor.predict(df)
    return y_pred


# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    #st.title("MPG Prediction") 
    st.write("""
    # MPG Prediction App
    based on a Random Forest Model built from
    "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
    """)
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">What is the mpg of my car? </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create dropdowns and nueemric sliders in which the user can enter  
    # the data required to make the prediction 
    st.sidebar.header('Set My Car Configurations')
    Orig = st.sidebar.selectbox("Select Car Origin",("India", "USA", "Germany"))
    
    Cyl = st.sidebar.slider('Cylinders', 3, 6, 8)
    Disp = st.sidebar.slider('Displacement', 68.0, 455.0, 193.0)
    Power = st.sidebar.slider('Horsepower', 46.0, 230.0, 104.0) 
    WT = st.sidebar.slider(' Weight', 1613.0, 5140.0, 2970.0)
    Acc = st.sidebar.slider('Acceleration', 8.0, 25.0, 15.57)
    MY = st.sidebar.slider('Model_Year', 70, 82, 76)
    
    
    image = Image.open('car.jpg')

    st.image(image, caption='MPG Prediction',
        use_column_width=True)
    
    st.subheader("Click the 'Predict' button below")
   
    
    # loading the saved model
    pickle_in = open('final_model.pkl', 'rb')
    regressor=pickle.load(pickle_in)
    
    result ="" 
    
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    # Set up the Vehicale configurations
    
    
    
            
    vehicle={"Origin": [Orig], "Cylinders": [Cyl], "Displacement": Disp, "Horsepower": [Power],
             "Weight":[WT], "Acceelation": [Acc], "Model Year": [MY]
            }
    
    if st.button("Predict"): 
        result = predict_mpg_web1(vehicle, regressor)
        mpg=int(result[0])
        st.success('The prediction is {}'.format(mpg)) 
     
if __name__=='__main__': 
    main() 