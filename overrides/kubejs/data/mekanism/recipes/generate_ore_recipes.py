import json

ban_recipe = {
	"type": "crafting_shapeless",
	"ingredients": [{"item": "minecraft:air"}],
	"result": {"item": "minecraft:air"}
}

metals = {
	"copper": {
		"clean_slurry": "mekanism:clean_copper",
		"clump": "mekanism:clump_copper",
		"crystal": "mekanism:crystal_copper",
		"dirty_slurry": "mekanism:dirty_copper",
		"dust": "mekanism:dust_copper",
		"ingot": "mekanism:ingot_copper",
		"ore_tag": "forge:ores/copper",
		"shard": "mekanism:shard_copper",
	},
	
	"gold": {
		"clean_slurry": "mekanism:clean_gold",
		"clump": "mekanism:clump_gold",
		"crystal": "mekanism:crystal_gold",
		"dirty_slurry": "mekanism:dirty_gold",
		"dust": "mekanism:dust_gold",
		"ingot": "mekanism:ingot_gold",
		"ore_tag": "forge:ores/gold",
		"shard": "mekanism:shard_gold",
	},
	
	"iron": {
		"clean_slurry": "mekanism:clean_iron",
		"clump": "mekanism:clump_iron",
		"crystal": "mekanism:crystal_iron",
		"dirty_slurry": "mekanism:dirty_iron",
		"dust": "mekanism:dust_iron",
		"ingot": "mekanism:ingot_iron",
		"ore_tag": "forge:ores/iron",
		"shard": "mekanism:shard_iron",
	},
	
	"coal": {
		"clean_slurry": "mekanism:clean_coal",
		"clump": "mekanism:clump_coal",
		"crystal": "mekanism:crystal_coal",
		"dirty_slurry": "mekanism:dirty_coal",
		"dust": "mekanism:dust_coal",
		"ingot": "mekanism:ingot_coal",
		"ore_tag": "forge:ores/coal",
		"shard": "mekanism:shard_coal",
	},
	
	"lead": {
		"clean_slurry": "mekanism:clean_lead",
		"clump": "mekanism:clump_lead",
		"crystal": "mekanism:crystal_lead",
		"dirty_slurry": "mekanism:dirty_lead",
		"dust": "mekanism:dust_lead",
		"ingot": "mekanism:ingot_lead",
		"ore_tag": "forge:ores/lead",
		"shard": "mekanism:shard_lead",
	},
	
	"netherite": {
		"clean_slurry": "mekanism:clean_netherite",
		"clump": "mekanism:clump_netherite",
		"crystal": "mekanism:crystal_netherite",
		"dirty_slurry": "mekanism:dirty_netherite",
		"dust": "mekanism:dust_netherite",
		"ingot": "mekanism:ingot_netherite",
		"ore_tag": "forge:ores/netherite",
		"shard": "mekanism:shard_netherite",
	},
	
	"osmium": {
		"clean_slurry": "mekanism:clean_osmium",
		"clump": "mekanism:clump_osmium",
		"crystal": "mekanism:crystal_osmium",
		"dirty_slurry": "mekanism:dirty_osmium",
		"dust": "mekanism:dust_osmium",
		"ingot": "mekanism:ingot_osmium",
		"ore_tag": "forge:ores/osmium",
		"shard": "mekanism:shard_osmium",
	},
	
	"tin": {
		"clean_slurry": "mekanism:clean_tin",
		"clump": "mekanism:clump_tin",
		"crystal": "mekanism:crystal_tin",
		"dirty_slurry": "mekanism:dirty_tin",
		"dust": "mekanism:dust_tin",
		"ingot": "mekanism:ingot_tin",
		"ore_tag": "forge:ores/tin",
		"shard": "mekanism:shard_tin",
	},
	
	"uranium": {
		"clean_slurry": "mekanism:clean_uranium",
		"clump": "mekanism:clump_uranium",
		"crystal": "mekanism:crystal_uranium",
		"dirty_slurry": "mekanism:dirty_uranium",
		"dust": "mekanism:dust_uranium",
		"ingot": "mekanism:ingot_uranium",
		"ore_tag": "forge:ores/uranium",
		"shard": "mekanism:shard_uranium",
	},
}

raws = {
	"coal": [],
	"diamond": [],
	"emerald": [],
	"fluorite": [],
	"lapis_lazuli": [],
	"quartz": [],
	"redstone": []
}

#convert ore to raw
for metal in metals:
	path = "processing/" + metal + "/dust"
	
	convert_to_raw = {
		"type": "mekanism:enriching",
		"input": {"ingredient": {"tag": "forge:ores/" + metal}},
		"output": {
			"item": "mekanism:dust_copper",
			"count": 2
		}
	}
