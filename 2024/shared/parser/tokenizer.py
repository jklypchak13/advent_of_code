

class Token:
    # Token Types
    NUMBER = 'NUMBER'
    MUL = 'MUL'
    L_PAREN = 'L_PAREN'
    R_PAREN = 'R_PAREN'
    COMMA = 'COMMA'
    INV = 'INV'
    DO = 'DO'
    DONT = 'DONT'
    CNT = 'CNT'

    def __init__(self, type: str, val=None):
        self.type = type
        self.val = val

    def __eq__(self, other):
        if isinstance(other, Token):
            return other.type == self.type
        return self.type == other

    def __repr__(self):
        return self.type


class Tokenizer:

    KEYWORDS = {
        '(': Token.L_PAREN,
        ')': Token.R_PAREN,
        ',': Token.COMMA,
        "don't": Token.DONT,
        "do": Token.DO,
        "mul": Token.MUL,
    }

    def __init__(self, data: str):
        self.tokens = []
        self.process_data_stream(data)
        self.index = 0

    def reset(self):
        self.index = 0

    def process_data_stream(self, data: str):
        i = 0
        while i < len(data):
            # Check for keywords
            found = False
            for keyword in Tokenizer.KEYWORDS:
                index = data.find(keyword, i)
                if data.find(keyword, i) == i:

                    self.tokens.append(Token(Tokenizer.KEYWORDS[keyword]))
                    i += len(keyword)
                    found = True
                    break
            if found:
                continue

            # Check for numbers
            if data[i].isdigit():
                end = i
                while data[end].isdigit():
                    end += 1
                self.tokens.append(Token(Token.NUMBER, int(data[i:end])))
                i = end
            else:
                self.tokens.append(Token(Token.INV))
                i += 1

        self.clean_tokens()

    def clean_tokens(self):
        for i in range(len(self.tokens) - 1, 0, -1):
            if self.tokens[i] == self.tokens[i - 1] and self.tokens[i] == Token.INV:
                self.tokens.pop(i)

    def has_tokens(self) -> bool:
        return len(self.tokens) != self.index

    def pop(self) -> Token:
        token = self.tokens[self.index]
        self.index += 1
        return token

    def check(self, token: str) -> bool:
        if self.peak(token):
            self.pop()
            return True
        return False

    def peak(self, token: str) -> bool:
        return self.tokens[self.index] == token
