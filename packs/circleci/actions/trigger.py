from lib.base import BaseCircleciAction

__all__ = [
    'TriggerBuildAction'
]

class TriggerBuildAction(BaseCircleciAction):
    def run(self, org, repo, ref):
        build = self._client.build.trigger(org, repo, ref)
        build_url = build.get('build_url')
        print "build_url is {}".format(build_url)
        return True
