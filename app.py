#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

# from pipeline_demo.pipeline_demo_stack import PipelineDemoStack
from pipeline_demo.pipeline_stack import PipelineStack

app = core.App()
# PipelineDemoStack(app, "PipelineDemoStack")
PipelineStack(app, "PipelineStack",
    env={
        'region': 'us-east-1', 
        'account': '454181958425'
        }
    )


app.synth()
