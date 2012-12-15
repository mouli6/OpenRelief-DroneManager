response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Home'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Mission Planner'),URL('mission','list')==URL(),URL('mission','list'),[]),
(T('Sahana Eden'),URL('sahana','index')==URL(),URL('sahana','index'),[]),
(T('Drones'),URL('drones','list')==URL(),URL('drones','list'),[]),
(T('Settings'),URL('settings','index')==URL(),URL('settings','index'),[]),
(T('Administration'),URL('appadmin','index')==URL(),URL('appadmin','index'),[]),
(T('Help'),URL('help','index')==URL(),URL('help','index'),[]),
]
