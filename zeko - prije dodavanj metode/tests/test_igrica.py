from pytest import *
from src.igrica import *

# def test_performAction(capsys, monkeypatch):
	# monkeypatch.setattr('path.to.yourmodule.input', lambda: 'no')
	# assert performAction("sakriti") == "smrt"
	
def test_performAction():
	assert performAction("sakriti") == "smrt"