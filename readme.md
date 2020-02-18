#### AWS CDK(Python)を使用し、CW DashboardとLogGroupのCloudFormationテンプレートを作成する。

■ CloudWatch_Dashboard

・CloudWatch_app.py

  メイン処理。Dashboardの作成とWidgetの追加を行う。
  
・widget_.py

  各サービスのMetricとWidgetを定義する。
  
・CloudWatch.py

  <code>python CloudWatch.py</code>でCloudFormationテンプレートを作成する。
