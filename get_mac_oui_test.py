from get_mac_oui import get_mac_oui

def test_get_mac_oui_1():
    print("\nTest 1: ")
    oui = get_mac_oui("d46a.3542.2800")
    assert oui == "Cisco Systems, Inc"
    print("\nOUI is :" + oui)

def test_get_mac_oui_2():
    print("\nTest 4: ")
    oui = get_mac_oui("d4ddddd")
    assert oui is None
    print("\nOUI is :" +str(oui))
    
def test_get_mac_oui_3():
    print("\nTest 3: ")
    oui = get_mac_oui("d4")
    assert oui is None
    print("\nOUI is :" +str(oui))
    
def test_get_mac_oui_4():
    print("\nTest 4: ")
    oui = get_mac_oui("4c:8d:79:00:01:02")
    assert oui == "Apple, Inc"
    print("\nOUI is :" +oui)