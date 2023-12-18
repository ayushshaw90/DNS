class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'dns_project_secret_key'
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///your-database.db'
   # MONGO_URI = 'mongodb://localhost:27017/mydatabase'
    

    

# class DevelopmentConfig(Config):
#      DEBUG = True
#    # SQLALCHEMY_DATABASE_URI = 'sqlite:///development-db.db'

# class ProductionConfig(Config):
#      DEBUG = False
#      #SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'

# # Other environment configurations (testing, staging, etc.) can be defined similarly

# # Select the configuration based on the environment
# configurations = {
#      'development': DevelopmentConfig,
#      'production': ProductionConfig,
#      # Add more configurations for other environments if needed
# }



