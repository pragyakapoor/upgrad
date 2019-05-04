from flask import Flask,render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import sqlite3
conn=sqlite3.connect('products.db')
c=conn.cursor()
products = list()
#for row in c.execute("SELECT * FROM products"):
    
for row in c.execute("SELECT * FROM products"):
    temp = dict()
    name = row[0]
    price = row[1]
    desc = row[2]
    temp['name'] = name
    temp['price'] = price
    temp['description'] = desc
    temp['imageURL']=row[3]
    products.append(temp)
conn.close()
app = Flask(__name__)
app.config['SECRET_KEY']='thisissecretsboi'
class ProductSearchForm(FlaskForm):
    product = StringField('product')

@app.route("/",methods=['GET','POST'])
def form():
    searches=list()
    form=ProductSearchForm()
    if form.validate_on_submit():
        query=form.product.data
        konn=sqlite3.connect('products.db')
        xc=konn.cursor()
        for row in xc.execute("SELECT * FROM products"):
            if row[0]==query:
                temp = dict()
                name = row[0]
                price = row[1]
                desc = row[2]
                temp['name'] = name
                temp['price'] = price
                temp['description'] = desc
                temp['imageURL']=row[3]
                searches.append(temp)
        return render_template("indexx.html",products=searches,form=form)

    return render_template('indexx.html',products=products,form=form)

app.run(debug=True)
