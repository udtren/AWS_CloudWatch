import sys
import os
import re


def create_template():
    """
    CloudWatchのCloudFormationテンプレート作成処理。
    「cdk synth」を実行し、CloudFormationテンプレートの標準出力を
    「CloudWatch_Logs.yaml」に出力する。

    次に「CloudWatch_Logs_app.py」のヘッダコメントを読取り、
    「CloudWatch_Logs.yaml」のトップに追記する。

    """
    os.system("cdk synth > CloudWatch_Logs.yaml")
    text = []

    with open("CloudWatch_Logs_app.py", encoding='UTF-8') as f:
        for line in f:
            if re.match(r'\#', line):
                output = line.rstrip('\n')
                text.append(output)

    comment = '\n'.join(text)+'\n'

    with open("CloudWatch_Logs.yaml", "r+", encoding='UTF-8') as f:
        a = f.read()

        with open("CloudWatch_Logs.yaml", "w+", encoding='UTF-8') as f:
            f.write(comment + a)

create_template()
