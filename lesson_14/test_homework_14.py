import os
import pytest
from log_event_module import log_event, LOG_FILE

@pytest.fixture(scope="session", autouse=True)
def clear_log_file_once(): # Очищає файл логів один раз перед запуском усіх тестів
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w"):
            pass  # очищаємо файл

def read_log_file():
    assert os.path.exists(LOG_FILE), "Log file is not created"
    with open(LOG_FILE, "r") as f:
        return f.read()
#print("Поточний лог-файл:", os.path.abspath(LOG_FILE))

def test_log_success():
    log_event("alice", "success")
    content = read_log_file()
    assert "INFO" in content
    assert "Username: alice, Status: success" in content

def test_log_expired():
    log_event("bob", "expired")
    content = read_log_file()
    assert "WARNING" in content
    assert "Username: bob, Status: expired" in content

def test_log_failed():
    log_event("carol", "failed")
    content = read_log_file()
    assert "ERROR" in content
    assert "Username: carol, Status: failed" in content

def test_log_unknown():
    log_event("dave", "invalid")
    content = read_log_file()
    assert "ERROR" in content
    assert "Username: dave, Status: invalid" in content

def test_for_admin():
    log_event("admin", "failed")
    log_event("admin", "unknown")
    content = read_log_file()
    assert "ERROR" in content
    assert "INFO" in content
    assert "Username: admin, Status: unknown" in content