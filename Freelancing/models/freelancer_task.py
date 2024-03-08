#-*- coding: utf-8 -*-

from odoo import api, fields, models

class Task(models.Model):
    _name = 'freelancer.task'
    _description = 'Project Task'

    name = fields.Char(string='Task Name', required=True)
    client_id = fields.Char(related="project_id.client_id.name", string='Client', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('freelancer.project', string='Project', required=True)
    deadline = fields.Datetime(string='Deadline', required=True)
    today = fields.Datetime.now()
    remaining_days = fields.Integer(string='Remaining Days', compute='_compute_remaining_days')
    deadline_check = fields.Char(string='Deadline Check', compute='_compute_deadline_check')
    label_days = fields.Char(string='Use Days', default='Days')
    color = fields.Integer(string='Color')
    assigned_to = fields.Many2one('freelancer.freelancer', string='Assigned To', required=True)
    tag_ids = fields.Many2many('freelancer.tags',string='Tags')
    task_count = fields.Integer(default=1)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'Progress'), 
        ('completed', 'Completed')], default='new', string='Status')

    @api.onchange('deadline', 'today')
    def _compute_remaining_days(self):
        for task in self:
            task.remaining_days = 0 if task.status == 'completed' else (task.deadline - fields.Datetime.now()).days

    @api.onchange('remaining_days')
    def _compute_deadline_check(self):
        for task in self:
            if task.remaining_days < 0:
                task.deadline_check = 'Overdue'
            elif task.remaining_days < 1:
                task.deadline_check = 'Due Soon'
            else:
                task.deadline_check = 'Due'

    def action_task_completed(self):
        self.status = 'completed'

    def action_task_started(self):
        self.status = 'in_progress'

    
        