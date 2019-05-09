from sqlalchemy import create_engine

db_string = "postgres://abc:babycrying@localhost:5432/baby_records"

db = create_engine(db_string)


def push(param):
    print(param)
    stmt = "insert into video_status(id,frame_number,status) values("+ str(param[0]) + ',' + str(param[1])+','+ "%s ) "
    db.execute(stmt,param[2])
