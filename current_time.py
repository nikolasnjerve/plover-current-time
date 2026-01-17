
import datetime
import locale
import threading

try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    ZoneInfo = None  # Fallback håndteres senere

# Valgfritt fallback til dateutil hvis tilgjengelig (hjelper på Windows)
try:
    from dateutil.tz import gettz
except Exception:
    gettz = None

# Global cache og lås for tråd-sikkerhet
_BEST_BM_LOCALE = None
_LOCALE_LOCK = threading.Lock()

def _candidate_locales_bokmal():
    """
    Vanlige Bokmål-locale på tvers av Linux/macOS/Windows.
    Merk: locale-strenger varierer mellom OS – vi prøver flere.
    """
    return [
        # POSIX/macOS-varianter
        "nb_NO.UTF-8", "nb_NO.utf8", "nb_NO",
        "no_NO.UTF-8", "no_NO.utf8", "no_NO",

        # ISO-8859-1 varianter (eldre systemer)
        "nb_NO.ISO8859-1", "no_NO.ISO8859-1",

        # Windows-varianter (Python på Windows)
        "Norwegian_Bokmal.1252",
        "Norwegian_Bokmal_Norway.1252",
        "Norwegian_Bokmal",
        "Norwegian_Norway.1252",    # noen installasjoner mapper dette til Bokmål
        "Norwegian",

        # Historiske/alternative alias (kan treffe enkelte systemer)
        "NOB",
    ]

def _try_find_bokmal_locale():
    candidates = _candidate_locales_bokmal()
    prev = locale.setlocale(locale.LC_TIME)
    try:
        for loc in candidates:
            try:
                # normalize kan hjelpe å utvide alias til full streng
                norm = locale.normalize(loc)
                locale.setlocale(locale.LC_TIME, norm)
                return locale.setlocale(locale.LC_TIME)  # kanonisk verdi
            except locale.Error:
                continue
        return None
    finally:
        locale.setlocale(locale.LC_TIME, prev)

def best_bokmal_locale():
    global _BEST_BM_LOCALE
    with _LOCALE_LOCK:
        if _BEST_BM_LOCALE is not None:
            return _BEST_BM_LOCALE
        _BEST_BM_LOCALE = _try_find_bokmal_locale()
        return _BEST_BM_LOCALE

def _oslo_tzinfo():
    """
    Gi en tzinfo for norsk tid med DST.
    Strategi:
      1 IANA via zoneinfo ("Europe/Oslo")
      2 dateutil (prøv både IANA-navn og Windows-Navn: "W. Europe Standard Time")
      3 None -> kall datetime.now() uten tz (sistelinje-fallback)
    """
    # 1) zoneinfo med IANA
    if ZoneInfo is not None:
        try:
            return ZoneInfo("Europe/Oslo")
        except Exception:
            pass

    # 2 dateutil fallbacks
    if gettz is not None:
        tz = gettz("Europe/Oslo") or gettz("W. Europe Standard Time")
        if tz:
            return tz

    # 3 Siste utvei: None -> naive lokal tid
    return None

def _now_oslo():
    """
    Returner nåtid i Europe/Oslo (med DST). Faller tilbake til systemets lokal-tid
    hvis ingen tzinfo fås tak i.
    """
    tz = _oslo_tzinfo()
    if tz is not None:
        return datetime.datetime.now(tz)
    return datetime.datetime.now()  # naive lokal tid som fallback

def time(formatting: str) -> str:
    """
    Formaterer tidspunkt i norsk Bokmål og norsk tidssone (Europe/Oslo).
    Alltid forsøk Bokmål-locale; faller tilbake til gjeldende locale hvis ikke tilgjengelig.

    Eksempler:
        time("%A %d. %B %Y %H:%M")
        time("%c")
    """
    prev = locale.setlocale(locale.LC_TIME)
    try:
        loc = best_bokmal_locale()
        if loc:
            locale.setlocale(locale.LC_TIME, loc)

        now = _now_oslo()
        return now.strftime(formatting)
    finally:
        locale.setlocale(locale.LC_TIME, prev)

# Valgfritt: integrer med meta()
def meta(ctx, cmdline):
    action = ctx.new_action()
    action.text = time(cmdline)
    return action

if __name__ == "__main__":
    # Rask røyk-test
    print(time("%A %d. %B %Y %H:%M"))

