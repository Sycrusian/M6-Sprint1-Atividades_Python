import math


# Atividade: Exercitando Funções e Builtins

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



# Atividade: Exercitando Loops e Condicionais

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


# if __name__ == "__main__":
#     # Exemplo 1
#     result = corresponding_parenthesis("()()")
#     print(result)   # ''
#     # Exemplo 2
#     result = corresponding_parenthesis("()))")
#     print(result)   # '))'
#     # Exemplo 3
#     result = corresponding_parenthesis("()()())()()(()((")
#     print(result)   # ')((('
    
#     text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
#     text = remove_more_than_two_repetitions(text)
#     print(text)     # 'Olloco meuu, taa peegaando fogoo biichoo'



# Atividade: Exercitando Listas


# if __name__ == "__main__":
#     #1
#     lista_1 = list(range(6,21))
#     #2
#     print(lista_1[-1])
#     #3
#     lista_1[1] = 'Kenzie'
#     print(lista_1)
#     #4
#     print(lista_1[2:5])
#     #5
#     lista_1.append('Academy')
#     print(lista_1)
#     #6
#     lista_1.remove('Kenzie')
#     lista_1.remove('Academy')
#     #7
#     lista_2 = sorted(lista_1, reverse=True)
#     print(lista_1)
#     print(lista_2)
#     #8
#     print(len(lista_1))
#     print(len(lista_2))
#     #9
#     lista_1.pop()
#     lista_2.pop()
#     print(lista_1)
#     print(lista_2)
#     #10
#     lista_1.clear()
#     lista_2.clear()
#     print(lista_1)
#     print(lista_2)



# S1-12 | 💪 Atividade: Exercitando Dicionários


# if __name__ == "__main__":
#     d1 = {
#         "nome": "Kenzinho",
#         "cidade": "Curitiba",
#         "modulo": "M5"
#     }
#     print(d1)
#     print(d1["nome"])
#     print(d1["cidade"])
#     print(d1.get("modulo"))
#     print(d1.get("telefone", "a chave telefone não existe"))
#     print(d1.keys())
#     print(d1.values())
#     lista_1 = ["telefone", "casado", "idade"]
#     lista_2 = ["999-999-999", False, 28]
#     d2 = dict(zip(lista_1, lista_2))
#     print(d2)
#     d1.update(d2)
#     print(d1)
#     del d1["casado"]
#     print(d1)
#     print(d1.pop("idade"))
#     print(d1)
#     d1.clear()
#     print(d1)



# S1-17 | 💪 Atividade: Exercitando Tuplas


# if __name__ == "__main__":
#     # 1
#     tupla_1 = ('Valor_1', 2, 3.1, 'Kenzie Academy', ['Elemento1', 'Elemento2'], 'Kenzie Academy')
#     print(tupla_1)
#     # 2
#     print(tupla_1[-1])
#     # 3
#     print(len(tupla_1))
#     # 4
#     print(tupla_1.count("Kenzie Academy"))
#     # 5
#     print(tupla_1.index(3.1))
#     # 6
#     tupla_1[-1] = 'Ultimo Elemento'



# S1-20 | 💪 Atividade: Exercitando args e kwargs

def sum_numbers(*args):
    total = 0
    for element in args:
        total += element
    return total


def get_multiplied_amount(multiplier, *args):
    for element in args:
        multiplier *= element
    return multiplier


def word_concatenator(*args):
    return " ".join(args)


def inverted_word_factory(*args):
    lst = list(args)[::-1]
    for i in range(len(lst) - 1):
        lst[i] = "".join(reversed(lst[i]))
    return word_concatenator(*lst)


def dictionary_separator(**kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    return (keys, values)


def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None
    values = list(kwargs.values())
    dict = {}
    for i in range(len(args) - 1):
        dict[args[i]] = values[i]
    return dict


def purchase_logger(**kwargs):
    result = str(kwargs.get("quantity"))
    result += " " + str(kwargs.get("name"))
    result += " bought by "
    result += str(kwargs.get("price"))
    return result


def world_cup_logger(country, *args):
    result = country + " - "
    if (len(args) == 1):
        result += str(args[0])
        return result
    lst = sorted(args)
    final = lst.pop()
    result += ", ".join(map(str, lst))
    result += " e " + str(final)
    return result


if __name__ == "__main__":
    # 1
    numbers = [1, 2, 3, 4, 5, 6]
    result = sum_numbers(*numbers)
    print(result)
    # 2
    numbers = [1, 2, 3]
    multiplier = 2
    result = get_multiplied_amount(multiplier, *numbers)
    print(result)
    # 3
    words = ["Tá", "pegando", "fogo", "bicho!!!"]
    concatenated_words = word_concatenator(*words)
    print(concatenated_words)
    # 4
    words = ["eae", "amigão", "belezinha?"]
    inverted_words = inverted_word_factory(*words)
    print(inverted_words)
    # 5
    user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}
    items = dictionary_separator(**user)
    print(type(items))
    print(items[0])
    print(items[1])
    # 6
    change_keys = ["username", "password", "address"]
    user = {"name": "Williams", "some_key": "1234"}
    modified_user = dictionary_creator(*change_keys, **user)
    print(modified_user)
    # 7
    purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}
    purchase_log = purchase_logger(**purchase)
    print(purchase_log)
    # 8
    country = 'Alemanha'
    year_list = [2014, 1990, 1974, 1954]
    log = world_cup_logger(country, *year_list)
    print(log)
