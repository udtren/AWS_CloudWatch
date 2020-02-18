import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

class CDKDashboard:
    def build_s3_size_widget(cls, BucketName):
        wid = cw.GraphWidget(
            title=BucketName,
            left=[
                cw.Metric(namespace='AWS/S3', metric_name='BucketSizeBytes',
                          dimensions={'BucketName': BucketName, 'StorageType': 'StandardStorage'}, ),
            ]
        )
        return wid

    def build_s3_number_widget(cls, BucketName):
        wid = cw.GraphWidget(
            title=BucketName,
            left=[
                cw.Metric(namespace='AWS/S3', metric_name='NumberOfObjects',
                          dimensions={'BucketName': BucketName, 'StorageType': 'AllStorageTypes'}, ),
            ]
        )
        return wid