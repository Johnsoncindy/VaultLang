# lexer.py
# VaultLang - Lexer (Tokenizer)
# Reads raw VaultLang source code and breaks it into tokens

from token import Token, KEYWORDS, INTEGER, FLOAT, STRING, NEWLINE, EOF, UNKNOWN


class Lexer:
    def __init__(self, source_code):
        self.source  = source_code        # Raw source code string
        self.pos     = 0                  # Current character position
        self.line    = 1                  # Current line number
        self.current = self.source[0] if source_code else None  # Current character

    # ── Core Navigation ──────────────────────────────────────
    def advance(self):
        """Move to the next character"""
        self.pos += 1
        if self.pos < len(self.source):
            self.current = self.source[self.pos]
        else:
            self.current = None  # End of source

    def peek(self):
        """Look at the next character without moving"""
        peek_pos = self.pos + 1
        if peek_pos < len(self.source):
            return self.source[peek_pos]
        return None

    # ── Skippers ─────────────────────────────────────────────
    def skip_whitespace(self):
        """Skip spaces and tabs"""
        while self.current is not None and self.current in (' ', '\t'):
            self.advance()

    def skip_comment(self):
        """Skip comments starting with #"""
        while self.current is not None and self.current != '\n':
            self.advance()

    # ── Token Readers ─────────────────────────────────────────
    def read_number(self):
        """Read an integer or float number"""
        result = ""
        while self.current is not None and self.current.isdigit():
            result += self.current
            self.advance()

        # Check for float
        if self.current == '.' and self.peek() and self.peek().isdigit():
            result += self.current
            self.advance()
            while self.current is not None and self.current.isdigit():
                result += self.current
                self.advance()
            return Token(FLOAT, float(result), self.line)

        return Token(INTEGER, int(result), self.line)

    def read_string(self):
        """Read a quoted string e.g. 'Alice' or 'John Doe' """
        result = ""
        self.advance()  # Skip opening quote

        while self.current is not None and self.current != '"':
            result += self.current
            self.advance()

        if self.current == '"':
            self.advance()  # Skip closing quote
        else:
            raise Exception(f"[Line {self.line}] Error: Unterminated string")

        return Token(STRING, result, self.line)

    def read_keyword(self):
        """Read a keyword or identifier"""
        result = ""
        while self.current is not None and (self.current.isalpha() or self.current == '_'):
            result += self.current
            self.advance()

        # Check if it's a known keyword
        upper = result.upper()
        token_type = KEYWORDS.get(upper, UNKNOWN)
        return Token(token_type, upper, self.line)

    # ── Main Tokenizer ────────────────────────────────────────
    def tokenize(self):
        """Convert entire source code into a list of tokens"""
        tokens = []

        while self.current is not None:

            # Skip whitespace
            if self.current in (' ', '\t'):
                self.skip_whitespace()

            # Track new lines
            elif self.current == '\n':
                tokens.append(Token(NEWLINE, '\\n', self.line))
                self.line += 1
                self.advance()

            # Skip comments
            elif self.current == '#':
                self.skip_comment()

            # Read numbers
            elif self.current.isdigit():
                tokens.append(self.read_number())

            # Read strings
            elif self.current == '"':
                tokens.append(self.read_string())

            # Read keywords
            elif self.current.isalpha():
                tokens.append(self.read_keyword())

            # Unknown character
            else:
                tokens.append(Token(UNKNOWN, self.current, self.line))
                self.advance()

        # Always end with EOF
        tokens.append(Token(EOF, None, self.line))
        return tokens
    
    
    
# test function to print tokens
if __name__ == "__main__":
    code = '''
    CREATE ACCOUNT "Alice" WITH 1000000
    DEPOSIT 200000 TO "Alice"
    WITHDRAW 50000 FROM "Alice"
    SHOW ACCOUNT "Alice"
    '''
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)