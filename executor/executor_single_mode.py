import argparse
from executor_class import performance_and_accuracy_test_single_mode

def main():
    args = parse_args()
    performance_and_accuracy_test_single_mode(args.model_file, args.batch_size, args.warmup, args.repeats, args.paddle_predictor_type, args.openvino_api_type)

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--model_file", type=str, default='', help="model filename, default(None)")
    parser.add_argument("--batch_size", type=int, default=1, help="batch size, default(1)")
    parser.add_argument("--warmup", type=int, default=0, help="warm up inference, default(0)")
    parser.add_argument("--repeats", type=int, default=1, help="repeat number of inference, default(1)")
    parser.add_argument("--openvino_api_type", type=str, default='sync', choices=['sync', 'async'], help="select openvino inference api type, default(sync)")
    parser.add_argument("--paddle_predictor_type", type=str, default='normal', choices=['normal', 'nlp'], help="select paddle predictor type, default(normal)")
    return parser.parse_args()

if __name__ == "__main__":
    main()


# usage:
# NLP
# python3 executor_single_mode.py --model_file=../exporter/paddlenlp/bert-base-cased/model.pdmodel --paddle_predictor_type=nlp --batch_size=1 --warmup=1 --repeats=10