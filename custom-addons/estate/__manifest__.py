{
    "name": "Estate module",
    "version": "1.0",
    "depends": ["base", "web"],
    "author": "Faiyaz",
    "category": "Real Estate",
    "description": """
    Description text
    """,
    # data files always loaded at installation
    "data": [
        #'views/mymodule_view.xml',
        "security/ir.model.access.csv",
        "views/estate_property_offer_view.xml",
        "views/estate_property_tag_view.xml",
        "views/estate_property_type_view.xml",
        "views/estate_property_view.xml",
        "views/res_users_view.xml",
        "views/estate_menus.xml",
        "report/estate_report_views.xml",
        "report/estate_reports.xml",
    ],
    # data files containing optionally loaded demonstration data
    "demo": [
        #'demo/demo_data.xml',
    ],
    "images": ["static/description/icon.png"],
}
