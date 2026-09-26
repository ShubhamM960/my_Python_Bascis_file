from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    #  Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>' , methods = ["GET"])
def show_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost)).where(BlogPost.id == post_id)
    #requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# add_new_post() to create a new blog post
@app.route("/new-post" , methods = ["GET","POST"])
def create_new_blog():
    #blogData = request.to_json() or request.form
    form = CreatePostForm()
    if form.validate_on_submit():
        try:
            new_post = BlogPost(
                title = form.get('title'),
                subtitle = form.get('subtitle'),
                author = form.get('author'),
                body = form.get('body'),
                img_url = form.get('img_url')
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
        except :
            return jsonify(error={"Could not able to enter record"}), 404
    
    return render_template("make-post.html", form=form)
            
# edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods = ["PUT","PATCH"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm()
    return render_template("make-post.html", form=edit_form, is_edit=True)

#delete_post
@app.route("/delete/<post_id>", methods = ["DELETE"])
def delete_post(post_id):
    
    try:
        post = db.get_or_404(BlogPost, post_id)
        db.session.add(new_post)
        db.session.commit()
    except :
        return jsonify(error={"Could not able to delete record"}), 404
    
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
