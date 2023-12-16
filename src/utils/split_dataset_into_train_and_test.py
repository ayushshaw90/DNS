from sklearn.preprocessing import train_test_split

def train_and_test_data_splitter(df):
     X = df.drop('label',axis=1)
     y = df['label']

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     return X_train, X_test, y_train, y_test