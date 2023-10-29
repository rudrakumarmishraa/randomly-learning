# Importing Modules
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_mysqldb import MySQL
import MySQLdb.cursors

# App
app = Flask(__name__)
api = Api(app)
app.config['MYSQL_HOST'] = 'bltcrwbzknxaqeaafuv5-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'urvfzptvvvvj9k9e'
app.config['MYSQL_PASSWORD'] = 'HnwQYqP07mVGca1RKTvr'
app.config['MYSQL_DB'] = 'bltcrwbzknxaqeaafuv5'
mysql = MySQL(app)

# Use abort for error messages
parser = reqparse.RequestParser()
parser.add_argument("apiKey", type=int, help="String type API KEY is required.", required=True)
parser.add_argument("username", type=str, help="String type username is required.", required=True)
parser.add_argument("password", type=str, help="String type password is required.", required=True)
parser.add_argument("firstName", type=str, help="String type First Name is required.", required=True)
parser.add_argument("lastName", type=str, help="String type Last Name is required.", required=True)
parser.add_argument("role", type=int, help="Int type Role is required.", required=True)
# Main route for flask api
class main(Resource):
    def get(self):
        return {"users":"user"}
    def put(self):
        args = parser.parse_args()
        table = args.apikey
        cursor = mysql.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS `bltcrwbzknxaqeaafuv5`.`%s` (
            `username` VARCHAR(50) NOT NULL,
            `password` VARCHAR(200) NOT NULL,
            `FirstName` VARCHAR(20) NOT NULL,
            `LastName` VARCHAR(20) NOT NULL,
            `Role` VARCHAR(10) NOT NULL);""", (table,))
        return {"success":"User Created", "username":args.username}
api.add_resource(main, "/createUser")


if __name__ == '__main__':
    app.run(debug=True)
