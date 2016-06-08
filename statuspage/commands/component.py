from statuspage.commands.base import StatuspageBase
import statuspage.util as util

class Component(StatuspageBase):
    def __init__(self):
        super().__init__()
        self.api_token = None
        self.page_id = None

    def run(self):
        handler = self.parse_subcommand_()
        handler()

    def list(self):
        results = []
        for comp in self.get_components_().json():
            results.append({"name": comp["name"],
                            "status": comp["status"]})
        self.response.content(results, template="comps_list").send()

    def status(self):
        if len(self.request.args) > 1:
            return self.filtered_status()
        results = []
        for comp in self.get_components_().json():
            results.append({"name": comp["name"],
                            "status": comp["status"],
                            "last_updated": comp["updated_at"]})
        self.response.content(results, template="comps_status").send()

    def filtered_status(self):
        results = []
        names = self.request.args[1:]
        for comp in self.get_components_().json():
            if comp["name"] in names:
                results.append({"name": comp["name"],
                                "status": comp["status"],
                                "last_updated": comp["updated_at"]})
        self.response.content(results, template="comps_status").send()

    def get_components_(self):
        components_url = "/pages/%s/components.json" % (self.page_id)
        return util.api_get(components_url, self.api_token)

    def parse_subcommand_(self):
        if self.request.args == None:
            return self.list
        if self.request.args[0] == "list":
            return self.list
        if self.request.args[0] == "status":
            return self.status
        self.fail("Unknown subcommand: '%s'" % self.request.args[0])
