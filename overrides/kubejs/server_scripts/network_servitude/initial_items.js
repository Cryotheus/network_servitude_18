var standard_issue_nbt = '{display:{Lore:["{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}"]}}'

function color_random() {return Math.floor(Math.random() * 16777215)}

function grant_items(player) {
	var inventory = player.inventory
	
	//player.setLegsArmorItem(Item.of('environmental:yak_pants', '{Unbreakable:1,Enchantments:[{id:"cyclic:traveler",lvl:1}],"quark:RuneAttached":1,"quark:RuneColor":{Count:1,id:"quark:blank_rune"},display:{Name:"{\\"text\\":\\"§fSerious Slacks§r\\"}",Lore:["{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}","{\\"text\\":\\"§7Although they are called \\\\\\"Slacks\\\\\\" please do not do so§r\\"}"]}}'))
	player.setOffHandItem(Item.of('minecraft:shield', '{Enchantments:[{id:"unbreaking",lvl:1}],"quark:RuneAttached":1,"quark:RuneColor":{Count:1,id:"quark:blank_rune"},display:{Name:"{\\"text\\":\\"§fWorker Rights§r\\"}",Lore:["{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}"]}}'))
	
	//hotbar
	inventory.set(0, Item.of('minecraft:iron_pickaxe', '{Enchantments:[{id:"unbreaking",lvl:2}],"quark:RuneAttached":1,"quark:RuneColor":{Count:1,id:"quark:blank_rune"},display:{Lore:["{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}"]}}'))
	inventory.set(1, Item.of('minecraft:iron_shovel', standard_issue_nbt))
	inventory.set(2, Item.of('minecraft:iron_axe', '{Enchantments:[{id:"unbreaking",lvl:1},{id:"enigmaticlegacy:nemesis_curse",lvl:1}],"quark:RuneAttached":1,"quark:RuneColor":{Count:1,id:"quark:blank_rune"},display:{Lore:["{\\"text\\":\\"§7Damn thing is useless in combat§r\\"}","{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}"]}}'))
	inventory.set(3, Item.of('minecraft:iron_sword', standard_issue_nbt))
	
	//inventory.set(7, Item.of('6x extendedmushrooms:mushroom_bread', '{display:{Name:"{\\"text\\":\\"§fBRED 46a-2§r\\"}",Lore:["{\\"text\\":\\"§7Expired... but still edible§r\\"}","{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}"]}}'))
	inventory.set(7, Item.of('8x pamhc2foodextended:driedsoupitem', '{display:{Name:"{\\"text\\":\\"§fMeat Supplement v2.4.19d (Revision A)§r\\"}",Lore:["{\\"text\\":\\"§7Best described as a \\\\\\"Jerky Brick\\\\\\"§r\\"}","{\\"text\\":\\"§7Standard issue for Network Serfs§r\\"}"]}}'))
	inventory.set(8, Item.of('sophisticatedbackpacks:backpack', "{borderColor:" + color_random() + ",clothColor:" + color_random() + "}"))
	
	//inventory
	//inventory.set(9, '2x lootbagmod:lootbag')
}

onEvent('ftbquests.completed.initial_items', event => {
	var player = event.player
	
	if (player) {grant_items(player)}
})

onEvent("player.logged_in", event => {
	if (!event.player.stages.has("network_servitude_initial_items")) {
		var player = event.player
		var stages = player.stages
		
		grant_items(player)
		
		stages.add("network_servitude_initial_items")
	}
})