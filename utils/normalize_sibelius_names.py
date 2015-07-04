import os
import re
import shutil
import argparse
import pdb


def main(sibelius_directory):
    if not sibelius_directory.endswith('/'):
        sibelius_directory = sibelius_directory + "/"

    for root, dirs, files in os.walk(sibelius_directory):
        foldername = os.path.basename(root)
        print(foldername)
        if not foldername:
            continue
        name = foldername.split("_")

        shelfmark = name[0]
        identifier = " ".join(name[0:])
        shelfmark_matcher = re.compile(r'(?P<src>[a-zA-Z0-9\.\-_]+)_(?P<pnum>[0-9]+)\.(?P<name>[a-zA-Z0-9\.])\.sib')
        for fl in files:
            if fl.startswith('.'):
                continue
            front = fl.split('.')[0]
            shelf = "_".join(front.split("_")[:-1])
            # print(len(front.split('_')))
            if len(front.split('_')) > 2:
                img = front.split('_')[2]
            else:
                img = front.split('_')[1]
            new_filename = "{0}__{1}.{2}.sib".format(shelfmark, img, "".join(fl.split('.')[1:-1]))
            print(fl, " --> ", new_filename)
            shutil.move(os.path.join(root, fl), os.path.join(root, new_filename))

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('sib', help="Path to the Sibelius files directory")

    args = parser.parse_args()

    main(args.sib)
