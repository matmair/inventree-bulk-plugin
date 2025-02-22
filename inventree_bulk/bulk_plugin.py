from plugin import InvenTreePlugin

from inventree_bulk.version import BULK_PLUGIN_VERSION
from plugin.mixins import SettingsMixin, PanelMixin

from stock.views import StockLocationDetail


class BulkActionPlugin(SettingsMixin, PanelMixin, InvenTreePlugin):
    AUTHOR = "wolflu05"
    DESCRIPTION = "Bulk action plugin"
    VERSION = BULK_PLUGIN_VERSION

    NAME = "Bulk Action"
    SLUG = "bulkaction"
    TITLE = "Bulk Action"

    SETTINGS = {}

    def get_custom_panels(self, view, request):
        panels = []
        print(view)
        if isinstance(view, StockLocationDetail):
            # We can use template rendering in the raw content
            content = """
            <div>
                <textarea></textarea>
                <br />
                {{location.id}}
                <button type="button" class="btn btn-primary">Erstellen</button>
            </div>
            """

            panels.append({
                'title': 'Bulk creation',
                'icon': 'fas fa-tools',
                'content': content,
                'description': 'Bulk creation tools',
            })

        return panels
