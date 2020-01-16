import sys
import os
import re


def create_template():
    """
    CloudWatchのCloudFormationテンプレート作成処理。
    「cdk synth」を実行し、CloudFormationテンプレートの標準出力を
    「CFn_COM_3_CloudWatch_Logs_00.yaml」に出力する。

    次に「CDK_COM_3_CloudWatch_Logs_app.py」のヘッダコメントを読取り、
    「CFn_COM_3_CloudWatch_Logs_00.yaml」のトップに追記する。

    """
    os.system("cdk synth > CFn_COM_3_CloudWatch_Logs_00.yaml")
    text = []

    with open("CDK_COM_3_CloudWatch_Logs_app.py", encoding='UTF-8') as f:
        for line in f:
            if re.match(r'\#', line):
                output = line.rstrip('\n')
                text.append(output)

    comment = '\n'.join(text)+'\n'

    with open("CFn_COM_3_CloudWatch_Logs_00.yaml", "r+", encoding='UTF-8') as f:
        a = f.read()

        with open("CFn_COM_3_CloudWatch_Logs_00.yaml", "w+", encoding='UTF-8') as f:
            f.write(comment + a)

create_template()
