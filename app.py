from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Department, Employee, get_directory, get_directory_join, get_directory_join_class, get_directory_all_join, Project, EmployeeProject
from forms import AddSnackForm, EmployeeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """Render home page"""
    return render_template("home.html")


@app.route('/phones')
def list_phones():
    """Renders directory of employees and phone numbers  (from dept)"""

    # Get all employees from employees_db database
    emps = Employee.query.all()
    return render_template('phones.html', emps=emps)


# Show form and handle form
@app.route('/snacks/new', methods=["GET", "POST"])
def add_snack():
    """Renders snack form (GET) or handles snack form submission (POST)"""

    # Get the appropriate form from forms.py
    form = AddSnackForm()

    # For POST request
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"Created new snack: name is {name}, price is ${price}")
        return redirect('/')
    else:
        return render_template("add_snack_form.html", form=form)


# Show a form to add new employee and handle form to add new employee
@ app.route('/employees/new', methods=["GET", "POST"])
def add_employee():
    """Show a form to add new employee and handle form to add new employee"""
    # Get the appropriate form from forms.py
    form = EmployeeForm()

    # Make options for select input
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts

    # For POST request
    if form.validate_on_submit():
        emp = Employee(name=form.name.data, state=form.state.data,
                       dept_code=form.dept_code.data)
        db.session.add(emp)
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('add_employee_form.html', form=form)


# Show form to edit employee and handle form to update existing employee
@ app.route('/employees/<int:id>/edit', methods=["GET", "POST"])
def edit_employee(id):
    """Show form to edit employee and handle form to update existing employee"""
    # Get employee based on input id
    emp = Employee.query.get_or_404(id)

    # Get the appropriate form from forms.py and re-pupolate the fields on HTML
    form = EmployeeForm(obj=emp)

    # Make options for select input
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts

    # For POST request
    if form.validate_on_submit():
        # Update employee, get data from the form
        emp.name = form.name.data
        emp.state = form.state.data
        emp.dept_code = form.dept_code.data
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template("edit_employee_form.html", form=form, emp=emp)
