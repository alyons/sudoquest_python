---
permalink: /gdd/mechanics/
title: "Mechanics"
---

## Skill Tree System

The skill tree system will be how the player creates their character for battle. Based on their level, the player will have a certain amount of points to spend in their skill trees. The skill trees will have nodes which give different bonuses and skills. As the player puts points into trees, new trees will become unlocked, allowing the player to have access to new skills and bonuses. Each tree will have the same number of tiers; however some of the more advance trees may not have as many nodes or have the space for as many points.  

**#**|**Bonus Type**|**Multiple Points**
:-----:|:-----:|:-----:
1|Increase Dot Length|No
2|Increase Hot Length|No
3|Increase Max HP|Yes
4|Start with X mana of Y Type|Yes
5|Gain X mana of Y type when solving a tile|No
6|Unlock a Skill|No
7|Boost a Skill|Yes
8|Start with an Effect in Battle (e.g. Shield or Wall)|No
9|Effects cause when solving rows, columns, or squares|No

## Battle System

Here we will look at what each combatant is and a true break down of how turns proceed.  
A combatant is a battle ready representation of a player or an enemy. A combatant has a name, health points, a mana pool, active equipment, statuses and available skills. The name is the name of the player or the enemy. The health points have two fields; maximum and current. When a combatant’s current health reaches zero points, they lose the match. The mana pool represents how much mana the combatant has saved up by solving tiles on the battle grid. Mana is used to pay for abilities. Active equipment is the equipment selected by the player (or assigned to the enemy) before battle starts. This equipment can include one helmet, one suit of armor, one weapon and one accessory. These will give the combatant bonus effects in battle. The skills will be set in a similar manner to the equipment. A combatant will have up to six skills in combat.  
For each turn, there will be three phases. The first phase will be an opening phase; statuses will be ticked and possibly cause effects, certain item effects will be triggered, and other possibly cost will be paid. The second phase will allow the player to use a skill and then will be completed when the player attempts to solve a tile. A skill does not have to be used, but must be used before attempting to solve a tile. The third phase will be a cleanup step, in which any necessary steps and cost will be accounted for.  

### Open Phase

During the first phase of battle, opening phase, the player will trigger certain item and status effects. The following table will describe, in order, what will be triggered.  

**#**|**Effect**
:-----:|:-----:
1|Damage over Time
2|Healing over Time
3|Trigger any Suspended Effects
4|Drop all expired Statuses
5|Trigger item triggers (Table 5)

### Action Phase

During this phase the combatant may choose to use a skill, and then must solve at tile on the battle grid.  
A skill can only be used if the combatant has the required mana in the mana pool. Certain skills may have other requirements outside of mana cost, which will also need to be fulfilled (i.e. cool downs, health cost, et cetera).  
When the combatant chooses to solve a tile; they put their answer in the tile and the tile will respond with either earning mana, if they are correct, or a punishment upon failure.  
When a tile is solved, the combatant earns three mana of the color of the tile. If a row, column, or square is solved, they also gain one mana for each tile in the row, column, and/or square they completed.  

### Close Phase

This phase will do some basic clean up functions, if we find necessary for the user to perform, such as item effects that may trigger after the Action Phase and such. This is in for the time being as a holder phase, but will be expanded upon as needed.  

## Skill System

Skills are what are used in battle to harm one’s opponent and aid oneself in the field of battle. However, one could have a move that damaged both the user and the enemy. Skills are collections of Effects which are things which happen in battle. Each skill will have a name, mana cost, set of Effects, additional cost (special abilities), and a cool down. The name will be a unique identifier for the skill, the mana cost will tell you how much mana will be spent on the move, the set of Effects will tell you what happens when the move is used, additional cost may include soft mana cost, health, or requirements for the skill to be used and, cool downs will determine how often a skill can be used. Mana cost, additional cost, and cool downs will all be implemented relative to the strength of a skill in battle; i.e. the stronger a skill, the higher the mana cost and cool down, and the more likely an additional cost will be added.  
Effects, the pieces of skills, will be rather unique in that they will each separately have a target and different pieces. This will enable skills to have effects that target the user and enemy separately.   

**#**|**Effect Type**|**Duration**|**Associative***
:-----:|:-----:|:-----:|:-----:
1|Damage|No|Yes
2|Healing|No|No
3|Damage over Time|Yes|No
4|Healing over Time|Yes|No
5|Damage Boost|Yes|Yes
6|Damage Reduction|Yes|Yes
7|Damage Wall|Yes|Yes
8|Damage Weakness|Yes|Yes
9|Damage Mana|No|Yes
10|Drain Mana|No|Yes
11|Transfer Mana|No|Yes
12|Reduce Healing|Yes|No
13|Damage Shield|A|Yes
14|Mana to Damage|No|Yes
15|Silence|Yes|Yes
16|Extra Turn|No|No
17|Suspended Effect|Yes|No
18|Change Board Color|B|No
19|Confusion|Yes|Yes
20|Buff Break|No|No
21|Buff Steal|No|No
22|Gain Maximum HP|C|No
23|Lose Maximum HP|C|No
24|Mana Flux|No|No
25|Add Ammo|No|No
26|Add Mark|Yes|No

