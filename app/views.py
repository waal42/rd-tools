from flask import render_template, request, redirect
from app import app
from .forms import PopulationForm

races = {  # domy, vodarna, norak, kanalizace, vodotok, bonus
        'dz': [2.0, 1.0, 1.0, 2.0, 1.5, -1.0],
        'el': [3.0, 0.5, 1.0, 1.5, 0.5,  0.0],
        'en': [2.0, 0.5, 1.0, 1.5, 0.5, -1.0],
        'ho': [3.0, 0.5, 1.0, 1.5, 0.5,  0.5],
        'cl': [5.0, 0.5, 1.0, 1.5, 1.0,  4.0],
        'ne': [3.0, 0.5, 1.0, 1.5, 0.5,  0.0],
        'ob': [3.0, 0.5, 0.5, 1.0, 0.5, -0.5],
        'sk': [3.0, 0.5, 0.5, 1.0, 0.5,  4.0],
        'tr': [3.0, 0.5, 1.0, 1.5, 0.5,  0.0],
        'va': [3.0, 0.5, 1.0, 1.5, 0.5,  0.0]
}

governy = {
        'race': 'ho',
        'lands': 0,
        'houses': 0,
        'popularity': 0,
        'vodarna': 0,
        'norak': 0,
        'kanaly': 0,
        'vodotok': 0,
        'people': 0
}

def count_people(governy):
        return int(governy['houses'] * (races[governy['race']][0] +
                                      governy['vodarna'] * races[governy['race']][1] +
                                      governy['norak'] * races[governy['race']][2] +
                                      governy['kanaly'] * races[governy['race']][3]) +
                                      governy['lands'] * (1 + (governy['popularity'] / 100) *
                                      (2 + governy['vodotok'] * races[governy['race']][4] +
                                       races[governy['race']][5])))

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='home')


@app.route('/population', methods=['GET', 'POST'])
def population():
    form = PopulationForm(data = governy)
    if form.validate_on_submit():
        governy['race'] = form.race.data
        governy['lands'] = form.lands.data
        governy['houses'] = form.houses.data
        governy['popularity'] = form.popularity.data
        governy['vodarna'] = form.vodarna.data
        governy['norak'] = form.norak.data
        governy['kanaly'] = form.kanaly.data
        governy['vodotok'] = form.vodotok.data
        governy['people'] = count_people(governy)
        form = PopulationForm(data = governy)
        return redirect('/population')
    return render_template("population.html", title='počítadlo obyvatelstva', form=form)


@app.route('/discussion')
def discussion():
    return render_template("discussion.html", title='diskuse')