from moyenne import moyenne

def test_moyenne():
    data = [1,2,3]

    result = moyenne(data)

    assert result == 3
