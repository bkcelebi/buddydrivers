Abstract

This report comprises the planning, design, and development of a web application, Buddydrivers, aimed at tackling and overcoming the hardships faced by learner drivers in Ireland who do not have adequate resources to practice outside of their mandatory EDT lesson hours. Through the use of Python, Flask, Bootstrap, SQLAlchemy, HTML, CSS and VSCode (IDE), an accessible platform on which learner drivers can search for and communicate with experienced drivers, who have created ads on the web app, based on their location and/or preferred language via a private messaging system.
Keywords: learner driver, experienced driver, sponsor driver, Python, Flask, Bootstrap, SQLAlchemy, HTML, CSS.





Acknowledgments
I would like to thank Shazia Afzal for her endless help and support throughout the project through zoom and email correspondence. In addition, the input sessions delivered by Mehran Rafiee enlightened me and assisted me in preparing this report to the highest possible standard. Lastly, I would like to thank all of my lecturers at DBS, without whose help and guidance over the past two years, I would have been unable to complete this project.






Contents
Abstract	2
Acknowledgments	3
Contents	3
1.	Background	4
2.	Introduction	5
3.	Specification and Design	6
4.	Implementation	14
5.	Project Testing and Evaluation	21
6.	Conclusions and Future Work	23
7.	References / Bibliography	24
8.	Appendices	25








Background 
Context
According to the Irish Central Statistics Office, 52.8% of driving license candidates could not pass their test first time (CSO, 2016). As obtaining a driving license is a costly endeavour, having to repeat the driving test is an inconvenience for many. It often arises that candidates, when taking the Essential Driver Training (EDT), do not have the opportunity to practice outside the mandatory EDT lessons. This can affect the ability to pass as extra practise with a sponsor is recommended by the RSA (RSA, 2019). In addition, the law stating that learners cannot drive unattended signifies that, if they do not have a sponsor, they must also use their Approved Driving Instructor’s car for the exam, which is a hefty and unnecessary addition to the existing high cost of learning to drive in Ireland at present.  As a result of said struggle, it has been made clear that there is a definite gap in the market. 
As the author himself is currently experiencing the aforementioned issue first hand, the project entails designing a web application to facilitate finding extra practice hours and exam accompaniment with experienced drivers within the learners’ vicinity. Similarly, the application would eliminate the need to pay to rent the instructor’s car for the exam as, if learners have their own car or are insured on another car, they would be able to drive to the test centre with the accompaniment of sponsor found on the app. 
Anticipated benefits of the system
The following are the expected benefits of the project:
It is a web app that allows learner drivers and experienced drivers to connect easily on an easy-to-use user interface with a minimalistic design.
The app gives learners the opportunity to find the resources they need to facilitate extra driving hours, which are both necessary and beneficial for their development as future qualified road-users. It may, if developed further outside of the scope of this project, cater to learners’ car maintenance needs in that the experienced drivers on the app may be able to accompany learner drivers to NCT and service appointments.
The app will be easily accessible to all users as they can access the app on all device types without any issues.
The app is free for all users. Experienced drivers can post ads free of charge and learner drivers can avail of the resources and services provided without adding to their existing driving-related expenses.
The app can be accessed across the island of Ireland, meaning that residents nationwide can avail of the service in their local area.
Each user is given a personalised user experience as they can use the ‘filter by’ feature to tailor search results to suit their needs and preferences, such as language and location.
Experienced drivers who are considering becoming ADIs can use the platform to gain experience and enhance their skills in this area.


The software development methods used
It is my objective to use Agile methodology, for the most part, when developing this project as I believe it is the optimal way to achieve the project aims in the project time provided. In addition, Agile will enable me to create a well-functioning, easy to navigate, aesthetically pleasing platform for users.
Relevant/similar existing software/hardware
While the web app’s concept is similar to the likes of DoneDeal.ie and Daft.ie in that users can post and respond to ads, there are no webs in existence that provide the same service for the context explained in the first part of this section at present. It is, therefore, unique.

Introduction 
Project Aims
The aims of this project are to:
1. Create an easily navigable environment for prospective driving test candidates, who do not have the facilities or opportunity to practise outside EDT lessons, to find an experienced driver in their local area and/or speaks their preferred language.
2. Allow learners and experienced drivers across Ireland to connect and communicate by providing necessary contact information and a messaging feature, which allows users to access both sent and received messages.
3.  Provide experienced drivers with the opportunity to exploit their driving expertise, maximise their free time with the potential scope of becoming an Approved Driving Instructor (ADI), and, if desired and feasible, the possibility of increasing their monthly income.
Scope
In scope:
Learner and experienced drivers on the island of Ireland.
A platform that is accessible nationwide.
Out of scope:
Users outside Ireland.
The ability to instant message in the standard format.
Insurance issues for learners who do not have their own cars.

Typical users of the project product
The main users of the app are learner drivers and experienced drivers across the island of Ireland. Other potential users are companies directly linked to driving, such as insurance companies, driving schools and instructors, and car dealerships, who want to promote their business through the strategic placement of pay-per-click advertisements on the web application. 

Assumptions
Any resources needed will be readily available to the author.
The project will be completed in line with the plan provided in the proposal.
The tools listed in the project proposal will allow its successful completion.
The user posts will be presented on an easily accessible timeline.
Users will be able to create and manage accounts and posts easily. 
The app will be accessible on all devices.
The app will provide information about learners and experienced drivers, their location, contact information, and any other relevant information that can be added at the user’s discretion

Specification and Design 
Specification
The following are the specifications of the web app to be designed and completed during this project:
The web app will work consistently and constantly without crashing and with the minimum downtime possible.
The web app will serve both users with and without accounts as follows:
Account holders can perform the following tasks:
 sign in and out
 post, edit and delete ads
 contact other account holders via an integrated messaging system, through which messages are divided into two sections, those sent and those received.
 edit personal information and delete their account
 search and filter posts 
Non-account holders can perform the following tasks:
create an account
view ads
see other user details
search and filter posts
Non-account holders cannot interact with account-holding users without creating an account.

Commercial advertisements will be hosted on the app in the form of Pay-per-click advertisements on every page on either side of the key content.
The web app will be easy to navigate due to its minimalistic design and user-friendly interface.
The web app will operate as a full-stack web application, consisting of back end, front end, and database elements.

Requirements Analysis
Use Case Diagram
This use case diagram illustrates what anonymous and authenticated users can do on the web application. Authenticated users can also use the parts that are used by anonymous users.




Design 

User Interface Design
Once the user accesses the website, they will be directed to the homepage/reception page. This page consists of a short, enticing text which welcomes the user to the website, and a tool that allows users to discover available experienced drivers, which can be filtered by language and/or location. In addition, there are commercial ads located on either side of the above content.
It must also be noted that a navigation menu and footer menu are present on every page of the app. From the navigation menu, users can easily navigate between the various pages on the site through clickable links on the left-hand side of the menu. Similarly, a search bar placed in the centre of the menu permits users to explore the site, and the sign up and sign in buttons on the right-hand side of the menu allow users to create an account or access an existing account. Once a user is logged in, a ‘message’ button appears where they can access their messages and are notified with a badge when a message is received. 
The footer menu, on the other hand, contains social media links, other useful links to the various web pages, and a copyright stamp containing the year and website link.
On the sign-up page, users are presented with a form they are required to fill out to create an account. The fields include first and last name, email, password, date of birth etc. Users must also tick a box to state they agree to the terms and conditions of the website. Once the ‘register’ button is clicked, front end sends all the data to back end, where said data is checked, verified and, if the criteria are satisfied, an account is created.
On the sign in page, a form containing two fields is displayed which enables the user to access their account. Once the sign-in button is clicked, the data provided is checked by back end and, if located in the database, the user is signed in successfully. 
On the create ad page, there is a form which users need to fill with information relevant to their ad and other details e.g. language, photo etc. Once the ‘create’ button is clicked, front end sends all the data to back end, where said data is checked, verified and, if the criteria are satisfied, an ad is created.
On the profile page, authenticated users can view their account information on the left side of the page and the ads they have created on the right. If there are no existing ads, a text saying ‘There are no posts yet. Create now’ appears. Users can access their account settings through the settings button below the profile picture, where they have the option to update or delete their profile. If a user wishes to update their profile/post, they are presented with a pre-populated variation of the form they filled out when creating an account/post. Once the data is adjusted, front end sends all the data to back end, where said data is checked, verified and, if the criteria are satisfied, the account/post is modified accordingly. If a user wants to delete their account, they are redirected to a page on which they are required to enter their password into a field. Once the delete button is clicked, the data is sent to back end and when approved, the account is subsequently deleted. In the case of deleting a post, once the delete button is clicked, the post is deleted directly without any further requirements.
On the drivers page, the tool on the homepage appears on the left side of the page and function in the same way. The centre of the page is populated with ads created by experienced drivers. If the ads’ content is longer than 200 characters, it is cropped and can be fully viewed by clicking the ‘view’ button. Each ad includes the user’s details, details about the ad e.g. language and location, when the ad was created, and a photo located above the ad. When view is clicked, users are provided with extra information and the option to message the ad creator. 
The messages page contains any messages received and sent by the user, which are displayed and stored in two separate sections and not in conversation format. Messages received from other users, whose names appear above the message, can be both answered and deleted. Messages sent by the user can be deleted and answered by their recipient, but cannot edited or unsent by the sender.  If there are no messages, a text stating so appears when the page is accessed. 

Database Design and Development

Database Models

User Database Table (see code below)
The structure of the user database entity is broken down into the following attributes:
id: This column contains unique integer id for users. It is the entity’s primary key.
email: This column consists of user emails, which cannot be nullable, over fifty characters, and must be unique.
first_name: This column comprises user first names in string data type, which can neither be nullable nor over fifty characters.
last_name: This column is made up of user last names in string data type, which can neither be nullable nor over fifty characters.
password: This column comprises user passwords in string data type, which can neither be nullable nor over eighty characters.
age: This column contains user ages in integer data type, which cannot be nullable.
profile_pic: This column comprises user profile pictures in string data type, which cannot be nullable.
posts: This column represents the relationship between the User and Post database entities. It also contains the ‘cascade=delete’ rule. 
messages_sent: This column represents the relationship between the User and Message database entities. 
messages_received: This column also represents the relationship between the User and Message database entities.
last_message_read_time: This column consists of the time users read incoming messages.

In addition, the user database entity contains a function which checks messages and signals that messages have been received using a badge. 

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
    profile_pic = db.Column(db.String(), nullable=False)  


    posts = db.relationship('Post', backref='user', cascade="delete")


    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)


    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()










Post Database Table (see code below)
The structure of the post database entity is broken down into the following attributes:
id: This column contains unique integer id for posts. It is the entity’s primary key.
content: This column comprises content for the post in string data type, which cannot be nullable.
date_created: This column consists of the date and time, in DateTime data type, that posts are created. 
user_id: This column is made up of the post creator’s user id. This is the entity’s foreign key. 
location: This column contains the user location in string data type, which cannot be nullable or over one-hundred characters.
language: This column contains the user’s spoken language(s) in string data type, which cannot be nullable or over one-hundred characters.
post_pic: This column comprises post pictures in string data type, which cannot be nullable.
In addition, the post database entity contains a representative function which identifies error-causing posts.
#creating post table in the database
#and creating the user_id to link this table
#with the parent
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    post_pic =db.Column(db.String(), nullable=False)


    #creating this representative function 
    #if there is an error I will be able to
    #see the post the error is coming from
    def __repr__(self):
        return f'<Post {self.id}>'






Message Database Table (see code below)
The structure of the message database entity is broken down into the following attributes:
id: This column contains unique integer id for messages. It is the entity’s primary key.
sender_id: This column is made up of the sender’s user id. This is the entity’s foreign key.
recipient_id: This column is made up of the recipient’s user id. This is also the entity’s foreign key.
body: This column comprises the message body content in string data type.
timestamp: This column consists of the date and time, in DateTime data type, that messages are sent.

