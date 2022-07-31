from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectMultipleField, DecimalRangeField, SubmitField
from wtforms.validators import DataRequired

class HealthInspectionForm(FlaskForm):
    choices = [('African','African'),
     ('American (New)','American (New)'),
     ('American (Traditional)','American (Traditional)'),
     ('Asian Fusion','Asian Fusion'),
     ('Barbeque','Barbeque'),
     ('Basque','Basque'),
     ('Breakfast & Brunch','Breakfast & Brunch'),
     ('Buffets','Buffets'),
     ('Burgers','Burgers'),
     ('Cafes','Cafes'),
     ('Cajun/Creole','Cajun/Creole'),
     ('Cantonese','Cantonese'),
     ('Caribbean','Caribbean'),
     ('Cheesesteaks','Cheesesteaks'),
     ('Chinese','Chinese'),
     ('Creperies','Creperies'),
     ('Cuban','Cuban'),
     ('Delis','Delis'),
     ('Dim Sum','Dim Sum'),
     ('Diners','Diners'),
     ('Ethiopian','Ethiopian'),
     ('Fast Food','Fast Food'),
     ('Food Stands','Food Stands'),
     ('French','French'),
     ('Gluten-Free','Gluten-Free'),
     ('Greek','Greek'),
     ('Haitian','Haitian'),
     ('Halal','Halal'),
     ('Hawaiian','Hawaiian'),
     ('Himalayan/Nepalese','Himalayan/Nepalese'),
     ('Hot Dogs','Hot Dogs'),('Hot Pot','Hot Pot'),('Indian','Indian'), ('Irish','Irish'), ('Italian','Italian'), ('Japanese','Japanese'),
     ('Korean','Korean'),('Latin American','Latin American'),('Live/Raw Food','Live/Raw Food'),('Mediterranean','Mediterranean'),('Mexican','Mexican'),
     ('Middle Eastern','Middle Eastern'),('Modern European','Modern European'),('Moroccan','Moroccan'),('Pakistani','Pakistani'),('Pizza','Pizza'),
     ('Russian','Russian'),('Salad','Salad'),('Salvadoran','Salvadoran'),('Sandwiches','Sandwiches'),('Seafood','Seafood'),('Soul Food','Soul Food'),
     ('Soup','Soup'),('Southern','Southern'),('Spanish','Spanish'),('Steakhouses','Steakhouses'),('Sushi Bars','Sushi Bars'),('Szechuan','Szechuan'),
     ('Taiwanese','Taiwanese'),('Tapas Bars','Tapas Bars'),('Tapas/Small Plates','Tapas/Small Plates'),('Tex-Mex','Tex-Mex'),('Thai','Thai'),
     ('Turkish','Turkish'),('Vegan','Vegan'),('Vegetarian','Vegetarian'),('Vietnamese','Vietnamese')]
    reviews = TextAreaField('Consolidated Reviews', validators=[DataRequired()])
    categories = SelectMultipleField('Categories', validators=[DataRequired()],
                           choices=choices)

    avg_rating = DecimalRangeField('Average Rating')
    submit = SubmitField('Predict')