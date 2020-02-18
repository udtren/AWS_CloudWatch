import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

class CDKDashboard:
    def build_aurora_writer_rep_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='RDSToAuroraPostgreSQLReplicaLag',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_writer_mem_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='BufferCacheHitRatio',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='FreeableMemory',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_writer_bq_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='MaximumUsedTransactionIDs',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
            ]
        )
        return wid

    def build_aurora_writer_nw_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='NetworkReceiveThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='NetworkThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='NetworkTransmitThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_writer_io_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='DiskQueueDepth',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='ReadIOPS',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='ReadLatency',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='ReadThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='WriteIOPS',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='WriteLatency',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='WriteThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='DatabaseConnections',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_writer_disk_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='FreeLocalStorage',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='SwapUsage',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_writer_queue_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='CommitLatency',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='CommitThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='Deadlocks',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_writer_instance_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='EngineUptime',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
            ]
        )
        return wid

    def build_aurora_writer_cpu_widget(cls, DBClusterIdentifier, Role='WRITER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='CPUUtilization',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
            ]
        )
        return wid

    # ---------------------------------------------------------------------------

    def build_aurora_reader_rep_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='RDSToAuroraPostgreSQLReplicaLag',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_reader_mem_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='BufferCacheHitRatio',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='FreeableMemory',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_reader_bq_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='MaximumUsedTransactionIDs',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
            ]
        )
        return wid

    def build_aurora_reader_nw_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='NetworkReceiveThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='NetworkThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='NetworkTransmitThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_reader_io_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='DiskQueueDepth',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='ReadIOPS',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='ReadLatency',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='ReadThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='WriteIOPS',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='WriteLatency',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='WriteThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='DatabaseConnections',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_reader_disk_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='FreeLocalStorage',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='SwapUsage',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_reader_queue_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='CommitLatency',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
                cw.Metric(namespace='AWS/RDS', metric_name='CommitThroughput',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='Deadlocks',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role}, ),
            ]
        )
        return wid

    def build_aurora_reader_instance_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='EngineUptime',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
            ]
        )
        return wid

    def build_aurora_reader_cpu_widget(cls, DBClusterIdentifier, Role='READER'):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='CPUUtilization',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier, 'Role': Role},),
            ]
        )
        return wid

    # ---------------------------------------------------------------------------

    def build_aurora_rep_widget(cls, DBClusterIdentifier):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='AuroraReplicaLag',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='AuroraReplicaLagMaximum',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier}, ),
                cw.Metric(namespace='AWS/RDS', metric_name='AuroraReplicaLagMinimum',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier}, ),
            ]
        )
        return wid

    def build_aurora_bk_widget(cls, DBClusterIdentifier):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='BackupRetentionPeriodStorageUsed',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier},),
                cw.Metric(namespace='AWS/RDS', metric_name='SnapshotStorageUsed',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier}, ),
            ]
        )
        return wid

    def build_aurora_disk_widget(cls, DBClusterIdentifier):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='TransactionLogsDiskUsage',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier},),
                cw.Metric(namespace='AWS/RDS', metric_name='VolumeBytesUsed',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier}, ),
            ]
        )
        return wid

    def build_aurora_io_widget(cls, DBClusterIdentifier):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='VolumeWriteIOPs',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier},),
            ]
        )
        return wid

    def build_aurora_bill_widget(cls, DBClusterIdentifier):
        wid = cw.GraphWidget(
            title='AWS/RDS',
            left=[
                cw.Metric(namespace='AWS/RDS', metric_name='TotalBackupStorageBilled',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier},),
                cw.Metric(namespace='AWS/RDS', metric_name='VolumeReadIOPs',
                          dimensions={'DBClusterIdentifier': DBClusterIdentifier}, ),
            ]
        )
        return wid

