'''Path definitions'''
from pathlib2 import Path
from glob import glob
import morphs

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "data"
EPHYS_DIR = DATA_DIR / 'ephys'
PROCESSED_DIR = DATA_DIR / "processed"
ACCURACIES_PKL = PROCESSED_DIR / "all_accuracies.pkl"


def blocks():
    '''
    Returns a list of different block paths that correspond to each
    electrophysiological recording Ive done. Understands if this is
    being run with local access to data.
    '''
    if morphs.parallel.is_local():
        block_path_template = '/mnt/cube/mthielk/analysis/%s/kwik/*'
    else:
        block_path_template = EPHYS_DIR.as_posix() + '/%s/kwik/*'

    blocks = []
    for subj in morphs.subj.EPHYS_SUBJS:
        blocks += glob(block_path_template % (subj,))
    return blocks
