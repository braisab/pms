# Copyright 2018 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api

from odoo.addons.component.core import Component


class PmsRoomTypeRestrictionImporter(Component):
    _name = "channel.pms.room.type.restriction.item.importer"
    _inherit = "pms.channel.importer"
    _apply_on = ["channel.pms.room.type.restriction.item"]
    _usage = "pms.room.type.restriction.item.importer"

    # FIXME: Reduce Nested Loops!!
    @api.model
    def _generate_restriction_items(self, plan_restrictions):
        raise NotImplementedError

    @api.model
    def import_restriction_values(self, date_from, date_to, channel_restr_id=False):
        raise NotImplementedError