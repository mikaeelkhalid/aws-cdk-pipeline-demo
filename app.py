#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from pipeline_demo.pipeline_demo_stack import PipelineDemoStack
from pipeline_demo.pipeline_stack import PipelineStack

app = core.App()
PipelineDemoStack(app, "PipelineDemoStack")
PipelineStack(app, "PipelineStack",
    env={
        'region': 'us-east-12', 
        'account': '12345678'
        }
    )


app.synth()
