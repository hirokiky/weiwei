from webob.request import BaseRequest


class Request(BaseRequest):
    @property
    def matching(self):
        return self.environ['matcha.matching']

    @property
    def matched_dict(self):
        return self.environ['matcha.matched_dict']
