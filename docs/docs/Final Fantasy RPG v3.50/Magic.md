- Design Level 3/4 of skills first, push silliness, make lower levels lesser effects
- Magic Die is simply d10, more or less MP
- Spells Cost half a Magic Die per Spell Level (6 right now)
- Given Fire deals 1x Damage, Fire II will deal 2x damage and cost 3x what Fire I costs
- AoE for Spells will be limited to certain levels of spells
  - Do we want to limit to only pure casters can alter spell AoE?
  - I.E. Dark Knight casting Darkness or Fire cannot make it AoE
  - Aero III or IV cannot be cast single target or it loses potency casting in a smaller AoE
  - Fire IV AoE is so large that it will hit the caster unless they cast it at max range
- Spells need a charge time
- Black Magic -> Fire, Ice, Thunder, Darkness
- White Magic -> Air, Earth, Water, Holy
- Time Magic -> Arcane, Time, Space

## Notes and Random Thoughts
- There will be 8 tiers of magic
- In some of the highest tiers, there will be an effective 9th tier (e.g. Ultima)
- Ultima will break the damage cap of 999
- Effects of Elemental Magic
  - Fire spells are giant AoEs with reduced damage to make smaller
  - Ice spells can be +1 AoE in highest tier
  - Lightning spells eventually have no range
  - Darkness can inflict blind(?) and maybe where we get Doom and Death?
  - Air deals extra damage to flying enemies, AoE based on Tier (Aero IV is 4 squares big)
  - Earth has a chance of knock down
  - Water can grant soaked status (Take extra damage from lighting or inflict freeze w/ high enough blizzard spell)
  - Holy is healing & can be used against undead
  - Arcane is only resisted by anti magic stuff
  - Time is haste stop quicken slow and the like
  - Space is ??? Quarter health effects and things like that.

- Magic Formulas should be something like `4 * Tier * Magic + ? d ?`
  - Example 1: Fire > 4 * Magic + 1d6
- Spell Cost by Tier: `Sum of 1..Tier`
  - 1 = 1
  - 2 = 3
  - 3 = 6
  - 4 = 10
  - 5 = 15
  - 6 = 21
  - 7 = 28
  - 8 = 36
  - 9 = 45

### Spell Damage Table (For Calculation)

| Tier | MP Cost  | At 30 Magic |
|:----:|:--------:|------------:|
|1     |6         |          120|
|2     |18        |          240|
|3     |36        |          360|
|4     |60        |          480|
|5     |90        |          600|
|6     |126       |          720|
|7     |168       |          840|
|8     |216       |          960|
|9*    |270       |   999 (1080)|




## Black Magic

Blind
Blizzard
Fire
Poison
Sleep
Thunder

Dark
Elemental Spikes
Lock
Rasp
Water

Blizzard 2
Fear
Fire 2
Thunder 2
Zombie

Bio
Debarrier
Despair
Drain
Osmose
Water 2

Blizzard 3
Curse
Fire 3
Scourge
Stone
Thunder 3

Death
Flare
Quake
Syphon
Water 3

Freeze
Nuke
Pain
Toad
Venom

Break
Scathe
Doomsday
Meltdown
Ultima