*Can be associated with a color of mana, so can be blocked or boosted in certain manners.  
A – Breaks after enough damage  
B – Changes the board for the rest of the fight  
C – Only for the duration of the battle   

### Effect Descriptions

This is simply a list of all of the effects which can be attached to a skill and how they shall function.  
Damage – This will deal damage to the target of the effect. Damage dealt will be associated with all types of mana used to pay for the skill.  
Healing – This will heal health to the target of the effect. Healing is not associated with mana types.  
Damage over Time – This effect will deal damage for a number of turns the target of the effect. Damage over Time is not associated with any mana types, and cannot be mitigated by normal means.  
Healing over Time - This will heal health to the target for a number of turns.  Heal over Time is not associated with mana types and cannot be boosted by normal means.  
Damage Boost - Increases direct damage dealt by the affected target.  The damage boost can be associated with mana types but does not boost damage over time.  
Damage Reduction - Reduces damage dealt by the affected target. The damage reduction can be associated with mana types and this does not reduce the damage dealt by DoTs.  
Damage Wall- Reduces damage taken by the affected target.  The damage wall can be associated with mana types and this does not reduce damage from DoTs.
Damage Weakness – Increases damage taken by the affected target.  The damage weakness can be associated with mana types and this does not increase damage from DoTs.  
Damage Mana – Reduces the target’s mana pools.  This can target one type of mana, the highest mana pool, or all of the mana pools.  
Drain Mana – Reduce the target’s mana pools and give it to the other combatant.  This can target one type of mana, the highest mana pool, or all the mana pools.  
Transfer Mana – Transfers mana from one pool to another for the selected target.  
Reduce Healing – Reduces the amount of healing the affected target receives.  This does not affect HoTs.  
Damage Shield – Prevents the next X direct damage dealt to the affected target.  This does not block DoT damage.  
Mana to Damage – Converts all the mana in a single mana pool to direct damage to the target.  This damage is associated with mana types.  
Silence – Prevents the target from playing abilities for X number of turns.  This can be associated with mana types.  
Extra Turn – The target gets to take an extra turn after this one.   
Suspended Effect – Effect X will happen after Y turns.  Suspended effect will pull from a table of effects to cause.  
Change Board Color – Changes the pattern of the entire board to a predetermined pattern  
Confusion – A target affected by confusion has their mana cost on their skills change colors; i.e. if a skill were to cost three physical, seven magical, and zero spiritual mana (3, 7, 0), when the target is confused it might cost zero physical, 3 magical, and 7 spiritual (0, 3, 7).  
Buff Break – Removes the first buff on the target.  
Buff Steal – Removes the first buff on the target and applies it to the other combatant with starting duration.  
Gain Maximum HP – Increases the target’s maximum HP and heals them by the increase.  
Lose Maximum HP – Decreases the target’s maximum HP, but doesn’t damage them for the decrease.  
Mana Flux – A target affected by mana flux gain mana randomly from a tile rather than the mana which they would normally receive; e.g. a target affected by mana flux who solves a blue tile for three magical mana could gain three physical or spiritual instead.  
Add Ammo – Add ammunition for use with specific skills; see description below.  
Add Mark – Add a mark to the target that adds bonuses to certain skills; see description below.  

### Skill Ammo System

For certain skills, there will be an additional cost associated with that skill which will be ammunition. This ammunition will be created via a separate skill, and a skill which uses ammunition can only be equipped when a skill which produces that type of ammunition is present.  

### Skill Bonus System

Certain skills will give a status of a Mark, which will stay on the combatant for X turns. Other skills will consume that Mark to trigger bonus effects. The bonus effects will be dependent on the skill which consumes the Mark.

### Skill Fusion System

The skill fusion system, SFS for short, will be a system which will allow players to combine certain skills and get new ones to use in battle. To unlock a Fusion Skill, one must first know the two skills required to make the Fusion Skill. Then the player must fight against the Skill Master to learn the Fusion Skill. The player must have the two skills equipped when fighting the Skill Master and the Skill Master will have the Fusion Skill and a skill set to help him use that skill. Fusion Skills will take up two slots of skills in battle and/or you can only have one Fusion Skill equipped at a time. Throughout the game, the player can find hints as to which skills could lead to a Fusion Skill, or can stumble upon them by checking frequently with the Skill Master.  
Fusion Skills will be much more commonly built from skills of differing trees. This will help players who choose to multi-class still get very solid skills to use, without reaching the end of the trees which they are in.

