# Завдання1:
import pytest

def test_palindrom_empty():
    assert palindrom("") == []

def test_palindrom_not_string():
    assert palindrom(123) == []

def test_palindrom_no_palindromes():
    assert palindrom("hello world") == []

def test_palindrom_even_palindromes():
    assert palindrom("level noon rotor") == ['level', 'noon', 'rotor']

def test_palindrom_odd_palindromes():
    assert palindrom("radar deed civic") == ['radar', 'deed', 'civic']

def test_palindrom_mixed_case_palindromes():
    assert palindrom("MaDAm abBa palindromic Rotor") == ['MaDAm', 'abBa', 'palindromic', 'Rotor']
    
    
#Завдання2:
def test_validate_ip():
    # Перевірка порожнього рядка
    assert validate_ip("") == False
    
    # Перевірка неправильного формату IP-адреси
    assert validate_ip("192.168.1.256") == False
    
    # Перевірка правильного формату IP-адреси
    assert validate_ip("192.168.1.1") == True
    
    # Додаткові перевірки формату IP-адреси
    
    # Перевірка неправильного формату IP-адреси з мережею
    assert validate_ip("192.168.1.1/24") == False
    
    # Перевірка правильного формату IP-адреси з мережею
    assert validate_ip("192.168.1.1/24") == True
    
    # Перевірка правильного формату IP-адреси з мережею
    assert validate_ip("10.0.0.0/8") == True
    

#Завдання3:
def test_get_os():
    os_name = platform.system()
    assert get_os() == os_name
