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
- Village Employment
'''

#paths
data_path = "overrides/kubejs/data/"
extended_crafting_path = data_path + "extendedcrafting/recipes/"
extended_crafting_singularities_path = "overrides/config/extendedcrafting/singularities/"
kubejs_path = data_path + "kubejs/recipes/"
kubejs_tag_conversion_path = kubejs_path + "tag_conversions/"
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
		"tin_singularity"
	],
	
	"twilightforest": [
		"uncrafting_table"
	],
	
	"village_employment": [
		"apiarist_apron_recipe",
		"apiarist_hat_recipe",
		"beekeeper_goggle_recipe",
		"beekeeper_jacket_recipe",
		"traveler_pants_recipe",
		"traveler_robe_recipe"
	]
}

extended_crafting_tiers = ["advanced", "basic", "elite"]

extended_crafting_recipes = {
	#default singularities, with exclusions
	"bronze": {"colors": ["d99f43", "bb6b3b"]},
	"coal": {"colors": ["363739", "261e24"], "item": "minecraft:coal"},
	"copper": {"colors": ["fa977c", "bc5430"]},
	"diamond": {"colors": ["a6fce9", "1aaca8"], "tag": "forge:gems/diamond"},
	"electrum": {"colors": ["f5f18e", "9e8d3e"]},
	"emerald": {"colors": ["7df8ac", "8e1a"], "tag": "forge:gems/emerald"},
	"glowstone": {"colors": ["ffd38f", "a06135"], "tag": "forge:dusts/glowstone"},
	"gold": {"colors": ["fdf55f", "d98e04"]},
	"invar": {"colors": ["bcc5bb", "5d7877"]},
	"iron": {"colors": ["e1e1e1", "6c6c6c"]},
	"lapis_lazuli": {"colors": ["678dea", "1b53a7"], "tag": "forge:gems/lapis"},
	"lead": {"colors": ["6c7d92", "323562"]},
	"nickel": {"colors": ["e1d798", "b1976c"]},
	"redstone": {"colors": ["ff0000", "8a0901"], "tag": "forge:dusts/redstone"},
	"silver": {"colors": ["c0cdd2", "5f6e7c"]},
	"steel": {"colors": ["565656", "232323"]},
	"tin": {"colors": ["a0bebd", "527889"]},
	
	#custom singularities
	"certus_quartz": {
		"colors": ["b8d8fc", "466580"],
		"name": "Certus Quartz",
		"tag": "forge:gems/certus_quartz"
	},
	
	"amethyst_bronze": {"colors": ["e3bdda", "8d5f88"], "name": "Amethyst Bronze"},
	"fluix_steel": {"colors": ["be8ef4", "4d3b93"], "name": "Fluix Steel"},
	"lumium": {"colors": ["fcf9e0", "fceea8"], "name": "Lumium"},
	"osmium": {"colors": ["d7eff6", "78829c"], "name": "Osmium"},
	"rose_gold": {"colors": ["f4cbb9", "cc8e7d"], "name": "Rose Gold"},
	"uranium": {"colors": ["defadc", "73a771"], "name": "Uranium"}
}

ingot_tag_conversions = {
	"bronze": {
		"dusts": "mekanism:dust_bronze",
		"ingots": "mekanism:ingot_bronze",
	},
	
	"lead": {
		"dusts": "mekanism:dust_lead",
		"ingots": "mekanism:ingot_lead",
		"raw_materials": "mekanism:raw_lead",
	},
	
	"steel": {
		"ingots": "mekanism:ingot_steel",
	},
	
	"tin": {
		"dusts": "mekanism:dust_tin",
		"ingots": "mekanism:ingot_tin",
		"raw_materials": "mekanism:raw_tin",
	},
}

item_self_recrafts = { #for items that we need to reset
	"ae2": [
		"spatial_storage_cell_2",
		"spatial_storage_cell_16",
		"spatial_storage_cell_128"
	]
}

metals = {
	"cobalt": {
		"clean_slurry": "jaopca:mekanism_clean.cobalt",
		"clump": "jaopca:mekanism_clumps.cobalt",
		"crystal": "jaopca:mekanism_crystals.cobalt",
		"dirty_slurry": "jaopca:mekanism_dirty.cobalt",
		"dust": "jaopca:dusts.cobalt",
		"ingot": "tconstruct:cobalt_ingot",
		"ore_tag": "forge:ores/cobalt",
		"raw_ore": "tconstruct:raw_cobalt",
		"shard": "jaopca:mekanism_shards.cobalt"
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
		"shard": "jaopca:mekanism_shards.nickel"
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
		"shard": "jaopca:mekanism_shards.silver"
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

#makes my life easier
def make_dirs(path): os.makedirs(path, 0o777, True)

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
print("\n - Building ban files...")

for namespace in bans: #general recipe bans
	recipe_path = data_path + namespace + "/recipes/"
	
	make_dirs(recipe_path)
	print("Building ban files for " + namespace)
	
	for local_path in bans[namespace]: write_ban(recipe_path + local_path + ".json")

print("\n - Building metal files...")

for metal in metals: #Mekanism and JAOPCA
	info = metals[metal]
	processing_path = mekanism_path + "processing/" + metal + "/"
	
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
	
	make_dirs(processing_path + "clump")
	make_dirs(processing_path + "shard")
	make_dirs(processing_path + "slurry/dirty")
	make_dirs(processing_path + "dust")
	make_dirs(processing_path + "ore")
	
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

print("\n - Building tag conversion files...")

for material in ingot_tag_conversions:
	ingot_tag_conversion = ingot_tag_conversions[material]
	material_path = kubejs_tag_conversion_path + material + "/"
	
	print("Building " + material + " conversion files...")
	
	for sub_tag in ingot_tag_conversion:
		make_dirs(material_path)
		write_json(material_path + sub_tag + ".json", {
			"type": "crafting_shapeless",
			"ingredients": [{"tag": "forge:" + sub_tag + "/" + material}],
			"result": {"item": ingot_tag_conversion[sub_tag]}
		})

print("\n - Building item self recraft files...")

for namespace in item_self_recrafts:
	path = kubejs_path + namespace + "/"
	
	make_dirs(path)
	print("Build recraft files for " + namespace)
	
	for item_name in item_self_recrafts[namespace]:
		fqin = namespace + ":" + item_name
		
		write_json(path + item_name + ".json", {
			"type": "crafting_shapeless",
			"ingredients": [{"item": fqin}],
			"result": {"item": fqin}
		})

print("\n - Building Extended Crafting files...")
make_dirs(extended_crafting_path)

for tier in extended_crafting_tiers: #Extended Crafting
	tier_path = extended_crafting_path + tier
	
	print("Building Extended Crafting tier files " + tier + "...")
	write_ban(tier_path + "_auto_table.json")
	write_ban(tier_path + "_catalyst.json")
	write_ban(tier_path + "_component.json")
	write_ban(tier_path + "_table.json")

print("\n - Building Extended Crafting singularity configurations...")
make_dirs(extended_crafting_singularities_path)

for type in extended_crafting_recipes:
	info = extended_crafting_recipes[type]
	
	if "ingredient" in info: ingredient_object = info["ingredient"]
	else:
		if "tag" in info: ingredient_object = {"tag": info["tag"]}
		elif "item" in info: ingredient_object = {"item": info["item"]}
		else: ingredient_object = {"tag": "forge:ingots/" + type}
	
	if "name" in info: name = info["name"]
	else: name = "singularity.extendedcrafting." + type
	
	object = {
		"name": name,
		"colors": info["colors"],
		"ingredient": ingredient_object
	}
	
	if "excluded" in info: object["inUltimateSingularity"] = False
	
	write_json(extended_crafting_singularities_path + type + ".json", object)

print("\n - Completed!")