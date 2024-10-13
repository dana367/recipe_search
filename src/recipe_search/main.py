import requests


def get_ability(ability: str):
    response = requests.get(f"https://pokeapi.co/api/v2/ability/{ability}/")
    if response.status_code != 200:
        raise Exception(f"expected response 200, but received {response.status_code}")
    data = response.json()
    effect_entries: list[dict] = data["flavor_text_entries"]
    for entry in effect_entries:
        if entry["language"]["name"] == "en":
            eng_effect = entry["flavor_text"]
            break
    print(eng_effect)


def get_user_input() -> str:
    print("Beginning")
    customer_input = input("Type in an ability: ")
    if not customer_input.isalpha():
        print("Please enter a valid ability: ")
        get_user_input()
    return customer_input


def main():
    ability = get_user_input()
    get_ability(ability)


if __name__ == "__main__":
    main()
