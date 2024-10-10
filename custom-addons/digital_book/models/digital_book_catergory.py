from odoo import api, fields, models


class EmployeeDigitalBookCategory(models.Model):
    _name = "employee.digital.book.category"
    _description = "Employee Digital Book Category"
    _sql_constraints = [
        (
            "check_name",
            "UNIQUE(name)",
            "Category name must be unique",
        ),
    ]

    name = fields.Char(string="Category Name", required=True)
