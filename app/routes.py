from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import HealthInspectionForm
import joblib
import numpy as np


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def health_inspection():
    form = HealthInspectionForm()
    if form.validate_on_submit(): # False during a GET request
        new_lr = joblib.load('LR_model')
        new_tfidf = joblib.load('TFIDF_model')
        new_cats = joblib.load('CAT_model')

        review_vecs = new_tfidf.transform([form.reviews.data]).toarray()
        category_vecs = np.delete(new_cats.transform([form.categories.data]), 46).reshape(1, -1) # Delete Restaurants

        pred_array = np.hstack((review_vecs, category_vecs))
        pred_array = np.append(pred_array, float(form.avg_rating.data))

        prediction = new_lr.predict(pred_array.reshape(1, -1))
        health_test = 'PASSED'if prediction[0] == '0' else 'FAILED'

        flash('The model predicts the restaurant has {} the health inspection test'.format(health_test))

        #return redirect(url_for('index'))
    return render_template('health_inspection.html', title='Sign In', form=form)