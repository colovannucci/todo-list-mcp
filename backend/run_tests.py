import sys
import pytest

def main():
    # Lista de argumentos opcionales a pytest, como:
    # -v : modo verboso
    # --tb=short : traceback corto
    # tests/ : carpeta donde están los tests
    args = ["-v", "--tb=short", "tests/"]
    exit_code = pytest.main(args)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
