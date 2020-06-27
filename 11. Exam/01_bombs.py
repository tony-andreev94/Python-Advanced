# https://judge.softuni.bg/Contests/Compete/Index/2456#0


def is_full(dict):
    if dict['Datura Bombs'] >= 3 and dict['Cherry Bombs'] >= 3 and dict['Smoke Decoy Bombs'] >= 3:
        return True
    else:
        return False


bombs_dict = {40: 'Datura Bombs',
              60: 'Cherry Bombs',
              120: 'Smoke Decoy Bombs'
              }

pouch_dict = {'Cherry Bombs': 0,
              'Datura Bombs': 0,
              'Smoke Decoy Bombs': 0
              }
datura = 0
cherry = 0
smoke = 0

bomb_effects = [int(x) for x in input().split(", ")]
bomb_casings = [int(x) for x in input().split(", ")]

while len(bomb_effects) > 0 and len(bomb_casings) > 0:
    temp_bomb = int(bomb_effects[0]) + int(bomb_casings[-1])
    if temp_bomb in bombs_dict:
        bomb_effects.pop(0)
        bomb_casings.pop()
        pouch_dict[bombs_dict[temp_bomb]] += 1
        if is_full(pouch_dict):
            break
    else:
        bomb_casings[-1] -= 5

if is_full(pouch_dict):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) == 0:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(item) for item in bomb_effects)}")

if len(bomb_casings) == 0:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(item) for item in bomb_casings)}")

for pair in pouch_dict.items():
    print(f"{pair[0]}: {pair[1]}")
