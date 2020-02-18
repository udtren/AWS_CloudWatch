import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

class CDKDashboard:

    def build_ebs_widget(cls, VolumeId, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'ebs', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/EBS',metric_name=metric,dimensions={'VolumeId': VolumeId},))
            wid = cw.GraphWidget(
                title=VolumeId+'_'+'EBS',
                left=leftlist,
                width=width
            )
            return wid

    def build_lambda_widget(cls, FunctionName, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'lambda', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/Lambda',metric_name=metric,dimensions={'FunctionName': FunctionName},))
            wid = cw.GraphWidget(
                title=FunctionName+'_'+'Lambda',
                left=leftlist,
                width=width
            )
            return wid

    def build_sqs_widget(cls, QueueName, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'sqs', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/SQS',metric_name=metric,dimensions={'QueueName': QueueName},))
            wid = cw.GraphWidget(
                title=QueueName+'_'+'sqs',
                left=leftlist,
                width=width
            )
            return wid

    def build_athena_widget(cls, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'athena', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/Athena',metric_name=metric,))
            wid = cw.GraphWidget(
                title=QueueName+'_'+'athena',
                left=leftlist,
                width=width
            )
            return wid

    def build_cw_events_widget(cls, RuleName, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'cwevents', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/Events',metric_name=metric,dimensions={'RuleName': RuleName},))
            wid = cw.GraphWidget(
                title=RuleName+'_'+'Events',
                left=leftlist,
                width=width
            )
            return wid

    def build_cw_logs_widget(cls, LogGroupName, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'cwlogs', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/Logs',metric_name=metric,dimensions={'LogGroupName': LogGroupName},))
            wid = cw.GraphWidget(
                title=LogGroupName+'_'+'Logs',
                left=leftlist,
                width=width
            )
            return wid

    def build_route53_widget(cls, EndpointId, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'route53', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/Route53Resolver',metric_name=metric,dimensions={'EndpointId': EndpointId},))
            wid = cw.GraphWidget(
                title=EndpointId+'_'+'route53',
                left=leftlist,
                width=width
            )
            return wid

    def build_dx_widget(cls, ConnectionId, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'dx', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/DX',metric_name=metric,dimensions={'ConnectionId': ConnectionId},))
            wid = cw.GraphWidget(
                title=ConnectionId+'_'+'dx',
                left=leftlist,
                width=width
            )
            return wid

    def build_shield_widget(cls, AttackVector, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'shield', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/DDoSProtection',metric_name=metric,dimensions={'AttackVector': AttackVector},))
            wid = cw.GraphWidget(
                title=AttackVector+'_'+'shield',
                left=leftlist,
                width=width
            )
            return wid

    def build_waf_widget(cls, Rule, RuleGroup, Region, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'waf', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/WAF',metric_name=metric,dimensions={'Rule': Rule, 'RuleGroup': RuleGroup, 'Region': Region},))
            wid = cw.GraphWidget(
                title=Rule+'_'+'waf',
                left=leftlist,
                width=width
            )
            return wid



    def build_cloudhsm_widget(cls, ClusterId, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'hsm', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/CloudHSM',metric_name=metric,dimensions={'ClusterId': ClusterId},))
            wid = cw.GraphWidget(
                title=ClusterId+'_'+'CloudHSM',
                left=leftlist,
                width=width
            )
            return wid

    def build_aurora_widget(cls, DBClusterIdentifier, Role, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'aurora', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/RDS',metric_name=metric,dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},))
            wid = cw.GraphWidget(
                title=DBClusterIdentifier+'_'+'aurora',
                left=leftlist,
                width=width
            )
            return wid

    def build_s3_widget(cls, BucketName, width = 6):
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r's3', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/S3',metric_name=metric,dimensions={'BucketName': BucketName, 'StorageType': 'AllStorageTypes'},))
            wid = cw.GraphWidget(
                title=BucketName+'_'+'S3',
                left=leftlist,
                width=width
            )
            return wid
