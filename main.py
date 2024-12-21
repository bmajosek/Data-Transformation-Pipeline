import pandas as pd
import argparse
from pipeline import TransformationPipeline

def parse_args():
    """
    Parses command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(description='Process a DataFrame with specified transformations.')
    parser.add_argument('model_name', type=str, help='Model name from HuggingFace')
    parser.add_argument('command', type=str, help='Command to execute on the DataFrame')
    parser.add_argument('path_to_csv', type=str, help='Path to the CSV file')
    parser.add_argument('api_token', type=str, help='Hugging Face API token')
    return parser.parse_args()

def main(args):
    """
    Main function to load the DataFrame, apply transformations, and print the result.
    """
    df = pd.read_csv(args.path_to_csv)
    pipeline = TransformationPipeline(
        df, args.model_name, args.api_token
    )
    df_transformed = pipeline.run(args.command)
    print(df_transformed)

if __name__ == "__main__":
    args = parse_args()
    main(args)
