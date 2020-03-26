from interpreter import Interpreter
from lexer import Lexer


def main():
    while True:
        try:
            text = input("calc>>")
        except Exception as e:
            break

        if len(text) == 0:
            continue
        if text == 'exit':
            break

        interpreter = Interpreter(Lexer(text))

        try:
            result = interpreter.interpret()
        except Exception as e:
            print(e)
            continue

        print(result)


if __name__ == "__main__":
    main()
