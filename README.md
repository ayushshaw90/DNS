# Secure Shield
<hr>
### A secure DNS resolver ( acts like a DNS proxy)

## Technologies used:
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit%20Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Bind9](https://img.shields.io/badge/Bind9-0078D7?style=for-the-badge&logo=bind9&logoColor=white)
![Linux Bash](https://img.shields.io/badge/Linux%20Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)



libraries used in test.py
- dnspython

# Using the models 

in the app.py, which acts as the flask server to create apis

AFTER CREATING THE END POINT AND USING POST METHOD TO GET THE DOMAIN NAME
-#-#-

preprocess the data(which is domain_name)
from utils.dga_domain_name_preprocessor import get_feature_rich_row
preprocessed_data = get_feature_rich_row(domain_name)

Load the encoder

with open('your_encoder.pkl', 'rb') as encoder_file:
loaded_encoder = pickle.load(encoder_file) 

encoded_data = loaded_encoder.transform(preprocessed_data)


Load the scaler

with open('scaler_name.pkl', 'rb') as encoder_file:
loaded_encoder = pickle.load(encoder_file) 

scaled_data = loaded_encoder.transform(encoded_data)

Load the model
with open('model_name.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)  

predictions = loaded_model.predict(scaled_data)
