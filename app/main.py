from app.book import Book
from app.display import STRATEGIES as DISPLAY_STRATEGIES
from app.print_book import STRATEGIES as PRINT_STRATEGIES
from app.serializer import STRATEGIES as SERIALIZE_STRATEGIES


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in DISPLAY_STRATEGIES:
                raise ValueError(f"Unknown display type: {method_type}")
            DISPLAY_STRATEGIES[method_type].display(book)
        elif cmd == "print":
            if method_type not in PRINT_STRATEGIES:
                raise ValueError(f"Unknown print type: {method_type}")
            PRINT_STRATEGIES[method_type].print_book(book)
        elif cmd == "serialize":
            if method_type not in SERIALIZE_STRATEGIES:
                raise ValueError(
                    f"Unknown serialize type: {method_type}"
                )
            return SERIALIZE_STRATEGIES[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
