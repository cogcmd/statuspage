from cog.command import Command

class StatuspageBase(Command):
    def __init__(self):
        super().__init__()
        self.api_token = None
        self.page_id = None

    def prepare(self):
        self.api_token = self.config("api_token")
        if self.api_token == None:
            self.fail("Missing dynamic configuration variable 'api_token'.")

        self.page_id = self.config("page_id")
        if self.page_id == None:
            self.fail("Missing dynamic configuration variable 'page_id'.")

