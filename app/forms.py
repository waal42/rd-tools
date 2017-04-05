from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField


class PopulationForm(FlaskForm):
    race = SelectField('race', choices=[('dz', 'džin'), ('el', 'elf'), ('en', 'ent'), ('ho', 'hobit'), ('cl', 'člověk'),
                                        ('ne', 'nekromant'), ('ob', 'obr'), ('sk', 'skřet'), ('tr', 'trpaslik'),
                                        ('va', 'vampýr')])
    lands = IntegerField('lands')
    houses = IntegerField('houses')
    popularity = IntegerField('popularity')
    vodarna = BooleanField('vodarna', default=True)
    norak = BooleanField('norak', default=True)
    kanaly = BooleanField('kanaly', default=True)
    vodotok = BooleanField('vodotok', default=True)
    people = IntegerField('people')
