__author__ = 'walters'

@auth.requires_login()
def edit():
    form = SQLFORM(db.eden)
    if form.process().accepted:
        response.flash = T('form accepted')
    elif form.errors:
        response.flash = T('form has errors')
    else:
        response.flash = T('please fill out the form')
    return dict(form=form)

@auth.requires_login()
def list():
    rows = SQLFORM.grid(db.eden)
    return locals()

def index():
    return dict()
