from enum import Enum



# Assuming SetHandleType is defined elsewhere (e.g., main.py) and accessible
# For standalone helper, it would need to be defined or imported.
# from main import SetHandleType # Or wherever SetHandleType is defined
# Mocking SetHandleType for this snippet if it's not available via import path
class SetHandleType(Enum):
    ADD = "add"
    EXCLUDE = "exclude"
    REPLACE = "replace"