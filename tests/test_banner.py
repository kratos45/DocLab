from doclab.banner import get_banner
 
def test_banner_is_not_empty():
    assert get_banner() != ""
 
def test_banner_mentions_name():
    assert "DocLab" in get_banner()
