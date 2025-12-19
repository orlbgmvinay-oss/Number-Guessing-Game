import os
import json
from pathlib import Path
import storage

SCORE_PATH = Path(__file__).with_name('..').resolve() / 'highest_score.json'


def test_save_and_load_and_reset(tmp_path, monkeypatch):
    # point storage to temp file
    p = tmp_path / 'hs.json'
    monkeypatch.setattr(storage, 'SCORE_PATH', p)

    try:
        storage.reset_best_score()
        assert storage.load_best_score() is None

        storage.save_best_score(5)
        data = storage.load_best_score()
        assert data is not None
        assert data[0] == 5
        assert isinstance(data[1], str)

        storage.reset_best_score()
        assert storage.load_best_score() is None
    finally:
        if p.exists():
            p.unlink()