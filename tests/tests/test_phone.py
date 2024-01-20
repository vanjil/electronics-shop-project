from phone import Phone

def test_phone_addition():
    phone1 = Phone("iPhone", 1000, 5, 2)
    phone2 = Phone("Samsung", 800, 3, 1)

    result_phone = phone1 + phone2
    assert result_phone.quantity == 8

def test_invalid_addition():
    phone = Phone("iPhone", 1000, 5, 2)
    non_phone_item = "Not a Phone"

    with pytest.raises(TypeError):
        result = phone + non_phone_item
