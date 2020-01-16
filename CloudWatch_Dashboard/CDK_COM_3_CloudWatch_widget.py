import re

from aws_cdk import (
    aws_cloudwatch as cw,
    core
)


class CDKDashboard:
    """
    グラフ作成メソッドに関するクラス
    Dashboardのグラフ作成メソッドをサービスごとに定義する。
    """

    def build_ec2_cpu_widget(cls, metricName, metricName2, metricName3, InstanceId):
        """
        EC2のCPUグラフ作成関数
        カスタムメトリクスを使用する場合のEC2グラフ作成関数。

        Parameters
        ----------
        metricName, metricName2, metricName2 : str
            グラフに表示するメトリクス。
        InstanceId : str
            EC2のインスタンスID。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        wid = cw.GraphWidget(
            title=InstanceId+'_'+'CPU',
            left=[
            cw.Metric(namespace='AWS/EC2',metric_name=metricName,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName2,dimensions={'InstanceId': InstanceId, 'cpu': 'cpu-total'},),
            cw.Metric(namespace='CWAgent',metric_name=metricName3,dimensions={'InstanceId': InstanceId, 'cpu': 'cpu-total'},)
            ]
        )
        return wid

    def build_ec2_mem_widget(cls, metricName, metricName2, metricName3, metricName4, metricName5, InstanceId):
        """
        EC2のメモリグラフ作成関数
        カスタムメトリクスを使用する場合のEC2グラフ作成関数。

        Parameters
        ----------
        metricName, metricName2, metricName3, metricName4, metricName5 : str
            グラフに表示するメトリクス。
        InstanceId : str
            EC2のインスタンスID。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        wid = cw.GraphWidget(
            title=InstanceId+'_'+'MEM',
            left=[
            cw.Metric(namespace='CWAgent',metric_name=metricName,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName2,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName3,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName4,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName5,dimensions={'InstanceId': InstanceId},),
            ]
        )
        return wid

    def build_ec2_disk_widget(cls, metricName, metricName2, InstanceId):
        """
        EC2のディスクグラフ作成関数
        カスタムメトリクスを使用する場合のEC2グラフ作成関数。

        Parameters
        ----------
        metricName, metricName2 : str
            グラフに表示するメトリクス。
        InstanceId : str
            EC2のインスタンスID。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        Notes
        -----
        この関数では「/」配下のメトリクスをグラフに出力する。

        """
        wid = cw.GraphWidget(
            title=InstanceId+'_'+'DISK',
            left=[
            cw.Metric(
            namespace='CWAgent',
            metric_name=metricName,
            dimensions={'InstanceId': InstanceId, 'path': '/', 'device': 'xvda1', 'fstype': 'xfs'},
            ),
            cw.Metric(
            namespace='CWAgent',
            metric_name=metricName,
            dimensions={'InstanceId': InstanceId, 'path': '/', 'device': 'xvda1', 'fstype': 'xfs'},
            ),]
        )
        return wid

    def build_ec2_net_widget(cls, metricName, metricName2, metricName3, metricName4, metricName5, metricName6, InstanceId):
        """
        EC2のネットワーク入出力グラフ作成関数
        カスタムメトリクスを使用する場合のEC2グラフ作成関数。

        Parameters
        ----------
        metricName, metricName2, metricName3, metricName4, metricName5, metricName6 : str
            グラフに表示するメトリクス。
        InstanceId : str
            EC2のインスタンスID。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        wid = cw.GraphWidget(
            title=InstanceId+'_'+'NET',
            left=[
            cw.Metric(namespace='CWAgent',metric_name=metricName,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName2,dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='CWAgent',metric_name=metricName3,dimensions={'InstanceId': InstanceId, 'interface': 'eth0'},),
            cw.Metric(namespace='CWAgent',metric_name=metricName4,dimensions={'InstanceId': InstanceId, 'interface': 'eth0'},),
            cw.Metric(namespace='CWAgent',metric_name=metricName5,dimensions={'InstanceId': InstanceId, 'interface': 'eth0'},),
            cw.Metric(namespace='CWAgent',metric_name=metricName6,dimensions={'InstanceId': InstanceId, 'interface': 'eth0'},),
            ]
        )
        return wid

    def build_ebs_widget(cls, VolumeId, width = 6):
        """
        Amazon Elastic Block Storeのグラフ作成関数
        「metric_ebs.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        VolumeId : str
            グラフ作成するEBSを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        AWS Lambdaのグラフ作成関数
        「metric_lambda.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        FunctionName : str
            グラフ作成するLambdaを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        Amazon Simple Queue Serviceのグラフ作成関数
        「metric_sqs.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        QueueName : str
            グラフ作成するSQSのキューを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        Amazon Athenaのグラフ作成関数
        「metric_athena.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        Amazon CloudWatch Eventsのグラフ作成関数
        「metric_cwevents.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        RuleName : str
            グラフ作成するEventを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        Amazon CloudWatch Logsのグラフ作成関数
        「metric_cwlogs.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        LogGroupName : str
            グラフ作成するLogGroupNameを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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

    def build_ec2_as_widget(cls, AutoScalingGroupName, width = 6):
        """
        Amazon EC2 Auto Scalingのグラフ作成関数
        「metric_as.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        AutoScalingGroupName : str
            グラフ作成するAutoScalingGroupNameを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'as', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/EC2',metric_name=metric,dimensions={'AutoScalingGroupName': AutoScalingGroupName},))
            wid = cw.GraphWidget(
                title=AutoScalingGroupName+'_'+'AS',
                left=leftlist,
                width=width
            )
            return wid

    def build_cloudfront_widget(cls, DistributionId, width = 6):
        """
        Amazon CloudFrontのグラフ作成関数
        「metric_cloudfront.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        DistributionId : str
            グラフ作成するDistributionIdを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'cloudfront', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/CloudFront',metric_name=metric,dimensions={'DistributionId': DistributionId,'Region': 'Global'},))
            wid = cw.GraphWidget(
                title=DistributionId+'_'+'metric_cloudfront',
                left=leftlist,
                width=width
            )
            return wid

    def build_route53_widget(cls, EndpointId, width = 6):
        """
        Amazon Route 53のグラフ作成関数
        「metric_route53.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        EndpointId : str
            グラフ作成するEndpointIdを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        AWS Direct Connectのグラフ作成関数
        「metric_dx.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        ConnectionId : str
            グラフ作成するConnectionIdを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        AWS Shieldのグラフ作成関数
        「metric_shield.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        AttackVector : str
            グラフ作成するAttackVectorを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        AWS WAFのグラフ作成関数
        「metric_waf.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        Rule, RuleGroup, Region : str
            グラフ作成するRule, RuleGroup, Regionを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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

    def build_clb_widget(cls, LoadBalancerName, width = 6):
        """
        Elastic Load Balancingのグラフ作成関数
        「metric_elb.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        LoadBalancerName : str
            グラフ作成するLoadBalancerNameを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'clb', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/ELB',metric_name=metric,dimensions={'LoadBalancerName': LoadBalancerName},))
            wid = cw.GraphWidget(
                title=LoadBalancerName+'_'+'elb',
                left=leftlist,
                width=width
            )
            return wid

    def build_alb_widget(cls, TargetGroup, width = 6):
        """
        Elastic Load Balancingのグラフ作成関数
        「metric_alb.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        TargetGroup : str
            グラフ作成するTargetGroupを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'alb', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/ApplicationELB',metric_name=metric,dimensions={'TargetGroup': TargetGroup},))
            wid = cw.GraphWidget(
                title=TargetGroup+'_'+'alb',
                left=leftlist,
                width=width
            )
            return wid

    def build_transitgateway_widget(cls, TransitGateway, width = 6):
        """
        AWS Transit Gatewayのグラフ作成関数
        「metric_transitgw.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        TransitGateway : str
            グラフ作成するTransitGatewayを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
        with open("metric.txt") as g:
            leftlist = []
            for line2 in g:
                if re.match(r'transitgw', line2):
                    metric = line2.split(',')[1].rstrip('\n')
                    leftlist.append(cw.Metric(namespace='AWS/TransitGateway',metric_name=metric,dimensions={'TransitGateway': TransitGateway},))
            wid = cw.GraphWidget(
                title=TransitGateway+'_'+'TransitGW',
                left=leftlist,
                width=width
            )
            return wid

    def build_cloudhsm_widget(cls, ClusterId, width = 6):
        """
        AWS CloudHSMのグラフ作成関数
        「metric_cloudhsm.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        ClusterId : str
            グラフ作成するClusterIdを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        Amazon Auroraのグラフ作成関数
        「metric_aurora.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        DBClusterIdentifier, Role : str
            グラフ作成するDBClusterIdentifier, Roleを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
        """
        Amazon S3のグラフ作成関数
        「metric_s3.txt」に記載されたメトリクスを1つのグラフに出力する。

        Parameters
        ----------
        BucketName : str
            グラフ作成するBucketNameを指定する。
        width : str
            グラフの幅を指定する。

        Returns
        -------
        wid : str
            aws_cdk.aws_cloudwatch.Dashboard.add_widgetsに渡すWidgetの引数

        """
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
