import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

class CDKDashboard:
    def build_cloudFront_errorRate_widget(cls, DistributionId):
        wid = cw.GraphWidget(
            title='AWS/CloudFront',
            left=[
                cw.Metric(namespace='AWS/CloudFront', metric_name='4xxErrorRate',
                          dimensions={'DistributionId': DistributionId, 'Region': 'Global'},),
                cw.Metric(namespace='AWS/CloudFront', metric_name='5xxErrorRate',
                          dimensions={'DistributionId': DistributionId, 'Region': 'Global'}, ),
                cw.Metric(namespace='AWS/CloudFront', metric_name='TotalErrorRate',
                          dimensions={'DistributionId': DistributionId, 'Region': 'Global'}, ),
            ]
        )
        return wid

    def build_cloudFront_bytes_widget(cls, DistributionId):
        wid = cw.GraphWidget(
            title='AWS/CloudFront',
            left=[
                cw.Metric(namespace='AWS/CloudFront', metric_name='BytesDownloaded',
                          dimensions={'DistributionId': DistributionId, 'Region': 'Global'},),
                cw.Metric(namespace='AWS/CloudFront', metric_name='BytesUploaded',
                          dimensions={'DistributionId': DistributionId, 'Region': 'Global'}, ),
            ]
        )
        return wid

    def build_cloudFront_requests_widget(cls, DistributionId):
        wid = cw.GraphWidget(
            title='AWS/CloudFront',
            left=[
                cw.Metric(namespace='AWS/CloudFront', metric_name='Requests',
                          dimensions={'DistributionId': DistributionId, 'Region': 'Global'},),
            ]
        )
        return wid

    def build_clb_count_widget(cls, LoadBalancerName):
        wid = cw.GraphWidget(
            title=LoadBalancerName,
            left=[
                cw.Metric(namespace='AWS/ELB', metric_name='RequestCount',
                          dimensions={'LoadBalancerName': LoadBalancerName},),
            ]
        )
        return wid

    def build_clb_count2_widget(cls, LoadBalancerName):
        wid = cw.GraphWidget(
            title=LoadBalancerName,
            left=[
                cw.Metric(namespace='AWS/ELB', metric_name='HealthyHostCount',
                          dimensions={'LoadBalancerName': LoadBalancerName}, ),
                cw.Metric(namespace='AWS/ELB', metric_name='UnHealthyHostCount',
                          dimensions={'LoadBalancerName': LoadBalancerName}, ),
            ]
        )
        return wid

    def build_clb_length_widget(cls, LoadBalancerName):
        wid = cw.GraphWidget(
            title=LoadBalancerName,
            left=[
                cw.Metric(namespace='AWS/ELB', metric_name='SurgeQueueLength',
                          dimensions={'LoadBalancerName': LoadBalancerName}, ),
                cw.Metric(namespace='AWS/ELB', metric_name='SpilloverCount',
                          dimensions={'LoadBalancerName': LoadBalancerName}, ),
            ]
        )
        return wid

    def build_clb_code_widget(cls, LoadBalancerName):
        wid = cw.GraphWidget(
            title=LoadBalancerName,
            left=[
                cw.Metric(namespace='AWS/ELB', metric_name='HTTPCode_ELB_4XX',
                          dimensions={'LoadBalancerName': LoadBalancerName}, ),
                cw.Metric(namespace='AWS/ELB', metric_name='HTTPCode_ELB_5XX',
                          dimensions={'LoadBalancerName': LoadBalancerName}, ),
            ]
        )
        return wid

    def build_alb_count_widget(cls, LoadBalancerFullName):
        wid = cw.GraphWidget(
            title=LoadBalancerFullName,
            left=[
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='ActiveConnectionCount',
                          dimensions={'LoadBalancer': LoadBalancerFullName},),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='ClientTLSNegotiationErrorCount',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='RequestCount',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='RejectedConnectionCount',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='HealthyHostCount',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='UnHealthyHostCount',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='RequestCountPerTarget',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
            ]
        )
        return wid

    def build_alb_byte_widget(cls, LoadBalancerFullName):
        wid = cw.GraphWidget(
            title=LoadBalancerFullName,
            left=[
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='ProcessedBytes',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
            ]
        )
        return wid

    def build_alb_code_widget(cls, LoadBalancerFullName):
        wid = cw.GraphWidget(
            title=LoadBalancerFullName,
            left=[
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='HTTPCode_ELB_3XX_Count',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='HTTPCode_ELB_4XX_Count',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
                cw.Metric(namespace='AWS/ApplicationELB', metric_name='HTTPCode_ELB_5XX_Count',
                          dimensions={'LoadBalancer': LoadBalancerFullName}, ),
            ]
        )
        return wid

    def build_transitgateway_byte_widget(cls, TransitGateway):
        wid = cw.GraphWidget(
            title='AWS/TransitGateway',
            left=[
                cw.Metric(namespace='AWS/TransitGateway', metric_name='BytesIn',
                          dimensions={'TransitGateway': TransitGateway},),
                cw.Metric(namespace='AWS/TransitGateway', metric_name='BytesOut',
                          dimensions={'TransitGateway': TransitGateway}, ),
            ]
        )
        return wid

    def build_transitgateway_packet_widget(cls, TransitGateway):
        wid = cw.GraphWidget(
            title='AWS/TransitGateway',
            left=[
                cw.Metric(namespace='AWS/TransitGateway', metric_name='PacketsIn',
                          dimensions={'TransitGateway': TransitGateway},),
                cw.Metric(namespace='AWS/TransitGateway', metric_name='PacketsOut',
                          dimensions={'TransitGateway': TransitGateway}, ),
            ]
        )
        return wid

    def build_transitgateway_count_widget(cls, TransitGateway):
        wid = cw.GraphWidget(
            title='AWS/TransitGateway',
            left=[
                cw.Metric(namespace='AWS/TransitGateway', metric_name='BytesDropCountBlackhole',
                          dimensions={'TransitGateway': TransitGateway},),
                cw.Metric(namespace='AWS/TransitGateway', metric_name='PacketDropCountNoRoute',
                          dimensions={'TransitGateway': TransitGateway}, ),
                cw.Metric(namespace='AWS/TransitGateway', metric_name='PacketDropCountBlackhole',
                          dimensions={'TransitGateway': TransitGateway}, ),
                cw.Metric(namespace='AWS/TransitGateway', metric_name='BytesDropCountNoRoute',
                          dimensions={'TransitGateway': TransitGateway}, ),
            ]
        )
        return wid