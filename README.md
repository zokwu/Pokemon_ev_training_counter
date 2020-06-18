# Pokemon_ev_training_counter
Simple python function to help tracking ev traning progress by defeating pokemons

I always found tracking ev training progress can be a bit tedious and complicated when training by defeating pokemons one by one, especially for some complicated combination. Or when you're training at route 7 for fast physical attacker (Persserker (+2 ATK),  Liepard / Galvantula (+2 SPD)), but have to keep checking your ev bar in order to decide when to change power item. 

So I use python notebook to write a simple program to help track ev progress by adding opponent defeated, and I think it's pretty convenient so I want to share it. I'm not really a programer and it's just a quick and easy tool to use. You do need to have python or preferrable jupyter notebook to use this little program.  

Some helpful information for ev training by defeating pokemon in Pokemon Sword and Shield:

***********************************************************************************
Pokemon location:
Attack: Route 7 Persserker (+2 ATK)
Defence: Wild Area Torkoal / Carkoal (+2 DEF)
Speed: Route 7 Liepard / Galvantula (+2 SPE)
SP. ATK: Wild Area / Route 6 Maractus (+2 SPA)
SP. DEF: Route 7  Thievul (+2 SPD)
HP: Wild Area Wobbuffet / Diggersby / Noctowl (+2 HP)

***********************************************************************************
Power item:
Power Anklet:	Speed +8
Power Band:	Special Defense +8
Power Belt: Defense +8
Power Bracer: Attack +8
Power Lens: Special Attack +8
Power Weight: HP +8

***********************************************************************************
Pokerus will double your EV gain.
e.g. Without pokerus, no item, defeat 1 Liepard will gain Speed EV 2
     Without pokerus, Power Anklet, defeat 1 Liepard will gain Speed EV 2 + 8 = 10
     With pokerus, Power Anklet, defeat 1 Liepard will gain Speed EV (2 + 8) x 2 = 20
     With pokerus, Power Bracer, defeat 1 Liepard will gain Speed EV 2 x 2 = 4 and Attack EV 2 x 8 = 16
