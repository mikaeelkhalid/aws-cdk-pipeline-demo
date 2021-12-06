from aws_cdk import core

from .pipeline_demo_stack import PipelineDemoStack

class WebserviceStage(core.Stage):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        service = PipelineDemoStack(self, "PipelineDemoStack")

        self.url_output = service.url_output

