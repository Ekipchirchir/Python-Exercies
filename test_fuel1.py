from fuel import convert, gauge

def test_convert():
    assert convert('3/4')==75
    assert convert('1/2')==50
    assert convert('0/2')==0
    assert convert('5/5')==100
    with pytest.raises(ValueError):
        convert('1.5/2')
    with pytest.raises(ValueError):
        convert('2/1')
    with pytest.raises(ValueError):
        convert('2/0')
        
def test_gauge():
    assert gauge(0)=="E"
    assert gauge(1)== "E"
    assert gauge(50)=="50%"
    assert gauge(99)=="F"
    assert gauge(100)=="F"