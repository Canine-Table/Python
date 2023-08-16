#!/usr/bin/python3
import re

text_to_search = '''exception caught! <bound method SQLAlchemyError.__str__ of IntegrityError('(pymysql.err.IntegrityError) (1062, \'target: enl8720_group_7_mysql_database.-.primary: vttablet: rpc error: code = AlreadyExists desc = Duplicate entry \\\'kkareyweidd\\\' for key \\\'account_list.username\\\' (errno 1062) (sqlstate 23000) (CallerID: 2bmhv2vg4tejeu6l48xf): Sql: "insert into account_list(username, password_hash, creation_date) values (:vtg1 /* VARCHAR */, :vtg2 /* VARCHAR */, now())", BindVars: {REDACTED}\')')>'''

pattern = re.compile(r'caught!')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(text_to_search[match.start():match.end()])
