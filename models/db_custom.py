__author__ = 'walters'

db.define_table('mission_status',
    Field('status_id', 'integer', notnull=True, unique=True),
    Field('name', notnull=True, unique=True))

db.define_table('mission_type',
    Field('type_id', 'integer', notnull=True, unique=True),
    Field('name', notnull=True, unique=True))

db.define_table('mission',
    Field('mission_id', 'integer', notnull=True, unique=True),
    Field('name', notnull=True),
    Field('type_id', db.mission_type),
    Field('startdate', 'datetime'),
    Field('status_id', db.mission_status))

