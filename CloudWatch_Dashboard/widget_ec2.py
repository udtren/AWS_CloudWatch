import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

class CDKDashboard:
    # EC2のデフォルトメトリクスのグラフ生成に関する関数。関数名は自由に決定する。
    def build_ec2_default_widget(self, metricName, InstanceId, namespace):
        # GraphWidgetクラスで作成したオブジェクトがグラフ。GraphWidgetのオブジェクトを
        # メイン処理のdashboard.add_widgets（）内に記載することで、dashboardオブジェクトにグラフが追加される。
        # Python CDKの関数は「https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_cloudwatch.html」から確認する。
        wid = cw.GraphWidget(
            # titleはグラフの左上に表示するタイトルを記載
            title=f'{namespace} CPU',
            # leftはグラフの左軸に表示するデータを記載。
            # Metricクラスを複数記載すれば同じグラフに複数のメトリクスデータが表示される。
            # namespaceの値はAWSサービスごとに異なる、metric_nameとdimensionsもAWSサービスごとに内容が変わる。
            # 上記の値に関しては、AWS DocumentやCloudWatchのMetric画面から確認したいMetricを選択し、Source画面から確認する。
            # MetricクラスにないParameter（https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_cloudwatch/Metric.html）はすべてdimension内に記載する。
            left=[
            cw.Metric(namespace='AWS/EC2',metric_name=metricName,dimensions={'InstanceId': InstanceId},),
            ]
        )
        return wid

    def build_ec2_default_nw_widget(self, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Network In/Out',
            left=[
            cw.Metric(namespace='AWS/EC2', metric_name='NetworkIn',dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='AWS/EC2', metric_name='NetworkOut',dimensions={'InstanceId': InstanceId},),
            ]
        )
        return wid

    def build_ec2_default_nw_packet_widget(self, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Network Packet',
            left=[
            cw.Metric(namespace='AWS/EC2', metric_name='NetworkPacketsIn',dimensions={'InstanceId': InstanceId},),
            cw.Metric(namespace='AWS/EC2', metric_name='NetworkPacketsOut',dimensions={'InstanceId': InstanceId},),
            ]
        )
        return wid

    def build_ec2_mem_widget(self, metricName, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} {metricName}',
            left=[
            cw.Metric(namespace=namespace, metric_name=metricName,dimensions={'InstanceId': InstanceId},),
            ]
        )
        return wid

    def build_ec2_disk_widget(self, metricName, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} {metricName}',
            left=[
            cw.Metric(namespace=namespace, metric_name=metricName,
            dimensions={'InstanceId': InstanceId, 'path': '/', 'device': 'xvda2', 'fstype': 'xfs'},
            ),
           ]
        )
        return wid

    def build_ec2_disk_io_time_widget(self, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} IO Times',
            left=[
            cw.Metric(namespace=namespace, metric_name="diskio_reads",
            dimensions={'InstanceId': InstanceId, 'name': 'xvda2'},),
            cw.Metric(namespace=namespace, metric_name="diskio_writes",
            dimensions={'InstanceId': InstanceId, 'name': 'xvda2'},),
           ]
        )
        return wid

    def build_ec2_disk_rw_byte_widget(self, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Read/Write Times',
            left=[
            cw.Metric(namespace=namespace, metric_name="diskio_read_bytes",
            dimensions={'InstanceId': InstanceId, 'name': 'xvda2'},),
            cw.Metric(namespace=namespace, metric_name="diskio_write_bytes",
            dimensions={'InstanceId': InstanceId, 'name': 'xvda2'},),
           ]
        )
        return wid

    def build_ec2_win_mem_widget(self, metricName, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} {metricName}',
            left=[
            cw.Metric(namespace=namespace,
                      metric_name=metricName, dimensions={'InstanceId':InstanceId, 'objectname':'Memory'}),
            ]
        )
        return wid

    def build_ec2_win_disk_time_widget(self, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} % Disk Time',
            left=[
            cw.Metric(namespace=namespace, metric_name="PhysicalDisk % Disk Time",
            dimensions={'InstanceId':InstanceId, 'objectname':'PhysicalDisk', 'instance':"0 C:"},),
            cw.Metric(namespace=namespace, metric_name="PhysicalDisk % Disk Write Time",
            dimensions={'InstanceId': InstanceId, 'objectname': 'PhysicalDisk', 'instance': "0 C:"}, ),
            cw.Metric(namespace=namespace, metric_name="PhysicalDisk % Disk Read Time",
            dimensions={'InstanceId': InstanceId, 'objectname': 'PhysicalDisk', 'instance': "0 C:"}, ),
           ]
        )
        return wid

    def build_ec2_win_disk_rw_byte_widget(self, InstanceId, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Disk Read/Write',
            left=[
            cw.Metric(namespace=namespace, metric_name="PhysicalDisk Disk Write Bytes/sec",
            dimensions={'InstanceId':InstanceId, 'objectname':'PhysicalDisk', 'instance':"0 C:"},),
            cw.Metric(namespace=namespace, metric_name="PhysicalDisk Disk Read Bytes/sec",
            dimensions={'InstanceId': InstanceId, 'objectname': 'PhysicalDisk', 'instance': "0 C:"}, ),
           ]
        )
        return wid

    def build_ec2_as_widget(self, AutoScalingGroupName, width = 6):
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