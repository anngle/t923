# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import User





        