### Skill Link System

Certain skills will be able to link into other skills, allowing multiple skills to be used in a single turn. For some skills, they can link into any skill; however, there should be some form of diminishing return for this use. For other skills, they will link directly into other skills with a lesser (possibly even no) diminishing return, due to the direct link. The diminishing return will be established by comparing mana to effect ratios of skills and determining through testing what would be best.

### Item System

In Sudokuest there will be three types of items; equipment, gems, and quest items. Equipment allows the player to boost their stats in battle. This is achieved by slotting gems into the equipment. Gems give the player various abilities; more health, better mana gaining, et cetera. Quest Items allow the player to complete certain quest in the campaign.

#### Equipment System

When the player is preparing for battle, they will be able to have equipment with various gems attached which will give them an edge in combat. Equipment can have two types of gem slots; ability and modifier. Ability slots allow a player to equip ability gems, which give the player a direct boost in combat ability. Modifier slots allow the player to equip modifier gems, which can amplify the power of an ability gem. Certain ability gems can only be placed in certain types of equipment. Ability gems can only be modified by certain modifier gems and some ability gems cannot be modified at all.  
How ability gems affect battle varies by gem. Certain gems modify damage dealt and how much starting health a character has; and can be triggered through various means such as taking damage or using a skill. Below are listed all of the potential bonuses and triggers which can be attributed to ability gems.  

Ability Gem Effects

**#**|**Effect Type**|**Associative***
:-----:|:-----:|:-----:
1|Damage Boost|Yes
2|Damage Reduction|Yes
3|Damage Wall|Yes
4|Damage Weak|Yes
5|Heal Boost|No
6|Dot Length Increase|No
7|Hot Length Increase|No
8|Gain Bonus Mana|Yes
9|Unlock Skillᵃ|No
10|Boost Skill|No
11|Cause Effect|No
12|Extra Exp|No
13|Extra Gold|No
14|Critical Gain of Exp|No
15|Critical Gain of Gold|No
16|Effects on Tile Completion|Yes
17|Item Clone|No
18|Reflect Damage|No
19|Add Ammunition|No
20|Silence Enemy|No
21|Gain Shield|No
22|Recover Health|No

Ability Gem Triggers

**#**|**Triggers**|**Associative***|**Trigger Phase**
:-----:|:-----:|:-----:|:-----:
1|Damage Dealt|No|Action Phase
2|Damage Dealt per Turn|No|Open Phase
3|Damage Taken|No|Action Phase
4|Damage Blocked|No|Action Phase
5|Healing Received|No|Open Phase
6|Healing Received per Turn|No|Open Phase
7|Mana Gain|Yes|Action Phase
8|Abilities used for X Turns|Yes|Open Phase
9|Have X Buffs|No|Open Phase
10|Have X De-buffs|No|Open Phase
11|Enemy has X Buffs|No|Open Phase
12|Enemy has X De-buffs|No|Open Phase
13|Health reaches Critical (First Time)|No|Action Phase
14|Health is Critical|No|All
15|Battle Start|No|N/A
16|Every Turn|No|Open Phase
17|End of Turn|No|Close Phase
18|Static|No|N/A
19|End of Battle|No|N/A
20|If incoming damage is greater than or equal too current health|No|N/A

**Trigger**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
1st Time Critical|X|X|X| | | | |X| | | | | | | | | | | | |X|X
Abilities used for X turns|X| | | | |X| |X| |X|X| | | | | | | |X| |X| 
Battle End| | | | | | | | | | | |X|X|X|X| | | | | | | 
Battle Start|X|X|X| | | | |X| | | | | | | | | |X|X| |X| 
Beginning/End of Turn| | | | | | | |X| | |X| | | | | | | | | | | 
Damage Blocked|X| |X| | |X| |X| | | | | | | | | | | | | | 
Damage Dealt| | | |X| | | |X| | |X| | | | | | | |X| | |X
Damage Taken|X|X| | |X| |X|X| |X|X| | | | | | |X| | | |X
Deal Damage for X turns|X| | | | | | |X| | |X|X|X|X|X| | | | | | |X
Have X buffs (self, enemy)| | | |X| | | |X| | |X|X|X| | | | |X|X| | | 
Have X de-buffs (self, enemy)|X| |X| |X| | |X|X| |X|X|X| | | | |X|X| |X| 
Healing Received| | | | | | | |X|X| | | | | | | | | |X| | | 
If would kill combatant (once per battle)|X| | | |X| | |X| | | | | | | | | | | |X| | 
Static|X|X| | | |X|X| | |X| | | | | |X| | | | | | 
While Critical |X|X|X| |X|X|X|X|X|X|X| | | | |X| | | | | | 
