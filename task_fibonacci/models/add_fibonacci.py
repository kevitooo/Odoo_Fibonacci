# -*- coding: utf-8 -*-

from odoo import models, fields


class AddFibonacci(models.Model):
    _name = 'add.fibonacci'

    task_id = fields.Many2one('project.task')


class TaskProject(models.Model):
    _inherit = 'project.task'

    fibonacci_lvl = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), (
        '4', '5'), ('5', '8'), ('6', '13'), ('7', '21')], string='Puntos de historia')
