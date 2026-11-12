# test.md から include で参照するコード
def greet(name):
    """あいさつの文を返す"""
    if not name:
        return "こんにちは"
    return f"こんにちは、{name} さん"


if __name__ == "__main__":
    print(greet("Pubpdf"))
