import requests
from statuspage.commands.base import StatuspageBase
import statuspage.util as util

class Incident(StatuspageBase):
    def __init__(self):
        super().__init__()

    def run(self):
        handler = self.parse_subcommand_()
        return handler()

    def list(self):
        results = []
        for incident in self.get_unresolved_().json():
            result = {"name": incident["name"],
                            "status": incident["status"],
                            "impact": incident["impact"],
                            "active_since": incident["created_at"],
                            "link": incident["shortlink"]}
            if "updates" in incident.keys():
                result["updates"] = incident["updates"]
            results.append(result)
        template = "incidents_list"
        if len(results) == 0:
            results = [{"incidents": 0}]
            template = "no_incidents"

        self.response.content(results, template=template).send()

    def create(self):
        body = self.build_create_body_()
        incidents_url = "/pages/%s/incidents.json" % (self.page_id)
        r = util.api_post(incidents_url, self.api_token, body=body)
        if r.status_code != 201:
            self.fail(r.text)
        else:
            incident = r.json()
            results = []
            result = {"name": incident["name"],
                      "status": incident["status"],
                      "impact": incident["impact"],
                      "active_since": incident["created_at"],
                      "link": incident["shortlink"]}
            if "updates" in incident.keys():
                result["updates"] = incident["updates"]
            results.append(result)
            self.response.content(results, template="incident_created").send()

    def update(self):
        try:
            name = self.request.options["name"]
            incident_id = self.get_incident_id_(name)
            if incident_id is None:
                self.fail("Incident %s not found" % (name))
            body = self.build_update_body_()
            incidents_url = "/pages/%s/incidents/%s.json" % (self.page_id, incident_id)
            r = util.api_patch(incidents_url, self.api_token, body=body)
            results = []
            template = None
            if r.status_code != 200:
                self.fail(r.text)
            else:
                incident = r.json()
                if incident["status"] == "resolved":
                    result = {"name": name,
                              "resolved_at": incident["resolved_at"],
                              "link": incident["shortlink"]}
                    if "updates" in incident.keys():
                        result["updates"] = incident["updates"]
                    results.append(result)
                    template = "incident_resolved"
                else:
                    result = {"name": name,
                              "link": incident["shortlink"]}
                    if "updates" in incident.keys():
                        result["updates"] = incident["updates"]
                    results.append(result)
                    template = "incident_updated"
            self.response.content(results, template=template).send()
        except KeyError as e:
            self.fail("Missing required option %s" % (e))

    def build_create_body_(self):
        impact = self.request.get_optional_option("impact")
        component_ids = self.get_component_ids_()
        message = " ".join(self.request.args[1:])
        if message == "":
            self.fail("Initial message is required to create an incident")
        try:
            body = dict()
            body["incident[name]"] = self.request.options["name"]
            body["incident[status]"] = self.request.options["status"]
            body["incident[message]"] = message
            if impact is not None:
                body["incident[impact_override]"] = impact
            if component_ids is not None:
                body["incident[component_ids]"] = component_ids
            return body
        except KeyError as e:
            self.fail("Missing required option %s" % (e))

    def build_update_body_(self):
        impact = self.request.get_optional_option("impact")
        component_ids = self.get_component_ids_()
        status = self.request.get_optional_option("status")
        message = " ".join(self.request.args[1:])
        body = dict()
        if impact is not None:
            body["incident[impact_override]"] = impact
        if component_ids is not None:
            body["incident[component_ids]"] = component_ids
        if status is not None:
            body["incident[status]"] = status
        if message != "":
            body["incident[message]"] = message
        return body

    def get_component_ids_(self):
        comps = self.request.get_optional_option("component")
        if comps is None:
            return None
        names = [c.strip() for c in comps.split(",")]
        components_url = "/pages/%s/components.json" % (self.page_id)
        results = []
        for comp in util.api_get(components_url, self.api_token).json():
            if comp["name"] in names:
                results.append(comp["id"])
        if len(results) == 0:
            self.fail("None of the components named were found.")
        return results

    def get_incident_id_(self, name):
        for incident in self.get_unresolved_().json():
            if incident["name"] == name:
                return incident["id"]
        return None

    def get_unresolved_(self):
        incidents_url = "/pages/%s/incidents/unresolved.json" % (self.page_id)
        return util.api_get(incidents_url, self.api_token)

    def parse_subcommand_(self):
        if self.request.args == None:
            return self.list
        if self.request.args[0] == "list":
            return self.list
        if self.request.args[0] == "new":
            return self.create
        if self.request.args[0] == "update":
            return self.update
        self.fail("Unknown subcommand: '%s'" % self.request.args[0])
