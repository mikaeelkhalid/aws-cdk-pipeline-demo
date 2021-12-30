from os import path
from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from aws_cdk import core

class PipelineDemoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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
