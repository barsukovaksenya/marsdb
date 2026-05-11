import datetime
from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.news import News
from data.jobs import Jobs
from forms.user import RegisterForm
from data.db_session import global_init, create_session


db_session.global_init("db/mars_explorer.db")
db_sess = db_session.create_session()

# user1 = User()
# user1.name = "Пользователь 1"
# user1.about = "биография пользователя 1"
# user1.email = "email1@email.ru"
# db_sess = db_session.create_session()
# db_sess.add(user1)
# db_sess.commit()
#
# user2 = User()
# user2.name = "Пользователь 2"
# user2.about = "биография пользователя 2"
# user2.email = "email2@email.ru"
# db_sess.add(user2)
# db_sess.commit()
#
# user3 = User()
# user3.name = "Пользователь 3"
# user3.about = "биография пользователя 3"
# user3.email = "email3@email.ru"
# db_sess.add(user3)
# db_sess.commit()

# user = db_sess.query(User).first()
# print(user.name)

# for user in db_sess.query(User).all():
#     print(user)

# for user in db_sess.query(User).filter(
#     User.id > 1, User.email.notilike("%1%")
# ):
#     print(user)

# for user in db_sess.query(User).filter(
#     (User.id > 1) | (User.email.notilike("%1%"))
# ):
#     print(user)

# user = db_sess.query(User).filter(User.id == 1).first()
# print(user)
# user.name = "Измененное имя пользователя"
# user.created_date = datetime.datetime.now()
# db_sess.commit()

# db_sess.query(User).filter(User.id >= 3).delete()
# db_sess.commit()
#
# user = db_sess.query(User).filter(User.id == 2).first()
# db_sess.delete(user)
# db_sess.commit()

# news = News(
#     title="Первая новость",
#     content="Привет блог!",
#     user_id=1, is_private=False
# )
# db_sess.add(news)
# db_sess.commit()

# user = db_sess.query(User).filter(User.id == 1).first()
# news = News(
#     title="Вторая новость",
#     content="Уже вторая запись!",
#     user=user, is_private=False
# )
# db_sess.add(news)
# db_sess.commit()

# user = db_sess.query(User).filter(User.id == 1).first()
# news = News(
#     title="Личная запись",
#     content="Эта запись личная",
#     is_private=True
# )
# user.news.append(news)
# db_sess.commit()

# for news in user.news:
#     print(news)

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Scott1"
user.name = "Ridley1"
user.age = 11
user.position = "colonist"
user.speciality = "research1middle"
user.address = "module_1"
user.email = "scott1@mars.org"
user.hashed_password = "cap1"
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Scott2"
user.name = "Ridley2"
user.age = 2
user.position = "colonist2"
user.speciality = "research chief engineer2"
user.address = "module_12"
user.email = "scott2@mars.org"
user.hashed_password = "cap2"
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Scott3"
user.name = "Ridley3"
user.age = 213
user.position = "colonist3chief"
user.speciality = "research3"
user.address = "module_1"
user.email = "scott3@mars.org"
user.hashed_password = "cap3"
db_sess.add(user)
db_sess.commit()

job = Jobs()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = "2, 3"
job.start_date = datetime.datetime.now()
job.is_finished = False
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 2
job.job = "exploration of mineral resources"
job.work_size = 9
job.collaborators = "4, 3"
job.start_date = datetime.datetime.now()
job.is_finished = False
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 3
job.job = "development of a management system"
job.work_size = 2
job.collaborators = "5"
job.start_date = datetime.datetime.now()
job.is_finished = False
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 4
job.job = "water supply setup"
job.work_size = 10
job.collaborators = "1, 2"
job.start_date = datetime.datetime.now()
job.is_finished = True
db_sess.add(job)
db_sess.commit()

# db_name = input()
# global_init(db_name)
# db_sess = create_session()

# for user in db_sess.query(User).filter(User.address == "module_1"):
#     print(user)

# db_name = input()
# global_init(db_name)
# db_sess = create_session()
#
# for user in db_sess.query(User).filter(
#     User.address == "module_1",
#     User.speciality.notlike("%engineer%"),
#     User.position.notlike("%engineer%")
# ):
#     print(user.id)

# db_name = input()
# global_init(db_name)
# db_sess = create_session()
#
# for user in db_sess.query(User).filter(User.age < 18):
#     print(f"<Colonist> {user.id} {user.surname} {user.name} {user.age} years")

# db_name = input()
# global_init(db_name)
# db_sess = create_session()
#
# for user in db_sess.query(User).filter(
#     (User.position.like("%chief%")) | (User.position.like("%middle%"))
# ):
#     print(f"<Colonist> {user.id} {user.surname} {user.name} {user.position}")

# db_name = input()
# global_init(db_name)
# db_sess = create_session()
#
# for job in db_sess.query(Jobs).filter(
#     Jobs.work_size < 20,
#     Jobs.is_finished != True
# ):
#     print(job)




# db_name = input()
# global_init(db_name)
# db_sess = create_session()
#
# jobs = db_sess.query(Jobs).all()
#
# max_size = 0
# for job in jobs:
#     count = len(job.collaborators.split(", "))
#     if count > max_size:
#         max_size = count
#
# printed = set()
# for job in jobs:
#     count = len(job.collaborators.split(", "))
#     if count == max_size and job.team_leader not in printed:
#         printed.add(job.team_leader)
#         user = db_sess.query(User).filter(
#             User.id == job.team_leader
#         ).first()
#         print(f"{user.name} {user.surname}")

# db_name = input()
# global_init(db_name)
# db_sess = create_session()
#
# printed = set()
# for user in db_sess.query(User).filter(
#     User.address == "module_1",
#     User.age < 21
# ):
#     if user.id not in printed:
#         printed.add(user.id)
#         print(f"<Colonist> {user.id} {user.surname} {user.name}")
#         user.address = "module_3"
#         db_sess.commit()
#
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()




@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).filter(News.is_private != True)
#     return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template(
                'register.html', title='Регистрация',
                form=form, message="Пароли не совпадают"
            )
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(
            User.email == form.email.data
        ).first():
            return render_template(
                'register.html', title='Регистрация',
                form=form, message="Такой пользователь уже есть"
            )
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template(
        'register.html', title='Регистрация', form=form
    )


if __name__ == '__main__':
    main()