import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%Y-%m-%d %I:%M:%S',)

with open('data.txt') as f:
        data = f.read().splitlines()
# explode every row of '101' -> ['1', '0', '1']
data_list = [ list(e) for e in data ]
# read list of lists into pandas
df = pd.DataFrame(data_list)
# describe() reveals most common characters in 'top'
desc = df.describe().T
# convert to numeric to calculate negation 
desc['gamma'] = pd.to_numeric(desc['top'])
# negation (=least common char)
desc['epsilon'] = 1 - desc['gamma'] 

descT = desc.T
# join 0 & 1 into one string
descT['concat'] = descT[descT.columns].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
# bin2dec
gamma = int(descT['concat'].loc['gamma'], 2)
epsilon = int(descT['concat'].loc['epsilon'], 2)
logging.debug(f"gamma = {gamma}")
logging.debug(f"epsilon = {epsilon}")
print(f"ANSWER = {gamma*epsilon}")