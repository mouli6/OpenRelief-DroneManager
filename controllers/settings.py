__author__ = 'walters'

def index():
    return dict()

def edit():
    form = SQLFORM(db.mission)
    if form.process().accepted:
        response.flash = T('form accepted')
    elif form.errors:
        response.flash = T('form has errors')
    else:
        response.flash = T('please fill out the form')
    return dict(form=form)

def list():
    return dict(rows=db().select(db.mission.ALL))
