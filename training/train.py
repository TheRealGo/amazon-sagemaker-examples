import argparse
import os
import subprocess
from pathlib import Path

from data_loader import load_data
from decorators import project_decorator
from model import Model


@project_decorator
def parse_args():
    # 全プロジェクト共通の引数
    parser = argparse.ArgumentParser()

    # ハイパーパラメータ
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--learning-rate", type=float, default=1e-5)
    parser.add_argument("--use-cuda", type=bool, default=False)

    parser.add_argument("--output-data-dir", type=str, default=os.environ["SM_OUTPUT_DATA_DIR"])
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])
    parser.add_argument("--train", type=str, default=os.environ["SM_CHANNEL_TRAIN"])
    parser.add_argument("--test", type=str, default=os.environ["SM_CHANNEL_TEST"])

    return parser

if __name__ == '__main__':
    # requirements.txtを--no-depsオプションでインストール
    subprocess.check_call(['pip', 'install', '--no-deps', '-r', 'requirements.txt'])

    # 引数の設定
    parser = parse_args()
    args, _ = parser.parse_known_args()
    print(args)

    result = "Epochs: {}, Batch size: {}, Learning rate: {}, Use CUDA: {}".format(
        args.epochs, args.batch_size, args.learning_rate, args.use_cuda
    )

    with open(Path(args.output_data_dir).joinpath("results.txt"), "w") as f:
        f.write(result)

    # 学習データの読み込み
    train_data, test_data = load_data(args.train, args.test)

    # モデルの定義
    model = Model(args)

    # モデルの学習
    model.train(train_data, test_data)

    with open(Path(args.model_dir).joinpath("model.pth"), "w") as f:
        f.write("MODEL")