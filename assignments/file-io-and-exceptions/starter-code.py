import os
from pathlib import Path


def read_lines(path_str: str) -> list[str]:
    """Read non-empty, stripped lines from a text file.
    Raises FileNotFoundError or PermissionError as appropriate.
    """
    p = Path(path_str)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    if p.is_dir():
        raise IsADirectoryError(f"Expected a file, got directory: {p}")

    lines: list[str] = []
    with p.open("r", encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            if s:
                lines.append(s)
    return lines


def write_lines_upper(lines: list[str], out_path: str) -> int:
    """Write lines uppercased to out_path and return count written."""
    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line.upper() + "\n")
    return len(lines)


def main() -> None:
    try:
        in_path = input("Enter input file path: ").strip()
        lines = read_lines(in_path)
        out_path = str(Path(in_path).parent / "output.txt")
        count = write_lines_upper(lines, out_path)
        print(f"Success: wrote {count} lines to {out_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        _log_error(str(e))
    except IsADirectoryError as e:
        print(f"Error: {e}")
        _log_error(str(e))
    except PermissionError as e:
        print(f"Error: {e}")
        _log_error(str(e))
    except Exception as e:
        # Fallback for unexpected errors
        print(f"Unexpected error: {e}")
        _log_error(f"Unexpected: {e}")


def _log_error(msg: str) -> None:
    try:
        with open("errors.log", "a", encoding="utf-8") as fh:
            fh.write(msg + "\n")
    except Exception:
        # Avoid raising during logging
        pass


if __name__ == "__main__":
    main()
