import re

from aws_cdk import core
from aws_cdk.core import RemovalPolicy
from aws_cdk import (
    aws_logs as logs,
)
from aws_cdk.aws_logs import RetentionDays

retention = {
    "EIGHTEEN_MONTHS": RetentionDays.EIGHTEEN_MONTHS,
    "FIVE_DAYS": RetentionDays.FIVE_DAYS,
    "FIVE_MONTHS": RetentionDays.FIVE_MONTHS,
    "FIVE_YEARS": RetentionDays.FIVE_YEARS,
    "FOUR_MONTHS": RetentionDays.FOUR_MONTHS,
    "INFINITE": RetentionDays.INFINITE,
    "ONE_DAY": RetentionDays.ONE_DAY,
    "ONE_MONTH": RetentionDays.ONE_MONTH,
    "ONE_WEEK": RetentionDays.ONE_WEEK,
    "ONE_YEAR": RetentionDays.ONE_YEAR,
    "SIX_MONTHS": RetentionDays.SIX_MONTHS,
    "TEN_YEARS": RetentionDays.TEN_YEARS,
    "THIRTEEN_MONTHS": RetentionDays.THIRTEEN_MONTHS,
    "THREE_DAYS": RetentionDays.THREE_DAYS,
    "THREE_MONTHS": RetentionDays.THREE_MONTHS,
    "TWO_MONTHS": RetentionDays.TWO_MONTHS,
    "TWO_WEEKS": RetentionDays.TWO_WEEKS,
    "TWO_YEARS": RetentionDays.TWO_YEARS,
}

removal = {
    "DESTROY": RemovalPolicy.DESTROY,
    "RETAIN": RemovalPolicy.RETAIN,
}

class CloudWatchLogs(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        """
        LogGroup作成のメイン処理。
        「loggroup.txt」の各行の設定値を読取り、1行ずつLogGroupを1つ作成する。

        「loggroup.txt」の各行の内容は以下となる。
        CloudFormationのリソースID,LogGroupの名前,削除ポリシー,保持期間
        例：/var/log/messages,/var/log/messages,RETAIN,THREE_MONTHS
        """
        with open("loggroup.txt") as f:
            for line in f:
                if line not in ['\n', '\r\n']:
                    id_ = line.split(',')[0].rstrip('\n')
                    log_group_name_ = line.split(',')[1].rstrip('\n')
                    removal_policy_ = line.split(',')[2].rstrip('\n')
                    retention_ = line.split(',')[3].rstrip('\n')

                    Loggroup = logs.LogGroup(self, id=id_, log_group_name=log_group_name_, removal_policy=removal[removal_policy_], retention=retention[retention_])

app = core.App()
CloudWatchLogs(app, "CloudWatchLogs")

app.synth()
