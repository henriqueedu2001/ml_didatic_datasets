import argparse
import sys

ML_TASKS = [
    'linear_regression',
    'logistic_regression',
    'classification',
    'clustering'
]

def parse_args(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='ML Didatic Datasets',
        description='A generator of machine learning datasets, for didatic purposes',
        epilog='',
        exit_on_error=False,
    )
    
    # possible parameters: ml_task, directory, name, size, dimensions, noise, lineary_separable
    
    # machine learning task
    parser.add_argument('--ml-task', dest='ml_task', type=str, required=True, choices=ML_TASKS,
                        help='the machine learning task')
    
    # the directory to save the dataset
    parser.add_argument('--directory', dest='directory', type=str, required=True,
                        help='the directory to save the dataset')
    
    # the name of the dataset
    parser.add_argument('--name', dest='name', type=str, required=False,
                        help='the name of the dataset')
    
    # size of the dataset
    parser.add_argument('--size', dest='size', type=int, default=50, required=False,
                        help='the size of the dataset (50 per default)')
    
    # number of dimensions
    parser.add_argument('--dim', dest='dimensions', type=int, required=False,
                        help='number of dimensions of feature space')
    
    # generate or not noise in the dataset
    parser.add_argument('--noise', dest='noise', type=bool, default=True, required=False,
                        help='generate or not noise in the dataset')
    
    # lineary_separable
    parser.add_argument('--lin-sep', dest='lineary_separable', type=bool, default=True, required=False,
                        help='')
    
    return parser.parse_args(args)


def generate_dataset(args: argparse.Namespace):
    """Generates a dataset for the given machine learning task

    Args:
        args (argparse.Namespace): arguments for the dataset creation
    """
    
    ml_task = args.ml_task
    directory = args.directory
    name = args.name
    size = args.size
    dimensions = args.dimensions
    noise = args.noise
    lineary_separable = args.lineary_separable
    
    print(f'''Generating the dataset "{name}" with the given configs:
    -> ml_task: {ml_task}
    -> directory: {directory}
    -> size: {size}
    -> dimensions: {dimensions}
    -> noise: {noise}
    -> lineary_separable: {lineary_separable}''')
    
    return

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    generate_dataset(args)
