import json
import os

'''
Generates similar recipes so we don't have to write them by hand.
Currently creates recipes for ore unification and bans some items that are useless to the pack.

Currently affects:
- Avaritia
- Extended Crafting
- JAOPCA
- Mekanism
'''

#paths
data_path = "overrides/kubejs/data/"
extended_crafting_path = data_path + "extendedcrafting/recipes/"
kubejs_path = data_path + "kubejs/recipes/"
mekanism_path = data_path + "mekanism/recipes/"

#the magical ban recipe
ban_recipe = {
	"type": "crafting_shapeless",
	"ingredients": [{"item": "minecraft:barrier"}],
	"result": {"item": "minecraft:barrier"}
}

#seedlings
bans = {
	"avaritia": [
		#general crafts
		"compressor",
		"extreme_crafting_table",
		
		#singularities
		"amethyst_singularity",
		"copper_singularity",
		"diamond_singularity",
		"emerald_singularity",
		"fluxed_singularity",
		"gold_singularity",
		"iridium_singularity",
		"iron_singularity",
		"lapis_singularity",
		"lead_singularity",
		"netherite_singularity",
		"nickel_singularity",
		"platinum_singularity",
		"quartz_singularity",
		"redstone_singularity",
		"silver_singularity",
		"tin_singularity",
	]
}

extended_crafting_tiers = ["advanced", "basic", "elite"]

