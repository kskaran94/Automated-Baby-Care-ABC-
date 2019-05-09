from sqlalchemy import create_engine
from database.config import host, database_name, database_port, database_password ,database_username

db_string = "postgres://" + database_username + ':' + database_password + "@" + \
            str(host) + ':' + str(database_port) + '/' + str(database_name)

print(db_string)

db = create_engine(db_string)


def push(param):
    stmt = "insert into video_status(id,frame_number,status) values("+ str(param[0]) + ',' + str(param[1])+','+ "%s ) "
    db.execute(stmt,param[2])
