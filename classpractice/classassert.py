
def average_gpa(gpas):

    assert type(gpas) == list or type(gpas) == tuple
    assert len(gpas) != 0

    sum = 0
    for gpa in gpas:
        assert type(gpa) == float
        assert 0 <= gpa <= 4.0
        
        sum += gpa
        assert sum >= 0.0

    average = sum / len(gpas)
    assert 0 <= average <= 4.0

    return average