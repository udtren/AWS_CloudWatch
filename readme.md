#### AWS CDK(Python)を使用し、CW DashboardとLogGroupのCloudFormationテンプレートを作成する。

■ CloudWatch_Dashboard

・CloudWatch_app.py

  メイン処理。Dashboardの作成とWidgetの追加を行う。
  
・widget_.py

  各サービスのMetricとWidgetを定義する。
  
 ・resource.txt
 
  サービスごとのMetric作成に必要の値を記入する。
  
  Formatは サービス名,サービス識別子のExport名,<一部サービスはNamespaceも記載>
  
・CloudWatch.py

  <code>python CloudWatch.py</code>でCloudFormationテンプレートを作成する。