In addition, the message database entity contains a representative function which identifies error-causing messages.

#creating message table in the database
#and creating the sender_id and recipient_id 
#to link this table with the parent
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


    def __repr__(self):
        return '<Message {}>'.format(self.body)










Database schema
This database schema illustrates the relation between each database entity. 












Implementation
As mentioned in the background section, the idea for BuddyDrivers stemmed from the author’s realisation of a gap in the market for a platform whereby learners have access to resources that are essential for developing driving skills. Upon thinking in depth about this concept, the author decided to turn his ideas into reality through this project. The following paragraphs detail how this idea was implemented to successfully become a fully functioning web application:
Front End/User Interface
The front end was designed and developed thanks the skills gained through taking the Web Design and Development module as part of the Higher Diploma, and Bootstrap and Flask documentation, both of which were studied autonomously by the author. 
Database
The Database Design and Development module, also taken as part of the Higher Diploma, aided the creation of the database models and the database schema. Similarly, SQLAlchemy documentation was one of the main sources taken into consideration during the implementation stage.
Back End
Both Flask documentation and the Advanced Programming module from the Higher Diploma assisted the author in implementing the aforementioned idea. Additionally, the educational videos in the bibliography further aided the development and implementation of the project.
Other
In addition to the resources mentioned in the previous paragraphs, the Information Systems Development and Management module taken during the Higher Diploma helped with the planning of the project as Agile methodology, which was a key component of the module, was use throughout the project. 
Lastly, some webpages, such as Stackoverflow, were used to discover and fix issues while the project was being undertaken.










Software and version of software used
The software and versions of software used can be found in the Requirement.txt file within the project, which can also be found below. 

Requirements.txt
bcrypt==3.2.2
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.12
click==8.1.3
colorama==0.4.4
dnspython==2.2.1
email-validator==1.2.1
Flask==2.1.2
Flask-Bcrypt==1.0.1
Flask-Login==0.6.1
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
greenlet==1.1.2
gunicorn==20.1.0
idna==3.3
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
numpy==1.22.3
pandas==1.4.2
pycparser==2.21
python-dateutil==2.8.2
pytz==2022.1
requests==2.27.1
six==1.16.0
SQLAlchemy==1.4.36
urllib3==1.26.9
Werkzeug==2.1.2
python==3.10.6







Backend Design and Development
Flask is an element of Python that facilitates the creation of web applications through its framework and is used for the backend of this project to handle http requests made by the user/client. The routes at the backend are as follows:
Home (“/”) route
This route is for the reception/home page of the web application. This route handles GET http requests and uses the index.html templates.
/signup
This route is a sign up for the users who do not have an account. This route handles GET and POST http requests. It uses the signup.html and index.html templates.
/login
This route handles login requests sent by the user/client. This route handles GET and POST http requests. It uses the login.html and drivers.html templates.
/logout
This route handles logout requests sent by the user/client. This route handles GET and POST http requests. It uses the index.html template.
/drivers
This route deals with the http request sent by the user/client and retrieves posts created by experienced drivers from the database. This route handles GET http requests. It uses the drivers.html template.
/search
This route shows the results of searches done by the user/client. This route handles GET http requests. It uses the search.html template.
/filtered-result
This route shows the results of the ‘filter by’ tool. This route handles GET and POST http requests. It uses the filtered-result.html and drivers.html templates.
/profile/<int:id>
This route is for users’ profile pages. This route handles GET http requests. It uses the profile.html template.
/update-user/<int:id>
This route handles GET and POST http requests that users send to update their profile information. It uses the update-user.html and profile.html templates.
/delete-user/<int:id>
This route handles GET http requests that users send to delete their profile/account. It uses the delete-user.html, profile.html, and index.html templates.
/create
This route deals with GET and POST http requests that users send to create posts.It uses the create.html and drivers.html templates.
/update-post/<int:id>
This route handles GET and POST http requests that users send to update their posts. It uses the update-post.html and drivers.html templates.
/delete-post/<int:id>
This route handles GET http requests that users send to delete their posts. It uses the profile.html template to be redirected.
/post/<int:id>
This route deals with GET http requests sent by the user to view full posts, containing extra information not displayed in the two-hundred-character preview. It uses the post.html template.
/send_message/<int:id>
This route handles GET and POST http requests sent by the user to send messages. It uses the send_message.html template.
/messages
This route deals with GET http requests sent by the user to view the messages they have received. It uses the messages.html template.
/messages_sent
This route handles GET http requests sent by the user to view the messages they have sent. It uses the messages_sent.html template.
/delete_message/<int:id>
This route deals with GET http requests sent by the user to delete messages. It uses the messages.html template to be redirected.
Each route has its own functionality and logic behind it. The algorithms are discussed in the implementation section. The routes’ code and html templates can be found in the appendix. 
















 Algorithm(s) developed during this process 
While more than one algorithm was developed during the course of the project, the author has chosen to display and briefly explain the sign-up algorithm below. All other algorithms can be found in the appendix under the app.py section.
Sign-up algorithm explanation
First, the algorithm checks whether the http request made by the user is a POST request or a GET request. If it is a GET request, the algorithm simply renders the signup.html template. If it is a POST request, the algorithm first assigns the values of each form element to a variable, such as ‘email = request.form['mail']’. Each piece of data assigned as a variable must subsequently satisfy certain specified conditions, for example, if len(first_name) > 50. If the conditions are not met, the system warns the user with a banner located at the top of the pages, detailing the unmet criteria.
If the above conditions are satisfied, the next condition checked by the algorithm is whether the email address entered is already registered on the system. If so, the user is unable to reuse the same email and is thus unable to register. If not, the profile picture’s path is created, the password entered by the user is hashed, and an account is created for the new user. Then the user is redirected to the homepage. 

@app.route('/signup', methods=['GET', 'POST'])
def signup():


    #getting the data from the form in the front end through post request
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['mail']
        password = request.form['pwd']
        password2 = request.form['pwd2']
        dob = request.form['age']
        profile_pic = request.files['profile_pic']


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
        elif profile_pic == "":
            flash('Profile photo is required', category='error')


        else:
            #checking if the email is used already
            existing_email = User.query.filter_by(
                    email=email).first()
            if existing_email:
                flash("This email already exists.", category='error')
                return redirect(url_for('signup'))


            #if email does not exist hashing the pw and creating the user profile
            else:


                profile_pic = request.files['profile_pic']
                #grab image name
                pic_filename = secure_filename(profile_pic.filename)
                # set uuid
                pic_name = str(uuid.uuid1()) + "_" + pic_filename
                # save the image
                profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                # Change from image to string to save
                #it to db
                profile_pic = pic_name


                #4 rows of code below is from https://www.youtube.com/watch?v=71EU8gnZqZQ&t=1442s
                hashed_pw = bcrypt.generate_password_hash(password)


                new_user = User(email=email, first_name=first_name, 
                password = hashed_pw ,last_name=last_name, age=dob,
                profile_pic=profile_pic) 
                
                db.session.add(new_user)
                db.session.commit()
                flash('Account created!', category='success')
                return redirect(url_for('index'))


        flash('Account not created!', category='error')
        return redirect(url_for('signup'))
    #if the request is get, just showing the template to the user           
    else:
        return render_template('signup.html')





















Project Testing and Evaluation 

Unit Testing
A small unit test was carried out solely to demonstrate the author’s knowledge of and ability to carry out a unit test. It must be noted at this point that, as this topic, in terms of web application development, was not covered in depth during the course, the author was only able to carry out a unit test of this scale. 
This particular unit test tests status code, which can be seen in the first function, content type, as per the second function, and data returned, as seen in the last function. 
from app import app
import unittest


class FlaskTest(unittest.TestCase):
    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    #check if content return is "text/html; charset=utf-8"
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")


    #check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Ready to drive?' in response.data)
    


if __name__ == "__main__":
    unittest.main()

On the other hand, after deploying the app to Heroku, the author was able to share the app with a number of potential users who tested the app and provided useful and insightful feedback. Based on this feedback, the author updated the app and fixed any bugs that were brought to his attention. 
The app has several minor weaknesses:
 Creating profile photos and thumbnails from uploaded photos is a challenge as there is no system that crops them to the necessary dimensions. 
The messaging system cannot be classed as instant messaging as it is missing so of the key features e.g. message history and ungrouped messages. 
Any DateTime related data in the system was difficult to manage as there are differences between Python, HTML and database’s DateTime, making it a challenge to accurately integrate. 
Overall, the author has successfully created a functioning web application and adhered to the plan and goals provided in the proposal.





















Conclusions and Future Work
Learning Experiences
The project has enabled me to become a more autonomous and independent learner which has allowed me to develop the skills necessary to become a confident, successful future IT professional. This is a valuable project for the author’s portfolio.
Future Work
The following are additional features and functionalities, which are beyond the scope of this project, that can be incorporated into the project during future development:
A better messaging system whereby the messages sent to and received from a particular user will appear in a chat format, rather than individual, separate messages. 
A forum through which users can express any doubts or queries they may have and/or share personal experience with others with the scope of providing helpful and useful information.
Turn the platform into a go-to resource for learners for any driving/car related queries and advice. For example, a function can be added to display points of contact for car-related companies, live talks, meetings etc. 

The following are aspects of the web application that have been either added, altered or removed:
The map/location feature was removed as the author realised that no fixed location is required given that the experienced drivers can move around and serve more than one area.
The chat feature was altered as the integration process was too advanced and complex. Instead, a combination of a messing and mail feature was added where instant messaging is possible, but the interface does not include message history. 
In addition to the previous point, the messaging section has been divided into two tabs: one for sent and one for received messages. 
 The delete and edit features are applicable to accounts and ads. The delete option is also applicable for messages. These give users flexibility and control. 
 A filter option was added to give users a more personalised and relevant experience.
Commercial pay-per-click ads were added to generate income for the app as it is free for users.




References / Bibliography
Bayer, M., 2022. SQLAlchemy Documentation — SQLAlchemy 1.4 Documentation. [online] Docs.sqlalchemy.org. Available at: <https://docs.sqlalchemy.org/en/14/> [Accessed 27 June 2022].
Codemy.com, 2022. Upload Profile Picture - Flask Fridays #38. [video] Available at: <https://www.youtube.com/watch?v=ZHQtxITPcAs> [Accessed 16 July 2022].
CSO, 2016. Driver and Vehicle Testing. [online] Central Statistics Office. Available at: <https://www.cso.ie/en/releasesandpublications/ep/p-tranom/to2016/dvt/> [Accessed 25 May 2022].
Flask.palletsprojects.com. 2010. Welcome to Flask — Flask Documentation (2.2.x). [online] Available at: <https://flask.palletsprojects.com/en/2.2.x/> [Accessed 31 June 2022].
freeCodeCamp.org, 2019. Learn Flask for Python - Full Tutorial. [video] Available at: <https://www.youtube.com/watch?v=Z1RJmh_OqeA> [Accessed 16 May 2022].
Grinberg, M., 2018. The Flask Mega-Tutorial Part XXI: User Notifications. [Blog] miguelgrinberg.com, Available at: <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxi-user-notifications> [Accessed 1 August 2022].
Mark Otto, a., n.d. Bootstrap. [online] Getbootstrap.com. Available at: <https://getbootstrap.com/> [Accessed 2 June 2022].
RSA, 2019. Essential Driver Training (EDT): Learner Driver Information Booklet. 2nd ed. Dublin: Road Safety Authority, p.7.














Appendices

Screenshots
Homepage




Sign Up Page



Sign In Page




Profile Page



Update Profile Page





Delete Profile Page



Create Ad Page


Update Ad Page





Drivers Page



Detailed Ad Page





Filter Page



Search Page




Messages Received Page


Messages Sent Page








Codes:

App.py

#importing the necessary packages and libraries for the app


from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid as uuid
import os



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


UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
    profile_pic = db.Column(db.String(), nullable=False)  


    posts = db.relationship('Post', backref='user', cascade="delete")


    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)


    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()


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
    location = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    post_pic =db.Column(db.String(), nullable=False)


    #creating this representative function 
    #if there is an error i will be able to
    #see the post the error coming from
    def __repr__(self):
        return f'<Post {self.id}>'


#creating message table in the database
#and creating the sender_id and recipient_id 
#to link this table with the parent
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


    def __repr__(self):
        return '<Message {}>'.format(self.body)


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
        profile_pic = request.files['profile_pic']


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
        elif profile_pic == "":
            flash('Profile photo is required', category='error')


        else:
            #checking if the email is used already
            existing_email = User.query.filter_by(
                    email=email).first()
            if existing_email:
                flash("This email already exists.", category='error')
                return redirect(url_for('signup'))


            #if email does not exist hashing the pw and creating the user profile
            else:


                profile_pic = request.files['profile_pic']
                #grab image name
                pic_filename = secure_filename(profile_pic.filename)
                # set uuid
                pic_name = str(uuid.uuid1()) + "_" + pic_filename
                # save the image
                profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                # Change from image to string to save
                #it to db
                profile_pic = pic_name


                #4 rows of code below is from https://www.youtube.com/watch?v=71EU8gnZqZQ&t=1442s
                hashed_pw = bcrypt.generate_password_hash(password)


                new_user = User(email=email, first_name=first_name, 
                password = hashed_pw ,last_name=last_name, age=dob,
                profile_pic=profile_pic) 
                
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
            filter(User.first_name.ilike(f'%{search}%') | \
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


        if request.form['location'] == 'any' and request.form['lang'].strip() != '':
            language = request.form['lang'].strip()


            result = db.session.query(Post). \
                order_by(Post.date_created.desc()). \
                filter(Post.language.ilike(f'%{language}%')) \
                .all()


            return render_template(
                'filtered-result.html', 
                result=result,
                date=date)


        elif request.form['location'] != 'any' and request.form['lang'].strip() == '':
            location = request.form['location']


            result = db.session.query(Post). \
                order_by(Post.date_created.desc()). \
                filter(Post.location == location).all()


            return render_template(
                'filtered-result.html', 
                result=result,
                date=date)


        elif request.form['location'] == 'any' and request.form['lang'].strip() == '':
            return redirect(url_for('drivers'))
        
        else:
            location = request.form['location']
            language = request.form['lang'].strip()


            result = db.session.query(Post). \
                order_by(Post.date_created.desc()). \
                filter(Post.location.like(f'%{location}%')). \
                filter(Post.language.ilike(f'%{language}%')). \
                    all()


            return render_template(
                'filtered-result.html', 
                result=result,
                date=date)


    else:
        return redirect(url_for('drivers'))
        


@app.route('/profile/<int:id>', methods=['GET'])
# @login_required
def profile(id):


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
            profile_pic = request.files['profile_pic']


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


                        #grab image name
                        pic_filename = secure_filename(profile_pic.filename)
                        # set uuid
                        pic_name = str(uuid.uuid1()) + "_" + pic_filename
                        # save the image
                        profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                        # Change from image to string to save
                        #it to db
                        profile_pic = pic_name


                        user.first_name = request.form['fname'].strip()
                        user.last_name = request.form['lname'].strip()
                        user.email = request.form['mail'].strip()
                        user.password = hashed_pw
                        user.age = request.form['age'].strip()
                        user.profile_pic = profile_pic
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
        pic = user.profile_pic
        pic = pic.split("_")
        pic = pic[1]
        return render_template(
            'update-user.html', 
            user=user,
            pic=pic)


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


        elif request.files['post_pic'] == '':
            flash('Post Photo cannot be empty', category='error')
            return render_template(
            'update-post.html', 
            posts=posts)


        else:
            post_pic = request.files['post_pic']
            #grab image name
            post_pic_filename = secure_filename(post_pic.filename)
            # set uuid
            post_pic_name = str(uuid.uuid1()) + "_" + post_pic_filename
            # save the image
            post_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], post_pic_name))
            # Change from image to string to save
            #it to db
            post_pic = post_pic_name


            #3 rows of code below is from https://www.youtube.com/watch?v=Z1RJmh_OqeA
            posts.content = request.form['content'].strip()
            posts.location = request.form['location']
            posts.language = request.form['lang'].strip()
            posts.post_pic = post_pic
            db.session.commit()
            flash('Ad updated', category='success')
            return redirect(url_for('drivers'))
            


    else:
        post_picture = posts.post_pic
        post_picture = post_picture.split("_")
        post_picture = post_picture[1]
        return render_template(
            'update-post.html', 
            posts=posts,
            post_picture=post_picture)


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
        post_pic = request.files['post_pic']


        #if the content is empty
        if len(content) < 1:
            flash("Task too short!", category='error')
        elif language.strip() == '':
            flash("Language cannot be empty!", category='error')
        elif location.strip() == '':
            flash("Please choose your county", category='error')
        elif post_pic == '':
            flash("Please select a photo for your post", category='error')
            
        else:


            #grab image name
            post_pic_filename = secure_filename(post_pic.filename)
            # set uuid
            post_pic_name = str(uuid.uuid1()) + "_" + post_pic_filename
            # save the image
            post_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], post_pic_name))
            # Change from image to string to save
            #it to db
            post_pic = post_pic_name


            #passing required info to create a new task
            new_post = Post(
                content=content, 
                user_id=current_user.id,
                location=location,
                language=language,
                post_pic = post_pic
                )


            #creating the task
            db.session.add(new_post)
            db.session.commit()
            flash("Ad created successfully", category='success')
            return redirect('drivers')
        
        return redirect(url_for('create'))


    return render_template(
            'create.html') 



@app.route('/send_message/<int:id>', methods=['GET', 'POST'])
@login_required
def send_message(id):
    user = User.query.filter_by(id=id).first_or_404()
    
    if request.method == 'POST':
        sms = request.form['message']


        if len(sms.strip()) == 0:
            flash('Message is empty.', category='error')
        else:
            msg = Message(author=current_user, recipient=user,
                      body=sms)
            db.session.add(msg)
            db.session.commit()
            flash('Your message has been sent.')
            return redirect(url_for('messages_sent', id=id))


        return render_template('send_message.html', 
            user=user)


    return render_template('send_message.html', 
            user=user)


