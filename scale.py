from argparse   import ArgumentParser
from csv        import reader, writer
from sklearn    import preprocessing

import numpy as np

def scale(dataset):
    with open(dataset) as csv_in, open(dataset[:5] + 's-' + dataset[5:], 'w') as csv_out:

        r = reader(csv_in)
        w = writer(csv_out)
        
        # Header
        w.writerow(next(r))

        d = np.array(list(r))

        # Separate Identifier Attributes
        ids, d = d[:,:2], d[:,2:].astype("float")
        
        c = (ids, preprocessing.scale(d[:,:18]), d[:,18:28], preprocessing.scale(d[:,28:]))

        for row in np.concatenate(c, axis=1): w.writerow(row)
            
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('dataset', type=str, help='CSV Dataset to be Normalized')
    args = parser.parse_args()

    if args.dataset: print(args.dataset); scale(args.dataset)
