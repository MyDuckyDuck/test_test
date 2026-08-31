# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: DeskQueue
import os

_ANSI = os.environ.get("DQ_NO_COLOR", "0") == "0"
if _ANSI:
    R, G, B, Y, BL, M, C, W = "\033[31m", "\033[32m", "\033[33m", "\033[36m", "\033[34m", "\033[35m", "\033[37m", "\033[0m"
else:
    R, G, B, Y, BL, M, C, W = "", "", "", "", "", "", "", ""

def _c(c, s):
    return f"{c}{s}{W}" if _ANSI else s

def _p(color, s):
    return _c(color, s)

def _status(s):
    return {
        "queued": _p(G, f"[{s}]"),
        "processing": _p(Y, f"[{s}]"),
        "done": _p(BL, f"[{s}]"),
        "error": _p(R, f"[{s}]"),
    }.get(s, _p(C, f"[{s}]"))
