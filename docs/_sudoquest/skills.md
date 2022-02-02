---
permalink: /gdd/mechanics/skills/
title: "Skills"
---

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