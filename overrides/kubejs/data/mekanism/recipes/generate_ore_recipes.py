import json
import os

ban_recipe = {
	"type": "crafting_shapeless",
	"ingredients": [{"item": "minecraft:barrier"}],
	"result": {"item": "minecraft:barrier"}
}

metals = {
	"copper": {
		"clean_slurry": "mekanism:clean_copper",
		"clump": "mekanism:clump_copper",
		"crystal": "mekanism:crystal_copper",
		"dirty_slurry": "mekanism:dirty_copper",
		"dust": "mekanism:dust_copper",
		"ingot": "minecraft:copper_ingot",
		"ore_tag": "forge:ores/copper",
		"raw_ore": "minecraft:raw_copper",
		"shard": "mekanism:shard_copper",
	},
	
	"gold": {
		"clean_slurry": "mekanism:clean_gold",
		"clump": "mekanism:clump_gold",
		"crystal": "mekanism:crystal_gold",
		"dirty_slurry": "mekanism:dirty_gold",
		"dust": "mekanism:dust_gold",
		"ingot": "minecraft:gold_ingot",
		"ore_tag": "forge:ores/gold",
		"raw_ore": "minecraft:raw_gold",
		"shard": "mekanism:shard_gold",
	},
	
	"iron": {
		"clean_slurry": "mekanism:clean_iron",
		"clump": "mekanism:clump_iron",
		"crystal": "mekanism:crystal_iron",
		"dirty_slurry": "mekanism:dirty_iron",
		"dust": "mekanism:dust_iron",
		"ingot": "minecraft:iron_ingot",
		"ore_tag": "forge:ores/iron",
		"raw_ore": "minecraft:raw_iron",
		"shard": "mekanism:shard_iron",
	},
	
	"lead": {
		"clean_slurry": "mekanism:clean_lead",
		"clump": "mekanism:clump_lead",
		"crystal": "mekanism:crystal_lead",
		"dirty_slurry": "mekanism:dirty_lead",
		"dust": "mekanism:dust_lead",
		"ingot": "mekanism:ingot_lead",
		"ore_tag": "forge:ores/lead",
		"raw_ore": "mekanism:raw_lead",
		"shard": "mekanism:shard_lead",
	},
	
	"osmium": {
		"clean_slurry": "mekanism:clean_osmium",
		"clump": "mekanism:clump_osmium",
		"crystal": "mekanism:crystal_osmium",
		"dirty_slurry": "mekanism:dirty_osmium",
		"dust": "mekanism:dust_osmium",
		"ingot": "mekanism:ingot_osmium",
		"ore_tag": "forge:ores/osmium",
		"raw_ore": "mekanism:raw_osmium",
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
		"raw_ore": "mekanism:raw_tin",
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
		"raw_ore": "mekanism:raw_uranium",
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

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#convert ore to raw
for metal in metals:
	path = "processing/" + metal + "/"
	
	convert_to_raw = {
		"type": "mekanism:enriching",
		"input": {"ingredient": {"tag": "forge:ores/" + metal}},
		"output": {
			"item": "mekanism:dust_copper",
			"count": 2
		}
	}
	
	os.makedirs(path + "dust", 0o777, True)
	
	dust_from_ore = open(path + "dust/from_ore.json", "w")
	dust_from_ore.write(json.dumps(ban_recipe))
	dust_from_ore.close()
	
