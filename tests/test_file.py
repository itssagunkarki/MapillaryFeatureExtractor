import os


def test_key():
  assert(os.getenv('SS') == "here")
