# -*- coding: utf-8 -*-

from openerp import models, fields, api

class school(models.Model):
    _name = 'school.school'
    name = fields.Char(required=True)

class Student(models.Model):
    _name = 'school.student'
    name = fields.Char(required=True)
    age = fields.Integer (required=True)
    gender = fields.Selection([
         ('male', "Male"),
         ('female', 'Female'),
    ], default="male",
    required=True)
    photo = fields.Binary("Image")
    student_class = fields.Many2one("school.class",  ondelete='cascade', string="Class", required=True)
    user = fields.Many2one("res.users",  ondelete='cascade', string="User", required=True)

class Course(models.Model):
    _name = 'school.course'
    name = fields.Char(required=True)
    starts_at = fields.Date(required=True)
    ends_at = fields.Date(required=True)
    book = fields.Binary(required=True)
    photo = fields.Binary("Image", required=True)
    course_class = fields.Many2one("school.class",  ondelete='cascade', string="Class", required=True)


class Class(models.Model):
    _name = 'school.class'
    name = fields.Char(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Integer()
    grades = fields.Float(required=True)
    courses = fields.Many2many("school.course",  ondelete='cascade', string="Course")




