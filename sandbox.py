# Fonction pour générer un jeton JWT valide pour l'utilisateur donné
import psycopg2 as psy
import jwt
from datetime import datetime, timedelta
import security

# Clé secrète pour signer les jetons JWT
SECRET_KEY = "jesuisunefougere974"

# Durée de validité du jeton (nous utilisons timedelta pour que nous puissions facilement ajouter ou soustraire du temps)
TOKEN_EXPIRATION_TIME = timedelta(days=7)


def set_connection():
  connection = psy.connect('postgres://testneon33:dfkFh5jcr1Tw@ep-hidden-forest-997741.eu-central-1.aws.neon.tech/neondb')
  connection.set_session(autocommit=True)
  cursor = connection.cursor()
  return connection, cursor


def generate_token(username: str) -> str:
    # Définir la date d'expiration du jeton
    expiration = datetime.utcnow() + TOKEN_EXPIRATION_TIME

    # Créer la charge utile pour le jeton JWT (nous incluons le nom d'utilisateur et la date d'expiration)
    payload = {"sub": username, "exp": expiration}

    # Créer le jeton JWT en signant la charge utile avec la clé secrète
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Retourner le jeton en tant que chaîne de caractères
    return token



def insert_admin_user(username, pwd, role):
  connection, cursor = set_connection()
  token = generate_token("mulder974")
  pwd = security.hash_pwd(pwd)
  user = (username, pwd, role, token, datetime.now())
  print(user)
  print("trying to insert")
  cursor.execute(
  """
  INSERT INTO Users (username, pwd, user_role, user_token, create_at)
  VALUES (%s, %s, %s, %s, %s)
  """,
  user
  )
  print("inserted")

  connection.close()



def select_all_users():
  connection, cursor = set_connection()

  cursor.execute("""SELECT * FROM Users""", )

  result = cursor.fetchall()
  connection.close()

  return result

insert_admin_user("mulder974","tiTeuf145*","1")

print(select_all_users())