#-*- coding: utf-8 -*-

from odoo import http, Command

class FreelancerController(http.Controller):

    @http.route(['/projects', '/filtered_projects', '/filtered_projects/page/<int:page>', '/projects/page/<int:page>'], type='http', auth="public", website=True)
    def freelancer_details(self, page=1, name=None, **kwargs):
        domain = [('state', 'not in', ['sold', 'canceled'])]

        # Filtering projects by available date.
        if name:
            domain.append(('client_id.name', '=', name))
            url = '/filtered_projects'
        else:
            url = '/projects'

        # Implementing Pagination using website.pager.
        page = int(page)
        projects_per_page = 6
        Project = http.request.env['freelancer.project']
        total_projects = Project.search_count(domain)
        total_pages = (total_projects + projects_per_page - 1) // projects_per_page
        projects = Project.search(domain, limit=projects_per_page, offset=(page - 1) * projects_per_page)
        clients = http.request.env['freelancer.client'].search([])

        pager = http.request.website.pager(
            url=url,
            total=total_projects,
            page=page,
            step=projects_per_page,
            scope=total_pages,
        )

        return http.request.render('Freelancing.website_projects_page',{
            'projects': projects,
            'pager': pager,
            'clients': clients,
        })
    
    @http.route('/projects/<model("freelancer.project"):project_id>', type='http', auth="public", website=True)
    def property_details(self, project_id, **kw):
        return http.request.render('Freelancing.project_details_template', {'project': project_id})
    
    @http.route(['/place_bid/<int:project_id>'], type='http', auth="public", website=True)
    def form_bids(self, project_id=None, **kw):
        freelancer = http.request.env['freelancer.freelancer'].search([])
        project = http.request.env['freelancer.project'].browse(project_id)
        return http.request.render('Freelancing.website_bids_page', {
            'project': project,
            'freelancer': freelancer
        })
    
    @http.route(['/bid_placed/<int:project_id>'], type='http', auth="public", website=True)
    def place_bids(self, project_id=None, **kw):

        freelancer_id = kw.get('freelancer_id')
        email= kw.get('email')
        mobile = kw.get('mobile')
        bid_ammount = kw.get('bid_ammount')
        description = kw.get('description')

        project = http.request.env['freelancer.project'].browse(project_id)
        freelancer = http.request.env['freelancer.freelancer']

        project.write({
            'bid_ids': [
                Command.create({
                    'freelancer_id': freelancer_id,
                    'bid_amount': bid_ammount,
                    'bid_description': description,
                })
            ]
        })

        return http.request.render('Freelancing.website_thank_you_page', {'project_id': project_id})
    