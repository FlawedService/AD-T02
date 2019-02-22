#!/usr/bin/env python
# coding=utf-8

import sqlite3
import json
import queries
from flask import Flask, request, make_response
from flask import jsonify
from flask import url_for
from flask import render_template_string
#import requests
import os.path as pa


DATABASE = "/Users/andrepeniche/Desktop/p3 files/novadb"
#DATABASE = "testDb"
app = Flask(__name__)

def dict_factory(cursor, row):

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db(dbname):
    # Existe ficheiro da base de dados?

    #db_is_created = pa.isfile('testDb')
    db_is_created = pa.isfile(dbname)
    #connection = sqlite3.connect(dbname, isolation_level=None)
    connection = sqlite3.connect(dbname, check_same_thread=False)
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    if not db_is_created:
        #cursor.execute(open(""))
        #cursor.executescript(open('/Users/andrepeniche/Desktop/p3 files/tables.sql').read())
        cursor.executescript(open("tables.sql").read())
        connection.commit()

    connection.commit()
    return connection, cursor


@app.route('/', methods=["GET"])
def index():
    #print url_for("users")

    return render_template_string('''<!doctype html>
    <html>
        <head></head>
            <body>
                <a href = "http://localhost:5000/utilizadores"> utilizadores </a><br>
                <a href = "http://localhost:5000/series"> series </a><br>
                <a href = "http://localhost:5000/episodios"> episodios </a><br>
            </body>
    </html>
    ''')

@app.route('/utilizadores', methods=["POST"])
def users():

    if request.headers['Content-Type'] == 'application/json': #contains the parsed JSON
        #print "users func"
        data = json.loads(request.json)
        print "first data!!!!!!!!!!!!!!!", data
        query = str(data["Comando"] + " " + data["category"])
        #query = str(data["Comando"] + data["category"] + data["name"] + data["username"] + data["password"])
        #args = [str(query[2]), str(query[3]), str(query[4])]
        if data["Comando"] == "ADD":
            #args = [str(query[2]), str(query[3]), str(query[4])]
            #db.execute(queries.add[query], args)
            print "User data: "
            print "Name:", data["name"][0:]
            print "Username:", data["username"][0:]
            print "Password:", data["password"][0:]
            args = [str(data["name"][0:]), str(data["username"][0:]), str(data["password"][0:])]

            db.execute(queries.add['ADD USERS'], args)
            #db.execute("INSERT INTO users (name, username, password) VALUES (?,?,?)",args)
            #db.execute(queries.add[query], args)

            #result = db.fetchone()
            #if result:
            #    print (result)
            print db.fetchone()

            conndb.commit()
            return json.dumps("OK")

        elif data["Comando"] == "REMOVE":
            args = [str(data["name"][0:])]
            db.execute(queries.remove['REMOVE USERS'], args)
            #db.execute(queries.remove[query], args)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["Comando"] == "SHOW":
            c = db.execute("SELECT * FROM users")
            #c = db.execute(queries.show_all["SHOW ALL USERS"], showhelper)
            requery = c.fetchall()
            conndb.commit()
            print requery
            return json.dumps(requery)

        elif data["comando"] == "UPDATE":
            args = [int(data["id"][0:])]
            db.execute(queries.update['UPDATE USER'], args)
            conndb.commit()
            print db.fetchone()
            return json.dumps("OK")

    else:
        return json.dumps("NOK") #precisa de jsonreturns senao diz que nao foi returnada resposta


@app.route('/series', methods = ["POST"])
def series():
    if request.headers['Content-Type'] == 'application/json':
        data = json.loads(request.json)
        print "Series!!!!!!!!!!!!!!!", data

        if data["Comando"] == "ADD":
            args = [str(data["name"][0:]), int(data["start_date"][0:]), str(data["synopse"][0:]), int(data["category_id"[0:]])]
            db.execute(queries.add['ADD SERIES'], args)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["Comando"] == "REMOVE":
            args = [str(data["name"][0:])]
            db.execute(queries.remove['REMOVE SERIE'], args)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["Comando"] == "SHOW":
            #c = db.execute("SELECT * FROM serie")
            c = db.execute(queries.show_all['SHOW ALL SERIES'])
            requery = c.fetchall()
            conndb.commit()
            print requery
            return json.dumps(requery)

        elif data["comando"] == "UPDATE":
            args = [str(data["name"][0:])]
            db.execute(queries.update['UPDATE SERIE'], args)
            conndb.commit()
            print db.fetchone()
            return json.dumps("OK")
        else:
            return jsonify("not ok at all")
    else:
        return jsonify("no series ok at all ")


@app.route('/episodios', methods=["GET", "POST"])
def episodes():
    if request.headers['Content-Type'] == 'application/json':
        print "episodes func"
        data = json.loads(request.json)
        print "EPISODES!!!!!!!!!!!!!!!", data

        if data["Comando"] == "ADD":
            args = [str(data["name"][0:]), str(data["description"][0:]), int(data["serie_id"][0:])]
            #c = db.execute(queries.show_all['SHOW ALL SERIES'])
            #results = c.fetchall()
            #for args[2] in results:
                #print(args[2])
            db.execute(queries.add['ADD EPISODE'], args)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["Comando"] == "REMOVE":
            args = [str(data["name"][0:])]
            db.execute(queries.remove['REMOVE EPISODE'], args)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["Comando"] == "SHOW":
            #c = db.execute("SELECT * FROM list_series")
            c = db.execute(queries.show_all['SHOW ALL EPISODES'])
            requery = c.fetchall()
            conndb.commit()
            print requery
            return json.dumps(requery)

        else:
            return jsonify("not ok at all")
    else:
        return jsonify("no series ok at all ")

if __name__ == '__main__':
    conndb, db = connect_db(DATABASE)
    #db = connect_db(database)
    print "Commands: "
    print "ADD (utilizadores/series/episodios) + one of the FOLLOWING"
    print "utilizadores: name, username, password"
    print "series: name, start date, synopse, serie id"
    print "episodios: name, description, serie id"
    print "REMOVE (utilizadores/series/episodios) + name "
    print "SHOW (utilizadores/series/episodios)"
    print "UPDATE (utilizadores/series/episodios) + id"

    app.debug = True
    app.run()