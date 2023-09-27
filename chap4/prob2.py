import random

hero_HP = random.randrange(50, 100)
monster_HP = random.randrange(50, 100)
hero_attack_value = random.randrange(-10, 20)
monster_attack_value = random.randrange(-10, 20)

print("hero Hp: ", hero_HP,", moster HP: ", monster_HP)

if hero_attack_value > 0:
  result1 = "success"
else:
  result1 = "fail"

if monster_attack_value > 0:
  result2 = "success"
else:
  result2 = "fail"

cnt = 0

while hero_HP > 0 or monster_HP > 0:
  print("hero(HP:", hero_HP, ", attack:", hero_attack_value, ")", result1, " <-> monster(HP:", monster_HP, ", attack:", monster_attack_value, ")", result2)

  cnt = cnt + 1

  if hero_attack_damage > 0 or monster_attack_damage > 0:
  hero_HP = Hero_HP - monster_attack_damage
  monster_HP = monster_HP - hero_attack_damage

print("Total phase: ", cnt)

if hero_HP <= 0
