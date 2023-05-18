import os
# import peewee

from flask import Flask, render_template, request, redirect, url_for

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('base.jinja2')
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

'''This code would work on local but in in Heroku, it would crash if I put a duplicate name.
So i implimented the below instead to follow the HW requirements.
'''
# @app.route('/add_donations/', methods =['GET', 'POST'])
# def add():
#     if request.method =='POST':
#         try:
#             new = Donor(name=request.form['Donor_Name'])
#             new.save()
#         except peewee.IntegrityError:
#             new = Donor.select().where(Donor.name==request.form['Donor_Name'])
#         Donation(donor=new, value=request.form['Amount']).save()
#         return redirect(url_for('all'))
#     return render_template('new_donations.jinja2')

@app.route('/add_donations/', methods =['GET', 'POST'])
def add():
    if request.method =='POST':
        new = Donor.select().where(Donor.name==request.form['Donor_Name'])
        Donation(donor=new, value=request.form['Amount']).save()
        return redirect(url_for('all'))
    return render_template('new_donations.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

