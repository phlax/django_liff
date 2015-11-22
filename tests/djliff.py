import os

import pytest

from djangoliff import PyLIFF


EXAMPLES = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__),
        "data/examples"))


@pytest.mark.test
def test_djangoliff_init():
    with open(os.path.join(EXAMPLES, "xliff/metadata.xliff")) as f:
        li = PyLIFF(f.read().decode("utf-8"))
    files = li.files

    for f in files:
        for note in f.notes:
            print note.id

        for unit in f.units:
            for segment in unit.segments:
                text = segment.source.text

        for group in f.groups:
            import pdb; pdb.set_trace()

    li.src.serialize()
