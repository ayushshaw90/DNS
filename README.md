# Secure Shield
### A secure DNS resolver ( acts like a DNS proxy)


## Technologies used:
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit%20Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Bind9](https://img.shields.io/badge/Bind9-0078D7?style=for-the-badge&logo=bind9&logoColor=white)
![Linux Bash](https://img.shields.io/badge/Linux%20Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Overview of setup

| Step | Description                                       |
|------|---------------------------------------------------|
| 1    | Setup your cloud VM environment and install bind9 using `sudo apt install bind9 bind9utils bind9-doc -y` |
| 2    | Configure Bind9 |
| 2    | Install dependencies using `pip install -r requirements.txt` | 
| 3    | Run the application using `python app.py`         | 


## How it works
| Step | Description |
|------|-------------|
| 1    | The cloud VM acts as a DNS resolver. It accepts DNS packets in port 53 |
| 2    | The Python script accepts raw DNS packets and decodes it with dnspython extracting each of the records and its type like 'A', 'AAAA', 'TXT' etc. |
| 3    | It checks the records against a model which predicts if the packet is malicious |
| 4    | If the packet is malicious, it responds after crafting a dummy DNS packet |
| 5    | If the packet is not malicious, it sends the packet to Bind9 which recursively resolves the DNS query and sends its response to the Python script |
| 6    | The python script sends back the DNS response from Bind9 back to the client |

libraries used in test.py
- dnspython

# Using the models 

in the app.py, which acts as the flask server to create apis

AFTER CREATING THE END POINT AND USING POST METHOD TO GET THE DOMAIN NAME
-#-#-

preprocess the data(which is domain_name)
```
from utils.dga_domain_name_preprocessor import get_feature_rich_row
preprocessed_data = get_feature_rich_row(domain_name)
```

### Load the encoder

```with open('your_encoder.pkl', 'rb') as encoder_file:
loaded_encoder = pickle.load(encoder_file) 

encoded_data = loaded_encoder.transform(preprocessed_data)
```


### Load the scaler

```with open('scaler_name.pkl', 'rb') as encoder_file:
loaded_encoder = pickle.load(encoder_file) 

scaled_data = loaded_encoder.transform(encoded_data)

Load the model
with open('model_name.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)  

predictions = loaded_model.predict(scaled_data)
```
