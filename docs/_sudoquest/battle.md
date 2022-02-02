---
permalink: /gdd/mechanics/battle/
title: "Battle"
---

A combatant is a battle ready representation of a player or an enemy.
A combatant has a name, health points, a mana pool, active equipment, statuses and available skills.
The name is the name of the player or the enemy.
The health points have two fields; maximum and current. When a combatant’s current health reaches zero points, they lose the match.
The mana pool represents how much mana the combatant has saved up by solving tiles on the battle grid.
Mana is used to pay for abilities.
Active equipment is the equipment selected by the player (or assigned to the enemy) before battle starts. This equipment can include one helmet, one suit of armor, one weapon and one accessory. These will give the combatant bonus effects in battle.
The skills will be set in a similar manner to the equipment. A combatant will have up to six skills in combat.  

Battle will progress where each combatant will take turns. On a combatant's turn there will be 3 phases.

1. Opening Phase
2. Action Phase
3. Clean Up Phase

## Opening Phase

During the first phase of battle, opening phase, the player will trigger certain item and status effects. The following table will describe, in order, what will be triggered.  

**#**|**Effect**
:-----:|:-----:
1|Damage over Time
2|Healing over Time
3|Trigger any Suspended Effects
4|Drop all expired Statuses
5|Trigger item triggers
6|Reduce timers on skills with cool downs

## Action Phase

During this phase the combatant may choose to use a skill, and then must solve at tile on the battle grid.  
A skill can only be used if the combatant has the required mana in the mana pool. Certain skills may have other requirements outside of mana cost, which will also need to be fulfilled (i.e. cool downs, health cost, et cetera).  
When the combatant chooses to solve a tile; they put their answer in the tile and the tile will respond with either earning mana, if they are correct, or a punishment upon failure.  
When a tile is solved, the combatant earns three mana of the color of the tile. If a row, column, or square is solved, they also gain one mana for each tile in the row, column, and/or square they completed.  

## Clean Up Phase

This phase will do some basic clean up functions, if we find necessary for the user to perform, such as item effects that may trigger after the Action Phase and such. This is in for the time being as a holder phase, but will be expanded upon as needed.
