import os


def test_key():
  assert(os.environ['SS'] == "here")
