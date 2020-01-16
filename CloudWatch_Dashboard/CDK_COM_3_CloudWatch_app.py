import re

from aws_cdk import core
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

import CDK_COM_3_CloudWatch_widget

cf = CDK_COM_3_CloudWatch_widget.CDKDashboard()

class Dashboard(core.Stack):
    """
    CloudWatchのDashboard作成とグラフ出力の処理を行う。
    """
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        """
        Dashboard作成とグラフ出力のメイン処理。

        各AWSサービスのMetricはアイデンティティの一部である名前と値のペアであるディメンション(Dimension)を持つ。
        Metricのグラフ作成時に正しいDimensionを指定することで、グラフを正確に作成することができる。
        例えばEC2はDimensionとしてInstanceIdを持っており、
        InstanceIdを指定することで特定のEC2のMetricグラフを作成できる。

        各AWSサービスのCloudFormationスタック作成後、OutputでDimensionと変数名を出力する。

        変数名をテキストファイル「resource.txt」に記入する。
        メイン処理ではテキストファイルを1行ずつ読取り、ImportValueでDimensionを取得し、配列を作成する。

        グラフ作成メソッドにDimensionを1つずつ渡すことで、同じサービスの異なるインスタンスのグラフを作成する。
        （例：異なるEC2インスタンス、S3の異なるバケット）
        """
        InstanceId = []
        AutoScalingGroupName = []
        FunctionName = []
        BucketName = []
        TransitGateway = []

        with open("resource.txt") as f:
            for line in f:
                if re.match(r'ec2', line):
                    output = line.split(',')[1].rstrip('\n')
                    InstanceId.append(core.Fn.import_value(output))
                if re.match(r'as', line):
                    output = line.split(',')[1].rstrip('\n')
                    #AutoScalingGroupName.append(core.Fn.import_value(output))
                    AutoScalingGroupName.append(output)
                if re.match(r'lambda', line):
                    output = line.split(',')[1].rstrip('\n')
                    #FunctionName.append(core.Fn.import_value(output))
                    FunctionName.append(output)
                if re.match(r's3', line):
                    output = line.split(',')[1].rstrip('\n')
                    #BucketName.append(core.Fn.import_value(output))
                    BucketName.append(output)
                if re.match(r'transitgw', line):
                    output = line.split(',')[1].rstrip('\n')
                    #TransitGateway.append(core.Fn.import_value(output))
                    TransitGateway.append(output)

        dashboard = cw.Dashboard(self, id="rDashboardA", dashboard_name="Role1")
        # グラフのwidthを指定しない場合、デフォルトの「6」となる。
        # CloudWatch Dashboardの幅は24のため、1行に並ぶグラフ数は4つとなる。
        dashboard.add_widgets(
            cf.build_ec2_cpu_widget('CPUUtilization', 'cpu_usage_system', 'cpu_usage_user', InstanceId[0]),
            cf.build_ec2_mem_widget('mem_free', 'mem_used', 'mem_buffered', 'mem_cached', 'mem_total', InstanceId[0]),
            cf.build_ec2_disk_widget('disk_used', 'disk_free', InstanceId[0]),
            cf.build_ec2_net_widget('NetworkIn', 'NetworkOut', 'net_drop_in', 'net_drop_out', 'net_err_in', 'net_err_out', InstanceId[0]),
        )

        dashboard = cw.Dashboard(self, id="rDashboardB", dashboard_name="Regular_Report_Role1")
        # グラフのwidthを指定することで、1行に並ぶグラフの数を調整する。
        # 複数のdashboard.add_widgetsを使用することにより、新しい行でグラフを出力する。
        dashboard.add_widgets(
                    cf.build_ec2_as_widget(AutoScalingGroupName[0],6),
                    cf.build_lambda_widget(FunctionName[0],6),
                    cf.build_lambda_widget(FunctionName[1],6),
                )
        dashboard.add_widgets(
                    cf.build_s3_widget(BucketName[0]),
                    cf.build_s3_widget(BucketName[1]),
                    cf.build_s3_widget(BucketName[2]),
                )
        dashboard.add_widgets(
                    cf.build_transitgateway_widget(TransitGateway[0],12),
                )

app = core.App()
Dashboard(app, "Dashboard")

app.synth()
