from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'DroneManager'
settings.subtitle = 'OpenRelief'
settings.author = 'Chris Walters'
settings.author_email = 'walters@id.com'
settings.keywords = 'drone mission planner mavproxy sahana eden openrelief'
settings.description = 'This is the Drone Manager for OpenRelief'
settings.layout_theme = 'KeepitSimple'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '9dceacfe-ed72-47bf-94e2-6b34163fc4a1'
settings.email_server = 'logging'
settings.email_sender = ''
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['datatable', 'matplotlib', 'utils', 'gmap', 'markitup', 'jqgrid', 'translate']
