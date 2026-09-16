def tartalmaz_szamot(text: str) -> bool:
    """Eldönti, hogy a szöveg tartalmaz-e legalább egy számjegyet.

    >>> tartalmaz_szamot("abc123")
    True
    >>> tartalmaz_szamot("abcdef")
    False
    >>> tartalmaz_szamot("")
    False
    """
    for karakter in text:
        if karakter.isdigit():
            return True
    return False


def tartalmaz_nagybetut(text: str) -> bool:
    """Eldönti, hogy a szöveg tartalmaz-e legalább egy nagybetűt.

    >>> tartalmaz_nagybetut("Alma")
    True
    >>> tartalmaz_nagybetut("alma123")
    False
    >>> tartalmaz_nagybetut("")
    False
    """
    for karakter in text:
        if karakter.isupper():
            return True
    return False


def password_strength(password: str) -> str:
    """Visszaadja a jelszó erősségét.

    A 8 karakternél rövidebb jelszó gyenge. A legalább 8 karakteres jelszó
    közepes, ha nincs benne szám vagy nincs benne nagybetű. Erős akkor,
    ha legalább 8 karakteres, tartalmaz számot és nagybetűt is.

    >>> password_strength("abc")
    'weak'
    >>> password_strength("abcdefgh")
    'medium'
    >>> password_strength("Abcdefgh")
    'medium'
    >>> password_strength("Abc12345")
    'strong'
    """
    if len(password) < 8:
        return "weak"
    if tartalmaz_szamot(password) and tartalmaz_nagybetut(password):
        return "strong"
    return "medium"
