import morphs
import pytest


@pytest.mark.run(order=2)
def test_shuffle_endpoints():
    assert len(morphs.paths.blocks()) > 0
    block_path = morphs.paths.blocks()[0]
    assert morphs.paths.ACCURACIES_PKL.exists()
    accuracies, cluster_accuracies = morphs.data.accuracies.load_cluster_accuracies()
    cluster = cluster_accuracies[block_path].index[-1]
    spikes = morphs.data.load.ephys(block_path, good_clusters=[cluster],
                                    shuffle_endpoints=True)
    assert len(spikes) > 0
