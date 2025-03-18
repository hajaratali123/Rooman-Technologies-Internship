 
from flask import Blueprint, render_template, redirect, url_for, request
from .models import db, Student
from .forms import StudentForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@main.route('/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        new_student = Student(name=form.name.data, email=form.email.data, age=form.age.data)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_student.html', form=form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        student.email = form.email.data
        student.age = form.age.data
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_student.html', form=form)

@main.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('main.index'))