@app.route('/messages')
@login_required
def messages():


    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()


    page = request.args.get('page', 1, type=int)


    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page=page, per_page=10)


    next_url = url_for('messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('messages', page=messages.prev_num) \
        if messages.has_prev else None
    
    return render_template('messages.html', messages=messages.items,
                           next_url=next_url, prev_url=prev_url)
                    
@app.route('/messages_sent')
@login_required
def messages_sent():


    page = request.args.get('page', 1, type=int)


    messages = current_user.messages_sent.order_by(
        Message.timestamp.desc()).paginate(
            page=page, per_page=10)


    next_url = url_for('messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('messages', page=messages.prev_num) \
        if messages.has_prev else None
    
    return render_template('messages_sent.html', messages=messages.items,
                           next_url=next_url, prev_url=prev_url)
            


@app.route('/delete_message/<int:id>')
@login_required
def delete_message(id):
    messages = Message.query.get_or_404(id)


    if messages:
        #3 rows of code below is from https://www.youtube.com/watch?v=Z1RJmh_OqeA
        db.session.delete(messages)
        db.session.commit()
        flash('Message deleted', category='success')
        return redirect(url_for('messages'))


    else:
        flash("Message not exist", category='error')
        return redirect(url_for('messages'))


if __name__ == "__main__":
    app.run(debug=True)



Test_app.py

from app import app
import unittest


class FlaskTest(unittest.TestCase):
    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    #check if content return is "text/html; charset=utf-8"
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")


    #check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Ready to drive?' in response.data)
    


if __name__ == "__main__":
    unittest.main()












Templates

 Base.html

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.2/font/bootstrap-icons.css">
        
        <style>
          html{
            scroll-behavior: smooth;
          }
          
      </style>
        {% block head %}{% endblock %}
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="{{url_for('index')}}">BuddyDrivers</a>
            <button 
              class="navbar-toggler" 
              type="button" 
              data-toggle="collapse" 
              data-target="#nav-menu"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
          
            <div id="nav-menu" class="collapse navbar-collapse">


                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                      <a class="nav-link" href="{{url_for('index')}}">
                        <i class="bi bi-house"></i>
                        Home
                      </a>
                    </li>
                    
                    <li class="nav-item">
                    {% if current_user.is_authenticated %}
                      <a class="nav-link" href="/profile/{{current_user.id}}">
                        <i class="bi bi-person"></i>
                        Profile
                      </a>
                    {% else %}
                      <a class="nav-link" href="/login">
                        <i class="bi bi-person"></i>
                        Profile
                      </a>
                    {% endif %}
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="{{url_for('drivers')}}">
                        <i class="bi bi-speedometer2"></i>
                        Drivers
                      </a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="{{url_for('create')}}">
                        <i class="bi bi-megaphone"></i>
                        Create Ad
                      </a>
                    </li>
                </ul>


                <ul class="navbar-nav">
                  <form 
                  class="form-inline my-2 my-lg-0"
                  action="/search">
                    <input 
                        class="form-control mr-sm-2" 
                        type="search" 
                        placeholder="Search" 
                        aria-label="Search"
                        name="search">
                    <button 
                        class="btn btn-outline-success my-2 my-sm-0 d-none d-lg-block" 
                        type="submit">
                        Search
                    </button>
                  </form>
                </ul>


                <ul class="navbar-nav ml-auto">
                    {% if current_user.is_authenticated %}


                    <li class="nav-item">
                        <a class="btn btn-outline-secondary" href="/messages">
                          <i class="bi bi-chat"></i> Messages
                          {% set new_messages = current_user.new_messages() %}
                          {% if new_messages %}
                            <span class="badge badge-success">{{new_messages}}</span>
                          {% endif %}
                        </a>
                        <a class="btn btn-outline-success" href="/profile/{{current_user.id}}">{{current_user.first_name}}</a>
                        <a class="btn btn-outline-secondary" href="{{url_for('logout')}}">Sign Out</a>
                    </li>   


                    {% else %}
                    
                    <li class="nav-item">
                        <a class="btn btn-success" href="{{url_for('login')}}">Sign In</a>
                        <a class="btn btn-outline-success" href="{{url_for('signup')}}">Sign Up</a>
                    </li>


                    {% endif %}
                </ul>


            </div>
          </nav>


          <!-- flash messages reference https://www.youtube.com/watch?v=abCSKRMGZ3A&t=410s -->
          {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
              {% for category, message in messages %}
                {% if category == 'error' %}
                  <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                {% else %}
                  <div class="alert alert-success alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                {% endif %}
              {% endfor %}
            {% endif %}
          {% endwith %}


        {% block body %}{% endblock %}


        <br>
    <!-- Footer -->
<footer class="bg-dark text-center text-white">
    <!-- Grid container -->
    <div class="container p-4">
      <!-- Section: Social media -->
      <section class="mb-4">
        <!-- Facebook -->
        <a class="btn btn-outline-light btn-floating m-1" href="https://www.facebook.com/" target="_blank" role="button">
            <i class="bi bi-facebook"></i>
        </a>
  
        <!-- Twitter -->
        <a class="btn btn-outline-light btn-floating m-1" href="https://twitter.com" target="_blank" role="button">
            <i class="bi bi-twitter"></i>
        </a>
  
        <!-- Google -->
        <!-- <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"
          ><i class="fab fa-google"></i
        ></a> -->
  
        <!-- Instagram -->
        <a class="btn btn-outline-light btn-floating m-1" href="https://www.instagram.com/" target="_blank" role="button">
            <i class="bi bi-instagram"></i>
        </a>
  
        <!-- Linkedin -->
        <a class="btn btn-outline-light btn-floating m-1" href="https://www.linkedin.com/" target="_blank" role="button">
            <i class="bi bi-linkedin"></i>
        </a>
  
        <!-- Github -->
        <!-- <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"
          ><i class="fab fa-github"></i
        ></a> -->
      </section>
      <!-- Section: Social media -->


  
      <!-- Section: Text -->
      <section class="mb-4">
        <p>
          Do you have a learner permit? Are you getting your essential driving lessons or already completed them? Do you need more practice? You are at the correct place. View the buddydrivers to find someone to practice with.
        </p>
      </section>
      <!-- Section: Text -->
  
      <!-- Section: Links -->
      <section class="">
        <!--Grid row-->
        <div class="row">
          <!--Grid column-->
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Links</h5>
  
            <ul class="list-unstyled mb-0">
              <li>
                <a style="color: white;" href="{{url_for('index')}}">
                  <i class="bi bi-house"></i>
                  Home
                </a>
              </li>
            </ul>
          </div>
          <!--Grid column-->
  
          <!--Grid column-->
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Links</h5>
  
            <ul class="list-unstyled mb-0">
              <li class="nav-item">
                {% if current_user.is_authenticated %}
                  <a style="color: white;" class="nav-link" href="/profile/{{current_user.id}}">
                    <i class="bi bi-person"></i>
                    Profile
                  </a>
                {% else %}
                  <a style="color: white;" class="nav-link" href="/login">
                    <i class="bi bi-person"></i>
                    Profile
                  </a>
                {% endif %}
                </li>
            </ul>
          </div>
          <!--Grid column-->
  
          <!--Grid column-->
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Links</h5>
  
            <ul class="list-unstyled mb-0">
              <li class="nav-item">
                <a style="color: white;" class="nav-link" href="{{url_for('drivers')}}">
                  <i class="bi bi-speedometer2"></i>
                  Drivers
                </a>
              </li>
              
            </ul>
          </div>
          <!--Grid column-->
  
          <!--Grid column-->
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Links</h5>
  
            <ul class="list-unstyled mb-0">
              <li class="nav-item">
                <a style="color: white;" class="nav-link" href="{{url_for('create')}}">
                  <i class="bi bi-megaphone"></i>
                  Create Ad
                </a>
              </li>
            </ul>
          </div>
          <!--Grid column-->
        </div>
        <!--Grid row-->
      </section>
      <!-- Section: Links -->
    </div>
    <!-- Grid container -->
  
    <!-- Copyright -->
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
      © 2022 Copyright:
      <a class="text-white" href="https://buddydrivers.com/">buddydrivers.com</a>
    </div>
    <!-- Copyright -->
  </footer>
  <!-- Footer -->


        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script src="https://kit.fontawesome.com/5c9a0150f6.js" crossorigin="anonymous"></script>
        
      </body>
</html>


Create.html

{% extends 'base.html' %}


{% block head %}
    <title>Create Post</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}
{% endblock %}


{% block body %}


    {% if current_user.is_authenticated %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-12  col-lg-6 text-left">
                    
               
                    <br>
                    <h3 align="center">Create Ad</h3>
                    <br>
            
                    <div class="d-row justify-content-center">
                        <!-- form design is from bootstrap https://getbootstrap.com/docs/5.0/forms/overview/-->
                        <form action="/create" method="POST" enctype="multipart/form-data">
                                
                            <div class="form-row">
            
                                <span style="margin-right: 5px;">I am in</span>
                                <select style="margin-left: 2%;" name="location"
                                class="form-select form-select-lg mb-3" 
                                aria-label="Default select example" required>
                                    <option value=""></option>
                                    <option value="Antrim">Antrim</option>
                                    <option value="Armagh">Armagh</option>
                                    <option value="Carlow">Carlow</option>
                                    <option value="Cavan">Cavan</option>
                                    <option value="Clare">Clare</option>
                                    <option value="Cork">Cork</option>
                                    <option value="Derry">Derry</option>
                                    <option value="Donegal">Donegal</option>
                                    <option value="Down">Down</option>
                                    <option value="Dublin">Dublin</option>
                                    <option value="Fermanagh">Fermanagh</option>
                                    <option value="Galway">Galway</option>
                                    <option value="Kerry">Kerry</option>
                                    <option value="Kildare">Kildare</option>
                                    <option value="Kilkenny">Kilkenny</option>
                                    <option value="Laois">Laois</option>
                                    <option value="Leitrim">Leitrim</option>
                                    <option value="Limerick">Limerick</option>
                                    <option value="Longford">Longford</option>
                                    <option value="Louth">Louth</option>
                                    <option value="Mayo">Mayo</option>
                                    <option value="Meath">Meath</option>
                                    <option value="Monaghan">Monaghan</option>
                                    <option value="Offaly">Offaly</option>
                                    <option value="Roscommon">Roscommon</option>
                                    <option value="Sligo">Sligo</option>
                                    <option value="Tipperary">Tipperary</option>
                                    <option value="Tyrone">Tyrone</option>
                                    <option value="Waterford">Waterford</option>
                                    <option value="Westmeath">Westmeath</option>
                                    <option value="Wexford">Wexford</option>
                                    <option value="Wicklow">Wicklow</option>
                                </select>
            
                            </div>
            
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="lang">I speak</label>
                                    <input class="form-control" type="text" id="lang" name="lang" placeholder="Language(s)">
                                </div>
            
                            </div>
            
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="content">Content</label><br>
                                    <textarea id="content" name="content" rows="5" cols="34"></textarea><br>
                                </div>
            
                            </div>


                            <div class="form-row">
                                <span style="margin-left: 1%;">Post Photo</span><br>
                                <div 
                                style="margin-top: 2%; margin-right: 1%; margin-left: 1%;" 
                                class="input-group row-md-6 mb-3">
                                    <input 
                                    type="file" 
                                    class="custom-file-input" 
                                    id="post_pic" 
                                    name="post_pic"
                                    accept=".jpg, .jpeg, .png"
                                    required>
                                    <label class="custom-file-label" for="post_pic">                                    
                                        Post Photo
                                    </label>
                                </div>
            
                            </div>
                            
                            <input class="btn btn-outline-success" type="submit" value="Create"></input>
                        </form>
                    </div>
                    
                <br>
                            
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>


    {% else %}


        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <br>
                        <h3 align="center" style="margin-top: 10%;">You are being redirected to log in!</h3>
                    <br>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-right: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>


    {% endif %}


    </div>
    
    
{% endblock %}





















Delete-user.html

{% extends 'base.html' %}


{% block head %}
    <title>Delete User Account</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}
{% endblock %}


{% block body %}


    {% if current_user.is_authenticated %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                    
                <div style="margin-top: 25%;" class="container">
            
                    <div class="d-flex justify-content-center" style="margin-bottom: 15%;">
                        <!-- form design is from bootstrap https://getbootstrap.com/docs/5.0/forms/overview/-->
                        <form action="/delete-user/{{user.id}}" method="POST" >
                                
                            <div class="form-row">            
                   
                                <label for="pwd">Enter Password to Delete User Account</label>
                                <input class="form-control" type="password" id="pwd" name="pwd" placeholder="Password">
                                                
                            </div>
                            
                            <input class="btn btn-outline-danger my-3" type="submit" value="Delete"></input>
                        </form>
                    </div>
                    
                </div><br>
                
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>


       
    {% else %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                    
                <br>
                    <h3 align="center" style="margin-top: 10%;">You are being redirected to log in!</h3>
                <br>
                
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>


    {% endif %}


    </div>
    
    
{% endblock %}



























Drivers.html

{% extends 'base.html' %}


{% block head %}
    <title>Drivers</title>
{% endblock %}


{% block body %}


    
    {% if posts.items|length < 1 %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                    
                <div class="container">
                    <h5 style="margin-top: 25%; margin-bottom: 300px;" align="center">There are no ads yet. <a href="{{url_for('create')}}">Create now</a></h5>     
                </div>
                
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


        </div>


    </div>
        
        {% else %}


        <div class="container text-center">
            <br>
            <div class="row justify-content-between"> 
                
                <div class="col-12  col-lg-3">
                    <div class="card mb-4">
                        <h5 style="margin-bottom: 2%; margin-top: 5%;">Filter by</h5>
                        
                        <div class="card-body">
                
                            <form action="/filtered-result" method="POST" >


                                <span>Location</span><br><br>


                                <select name="location"
                                class="form-group form-select mb-3 form-control" 
                                aria-label="Default select example">
                                    <option value="any">Any</option>
                                    <option value="Antrim">Antrim</option>
                                    <option value="Armagh">Armagh</option>
                                    <option value="Carlow">Carlow</option>
                                    <option value="Cavan">Cavan</option>
                                    <option value="Clare">Clare</option>
                                    <option value="Cork">Cork</option>
                                    <option value="Derry">Derry</option>
                                    <option value="Donegal">Donegal</option>
                                    <option value="Down">Down</option>
                                    <option value="Dublin">Dublin</option>
                                    <option value="Fermanagh">Fermanagh</option>
                                    <option value="Galway">Galway</option>
                                    <option value="Kerry">Kerry</option>
                                    <option value="Kildare">Kildare</option>
                                    <option value="Kilkenny">Kilkenny</option>
                                    <option value="Laois">Laois</option>
                                    <option value="Leitrim">Leitrim</option>
                                    <option value="Limerick">Limerick</option>
                                    <option value="Longford">Longford</option>
                                    <option value="Louth">Louth</option>
                                    <option value="Mayo">Mayo</option>
                                    <option value="Meath">Meath</option>
                                    <option value="Monaghan">Monaghan</option>
                                    <option value="Offaly">Offaly</option>
                                    <option value="Roscommon">Roscommon</option>
                                    <option value="Sligo">Sligo</option>
                                    <option value="Tipperary">Tipperary</option>
                                    <option value="Tyrone">Tyrone</option>
                                    <option value="Waterford">Waterford</option>
                                    <option value="Westmeath">Westmeath</option>
                                    <option value="Wexford">Wexford</option>
                                    <option value="Wicklow">Wicklow</option>
                                </select>
            
                                <div class="form-group mb-3">
                                    <label for="lang">Language</label>
                                    <input class="form-control" 
                                    type="text" 
                                    id="lang" 
                                    name="lang" 
                                    placeholder="Any"
                                    >
                                </div>
                
                                <input class="btn btn-outline-dark" type="submit" value="Filter"></input>
                            </form>
                                
                        </div>
                    </div>


                </div>    
                    
                


                <div class="col-sm-12  col-lg-6 text-left">
                    {% for post in posts.items %}
                        <div class="card">
                            <img class="card-img-top" src="{{url_for('static', filename='images/' + post.post_pic)}}" alt="Card image cap">
                            <div class="card-body">


                                <div class="d-flex justify-content-between">
                                    <a 
                                    style="margin-bottom: 2%;" 
                                    href="/profile/{{post.user.id}}">
                                        <div class="d-flex">
                                            <img class=" img-fluid" src="{{url_for('static', filename='images/' + post.user.profile_pic)}}" alt="thumbnail" style="width:40px; height:40px;">
                                            <h5 style="margin-left: 10%; margin-top: 15%;" class="card-title">{{ post.user.first_name }}</h5>
                                        </div>
                                    </a>
                                    {% if current_user.id == post.user.id %}
                                    <div class="dropdown">
                                        <i class="bi bi-gear-fill dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></i>
                                        
                                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                            <a class="dropdown-item" href="/update-post/{{post.id}}">Update</a>
                                            <a class="dropdown-item" href="/delete-post/{{post.id}}">Delete</a>
                                        </div>
                                    </div>


                                    {% endif %}
                                </div>


                                <p class="card-text">
                                    {% if post.content | length > 200  %}
                                        {{ post.content[0:200] }} ...
                                    {% else %}
                                        {{ post.content }}
                                    {% endif %}
                                </p>


                                <div class="d-flex align-items-center justify-content-center">
                                    <a 
                                    class="btn btn-outline-secondary btn-block"
                                    href="/post/{{post.id}}">View
                                    </a>                    
                                </div>


                            </div>
                            <div class="card-footer d-flex justify-content-between align-items-center">
                                <small class="text-muted">{{post.location}}</small>
                                <small class="text-muted">
                                    {% if post.language | length > 20  %}
                                        Language: {{ post.language[0:20] }} ...
                                    {% else %}
                                        Language: {{ post.language }}
                                    {% endif %}
                                </small>
                                <small class="text-muted">
                                    {% if (date).day - (post.date_created).day < 1 %}
                                        {% if (date).hour - (post.date_created).hour == 1 %}
                                            {% if (date).minute - (post.date_created).minute < 2 %}
                                                {{(date).minute - (post.date_created).minute}} min
                                            {% elif (date).minute - (post.date_created).minute > 1 %}
                                                {{(date).minute - (post.date_created).minute}} mins
                                            {% endif %}
                                        {% elif (date).hour - (post.date_created).hour < 2 %}
                                            {{(date).hour - (post.date_created).hour}} hour
                                        {% elif (date).hour - (post.date_created).hour > 1 %}
                                            {{(date).hour - (post.date_created).hour}} hours
                                        {% endif %}
                                    {% elif (date).day - (post.date_created).day == 1 %}
                                        {{(date).day - (post.date_created).day}} day
                                    {% elif (date).day - (post.date_created).day > 1 %}
                                        {{(date).day - (post.date_created).day}} days
                                    {% endif %}
                                </small>
                            </div>
                        </div>
                        <br>
                    {% endfor %}


                    {% for page_num in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
                        {% if page_num %}
                            {% if posts.page == page_num %}
                                <a class="btn btn-outline-dark mb-4 active" href="{{url_for('drivers', page=page_num)}}">{{page_num}}</a>
                            {% else %}
                                <a class="btn btn-outline-dark mb-4" href="{{url_for('drivers', page=page_num)}}">{{page_num}}</a>
                            {% endif %}
                        {% else %}
                            ...
                        {% endif %}
                    {% endfor %}
                </div>               
            
                <div 
                style="margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>


            </div>


            <a href="#top" class="btn btn-outline-success float-right">
                <i class="bi bi-chevron-double-up"></i>
                Go to top
            </a>
            <br>


        </div> 
        
    {% endif %}
         
    
{% endblock %}






























Filtered-result.html

{% extends 'base.html' %}


{% block head %}
    <title>Filtered Result</title>
{% endblock %}


{% block body %}


    {% if result == [] %}


    <div style="margin-top: 2%;" class="container text-center">
        <br>
        <div style="margin-bottom: 5%;" class="row justify-content-between">     
            <div 
            style="margin-top: 2%;" 
            class="col-2 sidenav text-left">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                <h3 style="margin-top: 15%;" align="center">No result found</h3>
            </div>               
        
            <div 
            style="margin-top: 2%;" 
            class="col-2 sidenav text-right">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>
        <br>
    </div>
        
    {% else %}


        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                    {% for post in result%}
                        <div class="card">
                            <img class="card-img-top" src="{{url_for('static', filename='images/' + post.post_pic)}}" alt="Card image cap">
                            <div class="card-body">
                                <div class="d-flex justify-content-between">
                                    <a 
                                    style="margin-bottom: 2%;" 
                                    href="/profile/{{post.user.id}}">
                                        <div class="d-flex">
                                            <img class="img-fluid" src="{{url_for('static', filename='images/' + post.user.profile_pic)}}" alt="thumbnail" style="width:40px; height:40px;">
                                            <h5 style="margin-left: 10%; margin-top: 15%;" class="card-title">{{ post.user.first_name }}</h5>
                                        </div>
                                    </a>
                                </div>
                                <p class="card-text">
                                    {% if post.content | length > 200  %}
                                        {{ post.content[0:200] }} ...
                                    {% else %}
                                        {{ post.content }}
                                    {% endif %}
                                </p>
                                <div class="d-flex align-items-center justify-content-center">
                                    <a 
                                    class="btn btn-outline-secondary btn-block"
                                    href="/post/{{post.id}}">View
                                    </a>                    
                                </div>
                            </div>
                            <div class="card-footer d-flex justify-content-between align-items-center">
                                <small class="text-muted">{{post.location}}</small>
                                <small class="text-muted">
                                    {% if post.language | length > 20  %}
                                        Language: {{ post.language[0:20] }} ...
                                    {% else %}
                                        Language: {{ post.language }}
                                    {% endif %}
                                </small>
                                <small class="text-muted">
                                    {% if (date).day - (post.date_created).day < 1 %}
                                        {% if (date).hour - (post.date_created).hour == 1 %}
                                            {% if (date).minute - (post.date_created).minute < 2 %}
                                                {{(date).minute - (post.date_created).minute}} min
                                            {% elif (date).minute - (post.date_created).minute > 1 %}
                                                {{(date).minute - (post.date_created).minute}} mins
                                            {% endif %}
                                        {% elif (date).hour - (post.date_created).hour < 2 %}
                                            {{(date).hour - (post.date_created).hour}} hour
                                        {% elif (date).hour - (post.date_created).hour > 1 %}
                                            {{(date).hour - (post.date_created).hour}} hours
                                        {% endif %}
                                    {% elif (date).day - (post.date_created).day == 1 %}
                                        {{(date).day - (post.date_created).day}} day
                                    {% elif (date).day - (post.date_created).day > 1 %}
                                        {{(date).day - (post.date_created).day}} days
                                    {% endif %}
                                </small>
                            </div>
                        </div>
                        <br>
                    {% endfor %}


                </div>               
            
                <div 
                style="margin-top: 2%;
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>


            </div>


            <a href="#top" class="btn btn-outline-success float-right">
                <i class="bi bi-chevron-double-up"></i>
                Go to top
            </a>
            <br>


        </div> 
    {% endif %}
    
{% endblock %}






















Index.html

{% extends 'base.html' %}


{% block head %}
    <title>Home</title>
{% endblock %}


{% block body %}


    <main class="container-fluid">
        
        <div class="row" style="margin-top: 2%;">


            <div 
            style="margin-top: 2%;" 
            class="col-2 sidenav text-right">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


            <div class="col-md-8 col-lg-8">
                <section class="py-4">
                    <div class="row py-lg-3">
                        <div class="col-lg-6 col-md-8 mx-auto">
                            <h3 class="fw-light text-center">Ready to drive?</h3>
                            <p class="lead text-muted text-justify mx-4">
                                Do you have a learner permit? 
                                Are you getting your essential driving lessons or 
                                already completed them? Do you need more practice? 
                                You are at the correct place.
                                View the buddydrivers to find someone to practice with.
                            </p>
                        </div>
                    </div>
                </section>
    
                <div class="d-flex justify-content-center" style="margin-bottom: 5%; margin-top: 3%;">
                    <!-- form design is from bootstrap https://getbootstrap.com/docs/5.0/forms/overview/-->
                    <form action="/filtered-result" method="POST" >


                        <fieldset>


                            <legend>Discover Drivers By</legend>
                            
                            <div class="form-row">            
                
                                <span style="margin-bottom: 7px;">Location</span><br>


                                <select name="location"
                                class="form-group form-select mb-3 form-control" 
                                aria-label="Default select example">
                                    <option value="any">Any</option>
                                    <option value="Antrim">Antrim</option>
                                    <option value="Armagh">Armagh</option>
                                    <option value="Carlow">Carlow</option>
                                    <option value="Cavan">Cavan</option>
                                    <option value="Clare">Clare</option>
                                    <option value="Cork">Cork</option>
                                    <option value="Derry">Derry</option>
                                    <option value="Donegal">Donegal</option>
                                    <option value="Down">Down</option>
                                    <option value="Dublin">Dublin</option>
                                    <option value="Fermanagh">Fermanagh</option>
                                    <option value="Galway">Galway</option>
                                    <option value="Kerry">Kerry</option>
                                    <option value="Kildare">Kildare</option>
                                    <option value="Kilkenny">Kilkenny</option>
                                    <option value="Laois">Laois</option>
                                    <option value="Leitrim">Leitrim</option>
                                    <option value="Limerick">Limerick</option>
                                    <option value="Longford">Longford</option>
                                    <option value="Louth">Louth</option>
                                    <option value="Mayo">Mayo</option>
                                    <option value="Meath">Meath</option>
                                    <option value="Monaghan">Monaghan</option>
                                    <option value="Offaly">Offaly</option>
                                    <option value="Roscommon">Roscommon</option>
                                    <option value="Sligo">Sligo</option>
                                    <option value="Tipperary">Tipperary</option>
                                    <option value="Tyrone">Tyrone</option>
                                    <option value="Waterford">Waterford</option>
                                    <option value="Westmeath">Westmeath</option>
                                    <option value="Wexford">Wexford</option>
                                    <option value="Wicklow">Wicklow</option>
                                </select>


                            </div>


                            <div class="form-row form-group mb-3"> 
            
                                <label for="lang">Language</label>
                                <input class="form-control" 
                                type="text" 
                                id="lang" 
                                name="lang" 
                                placeholder="Any"
                                >


                            </div>


                            <div class="form-row form-group mb-3"> 
                                
                                <input class="btn btn-outline-dark" type="submit" value="Discover"></input>
                                
                            </div>


                        </fieldset>
                        
                    </form>
                </div>
    
                
            </div>
            
            <div 
            style="margin-top: 2%;" 
            class="col-2 sidenav text-left">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>


        </div>
        
        
    </main>
          
    
    
        
{% endblock %}




















Login.html

{% extends 'base.html' %}


{% block head %}
    <title>Sign In</title>
    {% if current_user.is_authenticated %}
        <meta http-equiv="REFRESH" content="4; profile/{{current_user.id}}">
    {% endif %}


{% endblock %}


{% block body %}


    {% if current_user.is_authenticated %}


        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <br>
                    <h3 align="center" style="margin-top: 10%;">Hi {{ current_user.first_name }}! You are being redirected to your profile.</h3>


                    <br>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-right: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>
    
    {% else %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">


                <div class="container">
                    <div style="margin-top: 25%;" class="d-flex justify-content-center align-items-center">
                        <div class="card" style="width: 20rem;">
                            <div class="card-body">
                              <h5 class="card-title">Sign In</h5>
                              <form action="/login" method="POST">
                                    <div class="form-group">
                                    <label for="mail">Email</label>
                                    <input class="form-control" type="email" id="mail" name="mail">
                                    </div>
                                    <div class="form-group">
                                    <label for="pwd">Password</label>
                                    <input class="form-control" type="password" id="pwd" name="pwd">
                                    </div>
                                    <input class="btn btn-outline-dark" type="submit" value="Sign In">
                            </form>
                            </div>
                        </div>
                    </div>
                </div>
                <br><br>
                
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>
        


    {% endif%}


    </div>


    
{% endblock %}
    
























Messages_sent.html

{% extends 'base.html' %}


{% block head %}
    <title>Messages Sent</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}


{% endblock %}


{% block body %}


    {% if current_user.is_anonymous %}
    
        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <h3 align="center" style="margin-top: 10%;">You are being redirected to login!</h3>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>
    
    
    {% else %}


        {% if messages|length < 1 %}


            <div class="container text-center">
                <br>
                <div class="row justify-content-between">     
                    <div 
                    style="
                    margin-left: -10%;" 
                    class="col-2 sidenav">
                        <img src="../static/ads/default.jpeg" alt="ads">
                    </div>
                                
                    <div class="col-sm-6  col-lg-6 text-left">
                            
                        <div class="container">
        
                            <br>
                            <h3 align="center">Messages</h3>
                            
                            <div style="margin-top: 2%;" class=" d-flex justify-content-center align-items-center">


                                <a style="margin-right: 2%;" class="btn btn-sm btn-outline-dark" href="messages">
                                    Received
                                </a>
                                <a class="btn btn-sm btn-outline-dark active" href="messages_sent">
                                    Sent
                                </a>


                            </div>


                            <br>
        
                            <h5 style="margin-top: 5%;" align="center">There are no messages.</h5>     
                            
                            
                        </div><br>
                                    
                    </div>
                
                <div 
                style="
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>
        
        
            </div>


        {% else %}


            <div class="container text-center">
                <br>
                <div class="row justify-content-between">     
                    <div 
                    style="
                    margin-left: -10%;" 
                    class="col-2 sidenav">
                        <img src="../static/ads/default.jpeg" alt="ads">
                    </div>
                                
                    <div class="col-sm-6  col-lg-6 text-left">
                            
                        <div class="container">
        
                            <br>
                            <h3 align="center">Messages</h3>
                            


                            <div style="margin-top: 2%;" class=" d-flex justify-content-center align-items-center">


                                <a style="margin-right: 2%;" class="btn btn-sm btn-outline-dark" href="messages">
                                    Received
                                </a>
                                <a class="btn btn-sm btn-outline-dark active" href="messages_sent">
                                    Sent
                                </a>


                            </div>


                            <br>
                            
        
                            <div class="flex-row ">
        
                                
                                {% for post in messages %}
            
                                    <table class="table table-hover">
                                        <tr>
                                            <td width="70px">
                                                <a href="{{ url_for('profile', id=post.author.id) }}">
                                                    <img src="{{url_for('static', filename='images/' + post.author.profile_pic)}}" style="width:40px; height:40px;" />
                                                </a>
                                            </td>
                                            <td>
                                                {% set user_link %}
                                                    <span class="user_popup">
                                                        <a href="{{ url_for('profile', id=post.author.id) }}">
                                                            {{ post.author.id }}
                                                        </a>
                                                    </span>
                                                {% endset %}
                                                <div class=" d-flex justify-content-between align-items-center">
                                                    <span>
                                                        <a href="{{ url_for('profile', id=post.author.id) }}">
                                                            {{post.author.first_name}} 
                                                        </a>
                                                        to
                                                        <a href="{{ url_for('profile', id=post.recipient.id) }}">
                                                            {{post.recipient.first_name}} 
                                                        </a>
                                                </span>
                                                    <span>{{(post.timestamp).day}}.{{(post.timestamp).month}}.{{(post.timestamp).year}}</span>
        
                                                </div>


                                                <div class=" d-flex justify-content-between align-items-center">
                                                    <span style="margin-right: 5%;" id="post{{ post.id }}">{{ post.body }}</span>


                                                    <div class="flex-row">
                                                        <a style="margin-top: 2%;" class="btn btn-sm btn-outline-success" href="{{ url_for('send_message',id=post.author.id) }}">
                                                            <i class="bi bi-send"></i>
                                                        </a>
                                                        <a style="margin-top: 2%;" class="btn btn-sm btn-outline-danger" href="{{ url_for('delete_message',id=post.id) }}">
                                                            <i class="bi bi-trash"></i>
                                                        </a>
                                                    </div>
                                                    
                                                </div>
                                            
                                                
                                                
                                            </td>
                                        </tr>
                                    </table>
                                {% endfor %}
                                <br>
        
                                <nav aria-label="...">
                                    <ul class="pager">
                                        <div class=" d-flex justify-content-between align-items-center">
                                            <li class="previous{% if not prev_url %} disabled{% endif %}">
                                                <a href="{{ prev_url or '#' }}">
                                                    <span aria-hidden="true">&larr;</span> Newer messages
                                                </a>
                                            </li>
                                            <li class="next{% if not next_url %} disabled{% endif %}">
                                                <a href="{{ next_url or '#' }}">
                                                    Older messages <span aria-hidden="true">&rarr;</span>
                                                </a>
                                            </li>
                                        </div>
                                    </ul>
                                </nav>
                                            
                            </div>
                            
                        </div><br>
                                    
                    </div>
                
                <div 
                style="
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>
        
        
            </div>


        {% endif %}


    


    {% endif %}


    </div>


    <script>
        console.log(moment())
    </script>


{% endblock %}













Messages.html

{% extends 'base.html' %}


{% block head %}
    <title>Messages</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}


{% endblock %}


{% block body %}


    {% if current_user.is_anonymous %}
    
        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <h3 align="center" style="margin-top: 10%;">You are being redirected to login!</h3>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>
    
    
    {% else %}


        {% if messages|length < 1 %}


            <div class="container text-center">
                <br>
                <div class="row justify-content-between">     
                    <div 
                    style="
                    margin-left: -10%;" 
                    class="col-2 sidenav">
                        <img src="../static/ads/default.jpeg" alt="ads">
                    </div>
                                
                    <div class="col-sm-6  col-lg-6 text-left">
                            
                        <div class="container">
        
                            <br>
                            <h3 align="center">Messages</h3>
                            
                            <div style="margin-top: 2%;" class=" d-flex justify-content-center align-items-center">


                                <a style="margin-right: 2%;" class="btn btn-sm btn-outline-dark active" href="messages">
                                    Received
                                </a>
                                <a class="btn btn-sm btn-outline-dark" href="messages_sent">
                                    Sent
                                </a>


                            </div>


                            <br>
        
                            <h5 style="margin-top: 5%;" align="center">There are no messages.</h5>     
                            
                            
                        </div><br>
                                    
                    </div>
                
                <div 
                style="
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>
        
        
            </div>


        {% else %}


            <div class="container text-center">
                <br>
                <div class="row justify-content-between">     
                    <div 
                    style="
                    margin-left: -10%;" 
                    class="col-2 sidenav">
                        <img src="../static/ads/default.jpeg" alt="ads">
                    </div>
                                
                    <div class="col-sm-6  col-lg-6 text-left">
                            
                        <div class="container">
        
                            <br>
                            <h3 align="center">Messages</h3>
                            


                            <div style="margin-top: 2%;" class=" d-flex justify-content-center align-items-center">


                                <a style="margin-right: 2%;" class="btn btn-sm btn-outline-dark active" href="messages">
                                    Received
                                </a>
                                <a class="btn btn-sm btn-outline-dark" href="messages_sent">
                                    Sent
                                </a>


                            </div>


                            <br>
                            
        
                            <div class="flex-row ">
        
                                
                                {% for post in messages %}
            
                                    <table class="table table-hover">
                                        <tr>
                                            <td width="70px">
                                                <a href="{{ url_for('profile', id=post.author.id) }}">
                                                    <img src="{{url_for('static', filename='images/' + post.author.profile_pic)}}" style="width:40px; height:40px;" />
                                                </a>
                                            </td>
                                            <td>
                                                {% set user_link %}
                                                    <span class="user_popup">
                                                        <a href="{{ url_for('profile', id=post.author.id) }}">
                                                            {{ post.author.id }}
                                                        </a>
                                                    </span>
                                                {% endset %}
                                                <div class=" d-flex justify-content-between align-items-center">
                                                    <span>
                                                        <a href="{{ url_for('profile', id=post.author.id) }}">
                                                            {{post.author.first_name}}
                                                        </a>
                                                </span>
                                                    <span>{{(post.timestamp).day}}.{{(post.timestamp).month}}.{{(post.timestamp).year}}</span>
        
                                                </div>


                                                <div class=" d-flex justify-content-between align-items-center">
                                                    <span style="margin-right: 5%;" id="post{{ post.id }}">{{ post.body }}</span>


                                                    <div class="flex-row">
                                                        <a style="margin-top: 2%;" class="btn btn-sm btn-outline-success" href="{{ url_for('send_message',id=post.author.id) }}">
                                                            <i class="bi bi-send"></i>
                                                        </a>
                                                        <a style="margin-top: 2%;" class="btn btn-sm btn-outline-danger" href="{{ url_for('delete_message',id=post.id) }}">
                                                            <i class="bi bi-trash"></i>
                                                        </a>
                                                    </div>
                                                    
                                                </div>
                                            
                                                
                                                
                                            </td>
                                        </tr>
                                    </table>
                                {% endfor %}
                                <br>
        
                                <nav aria-label="...">
                                    <ul class="pager">
                                        <div class=" d-flex justify-content-between align-items-center">
                                            <li class="previous{% if not prev_url %} disabled{% endif %}">
                                                <a href="{{ prev_url or '#' }}">
                                                    <span aria-hidden="true">&larr;</span> Newer messages
                                                </a>
                                            </li>
                                            <li class="next{% if not next_url %} disabled{% endif %}">
                                                <a href="{{ next_url or '#' }}">
                                                    Older messages <span aria-hidden="true">&rarr;</span>
                                                </a>
                                            </li>
                                        </div>
                                    </ul>
                                </nav>
                                            
                            </div>
                            
                        </div><br>
                                    
                    </div>
                
                <div 
                style="
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>
        
        
            </div>


        {% endif %}


    


    {% endif %}


    </div>


    <script>
        console.log(moment())
    </script>


{% endblock %}
















Post.html

{% extends 'base.html' %}


{% block head %}
    <title>{{posts.user.first_name}}'s Post</title>


{% endblock %}


{% block body %}


    
    <div class="container">
        <br>
        <div class="row justify-content-between text-center">
            
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-7  col-lg-7 text-left">
                
                    <div class="card">
                        <img class="card-img-top" src="{{url_for('static', filename='images/' + posts.post_pic)}}" alt="Card image cap">
                        <div class="card-body">
                            <div class="d-flex justify-content-between">
                                <a 
                                style="margin-bottom: 2%;" 
                                href="/profile/{{posts.user.id}}">
                                    <div class="d-flex">
                                        <img class="img-fluid" src="{{url_for('static', filename='images/' + posts.user.profile_pic)}}" alt="thumbnail" style="width:40px; height:40px">
                                        <h5 style="margin-left: 10%; margin-top: 15%;" class="card-title">{{ posts.user.first_name }}</h5>
                                    </div>
                                </a>
                            </div>
                            <p class="card-text">{{ posts.content }}</p>
                            <small> <span style="font-weight: bold;">Language(s):</span> <i> {{posts.language}} </i> </small> <br>
                            <small> <span style="font-weight: bold;">Email:</span> <i> {{posts.user.email}}</i> </small> <br>
                            <a style="margin-top: 2%;" class="btn btn-sm btn-outline-primary" 
                                href="{{ url_for('send_message',id=posts.user.id) }}">
                                                    Message
                            </a>
                        </div>
                        <div class="card-footer d-flex justify-content-between align-items-center">
                            <small class="text-muted">{{posts.location}}</small>
                            <small class="text-muted">
                                {% if (date).day - (posts.date_created).day < 1 %}
                                    {% if (date).hour - (posts.date_created).hour == 1 %}
                                        {% if (date).minute - (posts.date_created).minute < 2 %}
                                            {{(date).minute - (posts.date_created).minute}} min
                                        {% elif (date).minute - (posts.date_created).minute > 1 %}
                                            {{(date).minute - (posts.date_created).minute}} mins
                                        {% endif %}
                                    {% elif (date).hour - (posts.date_created).hour < 2 %}
                                        {{(date).hour - (posts.date_created).hour}} hour
                                    {% elif (date).hour - (posts.date_created).hour > 1 %}
                                        {{(date).hour - (posts.date_created).hour}} hours
                                    {% endif %}
                                {% elif (date).day - (posts.date_created).day == 1 %}
                                    {{(date).day - (posts.date_created).day}} day
                                {% elif (date).day - (posts.date_created).day > 1 %}
                                    {{(date).day - (posts.date_created).day}} days
                                {% endif %}
                            </small>
                        </div>
                    </div>
                    <br>
                
            </div>               
        
            <div 
            style="margin-top: 2%;
            margin-right: -10%;" 
            class="col-2 sidenav text-right">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
    
        </div>
    </div>


    
{% endblock %}
    





















Profile.html

{% extends 'base.html' %}


{% block head %}
    {% if current_user.is_authenticated %}
        <title>{{current_user.first_name}}'s Profile</title>
    {% else %}
        <title>Profile</title>
    {% endif %}
{% endblock %}


{% block body %}


    
    <br>
   
        {% if posts|length < 1 %}


            <section 
                style="background-color: rgb(238, 238, 238);
                margin-top: -3%;
                margin-bottom: -3%;">
                <div class="container py-5">
                    
                    <div class="row">
                        <div class="col">
                            <nav aria-label="breadcrumb" class="rounded-3  mb-4">
                                <ol class="breadcrumb mb-0">
                                <li class="breadcrumb-item"><a href="{{url_for('index')}}">Home</a></li>
                                <li class="breadcrumb-item active" aria-current="page">Profile</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
            
                    <div class="row">
                        <div class="col-lg-4">
                            <div class="card mb-4">
                                <div class="card-body text-center">
                                    <img src="{{url_for('static', filename='images/' + user.profile_pic)}}" alt="profile picture"
                                    class="rounded-circle img-fluid" style="width: 150px;">
                                    <div class="d-flex justify-content-center">
                                        <h5 class="my-3">{{user.first_name}} - {{age-2}}</h5>
    
                                        {% if current_user.id == user.id %}
    
                                            <div class="dropdown my-3" style="margin-left: 7px;">
                                                <i class="bi bi-gear-fill dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></i>
                                                
                                                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                    <a class="dropdown-item" href="/update-user/{{user.id}}">Update</a>
                                                    <a class="dropdown-item" href="/delete-user/{{user.id}}">Delete</a>
                                                </div>
                                            </div>
    
                                        {% endif %}
    
                                    </div>


                                    <p class="my-3">{{user.email}}</p>


                                    {% if current_user.id == user.id %}


                                    {% else %}
                                    <div class="d-flex justify-content-center mb-2">
                                        <a class="btn btn-outline-primary" 
                                        href="{{ url_for('send_message',id=user.id) }}">
                                                            Message
                                        </a>
                                    </div>


                                    {% endif %}
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-8">
                            
                            <div class="row justify-content-center">
                                            
                                <div class="col-sm-10  col-lg-10 text-left">
                                    
                                    <div class="container">
                                        <h5 style="margin-top: 5%;" align="center">There are no posts yet. <a href="{{url_for('create')}}">Create now</a></h5>     
                                    </div>
            
                                </div>               
            
                            </div>
            
                        </div> 
                        
                    </div>
                    </div>
                </div>
                </div>
            </section>
            
        {% else %}
    
            <section 
            style="background-color: rgb(238, 238, 238);
            margin-top: -3%;
            margin-bottom: -3%;">
                <div class="container py-5">
                    
                    <div class="row">
                        <div class="col">
                            <nav aria-label="breadcrumb" class="rounded-3  mb-4">
                                <ol class="breadcrumb mb-0">
                                <li class="breadcrumb-item"><a href="{{url_for('index')}}">Home</a></li>
                                <li class="breadcrumb-item active" aria-current="page">Profile</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
            
                <div class="row">
                    <div class="col-lg-4">
                        <div class="card mb-4">
                            <div class="card-body text-center">
                                <img src="{{url_for('static', filename='images/' + user.profile_pic)}}" alt="profile pic"
                                    class="rounded-circle img-fluid" style="width: 150px;">       
                                
                                <div class="d-flex justify-content-center">
                                    <h5 class="my-3">{{user.first_name}} - {{age-2}}</h5>


                                    {% if current_user.id == user.id %}


                                        <div class="dropdown my-3" style="margin-left: 7px;">
                                            <i class="bi bi-gear-fill dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></i>
                                            
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="/update-user/{{user.id}}">Update</a>
                                                <a class="dropdown-item" href="/delete-user/{{user.id}}">Delete</a>
                                            </div>
                                        </div>


                                    {% endif %}


                                </div>


                                <p class="my-1">{{user.email}}</p>


                                {% if current_user.id == user.id %}


                                {% else %}
                                <div class="d-flex justify-content-center mb-2">
                                    <a class="btn btn-outline-primary" 
                                    href="{{ url_for('send_message',id=user.id) }}">
                                                        Message
                                    </a>
                                </div>


                                {% endif %}
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-8">
                        
                        <div class="row justify-content-center">
                                        
                            <div class="col-sm-10  col-lg-10 text-left">
                                {% for post in posts %}
                                    <div class="card">
                                        <img class="card-img-top" src="{{url_for('static', filename='images/' + post.post_pic)}}" alt="Card image cap">
                                        <div class="card-body">
                                            <div class="d-flex justify-content-between">
                                                <a 
                                                style="margin-bottom: 2%;" 
                                                href="/profile/{{post.user.id}}">
                                                    <div class="d-flex">
                                                        <img class="img-fluid" src="{{url_for('static', filename='images/' + user.profile_pic)}}" alt="thumbnail" style="width:40px; height:40px;">
                                                        <h5 style="margin-left: 10%; margin-top: 15%;" class="card-title">{{ post.user.first_name }}</h5>
                                                    </div>
                                                </a>
                                                {% if current_user.id == post.user.id %}
                                                <div class="dropdown">
                                                    <i class="bi bi-gear-fill dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></i>
                                                    
                                                    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                    <a class="dropdown-item" href="/update-post/{{post.id}}">Update</a>
                                                    <a class="dropdown-item" href="/delete-post/{{post.id}}">Delete</a>
                                                    </div>
                                                </div>


                                                {% endif %}
                                                
                                            </div>
                                            <p class="card-text">
                                                {% if post.content | length > 200  %}
                                                    {{ post.content[0:200] }} ...
                                                {% else %}
                                                    {{ post.content }}
                                                {% endif %}
                                            </p>
        
                                            <div class="d-flex align-items-center justify-content-center">
                                                <a 
                                                class="btn btn-outline-secondary btn-block"
                                                href="/post/{{post.id}}">View
                                                </a>                    
                                            </div>
        
                                        </div>
        
                                        <div class="card-footer d-flex justify-content-between align-items-center">
                                            <small class="text-muted">{{post.location}}</small>
                                            <small class="text-muted">Language: {{post.language}}</small>
                                            <small class="text-muted">
                                                {% if (date).day - (post.date_created).day < 1 %}
                                                    {% if (date).hour - (post.date_created).hour == 1 %}
                                                        {% if (date).minute - (post.date_created).minute < 2 %}
                                                            {{(date).minute - (post.date_created).minute}} min
                                                        {% elif (date).minute - (post.date_created).minute > 1 %}
                                                            {{(date).minute - (post.date_created).minute}} mins
                                                        {% endif %}
                                                    {% elif (date).hour - (post.date_created).hour < 2 %}
                                                        {{(date).hour - (post.date_created).hour}} hour
                                                    {% elif (date).hour - (post.date_created).hour > 1 %}
                                                        {{(date).hour - (post.date_created).hour}} hours
                                                    {% endif %}
                                                {% elif (date).day - (post.date_created).day == 1 %}
                                                    {{(date).day - (post.date_created).day}} day
                                                {% elif (date).day - (post.date_created).day > 1 %}
                                                    {{(date).day - (post.date_created).day}} days
                                                {% endif %}
                                            </small>
                                        </div>
                                    </div>
                                    <br>
                                {% endfor %}
        
                            </div>               
        
                        </div>
        
                        <a href="#top" class="btn btn-outline-success float-right">
                            <i class="bi bi-chevron-double-up"></i>
                            Go to top
                        </a>
        
                    </div> 
                    
                {% endif %}
                        
                    </div>
                    </div>
                </div>
                </div>
            </section>
    


    
{% endblock %}





Search.html

{% extends 'base.html' %}


{% block head %}
    <title>Search</title>
{% endblock %}


{% block body %}


    {% if search == "" %}


        <div style="margin-top: 2%;" class="container text-center">
            <br>
            <div style="margin-bottom: 5%;" class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                    <h3 style="margin-top: 15%;" align="center">No result found</h3> 
                </div>               
            
                <div 
                style="margin-top: 2%;
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>


            </div>
            <br>
        </div> 


    {% elif result.items == [] %}


        <div style="margin-top: 2%;" class="container text-center">
            <br>
            <div style="margin-bottom: 5%;" class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                    <h3 style="margin-top: 15%;" align="center">No result found for {{search}}</h3>
                </div>               
            
                <div 
                style="margin-top: 2%;
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>


            </div>
            <br>
        </div> 
            
    {% else %}
        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                    {% for post, user in result.items %}
                        <div class="card">
                            <img class="card-img-top" src="{{url_for('static', filename='images/' + post.post_pic)}}" alt="Card image cap">
                            <div class="card-body">
                                <div class="d-flex justify-content-between">
                                    <a 
                                    style="margin-bottom: 2%;" 
                                    href="/profile/{{post.user.id}}">
                                        <div class="d-flex">
                                            <img class="img-fluid" src="{{url_for('static', filename='images/' + user.profile_pic)}}" alt="thumbnail" style="width:40px; height:40px;">
                                            <h5 style="margin-left: 10%; margin-top: 15%;" class="card-title">{{ post.user.first_name }}</h5>
                                        </div>
                                    </a>
                                </div>
                                
                                <p class="card-text">
                                    {% if post.content | length > 200  %}
                                        {{ post.content[0:200] }} ...
                                    {% else %}
                                        {{ post.content }}
                                    {% endif %}
                                </p>
                                <div class="d-flex align-items-center justify-content-center">
                                    <a 
                                    class="btn btn-outline-secondary btn-block"
                                    href="/post/{{post.id}}">View
                                    </a>                    
                                </div>
                            </div>
                            <div class="card-footer d-flex justify-content-between align-items-center">
                                <small class="text-muted">{{post.location}}</small>
                                <small class="text-muted">
                                    {% if post.language | length > 20  %}
                                        Language: {{ post.language[0:20] }} ...
                                    {% else %}
                                        Language: {{ post.language }}
                                    {% endif %}
                                </small>
                                <small class="text-muted">
                                    {% if (date).day - (post.date_created).day < 1 %}
                                        {% if (date).hour - (post.date_created).hour == 1 %}
                                            {% if (date).minute - (post.date_created).minute < 2 %}
                                                {{(date).minute - (post.date_created).minute}} min
                                            {% elif (date).minute - (post.date_created).minute > 1 %}
                                                {{(date).minute - (post.date_created).minute}} mins
                                            {% endif %}
                                        {% elif (date).hour - (post.date_created).hour < 2 %}
                                            {{(date).hour - (post.date_created).hour}} hour
                                        {% elif (date).hour - (post.date_created).hour > 1 %}
                                            {{(date).hour - (post.date_created).hour}} hours
                                        {% endif %}
                                    {% elif (date).day - (post.date_created).day == 1 %}
                                        {{(date).day - (post.date_created).day}} day
                                    {% elif (date).day - (post.date_created).day > 1 %}
                                        {{(date).day - (post.date_created).day}} days
                                    {% endif %}
                                </small>
                            </div>
                        </div>
                        <br>
                    {% endfor %}


                    {% for page_num in result.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2) %}
                        {% if page_num %}
                            {% if result.page == page_num %}
                                <a class="btn btn-outline-dark mb-4 active" href="{{url_for('search', page=page_num)}}">{{page_num}}</a>
                            {% else %}
                                <a class="btn btn-outline-dark mb-4" href="{{url_for('search', page=page_num)}}">{{page_num}}</a>
                            {% endif %}
                        {% else %}
                            ...
                        {% endif %}
                    {% endfor %}
                </div>               
            
                <div 
                style="margin-top: 2%;
                margin-right: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default_3.jpeg" alt="ads">
                </div>


            </div>


            <a href="#top" class="btn btn-outline-success float-right">
                <i class="bi bi-chevron-double-up"></i>
                Go to top
            </a>
            <br>


        </div> 
    {% endif %}
        


{% endblock %}





















Send_message.html

{% extends 'base.html' %}


{% block head %}
    <title>Messages</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}


{% endblock %}


{% block body %}


    {% if current_user.is_anonymous %}
    
        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <h3 align="center" style="margin-top: 10%;">You are being redirected to login!</h3>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>
    
    
    {% else %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                    
                <div class="container">


                    <br>
                    <h3 align="center">Messages</h3>
                    <br>


                    <div class="d-flex justify-content-center">


                        <form action="/send_message/{{user.id}}" method="POST">


                            <h5> Send Message to {{user.first_name}}</h5>
                            
                            <div class="form-row">
            
                                <div class="form-group">
                                    <label for="message">Message</label>
                                    <textarea class="form-control" placeholder="Message" name="message" id="message" cols="30" rows="10"></textarea>
                                </div>


                            </div>


                            <input class="btn btn-outline-success" type="submit" value="Send"></input>


                        </form>
                        
                    </div>
                    
                </div><br>
                            
            </div>
        
        <div 
        style="
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>


    {% endif %}


    </div>


{% endblock %}























Signup.html

{% extends 'base.html' %}


{% block head %}
    <title>Sing Up</title>
    {% if current_user.is_authenticated %}
        <meta http-equiv="REFRESH" content="4; profile/{{current_user.id}}">
    {% endif %}


{% endblock %}


{% block body %}


    {% if current_user.is_authenticated %}
    
        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <h3 align="center" style="margin-top: 10%;">Hi {{ current_user.first_name }}! You are being redirected to your profile!</h3>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>
    
    
    {% else %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="
            margin-left: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                    
                <div class="container">


                    <br>
                    <h3 align="center">Sign Up</h3>
                    <br>


                    <div class="d-flex justify-content-center">
                        <!-- form design is from bootstrap https://getbootstrap.com/docs/5.0/forms/overview/-->
                        <form action="/signup" method="POST" enctype="multipart/form-data">
                            
                            <div class="form-row">


                                <div class="form-group col-md-4 mb-3">
                                    <label for="fname">First name</label>
                                    <input class="form-control" type="text" id="fname" name="fname" placeholder="First Name">
                                </div>


                                <div class="form-group col-md-4 mb-3">
                                    <label for="lname">Last name</label>
                                    <input class="form-control" type="text" id="lname" name="lname" placeholder="Last Name">
                                </div>


                                <div class="form-group col-md-4 mb-3">
                                    <label for="mail">Email</label>
                                    <input class="form-control" type="email" id="mail" name="mail" placeholder="Email">
                                </div>


                            </div>


                            <div class="form-row">
                                
                                <div class="form-group col-md-4 mb-3">
                                    <label for="pwd">Password</label>
                                    <input class="form-control" type="password" id="pwd" name="pwd" placeholder="Password">
                                </div>


                                <div class="form-group col-md-4 mb-3">
                                    <label for="pwd2">Confirm Password</label>
                                    <input class="form-control" type="password" id="pwd2" name="pwd2" placeholder="Confirm Password">
                                </div>
                            
                            </div>


                            <div class="form-row">


                                <div class="form-group col-md-4 mb-3">
                                    <label for="age">Date of Birth</label>
                                    <input 
                                    class="form-control" 
                                    type="date" 
                                    id="age" 
                                    name="age"
                                    >
                                </div>


                            </div>


                            


                            <div class="form-row">
                                <span style="margin-left: 1%;">Profile Photo</span><br>
                                <div 
                                style="margin-top: 2%; margin-right: 1%; margin-left: 1%;" 
                                class="input-group row-md-6 mb-3">
                                <input 
                                type="file" 
                                class="custom-file-input" 
                                id="profile_pic" 
                                name="profile_pic"
                                accept=".jpg, .jpeg, .png"
                                required>
                                <label class="custom-file-label" for="profile_pic">Upload Profile Photo</label>
                                </div>
            
                            </div>
            


                            <div style="margin-top: 1%;" class="form-row">


                                <div style="margin-left: 1%;" class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="T&C" name="T&C" required>
                                <label class="form-check-label" for="T&C">
                                    Agree to terms and conditions
                                </label>
                                </div>


                            </div>


                            <br>
                            
                            <input class="btn btn-outline-success" type="submit" value="Register"></input>
                        </form>
                    </div>
                    
                </div><br>


                <h5 align="center">Already have an account? <a href="{{url_for('login')}}"> Sign in!</a></h5>
                            
            </div>


        <div 
        style="
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>


    {% endif %}


    </div>


{% endblock %}






























Update-post.html

{% extends 'base.html' %}


{% block head %}
    <title>Update Post</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}
{% endblock %}


{% block body %}


    {% if current_user.is_authenticated %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav text-left">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-12  col-lg-6 text-left">
                    
                
                    <br>
                    <h3 align="center">Update Ad</h3>
                    <br>
            
                    <div class="d-row justify-content-center">
                        <!-- form design is from bootstrap https://getbootstrap.com/docs/5.0/forms/overview/-->
                        <form action="/update-post/{{posts.id}}" method="POST" enctype="multipart/form-data">
                                
                            <div class="form-row">
            
                                <span>I am in</span>
                                <select style="margin-left: 5px;" name="location"
                                class="form-select form-select-lg mb-3" 
                                aria-label="Default select example">
                                    <option value="{{posts.location}}">{{posts.location}}</option>
                                    <option value="Antrim">Antrim</option>
                                    <option value="Armagh">Armagh</option>
                                    <option value="Carlow">Carlow</option>
                                    <option value="Cavan">Cavan</option>
                                    <option value="Clare">Clare</option>
                                    <option value="Cork">Cork</option>
                                    <option value="Derry">Derry</option>
                                    <option value="Donegal">Donegal</option>
                                    <option value="Down">Down</option>
                                    <option value="Dublin">Dublin</option>
                                    <option value="Fermanagh">Fermanagh</option>
                                    <option value="Galway">Galway</option>
                                    <option value="Kerry">Kerry</option>
                                    <option value="Kildare">Kildare</option>
                                    <option value="Kilkenny">Kilkenny</option>
                                    <option value="Laois">Laois</option>
                                    <option value="Leitrim">Leitrim</option>
                                    <option value="Limerick">Limerick</option>
                                    <option value="Longford">Longford</option>
                                    <option value="Louth">Louth</option>
                                    <option value="Mayo">Mayo</option>
                                    <option value="Meath">Meath</option>
                                    <option value="Monaghan">Monaghan</option>
                                    <option value="Offaly">Offaly</option>
                                    <option value="Roscommon">Roscommon</option>
                                    <option value="Sligo">Sligo</option>
                                    <option value="Tipperary">Tipperary</option>
                                    <option value="Tyrone">Tyrone</option>
                                    <option value="Waterford">Waterford</option>
                                    <option value="Westmeath">Westmeath</option>
                                    <option value="Wexford">Wexford</option>
                                    <option value="Wicklow">Wicklow</option>
                                </select>
            
                            </div>
            
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="lang">I speak</label>
                                    <input class="form-control" 
                                    type="text" 
                                    id="lang" 
                                    name="lang" 
                                    placeholder="Language(s)"
                                    value="{{posts.language}}">
                                </div>
            
                            </div>
            
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="content">Content</label><br>
                                    <textarea id="content" name="content" rows="5" cols="34">{{posts.content}}
                                    </textarea><br>
                                </div>
            
                            </div>


                            <div class="form-row">
                                <span style="margin-left: 1%;">Post Photo</span><br>
                                <div 
                                style="margin-top: 2%; margin-right: 1%; margin-left: 1%;" 
                                class="input-group row-md-6 mb-3">
                                    <input 
                                    type="file" 
                                    class="custom-file-input" 
                                    id="post_pic" 
                                    name="post_pic"
                                    accept=".jpg, .jpeg, .png"
                                    required>
                                    <label class="custom-file-label" for="post_pic">                                    
                                        {{post_picture}}
                                    </label>
                                </div>
            
                            </div>
                            
                            <input class="btn btn-outline-success" type="submit" value="Update"></input>
                        </form>
                    </div>
                    
                <br>
                            
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>
    
       
    {% else %}


        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <br>
                        <h3 align="center" style="margin-top: 10%;">You are being redirected to log in!</h3>
                    <br>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-right: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>


    {% endif %}
    
    </div>
    
{% endblock %}



















Update-user.html

{% extends 'base.html' %}


{% block head %}
    <title>Update User Info</title>
    {% if current_user.is_anonymous %}
        <meta http-equiv="REFRESH" content="4; login">
    {% endif %}
{% endblock %}


{% block body %}


    {% if current_user.is_authenticated %}


    <div class="container text-center">
        <br>
        <div class="row justify-content-between">     
            <div 
            style="margin-top: 2%;
            margin-left: -10%;" 
            class="col-2 sidenav text-left">
                <img src="../static/ads/default.jpeg" alt="ads">
            </div>
                        
            <div class="col-sm-6  col-lg-6 text-left">
                    
                <div class="container">
                    <br>
                    <h3 align="center">Update User Info</h3>
                    <br>
            
                    <div class="d-flex justify-content-center">
                        <!-- form design is from bootstrap https://getbootstrap.com/docs/5.0/forms/overview/-->
                        <form action="/update-user/{{user.id}}" method="POST" enctype="multipart/form-data">
                                
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="fname">First name</label>
                                    <input class="form-control" type="text" id="fname" name="fname" placeholder="First Name" value="{{user.first_name}}">
                                </div>
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="lname">Last name</label>
                                    <input class="form-control" type="text" id="lname" name="lname" placeholder="Last Name" value="{{user.last_name}}">
                                </div>
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="mail">Email</label>
                                    <input class="form-control" type="email" id="mail" name="mail" placeholder="Email" value="{{user.email}}">
                                </div>
            
                            </div>
            
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="current_pwd">Current Password</label>
                                    <input class="form-control" type="password" id="current_pwd" name="current_pwd" placeholder="Current Password">
                                </div>
                                
                                <div class="form-group col-md-4 mb-3">
                                    <label for="pwd">New Password</label>
                                    <input class="form-control" type="password" id="pwd" name="pwd" placeholder="Password">
                                </div>
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="pwd2">Confirm New Password</label>
                                    <input class="form-control" type="password" id="pwd2" name="pwd2" placeholder="Confirm Password">
                                </div>
                            
                            </div>
            
                            <div class="form-row">
            
                                <div class="form-group col-md-4 mb-3">
                                    <label for="age">Date of Birth</label>
                                    <input 
                                    class="form-control" 
                                    type="date" 
                                    id="age" 
                                    name="age"
                                    value="{{user.age}}"
                                    >
                                </div>
            
                            </div>
            
                            <div class="form-row">
                                <span style="margin-left: 1%;">Profile Photo</span><br>
                                <div 
                                style="margin-top: 2%; margin-right: 1%; margin-left: 1%;" 
                                class="input-group row-md-6 mb-3">
                                    <input 
                                    type="file" 
                                    class="custom-file-input" 
                                    id="profile_pic" 
                                    name="profile_pic"
                                    accept=".jpg, .jpeg, .png"
                                    required>
                                    <label class="custom-file-label" for="profile_pic">                                    
                                        {{pic}}
                                    </label>
                                </div>
            
                            </div>
            
                            <br>
                            
                            <input class="btn btn-outline-success" type="submit" value="Update"></input>
                        </form>
                    </div>
                    
                </div><br>
                            
            </div>


        <div 
        style="margin-top: 2%;
        margin-right: -10%;" 
        class="col-2 sidenav">
            <img src="../static/ads/default_3.jpeg" alt="ads">
        </div>


    </div>
 
       
    {% else %}


        <div class="container text-center">
            <br>
            <div class="row justify-content-between">     
                <div 
                style="margin-top: 2%;
                margin-left: -10%;" 
                class="col-2 sidenav">
                    <img src="../static/ads/default.jpeg" alt="ads">
                </div>
                            
                <div class="col-sm-6  col-lg-6 text-left">
                        
                    <br>
                        <h3 align="center" style="margin-top: 10%;">You are being redirected to log in!</h3>
                    <br>
                    
                </div>


            <div 
            style="margin-top: 2%;
            margin-right: -10%;" 
            class="col-2 sidenav">
                <img src="../static/ads/default_3.jpeg" alt="ads">
            </div>


        </div>


    {% endif %}
    
    </div>
    
{% endblock %}

