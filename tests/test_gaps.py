import pytest

def test_replay_is_open_gap():
    from src.streamgrab import replay
    with pytest.raises(NotImplementedError):
        replay.process({"id": "x"})

def test_window_agg_is_open_gap():
    from src.streamgrab import window_agg
    with pytest.raises(NotImplementedError):
        window_agg.process({"id": "x"})
