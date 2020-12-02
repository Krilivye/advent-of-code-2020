from day2 import OfficialToboganCorporatePolicy, CorporatePolicy


def test_unitaire():
    corp = OfficialToboganCorporatePolicy("1-3 a")
    assert corp.match("abcde") is True
    assert corp.match("cdefg") is False
    assert corp.match("cdafg") is True

    corp = OfficialToboganCorporatePolicy("2-9 c")
    assert corp.match("ccccccccc") is False


if __name__ == "__main__":
    print(CorporatePolicy("1-3 a"))
    print(OfficialToboganCorporatePolicy("1-3 a"))
