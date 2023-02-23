{
    'name': "Travel & Hospitality",
    'version': '1.0',
    'depends': ['base'],
    'author': "Surabhi Varma",
    'category': 'Category',
     'license': 'LGPL-3',

    'description': """
    Description text
    """,

    'depends': ['base_address_extended'],


    'data': [
        "security/ir.model.access.csv",
        "views/host_details_views.xml",
        "views/place_details_views.xml",
        "views/travel_booking_views.xml",
        "views/travel_transport_views.xml",
        "views/travel_place_types_views.xml",
        "views/travel_facilites_views.xml",
        "views/place_menus.xml"
           
    ],
    
    'application':True


}
