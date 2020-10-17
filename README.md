# Predict_MPG a Machine Learning Web App
A random forest ml model is built from a dataset that contains vehicle observations from 70s and 80s. A simple streamlit web application on Heroku accepts user inputs of vehicale configuration and predicts mpg using the saved model.  
You can test drive it by clicking on the link below:  
https://dry-fortress-30256.herokuapp.com/


Data: auto-mpg.data 
"http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

1. Technologeis:  
   - jupyter Notebook 6.0.1
   - streamlit
   - Heroku
    
1. Contents:  
    - MPGPrectionPart1&2:data collection, exploration, tranformations and cleaning. 
    - MPGPredctionart3&4:pipeline building, model selection, hyperparameter tuning and Predict functions.  
    - MPG_APP folder: collection of files to be pushed to Heroku. 
        - Procfile: start webservice and run streamlit app. 
        - setup.sh: set up 2 streamlit toml files: credentials and config
        - car.jpg: car image used in the web app
        - final_model.pkl: model generated from a tuned random forest regressor in MPGPredictPart3&4
        - app.py: streamlit app
        - requirements.txt: requirements for the included codebase

Author: Tsun Chow 10/12/2020

It is loosely based on a tutorial(Tyagi, 2020) with significant changes.  
Reference:
Tyagi, H (2020, Auguest 3). How to Develop an End-to-End Machine Learning Proejct and Deploy It to Heroku with Flask. 
freeCodeCamp(). Retrieved from https://www.freecodecamp.org/news/end-to-end-machine-learning-project-turorial/
 
 

