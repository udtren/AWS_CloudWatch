import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)
import widget_ec2
import widget_ecs
import widget_network
import widget_rds
import widget_s3

cf = widget_ec2.CDKDashboard()
cf_ecs = widget_ecs.CDKDashboard()
cf_nw = widget_network.CDKDashboard()
cf_rds = widget_rds.CDKDashboard()
cf_s3 = widget_s3.CDKDashboard()

class Dashboard(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 各サービスのグラフ作成には対象の識別子が必要。
        # 識別子は各サービスのCloudFormationからExportする。
        # サービスごとにExportした識別子の配列を作成し、ループ処理でダッシュボードにグラフを作成する。
        InstanceId = []
        ec2_namespace = []
        ecs_cluster_service = []
        clb_name = []
        alb_name = []
        cloudFront_name = []
        tgw_name = []
        rds_name = []
        s3_name = []

        # resource.txtには各AWSサービスのCloudFormationのExport名を記載しているため、
        # それぞれのAWｓサービスの配列に記載する。
        # サービスによってはグラフ作成に2つ以上のExport名が必要となる場合もある。
        # ”,”でExport名を区切り、配列に値を記載する。
        with open("resource.txt") as f:
            for line in f:
                if re.match(r'ec2', line):
                    output = line.split(',')[1].rstrip('\n')
                    # EC2のインスタンスIDとサーバ名をリストに追加
                    # EC2のインストールIDはCloudFormationのExport値から取得するため、
                    # core.Fn.import_valueを使用する。
                    InstanceId.append(core.Fn.import_value(output))
                    ec2_namespace.append(line.split(',')[2].rstrip('\n'))
                if re.match(r'ecs', line):
                    # [clustername, servicename]のデータをリストに追加
                    ecs_cluster_service.append([core.Fn.import_value(line.split(',')[1].rstrip('\n')),
                                                core.Fn.import_value(line.split(',')[2].rstrip('\n'))])
                if re.match(r'clb', line):
                    clb_name.append(core.Fn.import_value(line.split(',')[1].rstrip('\n')))
                if re.match(r'alb', line):
                    alb_name.append(core.Fn.import_value(line.split(',')[1].rstrip('\n')))
                if re.match(r'tgw', line):
                    tgw_name.append(core.Fn.import_value(line.split(',')[1].rstrip('\n')))
                if re.match(r'rds', line):
                    rds_name.append(line.split(',')[1].rstrip('\n'))
                if re.match(r's3', line):
                    s3_name.append(line.split(',')[1].rstrip('\n'))
                if re.match(r'clf', line):
                    cloudFront_name.append(core.Fn.import_value(line.split(',')[1].rstrip('\n')))

        # EC2のダッシュボードを作成する
        # Dashboardクラスのオブジェクトを作成し、そのインスタンス内にグラフオブジェクトを追加する。
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_cloudwatch/Dashboard.html
        # Python CDKの関数は「https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_cloudwatch.html」から確認する。
        dashboard = cw.Dashboard(self, id="rDashboardEC2", dashboard_name="Dashboard-Server")
        # dashboard.add_widgetsがダッシュボードを作成。
        # dashboard.add_widgets（）の中にある値がグラフとなる。
        for instanceid_index in range(len(InstanceId)):
            if ec2_namespace[instanceid_index] != 'testWindows':
                dashboard.add_widgets(
                    cf.build_ec2_default_widget('CPUUtilization', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_default_nw_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_default_nw_packet_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_default_widget('StatusCheckFailed', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_mem_widget('mem_used', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_disk_widget('disk_used_percent', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_disk_io_time_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_disk_rw_byte_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index])
                )
            elif ec2_namespace[instanceid_index] == 'testWindows':
                dashboard.add_widgets(
                    cf.build_ec2_default_widget('CPUUtilization', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_default_nw_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_default_nw_packet_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_default_widget('StatusCheckFailed', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_win_mem_widget('Memory % Committed Bytes In Use', InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_win_disk_time_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cf.build_ec2_win_disk_rw_byte_widget(InstanceId[instanceid_index], ec2_namespace[instanceid_index]),
                    cw.TextWidget(markdown='', height=6)
                )

        # ECSのダッシュボードを作成する。
        dashboard = cw.Dashboard(self, id="rDashboardECS", dashboard_name="Dashboard-Container")
        for instanceid_index in range(len(ecs_cluster_service)):
            clusterName = ecs_cluster_service[instanceid_index][0]
            serviceName = ecs_cluster_service[instanceid_index][1]
            dashboard.add_widgets(
                cf_ecs.build_ecs_service_cpu_widget(clusterName, serviceName, f'{clusterName}_{serviceName}'),
                cf_ecs.build_ecs_service_mem_widget(clusterName, serviceName, f'{clusterName}_{serviceName}'),
                cf_ecs.build_ecs_container_insight_cpu_widget(clusterName, serviceName, f'{clusterName}_{serviceName}'),
                cf_ecs.build_ecs_container_insight_mem_widget(clusterName, serviceName, f'{clusterName}_{serviceName}'),
                cf_ecs.build_ecs_container_insight_storage_widget(clusterName, serviceName, f'{clusterName}_{serviceName}'),
                cf_ecs.build_ecs_container_insight_task_count_widget(clusterName, serviceName, f'{clusterName}_{serviceName}')
            )

        # ネットワークのダッシュボードを作成する。
        dashboard = cw.Dashboard(self, id="rDashboardNW", dashboard_name="Dashboard-Network")
        for instanceid_index in range(len(clb_name)):
            dashboard.add_widgets(
                cf_nw.build_clb_count_widget(clb_name[instanceid_index]),
                cf_nw.build_clb_count2_widget(clb_name[instanceid_index]),
                cf_nw.build_clb_length_widget(clb_name[instanceid_index]),
                cf_nw.build_clb_code_widget(clb_name[instanceid_index]),
            )

        for instanceid_index in range(len(alb_name)):
            dashboard.add_widgets(
                cf_nw.build_alb_count_widget(alb_name[instanceid_index]),
                cf_nw.build_alb_byte_widget(alb_name[instanceid_index]),
                cf_nw.build_alb_code_widget(alb_name[instanceid_index]),
                cw.TextWidget(markdown='', height=6)
            )

        for instanceid_index in range(len(tgw_name)):
            dashboard.add_widgets(
                cf_nw.build_transitgateway_byte_widget(tgw_name[instanceid_index]),
                cf_nw.build_transitgateway_packet_widget(tgw_name[instanceid_index]),
                cf_nw.build_transitgateway_count_widget(tgw_name[instanceid_index]),
                cw.TextWidget(markdown='', height=6)
            )

        for instanceid_index in range(len(cloudFront_name)):
            DistributionId = cloudFront_name[instanceid_index]
            dashboard.add_widgets(
                cf_nw.build_cloudFront_errorRate_widget(DistributionId),
                cf_nw.build_cloudFront_bytes_widget(DistributionId),
                cf_nw.build_cloudFront_requests_widget(DistributionId),
                cw.TextWidget(markdown='', height=6)
            )

        # RDSのダッシュボードを作成する。
        dashboard = cw.Dashboard(self, id="rDashboardDB", dashboard_name="Dashboard-Database")
        for instanceid_index in range(len(rds_name)):
            DBClusterIdentifier = rds_name[instanceid_index]
            dashboard.add_widgets(
                cf_rds.build_aurora_writer_rep_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_mem_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_bq_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_nw_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_io_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_disk_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_queue_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_instance_widget(DBClusterIdentifier),
                cf_rds.build_aurora_writer_cpu_widget(DBClusterIdentifier),

                cf_rds.build_aurora_reader_rep_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_mem_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_bq_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_nw_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_io_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_disk_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_queue_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_instance_widget(DBClusterIdentifier),
                cf_rds.build_aurora_reader_cpu_widget(DBClusterIdentifier),

                cf_rds.build_aurora_rep_widget(DBClusterIdentifier),
                cf_rds.build_aurora_bk_widget(DBClusterIdentifier),
                cf_rds.build_aurora_disk_widget(DBClusterIdentifier),
                cf_rds.build_aurora_io_widget(DBClusterIdentifier),
                cf_rds.build_aurora_bill_widget(DBClusterIdentifier)
            )

        # S3のダッシュボードを作成する。
        dashboard = cw.Dashboard(self, id="rDashboardS3", dashboard_name="Dashboard-S3")
        for instanceid_index in range(len(s3_name)):
            BucketName = s3_name[instanceid_index]
            dashboard.add_widgets(
                cf_s3.build_s3_size_widget(BucketName),
                cf_s3.build_s3_number_widget(BucketName)
            )


app = core.App()
Dashboard(app, "Dashboard")

app.synth()
