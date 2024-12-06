# SAM_SNS_SQS_Lambda_Stack_Sample

AWS SAM を使用して、SNS トピック、SQS キュー (およびデッドレターキュー)、および Lambda 関数をデプロイするためのサンプルプロジェクトです。

## プロジェクト構成

```bash
SAM_SNS_SQS_Lambda_Stack_Sample
├── parameters/
│   └── samconfig.yaml ・・・手動デプロイ用の設定ファイルです。パラメータも記載しています。
├── templates/
│   ├── root-template.yaml ・・・テンプレートを統合するためのルートテンプレートです。
│   ├── sqs.yaml ・・・デッドレターキューと SQS キューを作成するテンプレートです。
│   ├── sns.yaml ・・・SNS トピックを作成するテンプレートです。
│   └── lambda.yaml ・・・Lambda 関数を作成するテンプレートです。
└── functions/
    └── app.py ・・・SQS メッセージを処理する Lambda 関数のコードです。
```

## 手動デプロイ

以下のコマンドを使用して、CloudFormation スタックをデプロイします。

```bash
sam build --template-file templates/root-template.yaml
sam package --template-file templates/root-template.yaml --s3-bucket <YOUR_S3_BUCKET> --output-template-file packaged-template.yaml
sam deploy --template-file packaged-template.yaml --config-file parameters/samconfig.yaml
```

## 削除

不要になったリソースを削除するには、以下のコマンドを実行します。

```bash
aws cloudformation delete-stack --stack-name <YOUR_STACK_NAME>
```

## Output

| キー        | 説明                             | エクスポート名 |
| ----------- | -------------------------------- | -------------- |
| SNSTopicArn | The ARN of the SNS Topic         | MySNSTopicArn  |
| SQSQueueArn | The ARN of the SQS Queue         | MySQSQueueArn  |
| DLQArn      | The ARN of the Dead Letter Queue | MyDLQArn       |
