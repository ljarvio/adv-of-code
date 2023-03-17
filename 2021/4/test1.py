import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

def read_bingo_data(datafile):
    # cat data.txt.orig | sed -e's/^\s*//' | sed 's/  / /g' > data.txt
    with open(datafile) as f:
        first_line = next(f)
        lines = f.read()
        squares = [ s for s in lines.split("\n\n") ]

    guesses = first_line.strip().split(',')
    guesses = [int(g) for g in guesses]
    df_list = [ pd.DataFrame(sq.split('\n')) for sq in squares ]
    df_list2 = []
    for df in df_list:
        df = df[0].str.split(" ", expand=True)
        df = df.dropna()
        df = df.astype(int)
        df_list2.append(df)
    return guesses, df_list2

def is_it_bingo(df):
    col_bingo = any(df.sum() == 0)
    row_bingo = any(df.T.sum() == 0)
    if col_bingo or row_bingo:
        return True
    else:
        return False

guesses, dfs = read_bingo_data('data.txt')
for g in guesses:
    logging.debug(f"guess = {g}")

    for i, d in enumerate(dfs):
        d = d.replace(g, 0)
        dfs[i] = d
        if is_it_bingo(d):
                s = d.values.sum()
                logging.debug(f"bingo at df = \n {d} \n with guess g = {g}")
                logging.debug(f"sum of non-matching elements s = {s}")

                logging.info(f"ANSWER = {s*g}")
                exit()

