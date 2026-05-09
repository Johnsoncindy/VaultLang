# tokens.py
# VaultLang - Token Type Definitions
# Defines all token types used by the VaultLang lexer

# Data Types
INTEGER = "INTEGER"       # e.g. 500000
FLOAT   = "FLOAT"         # e.g. 500000.50
STRING  = "STRING"        # e.g. "Alice"

# Keywords
CREATE   = "CREATE"
ACCOUNT  = "ACCOUNT"
DELETE   = "DELETE"
DEPOSIT  = "DEPOSIT"
WITHDRAW = "WITHDRAW"
TRANSFER = "TRANSFER"
LOAN     = "LOAN"
REPAY    = "REPAY"
FREEZE   = "FREEZE"
UNFREEZE = "UNFREEZE"
SHOW     = "SHOW"
ALL      = "ALL"
ACCOUNTS = "ACCOUNTS"

# connectors
WITH = "WITH"
TO   = "TO"
FROM = "FROM"
FOR  = "FOR"

# Special Tokens 
EOF     = "EOF"           # End of file
NEWLINE = "NEWLINE"       # End of a line
UNKNOWN = "UNKNOWN"       # Unrecognized character


# Token Class
class Token:
    def __init__(self, type, value, line=None):
        self.type  = type    # Token type (e.g. INTEGER, KEYWORD)
        self.value = value   # Actual value (e.g. 500000, "Alice")
        self.line  = line    # Line number (for error reporting)

    def __repr__(self):
        return f"Token({self.type}, {self.value}, line={self.line})"


# ── Keyword Map ───────────────────────────────────────────
# Maps raw text → token type
KEYWORDS = {
    "CREATE"   : CREATE,
    "ACCOUNT"  : ACCOUNT,
    "DELETE"   : DELETE,
    "DEPOSIT"  : DEPOSIT,
    "WITHDRAW" : WITHDRAW,
    "TRANSFER" : TRANSFER,
    "LOAN"     : LOAN,
    "REPAY"    : REPAY,
    "FREEZE"   : FREEZE,
    "UNFREEZE" : UNFREEZE,
    "SHOW"     : SHOW,
    "ALL"      : ALL,
    "ACCOUNTS" : ACCOUNTS,
    "WITH"     : WITH,
    "TO"       : TO,
    "FROM"     : FROM,
    "FOR"      : FOR,
}