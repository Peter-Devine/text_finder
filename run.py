from embedding import encode_text
from interface import create_html
from similarity import get_pairwise_dist

import pandas as pd
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--text_csv_dir', default="", required=True, type=str, help='The directory where your csv containing text that you would like to browse is in.')
    parser.add_argument('--csv_text_column_name', default="text", required=False, type=str, help='The name of the column in your csv file that contains the text you would like to browse. (Defaults to "text")')
    parser.add_argument('--output_dir', default="./text_browser", required=False, type=str, help='The directory that you would like the tool to output the resulting .html file to. (Defaults to "./text_browser.html")')

    args = parser.parse_args()

    text_df = pd.read_csv(args.text_csv_dir)

    text_list = text_df[args.csv_text_column_name]

    encoding = encode_text(text_list)

    distances = get_pairwise_dist(encoding)

    create_html(distances, text_list,  args.output_dir, num_similar_shown=30)
