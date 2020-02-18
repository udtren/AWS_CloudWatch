import sys
import os
import re


def create_template():
    """
    CloudWatchのCloudFormationテンプレート作成処理。
    「cdk synth」を実行し、CloudFormationテンプレートの標準出力を
    「CDK_DEV_3_CloudWatch_00.yaml」に出力する。

    次に「app.py」のヘッダコメントを読取り、
    「CDK_DEV_3_CloudWatch_00.yaml」のトップに追記する。

    """
    os.system("cdk synth > CloudWatch_Dashboard.yaml")
    text = []

    with open("CloudWatch_app.py", encoding='UTF-8') as f:
        for line in f:
            if re.match(r'\#', line):
                output = line.rstrip('\n')
                text.append(output)

    comment = '\n'.join(text)+'\n'

    with open("CloudWatch_Dashboard.yaml", "r+", encoding='UTF-8') as f:
        a = f.read()

        with open("CloudWatch_Dashboard.yaml", "w+", encoding='UTF-8') as f:
            f.write(comment + a)

create_template()
