{
    "name": "Employee Digital Book",
    "version": "1.0",
    "depends": ["hr"],
    "author": "Faiyaz",
    "category": "Digital Book",
    "description": """
    A module in BJIT ERP named Employee Digital Bookin which all the employees' documents can be stored. It's an alternative optionof our current file management system of keeping hardcopies. Instead, we’ll should be able to upload all the filesin the Employee Digital Book and can view, export, andprint anytime.
""",
    # data files always loaded at installation
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/employee_digital_book_type.xml",
        "views/employee_digital_book_category.xml",
        "views/employee_digital_book_view.xml",
        "views/employee_digital_book_menu.xml",
    ],
    # data files containing optionally loaded demonstration data
    "demo": [
        # 'demo/demo_data.xml',
    ],
}
