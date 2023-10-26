import os
from sqlalchemy import create_engine, MetaData


# Récupérer les valeurs via les variables d'environnement
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PWD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Créez la chaîne de connexion en utilisant les variables
db_connection_string = f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Créez l'objet engine en utilisant la chaîne de connexion
engine = create_engine(db_connection_string)
meta = MetaData()

conn = engine.connect()
