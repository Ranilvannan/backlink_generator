from odoo import models, fields, api
from datetime import datetime


class BacklinkGenerator(models.Model):
    _name = "backlink.generator"
    _description = "Backlink Generator"

    domain_url = fields.Char(string="Domain", required=True)
    item_ids = fields.One2many(comodel_name="backlink.generator.item", inverse_name="backlink_id")
    comment = fields.Text(string="Comment")


class BacklinkGeneratorItem(models.Model):
    _name = "backlink.generator.item"
    _description = "Backlink Generator Item"

    date = fields.Date(string="Date", default=datetime.now(), required=True)
    domain_url = fields.Char(string="Domain URL", required=True)
    backlink_id = fields.Many2one(comodel_name="backlink.generator", string="Backlink", required=True)
    comment = fields.Text(string="Comment")
