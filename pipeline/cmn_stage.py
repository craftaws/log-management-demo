from aws_cdk import core

from cmn.network import Network

class CmnStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        Network(self, 'Network')