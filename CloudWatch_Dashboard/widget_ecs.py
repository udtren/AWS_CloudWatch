import re
from aws_cdk import (
    aws_cloudwatch as cw,
    core
)

class CDKDashboard:
    def build_ecs_service_cpu_widget(cls, ClusterName, ServiceName, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} CPU',
            left=[
            cw.Metric(namespace='AWS/ECS',metric_name='CPUUtilization',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName},),
            ]
        )
        return wid

    def build_ecs_service_mem_widget(cls, ClusterName, ServiceName, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Memory',
            left=[
            cw.Metric(namespace='AWS/ECS',metric_name='MemoryUtilization',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName},),
            ]
        )
        return wid

    def build_ecs_container_insight_cpu_widget(cls, ClusterName, ServiceName, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} CPU',
            left=[
            cw.Metric(namespace='ECS/ContainerInsights',metric_name='CpuReserved',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName},),
            cw.Metric(namespace='ECS/ContainerInsights', metric_name='CpuUtilized',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
            ]
        )
        return wid

    def build_ecs_container_insight_mem_widget(cls, ClusterName, ServiceName, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Memory',
            left=[
            cw.Metric(namespace='ECS/ContainerInsights',metric_name='MemoryUtilized',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName},),
            cw.Metric(namespace='ECS/ContainerInsights', metric_name='MemoryReserved',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
            ]
        )
        return wid

    def build_ecs_container_insight_storage_widget(cls, ClusterName, ServiceName, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Storage',
            left=[
            cw.Metric(namespace='ECS/ContainerInsights',metric_name='StorageReadBytes',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName},),
            cw.Metric(namespace='ECS/ContainerInsights', metric_name='StorageWriteBytes',
                      dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
            ]
        )
        return wid

    def build_ecs_container_insight_task_count_widget(cls, ClusterName, ServiceName, namespace):
        wid = cw.GraphWidget(
            title=f'{namespace} Task Count',
            left=[
                cw.Metric(namespace='ECS/ContainerInsights',metric_name='PendingTaskCount',
                          dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName},),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='RunningTaskCount',
                          dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='DesiredTaskCount',
                          dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='TaskSetCount',
                          dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='DeploymentCount',
                          dimensions={'ServiceName': ServiceName, 'ClusterName': ClusterName}, ),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='ServiceCount',
                          dimensions={'ServiceName': ServiceName}, ),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='TaskCount',
                          dimensions={'ServiceName': ServiceName}, ),
                cw.Metric(namespace='ECS/ContainerInsights', metric_name='ContainerInstanceCount',
                          dimensions={'ServiceName': ServiceName}, ),
            ]
        )
        return wid