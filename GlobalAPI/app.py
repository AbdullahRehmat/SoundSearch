import os
import json
import time
import redis
import pymongo
import requests
from dotenv import load_dotenv
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

# TEST
from datetime import datetime


app = Flask(__name__)
api = Api(app)
load_dotenv()

# Redis .env Variable
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")

# MongoDB General Settings
mongo_port = os.getenv("MONGO_PORT")

# MongoDB DB1 .env Variables
mongo_host_1 = os.getenv("MONGO_HOST_1")
mongo_db_1 = os.getenv("MONGO_DB_1")
mongo_col_1 = os.getenv("MONGO_COL_1")

# Redis Database
r0 = redis.Redis(host=redis_host, port=redis_port,
                 password=redis_password, db=0, decode_responses=True)

# Redis Streams
r1 = redis.Redis(host=redis_host, port=redis_port,
                 password=redis_password, db=1, decode_responses=True)

# Connect to MongoSE Database
conn1 = pymongo.MongoClient(
    host='mongodb://' + mongo_host_1 + ':' + str(mongo_port) + '/')
db1 = conn1[mongo_db_1]
col1 = db1[mongo_col_1]


def find_MongoSE(identifier):
    for i in col1.find({"_id": identifier}):
        data = i['data'][0]
        return data


class queryAPI(Resource):

    def get(self):  # Send Results
        parser = reqparse.RequestParser()
        parser.add_argument('identifier', required=True)
        args = parser.parse_args()

        # Parse Identifier from args
        identifier = args.get('identifier')

        # Get Results from MongoSE
        time.sleep(0.1)

        startTime = datetime.now()
        results = find_MongoSE(identifier=identifier)
        timeTaken = datetime.now() - startTime

        # Return Results
        return str(timeTaken), 200

    def post(self):  # Reveive Query
        parser = reqparse.RequestParser()
        parser.add_argument('identifier', required=True)
        parser.add_argument('query', required=True)
        args = parser.parse_args()

        # Save Query to RedisDB
        r0.set('queryDB', str(args))

        # Add message to Stream
        r1.xadd('streamA', fields=args)

        # Return Data to Site
        return {'data': args}, 202


class matrix(Resource):

    def get(self):
        queryCount = col1.estimated_document_count()
        return queryCount, 200


# Create routes
api.add_resource(queryAPI, "/api")
api.add_resource(matrix, "/matrix")
