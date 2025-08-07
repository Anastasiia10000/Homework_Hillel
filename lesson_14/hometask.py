import os
from log_event_module import log_event, logger, LOG_FILE


def read_log_file():
    assert os.path.exists(LOG_FILE), "Файл логування не створено"
    with open(LOG_FILE, "r") as f:
        return f.read()

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
    content = read_log_file()
    assert "ERROR" in content
    assert "INFO" in content
    assert "Username: admin, Status: unknown" in content