from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
import mimetypes


class EmployeeDigitalBook(models.Model):
    _name = "employee.digital.book"
    _description = "Employee Digital Book"
    _order = "create_date desc"

    title = fields.Char(string="Document Title", required=True)
    # fields.Selection(
    # string="Document Type",
    #    required=True,
    #    selection=[
    #        ("application/pdf", "PDF"),
    #        ("application/msword", "DOC"),
    #        ("application/vnd.openxmlformats-officedocument.wordprocessingml.document", "DOCX"),
    #        ("text/csv", "CSV"),
    #    ])
    type_id = fields.Many2one("employee.digital.book.type", string="Document Type", ondelete='set null')
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True, ondelete='cascade')
    category_id = fields.Many2one("employee.digital.book.category", string="Category", ondelete='set null')
    attachment = fields.Binary(string="Attachment", copy=False, required=True)
    file_name = fields.Char(string="File name", copy=False)

    @api.constrains('attachment')
    def _check_extension(self):
        for record in self:
            mime_type = mimetypes.guess_type(record.file_name)[0]
            if mime_type != record.type_id.file_type:
                raise ValidationError("Invalid file type")

    @api.constrains("type_id", "category_id")
    def _check_related_required_fields(self):
        for record in self:
            if not record.type_id:
                raise ValidationError("Document type is required")
            if not record.category_id:
                raise ValidationError("Document category is required")
