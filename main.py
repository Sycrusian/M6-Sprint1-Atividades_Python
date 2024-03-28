import math


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return "Delta Negativo"
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (round(x1, 2), round(x2, 2))


# if __name__ == "__main__":
#     print(bhaskara(7, 3, 4))
#     # Delta Negativo
#     print(bhaskara(1, 5, 2))
#     # x1=-0.44, x2=-4.56
#     print(bhaskara(3, 10, 2))
#     # x1=-0.21, x2=-3.12'

def corresponding_parenthesis(text):
    result = ""
    for i in range(len(text)):
        if i < len(text) - 1:
            if text[i] == "(":
                if text[i+1] == ")":
                    continue
        if i > 0:
            if text[i] == ")":
                if text[i-1] == "(":
                    continue
        result += text[i]
    return result

def remove_more_than_two_repetitions(text):
    result = ""
    for i in range(len(text)):
        if i > 1:
            if text[i] == text[i-1]:
                if text[i] == text[i-2]:
                    continue
        result += text[i]
    return result

if __name__ == "__main__":
    # Exemplo 1
    result = corresponding_parenthesis("()()")
    print(result)   # ''
    # Exemplo 2
    result = corresponding_parenthesis("()))")
    print(result)   # '))'
    # Exemplo 3
    result = corresponding_parenthesis("()()())()()(()((")
    print(result)   # ')((('
    
    text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
    text = remove_more_than_two_repetitions(text)
    print(text)     # 'Olloco meuu, taa peegaando fogoo biichoo'