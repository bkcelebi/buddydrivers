#importing the necessary packages and libraries for the app

from tkinter import CASCADE
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime


#In this app, Flask documentation, sqlalchemy documentation and 
#bcrypt documentations are used.
#https://flask.palletsprojects.com/en/2.1.x/ (Flask doc)
#https://pypi.org/project/bcrypt/ (bcrypt doc)
#https://docs.sqlalchemy.org/en/14/ (sqlalchemy doc)



#creating the app and database
#creating bcrypt to hash the password
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secretkey'

#creating the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#creating user table in the database
#and creating posts attribute to link
#the child table with the parent
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    #create the ones below
    # profile_pic =db.Column(db.String(30), nullable=False, default='default.png')

    
    
    
    posts = db.relationship('Post', backref='user', cascade="delete")

    #creating this representative function 
    #if there is an error i will be able to
    #see the user the error coming from
    def __repr__(self):
        return f'<User {self.id}>'

#creating post table in the database
#and creating the user_id to link this table
#with the parent
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(400), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    language = db.Column(db.String(100), nullable=True)

    # post_pic =db.Column(db.String(), nullable=True)

    #creating this representative function 
    #if there is an error i will be able to
    #see the post the error coming from
    def __repr__(self):
        return f'<Post {self.id}>'

#home page / reception page
@app.route('/')
def index():
    return render_template('index.html')

