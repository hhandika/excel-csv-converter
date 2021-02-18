import click

from ecc import utils

@click.command()
@click.option('--dir', '-d', help="Add dir to the files")
def main(dir):
    fpath = dir + "/*.xlsx"
    files = utils.find_files(fpath)
    utils.convert_excel_to_csv(files)
    print("DONE!")