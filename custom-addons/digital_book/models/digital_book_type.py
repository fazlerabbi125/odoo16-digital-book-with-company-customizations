from odoo import api, fields, models


class EmployeeDigitalBookType(models.Model):
    _name = "employee.digital.book.type"
    _description = "Employee Digital Book Type"
    _sql_constraints = [
        (
            "check_name",
            "UNIQUE(name)",
            "Category name must be unique",
        ),
        (
            "check_mime_type",
            "UNIQUE(mime_type)",
            "Mime type must be unique",
        ),
    ]

    name = fields.Char(string="Name", required=True)
    file_type = fields.Char(string="Mime Type", required=True)
