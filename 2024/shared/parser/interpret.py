from shared.parser.tokenizer import Tokenizer, Token


def process_mul(tokenizer: Tokenizer) -> int:
    a = 0
    b = 0

    if not tokenizer.check(Token.L_PAREN):
        return 0

    if tokenizer.peak(Token.NUMBER):
        a = tokenizer.pop().val

    if not tokenizer.check(Token.COMMA):
        return 0

    if tokenizer.peak(Token.NUMBER):
        b = tokenizer.pop().val

    if not tokenizer.check(Token.R_PAREN):
        return 0

    return a * b


def interpret_tokens(tokenizer: Tokenizer, use_do=False) -> int:
    total = 0
    enable = True
    while tokenizer.has_tokens():
        current = tokenizer.pop()
        match (current.type):
            case Token.DO:
                enable = True
            case Token.DONT:
                enable = False
            case Token.MUL:
                if (not use_do) or enable:
                    total += process_mul(tokenizer)
    return total
