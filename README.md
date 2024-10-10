# amazon-sagemaker-examples
Amazon SageMakerのサンプルコード

## ディレクトリ構成

```markdown
training/
├── data_loader.py
├── decorators.py
├── model.py
├── requirements.txt
├── train.py
└── utils.py
```

## ファイルの役割

### [train.py](training/train.py)
- 役割: SageMakerで実行するためのメインスクリプト。
- 特徴: 全プロジェクトで共通のコードを含み、変更は加えません。
- 機能:
  - 引数のパースと設定。
  - 学習データの読み込み。
  - モデルの定義。
  - モデルの学習プロセスの開始。

### [data_loader.py](training/data_loader.py)
- 役割: データの読み込みと基本的な前処理を行う。
- 特徴: プロジェクトごとに学習に利用するデータを定義。
- 機能:
  - データセットの読み込み。
  - データの分割やシャッフルなどの基本的な処理。

### [decorators.py](training/decorators.py)
- 役割: プロジェクト特有の引数を追加するためのデコレータを定義。
- 特徴: train.pyの引数パーサーに追加の引数を簡潔に追加。
- 機能:
  - @project_decoratorデコレータを使用して、プロジェクト固有の引数をパーサーに追加。

### [model.py](training/model.py)
- 役割: モデルの定義とトレーニングのロジックを含む。
- 特徴: プロジェクトごとに使用するモデルを定義。
- 機能:
  - モデルとトークナイザーの初期化。
  - トレーニング設定の定義。
  - トレーナーの作成とトレーニングの実行。
  - モデルの保存。

### [utils.py](training/utils.py)
- 役割: プロジェクト固有の補助関数を定義。
- 特徴: データの前処理やチェックポイントの保存などの関数を含む。
- 機能:
  - preprocess_functionによるデータの前処理。
  - 必要に応じて、その他のユーティリティ関数を追加。

## [requirements.txt](training/requirements.txt)
- 役割: プロジェクトで使用するPythonパッケージを列挙。
- 特徴: pipで一括インストールが可能。
- 機能:
  - transformers、datasetsなどの必要なライブラリを指定。

---

## カスタマイズ方法

- プロジェクト特有の引数の追加
    - decorators.pyのproject_decorator関数に引数を追加します。
- その他のユーティリティ関数の追加
    - utils.pyに新しい関数を定義し、必要なモジュールでインポートして使用します。

## 注意点

- train.pyの編集は禁止
  - train.pyは全プロジェクトで共通のため、変更を加えないでください。
- model.py、data_loader.py、decorators.pyに新しい関数の追加は禁止
  - utils.pyに関数を追加することで対応します。
- コードの再利用性
  - プロジェクト固有の変更は、model.py、data_loader.py、decorators.py、utils.pyの編集で対応します。
- 新しいユーザーへの配慮
  - 変更すべき点を明確にし、理解しやすいコード構成を心がけています。