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
    df_list = [pd.DataFrame(sq.split('\n')) for sq in squares]
    for i, df in enumerate(df_list):
        # 5x1 -> 5x5 
        df = df[0].str.split(" ", expand=True)
        df = df.dropna()
        df = df.astype(int)
        df_list[i] = df
    return guesses, df_list

def is_bingo(df):
    n = df.shape[0]
    # count if row or col has 5 x nans
    col_bingo = any(df.isna().sum() == n)
    row_bingo = any(df.T.isna().sum() == n)
    if col_bingo or row_bingo:
        return True
    else:
        return False

guesses, dfs = read_bingo_data('data.txt')

n_bingos = 0
# collect bingoed squares' indices
bingoed_indices = []
for g in guesses:
    logging.debug(f"guess = {g}")
    # change matches in all squares to NaN
    for i, d in enumerate(dfs):
        # skip those squares that already have a bingo
        if i in bingoed_indices: continue
        d = d.replace(g, np.nan)
        dfs[i] = d

        if is_bingo(d):
            n_bingos += 1
            # dont try to find bingos in this square anymore
            bingoed_indices.append(i)
            # sum of remaining numbers
            s = d.sum(skipna=True).sum()
            logging.debug(f"bingo at df({i}) = \n {d} \n with guess g = {g}")
            logging.debug(f"sum of non-matching elements s = {s}")
            logging.debug(f"bingos so far: {n_bingos}")
            if n_bingos == len(dfs):
                logging.info(f"That was the last bingo!")
                logging.info(f"ANSWER = {s*g}")
                exit()

