# -*- coding: utf-8 -*-
{
    'name': "Task Fibonacci",  # Module title
    'summary': "Select a Fibonacci level",  # Module subtitle phrase
    'description': """
Manage Tasks
==============
Description related to Fibonacci.
    """,  # Supports reStructuredText(RST) format
    'author': "Ragiant",
    'website': "https://ragiant.com.ar/#!/-home/",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base', 'project'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/add_fibonacci.xml',
    ],
}