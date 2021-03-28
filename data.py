import os
import psycopg2
from dotenv import load_dotenv
from guild import guild
from guild_bot import guild_bot
from track import track
from request import request

class data:
    def __init__(self):
        try:
            load_dotenv()
            db_host = os.getenv('PSQL_HOST')
            db_port = os.getenv('PSQL_PORT')
            db_name = os.getenv('PSQL_DB')
            db_user = os.getenv('PSQL_USER')
            db_pass = os.getenv('PSQL_PW')
            connect_str = f"dbname={db_name} user={db_user} host={db_host} port={db_port} password={db_pass}"

            self.conn = psycopg2.connect(connect_str)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Fuck!! Can't connect. WTF >:( MAke sure you have valid environment variables set (PSQL_HOST, PSQL_PORT, PSQL_DB, PSQL_USER, PSQL_PW)")
            print(e)
    
    def db_test(self):
        self.cursor.execute("""SELECT discord_id from guild""")
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        message = "rows"
        return rows

    def get_guild_identifiers(self):
        try:
            self.cursor.execute("""SELECT discord_id from guild""")
            rows = self.cursor.fetchall()
            self.cursor.close()
            self.conn.close()
            return rows
        except Exception as e:
            print("Erp. Something has gone wrong.")
            print(e)

    def get_track_by_name(self, track_name):
        try:
            query = f"SELECT track_id, name, url, host, length from track WHERE name = {track_name}"
            self.cursor.execute()
            rows = self.cursor.fetchall()
            self.cursor.close()
            self.conn.close()
            return rows
        except Exception as e:
            print("Erp. Something has gone wrong.")
            print(e)

    def upsert_guild(self, guild):
        try:
            query = f"""
                INSERT INTO guild (discord_id, name, command, nickname, monitor_channel, join_user)
                VALUES (
                    {guild.discord_id},
                    {guild.name},
                    {guild.command},
                    {guild.nickname},
                    {guild.monitor_channel},
                    {guild.join_user})"""
            
            self.conn = psycopg2.connect(self.connect_str)
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            self.conn.commit()
            affected = self.cursor.rowcount
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print("Erp. Something has gone wrong.")
            print(e)

    def upsert_track(self, track):
        try:
            query = f"""
                INSERT INTO track (discord_id, name, command, nickname, monitor_channel, join_user)
                VALUES (
                    {guild.discord_id},
                    {guild.name},
                    {guild.command},
                    {guild.nickname},
                    {guild.monitor_channel},
                    {guild.join_user})"""
            
            self.conn = psycopg2.connect(self.connect_str)
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            self.conn.commit()
            affected = self.cursor.rowcount
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print("Erp. Something has gone wrong.")
            print(e)