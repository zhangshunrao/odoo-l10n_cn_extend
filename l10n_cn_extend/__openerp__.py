# -*- coding: utf-8 -*-
{
    "name": "中国行政区",
    "version": "1.0",
    "author": "HPF,RZS",
    'website': 'https://www.odoo.com',
    "depends": ["base", "l10n_cn"],
    'summary': '中国行政区地区信息',
    "category": "通用模块/行政区划分（中国）",
    "description": """中国行政区模块，完善了中国省下属城市、中国城市下属地区,数据来源为:
    中华人民共和国国家统计局最新县及县以上行政区划代码【2014-10-31】（其中有部分城市下属地区没有记录e.g东莞）""",
    "data": [
        'base_data_extend.xml',
    ],
    "installable": True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

