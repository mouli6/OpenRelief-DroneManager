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

db.define_table('drone_status_type',
    Field('status_id', 'integer', notnull=True, unique=True),
    Field('name', notnull=True, unique=True))

db.define_table('drone',
    Field('drone_id', 'integer', notnull=True, unique=True),
    Field('name', notnull=True),
    Field('type_id', db.mission_type),
    Field('status_id', db.drone_status_type))

db.define_table('eden',
    Field('hostname', notnull=True, unique=True),
    Field('active', 'boolean', notnull=True),
    Field('syncdate', 'datetime'),
    Field('syncstatus', 'boolean'))