metals = {
	"cobalt": {
		"clean_slurry": "jaopca:mekanism_clean.cobalt",
		"clump": "jaopca:mekanism_clumps.cobalt",
		"crystal": "jaopca:mekanism_crystals.cobalt",
		"dirty_slurry": "jaopca:mekanism_dirty.cobalt",
		"dust": "jaopca:mekanism_dusts.cobalt",
		"ingot": "tconstruct:cobalt_ingot",
		"ore_tag": "forge:ores/cobalt",
		"raw_ore": "tconstruct:raw_cobalt",
		"shard": "jaopca:mekanism_shards.cobalt",
		
		"write_kubejs": True
	},
	
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
	
	"nickel": {
		"clean_slurry": "jaopca:mekanism_clean.nickel",
		"clump": "jaopca:mekanism_clumps.nickel",
		"crystal": "jaopca:mekanism_crystals.nickel",
		"dirty_slurry": "jaopca:mekanism_dirty.nickel",
		"dust": "thermal:nickel_dust",
		"ingot": "thermal:nickel_ingot",
		"ore_tag": "forge:ores/nickel",
		"raw_ore": "thermal:raw_nickel",
		"shard": "jaopca:mekanism_shards.nickel",
		
		"write_kubejs": True
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
	
	"silver": {
		"clean_slurry": "jaopca:mekanism_clean.silver",
		"clump": "jaopca:mekanism_clumps.silver",
		"crystal": "jaopca:mekanism_crystals.silver",
		"dirty_slurry": "jaopca:mekanism_dirty.silver",
		"dust": "thermal:silver_dust",
		"ingot": "thermal:silver_ingot",
		"ore_tag": "forge:ores/silver",
		"raw_ore": "thermal:raw_silver",
		"shard": "jaopca:mekanism_shards.silver",
		
		"write_kubejs": True
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

#simple function for the sole purpose of writing ban_recipe to a json file
def write_ban(file_path):
	recipe = open(file_path, "w")
	
	json.dump(ban_recipe, recipe, separators=(',', ':'))
	recipe.close()

#simple function for the sole purpose of writing a json file
def write_json(file_path, object):
	recipe = open(file_path, "w")
	
	json.dump(object, recipe, separators=(',', ':'))
	recipe.close()

#sets the current working directory to the parent folder of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(extended_crafting_path, 0o777, True)
print("\n - Building ban files...")

for namespace in bans: #general recipe bans
	recipe_path = data_path + namespace + "/recipes/"
	
	os.makedirs(recipe_path, 0o777, True)
	print("Building ban files for " + namespace)
	
	for local_path in bans[namespace]: write_ban(recipe_path + local_path + ".json")

print("\n - Building metal files...")

for metal in metals: #Mekanism and JAOPCA
	info = metals[metal]
	processing_path = mekanism_path + "processing/" + metal + "/"
	
	#if info.has_key("write_kubejs"): processing_path = kubejs_path + "processing/" + metal + "/"
	#else: processing_path = mekanism_path + "processing/" + metal + "/"
	
	print("Building metal files " + metal + "...")
	
	clean_slurry = info["clean_slurry"]
	clump = info["clump"]
	crystal = info["crystal"]
	dirty_slurry = info["dirty_slurry"]
	dust = info["dust"]
	ingot = info["ingot"]
	ore_tag = info["ore_tag"]
	raw_ore = info["raw_ore"]
	shard = info["shard"]
	
	os.makedirs(processing_path + "clump", 0o777, True)
	os.makedirs(processing_path + "shard", 0o777, True)
	os.makedirs(processing_path + "slurry/dirty", 0o777, True)
	os.makedirs(processing_path + "dust", 0o777, True)
	os.makedirs(processing_path + "ore", 0o777, True)
	
	#replace recipe for ore to dust with ore to raw ore
	write_json(processing_path + "dust/from_ore.json", {
		"type": "mekanism:enriching",
		"input": {"ingredient": {"tag": ore_tag}},
		"output": {
			"item": raw_ore,
			"count": 2
		}
	})
	
	#modify the count for the output of raw ore crafts
	write_json(processing_path + "clump/from_raw_ore.json", {
		"type": "mekanism:purifying",
		"itemInput": {"ingredient": {"item": raw_ore}},
		"chemicalInput": {"amount": 1, "gas": "mekanism:oxygen"},
		"output": {
			"item": clump,
			"count": 3
		}
	})
	
	write_json(processing_path + "dust/from_raw_ore.json", {
		"type": "mekanism:enriching",
		"input": {"ingredient": {"item": raw_ore}},
		"output": {
			"item": info["dust"],
			"count": 4
		}
	})
	
	write_json(processing_path + "shard/from_raw_ore.json", {
		"type": "mekanism:injecting",
		"itemInput": {"ingredient": {"item": raw_ore}},
		"chemicalInput": {
			"amount": 1,
			"gas": "mekanism:hydrogen_chloride"
		},
		
		"output": {
			"item": shard,
			"count": 4
		}
	})
	
	write_json(processing_path + "slurry/dirty/from_raw_ore.json", {
		"type": "mekanism:dissolution",
		"itemInput": {"ingredient": {"item": raw_ore}},
		"gasInput": {
			"amount": 1,
			"gas": "mekanism:sulfuric_acid"
		},
		
		"output": {
			"amount": 1000,
			"chemicalType": "slurry",
			"slurry": dirty_slurry
		}
	})
	
	#ban these recipes
	write_ban(processing_path + "clump/from_ore.json")
	write_ban(processing_path + "clump/from_raw_block.json")
	write_ban(processing_path + "dust/from_raw_block.json")
	write_ban(processing_path + "ore/deepslate_from_raw.json")
	write_ban(processing_path + "ore/from_raw.json")
	write_ban(processing_path + "shard/from_ore.json")
	write_ban(processing_path + "shard/from_raw_block.json")
	write_ban(processing_path + "slurry/dirty/from_ore.json")
	write_ban(processing_path + "slurry/dirty/from_raw_block.json")

print("\n - Building Extended Crafting files...")

for tier in extended_crafting_tiers: #Extended Crafting
	tier_path = extended_crafting_path + tier
	
	print("Building Extended Crafting tier files " + tier + "...")
	
	write_ban(tier_path + "_auto_table.json")
	write_ban(tier_path + "_catalyst.json")
	write_ban(tier_path + "_component.json")
	write_ban(tier_path + "_table.json")

print("\n - Completed!")