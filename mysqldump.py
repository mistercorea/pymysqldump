#!/usr/bin/env python


##
## Grabs all the database name and dumps to each file.
##      EX) database/table.sql
##      This way each table can be recovered independently
##
import MySQLdb
import os

class mysqldump():
 
        def __init__(self):
                self.connection = None 
                self.username = "user_name"
                self.password = "password"
                self.base_dir = "./sqldump/"

        def grabDBs(self):
                dbs = []
                self.connection = MySQLdb.connect(host='127.0.0.1', db='',user=self.username,passwd=self.password)
                c = self.connection.cursor()
                c.execute("SHOW DATABASES")
                databases = c.fetchall()
                c.close()
                for (db,) in databases:
                        dbs.append(db)
                # print(dbs)
                return dbs

        def grabTables(self,database_name):
                tables = []
                conn = MySQLdb.connect(host='127.0.0.1', db=database_name,user=self.username,passwd=self.password)
                c = conn.cursor()
                c.execute("SHOW TABLES")
                ts = c.fetchall()
                c.close()
                for (t,) in ts:
                        tables.append(t)
                return tables

        def dumpDBs(self, databases):
                for database in databases:
                        print("Dumping " + database)
                        tables = self.grabTables(database)
                        for t in tables:
                                directory = self.base_dir + database +"/"
                                file = t+'.sql'
                                if not os.path.isdir(directory):
                                        os.makedirs(directory)
                                dump_exec = ("mysqldump -h127.0.0.1 -u "+self.username + " -p"+self.password+ " " + database + " "+t+" > "+directory+file)
                                # print(dump_exec)
                                os.system(dump_exec)

def main():
        mysql = mysqldump()
        dbs = mysql.grabDBs()
        mysql.dumpDBs(dbs)
        print("Finished")


if __name__ == "__main__":
        main();


