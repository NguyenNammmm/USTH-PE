import keyword
def valid_name(name):
    """Kiểm tra tên Python hợp lệ và không thuộc từ khóa."""
    return name.isidentifier() and not keyword.iskeyword(name)
def type_trace():
    value = "8"
    before = type(value).__name__
    value = int(value)
    return before, type(value).__name__
