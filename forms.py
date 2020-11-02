
# We can define many forms in form.py file and show it in an appropriate templates.
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


# Define Snacks Form
class AddSnackForm(FlaskForm):
    email = StringField("Email", validators=[Optional(), Email()])
    name = StringField("Snack Name", validators=[
                       InputRequired(message="Snack Name can't be blank")])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    is_healthy = BooleanField("This is a healthy snack")

    # Radio: shows list <ul>
    # category = RadioField("Category", choices=[
    #                       ('ic', 'Ice Cream'),  ('chips', 'Potato Chips'),  ('candy', 'Candy/Sweets')])

    # Select: shows dropdown button
    category = SelectField("Category", choices=[
                          ('ic', 'Ice Cream'),  ('chips', 'Potato Chips'),  ('candy', 'Candy/Sweets')])


# Define Employee Form
class EmployeeForm(FlaskForm):
    name = StringField("Employee Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    # Choices: list of tuple
    state = SelectField('State', choices=[(st, st) for st in states])
    # We can set choices dynamically in View Function at app.py
    dept_code = SelectField("Department Code")
