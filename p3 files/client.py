#!/usr/bin/env python
# coding=utf-8

import json
import requests
import pprint

cmdlist = ["ADD", "REMOVE", "SHOW", "UPDATE"]
cmd2list = ["utilizadores", "series", "episodios"]
utillist = ["NAME", "USERNAME", "PASSWORD", "ID"]
serielist = ["NAME", "START_DATE", "SYNOPSE", "CATEGORY_ID"]
episodelist = ["NAME", "DESCRIPTION", "SERIE_ID"]
tablelist = {"UTILIZADORES": "utilizadores", "CLASSIFICACAO": "classificacao", "CATEGORIA": "categoria",
             "LIST_SERIES": "series lista", "SERIES": "series", "EPISODIOS": "episodios"}


def checkmsg():
    if data["category"] == "utilizadores".upper():
        data["category"] = "utilizadores"
        if cmd in utillist and cmd[4].isdigit():
        #if cmd[4].isdigit():  # para comparacao com o user id
            return True
        else:
            return False

    elif data["category"] == "series".upper():
        data["category"] = "series"
        return True

    elif data["category"] == "episodios".upper():
        data["category"] = "episodios"
        return True

    else:
        print "unknown command"
        return False


while True:
    try:
        # msg = []
        cmd = raw_input("Comando:")
        cmd2 = cmd.split()
        #if cmd2[0] in cmdlist:
        if len(cmd.split(" ")) > 6:
            print "too much parameters"

        if cmd2[0] == "ADD":
            if cmd2[1] == "utilizadores":
            #if cmd2[1] in cmd2list:
                data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "username": cmd2[3], "password": cmd2[4]}
                print "data", data
                print data['category']
                r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data))
                #msg = json.loads(json.dumps(r.text))
                #lilhelper = r.text
                msg = json.loads(r.text)
                print "fim client users", msg

            elif cmd2[1] == "series":
                data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "start_date": cmd2[3], "synopse": cmd2[4], "category_id": cmd2[5]}
                print "data series", data
                if int(data["category_id"]) < 15:
                    r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data))
                    msg = json.loads(r.text)
                    print "fim client series", msg
                else:
                    print "Categoria errada"

                # print "deu ainda mais mrd no client"
            elif cmd2[1] == "episodios":
                data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "description": cmd2[3], "serie_id": cmd2[4]}
                print "data episodes", data
                #if cmd2[4] == serie.id
                r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data))
                msg = json.loads(r.text)
                print "fim client episodes"

            else:
                print "no etiendo!!!"

        elif cmd2[0] == "SHOW":
            if cmd2[1] == "ALL":
                data = {"Comando": cmd2[0], "subComando": cmd2[1], "category": cmd2[2]}
                if cmd2[2] in cmd2list:
                    r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json = json.dumps(data))
                    msg = json.loads(r.text)
                    print "show ALL list is here!", msg

            if cmd2[1] in cmd2list:
                data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2]}
                r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json = json.dumps(data))
                msg = json.loads(r.text)
                print "show list is here", msg

        elif cmd2[0] == "REMOVE":
            data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2]}
            if cmd2[1] in cmd2list:
                r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json = json.dumps(data))
                msg = json.loads(r.text)
                print "Remove done right!"
                pprint.pprint(msg)
            else:
                print "upsie! can't do that"

        elif cmd2[0] == "UPDATE":
            data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "username": cmd2[3], "password": cmd2[4], "id": cmd2[5]}
            print "update data", data
            r = requests.post('http://localhost:5000/' + tablelist[data["category"].upper()], json = json.dumps(data))
            print "between post and loads"
            msg = json.loads(r.text)
            print "Updated, i guess!"
            pprint.pprint(msg)
    except ValueError:
        print"got a dusie!"