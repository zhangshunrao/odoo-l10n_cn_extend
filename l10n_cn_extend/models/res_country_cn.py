# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


def location_name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
    if not args:
        args = []

    ids = []
    if len(name) == 2:
        ids = self.search(cr, user, [('code', 'ilike', name)] + args,
                          limit=limit, context=context)

    search_domain = [('name', operator, name)]
    if ids:
        search_domain.append(('id', 'not in', ids))
    ids.extend(self.search(cr, user, search_domain + args,
                           limit=limit, context=context))

    locations = self.name_get(cr, user, ids, context)
    return sorted(locations, key=lambda (id, name): ids.index(id))


class Country(osv.osv):
    _inherit = 'res.country'

    _columns = {
        'state_ids': fields.one2many('res.country.state', 'country_id', string='States'),
    }


class CountryState(osv.osv):
    _inherit = 'res.country.state'

    _columns = {
        'code': fields.char('State Code', size=6, help='The state code in max six chars.', required=True),
    }


class StateCity(osv.osv):
    _description = "State City"
    _name = 'res.country.city'
    _columns = {
        'state_id': fields.many2one('res.country.state', 'State', required=True),
        'name': fields.char(u'城市名称', required=True,
                            help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton'),
        'code': fields.char(u'城市编码', size=6,
                            help='The state code in max. three chars.', required=True),
    }
    _order = 'code'

    name_search = location_name_search


class CityRegion(osv.osv):
    _description = "City Region"
    _name = 'res.country.region'
    _columns = {
        'city_id': fields.many2one('res.country.city', 'Region', required=True),
        'name': fields.char(u'地区名称', required=True,
                            help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton'),
        'code': fields.char(u'地区编码', size=6,
                            help='The state code in max. three chars.', required=True),
    }
    _order = 'code'

    name_search = location_name_search
