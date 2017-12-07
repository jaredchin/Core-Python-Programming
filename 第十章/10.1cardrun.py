

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval