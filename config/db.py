import os
from sqlalchemy import create_engine, MetaData


# Récupérer les valeurs via les variables d'environnement
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Créez la chaîne de connexion en utilisant les variables
db_connection_string = f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Créez l'objet engine en utilisant la chaîne de connexion
engine = create_engine(db_connection_string)
meta = MetaData()

conn = engine.connect()
