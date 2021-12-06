from os import path
from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class PipelineDemoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PipelineDemoQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )
        this_dir = path.dirname(__file__)

        handler = _lambda.Function(
            self,"Handler",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset(path.join(this_dir, "lambda")),
            handler="handler.handler",
        )

        gw = apigw.LambdaRestApi(
            self, "Gateway",
            handler=handler.current_version
        )

        self.url_output = core.CfnOutput(
            self, "GatewayURL",
            value=gw.url,
        )
