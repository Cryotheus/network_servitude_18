import json
import os

ban_recipe = json.dumps({
	"type": "crafting_shapeless",
	"ingredients": [{"item": "minecraft:barrier"}],
	"result": {"item": "minecraft:barrier"}
})

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

#simple function for the sole purpose of writing a json file
def write_json(file_path, object):
	him = open(file_path, "w")
	him.write(json.dumps(object))
	him.close()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for metal in metals:
	info = metals[metal]
	path = "processing/" + metal + "/"
	
	clean_slurry = info["clean_slurry"]
	clump = info["clump"]
	crystal = info["crystal"]
	dirty_slurry = info["dirty_slurry"]
	dust = info["dust"]
	ingot = info["ingot"]
	ore_tag = info["ore_tag"]
	raw_ore = info["raw_ore"]
	shard = info["shard"]
	
	os.makedirs(path + "clump", 0o777, True)
	os.makedirs(path + "dust", 0o777, True)
	os.makedirs(path + "ore", 0o777, True)
	
	#replace recipe for ore to dust with ore to raw ore
	write_json(path + "dust/from_ore.json", {
		"type": "mekanism:enriching",
		"input": {"ingredient": {"tag": ore_tag}},
		"output": {
			"item": raw_ore,
			"count": 2
		}
	})
	
	#modify the count for raw ore to dust
	#{"type":"mekanism:enriching","input":{"amount":3,"ingredient":{"tag":"forge:raw_materials/copper"}},"output":{"item":"mekanism:dust_copper","count":4}}
	write_json(path + "dust/from_raw_ore.json", {
		"type": "mekanism:enriching",
		"input": {"ingredient": {"item": raw_ore}},
		"output": {
			"item": info["dust"],
			"count": 4
		}
	})
	
	#write_json(path + "clump/from_raw_ore.json", {"type":"mekanism:purifying","itemInput":{"ingredient":{"tag":"forge:raw_materials/copper"}},"chemicalInput":{"amount":1,"gas":"mekanism:oxygen"},"output":{"item":"mekanism:clump_copper","count":2}}
	#
	write_json(path + "clump/from_raw_ore.json", {
		"type": "mekanism:purifying",
		"itemInput": {"ingredient": {"tag": raw_ore}},
		"chemicalInput": {"amount": 1, "gas": "mekanism:oxygen"},
		"output": {
			"item": clump,
			"count": 3
		}
	})
	
	#ban these recipes
	write_json(path + "clump/from_ore.json", ban_recipe)
	write_json(path + "clump/from_raw_block.json", ban_recipe)
	write_json(path + "dust/from_raw_block.json", ban_recipe)
	write_json(path + "ore/deepslate_from_raw.json", ban_recipe)
	write_json(path + "ore/from_raw.json", ban_recipe)
