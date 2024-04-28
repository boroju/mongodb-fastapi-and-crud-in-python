from pymongo.mongo_client import MongoClient
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

# Read MongoDB credentials
mongodb_cluster = config['mongodb']['db_cluster']
mongodb_user = config['mongodb']['db_user']
mongodb_pwd = config['mongodb']['db_pwd']

uri = f'''mongodb+srv://{mongodb_user}:{mongodb_pwd}@{mongodb_cluster}.opwjush.mongodb.net/?retryWrites=true&w=majority&appName={mongodb_cluster}'''

client = MongoClient(uri)

db = client.sample_mflix

collection_users = db["users"]