#Signup page to collect data to create a user profile
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    #getting the data from the form in the fronend through post request
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['mail']
        password = request.form['pwd']
        password2 = request.form['pwd2']
        dob = request.form['age']
        
        # profile_pic = request.files['profile_pic']

        #validating the data before pushing them to database to create a user profile
        if len(first_name) > 50:
            flash('First name must be less than 50 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif len(last_name) > 50:
            flash('Last name must be less than 50 characters.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 2 characters.', category='error')
        elif len(email) > 50: 
            flash('Email must be less than 50 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif password != password2:
            flash('Passwords do NOT match', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters', category='error')
        elif dob == "":
            flash('Age must be filled', category='error')
        
        else:
            #checking if the email is used already
            existing_email = User.query.filter_by(
                    email=email).first()
            if existing_email:
                flash("This email already exists.", category='error')
                return redirect(url_for('signup'))

            #if email does not exist hashing the pw and creating the user profile
            else:
                #4 rows of code below is from https://www.youtube.com/watch?v=71EU8gnZqZQ&t=1442s
                hashed_pw = bcrypt.generate_password_hash(password)
            

                new_user = User(email=email, first_name=first_name, 
                password = hashed_pw ,last_name=last_name, age=dob)
                #profile_pic=profile_pic) 
                
            
                db.session.add(new_user)
                db.session.commit()
                flash('Account created!', category='success')
                return redirect(url_for('index'))

        flash('Account not created!', category='error')
        return redirect(url_for('signup'))
    #if the request is get, just showing the template to the user           
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        #getting the credentials 
        email = request.form['mail']
        password = request.form['pwd']
        user = User.query.filter_by(email=email).first()

        #validating the input
        if email == '':
            flash('Please enter your Email', category='error')
        elif password == '':
            flash('Please enter your Password', category='error')
        else:
            #if user exist
            if user:
                #checking if the pw user entered and the 
                #hashed ones are matching and if so log in user
                if bcrypt.check_password_hash(user.password, password):
                    login_user(user)
                    flash('Successfully signed in', category='success')
                    return redirect(url_for('drivers'))
                #else reject login request
                else:
                    flash('Incorrect Email or Password', category='error')
                    return redirect(url_for('login'))
            #if user does not exist
            else:
                flash("This user does not exist", category='error')
                return redirect(url_for('login'))

        return redirect(url_for('login'))
        
    else:
        return render_template('login.html')

#logout user
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/drivers', methods=['GET'])
# @login_required
def drivers():

    date = datetime.now()
    
   
    page = request.args.get('page',1 , type=int)
    posts = Post.query.order_by(Post.date_created.desc()). \
    paginate(page=page, per_page=10) 
    
    return render_template(
        'drivers.html',
        posts=posts,
        date=date)

@app.route('/search', methods=['GET'])
def search():
    #create join on user table and filter by search param insensitively 
    date = datetime.now()
    search = request.args.get('search')

    page = request.args.get('page', 1, type=int)

    result = db.session.query(Post, User).join(User). \
            order_by(Post.date_created.desc()). \
            filter((User.first_name.ilike(f'%{search}%')) | \
                Post.content.ilike(f'%{search}%') | \
                Post.language.ilike(f'%{search}%') | \
                Post.location.ilike(f'%{search}%')) . \
                paginate(page=page, per_page=5) 

    return render_template(
        'search.html', 
        result=result,
        search=search,
        date=date)


@app.route('/filtered-result', methods=['GET', 'POST'])
def filtered_result():
    #create join on user table and filter by search param insensitively 
    date = datetime.now()

    if request.method == 'POST':

        if request.form['location'] == 'any':
            language = request.form['lang'].strip()

            result = db.session.query(Post). \
                    filter_by(Post.language.like(language))

            return render_template(
                'filtered-result.html', 
                result=result,
                date=date)

        elif request.form['lang'].strip() == '':
            location = request.form['location']

            result = db.session.query(Post). \
                filter_by(Post.location.like(location))

            return render_template(
                'filtered-result.html', 
                result=result,
                date=date)
        
        else:
            location = request.form['location']
            language = request.form['lang'].strip()

            result = db.session.query(Post). \
                    filter_by(Post.location.like(location)). \
                    filter_by(Post.language.like(language))

            return render_template(
                'filtered-result.html', 
                result=result,
                date=date)

    else:
        return redirect(url_for('drivers'))
        

@app.route('/profile/<int:id>', methods=['GET'])
# @login_required
def profile(id):

    # profile_pic = url_for('static', filename='profile_pics/' + current_user.profile_pic )

    date = datetime.now()
    
    posts = db.session.query(Post). \
        order_by(Post.date_created.desc()). \
        filter(Post.user_id == id).all()
        
    user = db.session.query(User). \
        filter(User.id == id).first()

    yyyy = int(user.age[:4])
    mm = int(user.age[5:7])

    age = (date.month + ((date.year - yyyy)*12) + mm) // 12

    return render_template(
        'profile.html', 
        posts=posts,
        date=date,
        user=user,
        age=age)


@app.route('/update-user/<int:id>', methods=['GET', 'POST'])
@login_required
def update_user(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':

        if request.method == 'POST':
            first_name = request.form['fname']
            last_name = request.form['lname']
            email = request.form['mail']
            current_password = request.form['current_pwd']
            password = request.form['pwd']
            password2 = request.form['pwd2']
            dob = request.form['age']
            
            # profile_pic = request.files['profile_pic']

            #validating the data before pushing them to database to create a user profile
            if len(first_name) > 50:
                flash('First name must be less than 50 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 2 characters.', category='error')
            elif len(last_name) > 50:
                flash('Last name must be less than 50 characters.', category='error')
            elif len(last_name) < 2:
                flash('Last name must be greater than 2 characters.', category='error')
            elif len(email) > 50: 
                flash('Email must be less than 50 characters.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 4 characters.', category='error')
            elif not bcrypt.check_password_hash(user.password, current_password):
                flash('Current password NOT correct', category='error')
            elif password != password2:
                flash('Passwords do NOT match', category='error')
            elif len(password) < 8:
                flash('Password must be at least 8 characters', category='error')
            elif dob == "":
                flash('Age must be filled', category='error')

            else:
                existing_email = User.query.filter_by(
                    email=email).first()

                if existing_email:

                    if user.email == email:
                        hashed_pw = bcrypt.generate_password_hash(request.form['pwd'])

                        user.first_name = request.form['fname'].strip()
                        user.last_name = request.form['lname'].strip()
                        user.email = request.form['mail'].strip()
                        user.password = hashed_pw
                        user.age = request.form['age'].strip()
                        db.session.commit()
                        flash("Account info updated", category='success')
                        return redirect(url_for('profile', id=user.id))
                        

                    else:
                        flash("This email already exists.", category='error')
                        return render_template(
                        'update-user.html', 
                        user=user)
                        
                        

                else:
                    hashed_pw = bcrypt.generate_password_hash(request.form['pwd'])

                    user.first_name = request.form['fname'].strip()
                    user.last_name = request.form['lname'].strip()
                    user.email = request.form['mail'].strip()
                    user.password = hashed_pw
                    user.age = request.form['age'].strip()
                    db.session.commit()
                    flash("Account info updated", category='success')
                    return redirect(url_for('profile', id=user.id))
                        

            flash('Account not updated!', category='error')
            return render_template(
                    'update-user.html', 
                    user=user)

    else:
        return render_template(
            'update-user.html', 
            user=user)


@app.route('/delete-user/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':

        if user:

            password = request.form['pwd']

            if bcrypt.check_password_hash(user.password, password):

            #3 rows of code below is from https://www.youtube.com/watch?v=Z1RJmh_OqeA
                db.session.delete(user)
                db.session.commit()
                flash('User deleted', category='success')
                return redirect(url_for('index'))

            else:
                flash("Password not correct", category='error')
                return redirect(url_for('profile', id=user.id))


        else:
            flash("User not exist", category='error')
            return redirect(url_for('index'))

    else:
        return render_template(
            'delete-user.html',
            user=user)
    

@app.route('/update-post/<int:id>', methods=['GET', 'POST'])
@login_required
def update_post(id):
    posts = Post.query.get_or_404(id)

    if request.method == 'POST':
        #if input is left blank
        if request.form['content'].strip() == '':
            flash('Post cannot be blank', category='error')
            return render_template(
            'update-post.html', 
            posts=posts)

        elif request.form['location'].strip() == '':
            flash('Location cannot be blank', category='error')
            return render_template(
            'update-post.html', 
            posts=posts)

        elif request.form['lang'].strip() == '':
            flash('Language cannot be empty', category='error')
            return render_template(
            'update-post.html', 
            posts=posts)
        else:
            #3 rows of code below is from https://www.youtube.com/watch?v=Z1RJmh_OqeA
            posts.content = request.form['content'].strip()
            posts.location = request.form['location']
            posts.language = request.form['lang'].strip()
            db.session.commit()
            flash('Ad updated', category='success')
            return redirect(url_for('drivers'))
            

    else:
        return render_template(
            'update-post.html', 
            posts=posts)


@app.route('/delete-post/<int:id>')
@login_required
def delete(id):
    posts_to_delete = Post.query.get_or_404(id)

    
    if posts_to_delete:
        #3 rows of code below is from https://www.youtube.com/watch?v=Z1RJmh_OqeA
        db.session.delete(posts_to_delete)
        db.session.commit()
        flash('Ad deleted', category='success')
        return redirect(url_for('profile', id=posts_to_delete.user_id))

    else:
        flash("Ad not exist", category='error')
        return redirect(url_for('profile', id=posts_to_delete.user_id))



@app.route('/post/<int:id>')
def post(id):

    date = datetime.now()

    posts = Post.query.get_or_404(id)

    return render_template(
            'post.html', 
            posts=posts,
            date=date)


@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        content = request.form['content']
        language = request.form['lang']
        location = request.form['location']

        #if the content is empty
        if len(content) < 1:
            flash("Task too short!", category='error')
        elif language.strip() == '':
            flash("Language cannot be empty!", category='error')
        elif location.strip() == '':
            flash("Please choose your county", category='error')
            
        else:
            #passing required info to create a new task
            new_post = Post(
                content=content, 
                user_id=current_user.id,
                location=location,
                language=language
                )


            #creating the task
            db.session.add(new_post)
            db.session.commit()
            flash("Ad created successfully", category='success')
            return redirect('drivers')
        
        return redirect(url_for('create'))

    return render_template(
            'create.html') 
            


if __name__ == "__main__":
    app.run(debug=True)
