onEvent("jei.remove.categories", event => {
	//console.log(event.getCategoryIds())
	/* alphabetically sorted and formatted output of the above
		ae2:ae2.inscriber
		ae2:attunement
		ae2:condenser
		ae2:entropy
		ae2:throwing_in_water
		
		agricraft:jei/clipping
		agricraft:jei/growth_req
		agricraft:jei/mutation
		agricraft:jei/produce
		
		apotheosis:enchanting
		apotheosis:fletching
		apotheosis:spawner_modifiers
		
		blue_skies:alchemy
		blue_skies:horizonite_forge_fuel
		blue_skies:snowcap_mushroom_freezing
		blue_skies:snowcap_oven_freezing
		
		botania:brewery
		botania:elven_trade
		botania:mana_pool
		botania:marimorphosis
		botania:orechid
		botania:orechid_ignem
		botania:petals
		botania:pure_daisy
		botania:runic_altar
		botania:terra_plate
		
		brazier:light_on_brazier
		
		brewinandchewin:fermenting
		
		chipped:alchemy_bench
		chipped:botanist_workbench
		chipped:carpenters_table
		chipped:glassblower
		chipped:loom_table
		chipped:mason_table
		chipped:mechanist_workbench
		
		cookingforblockheads:cow_jar
		
		cyclic:crusher
		cyclic:generator_fluid
		cyclic:generator_item
		cyclic:melter
		cyclic:packager
		cyclic:solidifier
		
		enchdesc:compatible_items
		
		extendedcrafting:compressor
		extendedcrafting:ender_crafting
		extendedcrafting:ultimate_crafting
		
		farmersdelight:cooking
		farmersdelight:cutting
		farmersdelight:decomposition
		
		farmersrespite:brewing
		
		farmingforblockheads:market
		
		forbidden_arcanus:hephaestus_smithing
		
		hostilenetworks:loot_fabricator
		hostilenetworks:sim_chamber
		
		industrialforegoing:bioreactor
		industrialforegoing:dissolution
		industrialforegoing:fermenter
		industrialforegoing:fluid_extractor
		industrialforegoing:laser_fluid
		industrialforegoing:laser_ore
		industrialforegoing:machine_produce
		industrialforegoing:mycelial_crimed
		industrialforegoing:mycelial_culinary
		industrialforegoing:mycelial_death
		industrialforegoing:mycelial_disenchantment
		industrialforegoing:mycelial_ender
		industrialforegoing:mycelial_explosive
		industrialforegoing:mycelial_frosty
		industrialforegoing:mycelial_furnace
		industrialforegoing:mycelial_halitosis
		industrialforegoing:mycelial_magma
		industrialforegoing:mycelial_meatallurgic
		industrialforegoing:mycelial_netherstar
		industrialforegoing:mycelial_pink
		industrialforegoing:mycelial_potion
		industrialforegoing:mycelial_slimey
		industrialforegoing:ore_sieve
		industrialforegoing:ore_washer
		industrialforegoing:stone_work
		industrialforegoing:stone_work_generator
		
		integrateddynamicscompat:drying_basin
		integrateddynamicscompat:mechanical_drying_basin
		integrateddynamicscompat:mechanical_squeezer
		integrateddynamicscompat:squeezer
		
		jei:information
		
		jeresources:dungeon
		jeresources:enchantment
		jeresources:mob
		jeresources:plant
		jeresources:villager
		jeresources:worldgen
		
		justenoughprofessions:professions
		
		lazierae2:aggregator
		lazierae2:etcher
		lazierae2:grinder
		lazierae2:infuser
		
		mekanism:antiprotonic_nucleosynthesizer
		mekanism:boiler_casing
		mekanism:chemical_crystallizer
		mekanism:chemical_dissolution_chamber
		mekanism:chemical_infuser
		mekanism:chemical_injection_chamber
		mekanism:chemical_oxidizer
		mekanism:chemical_washer
		mekanism:combiner
		mekanism:condensentrating
		mekanism:crusher
		mekanism:decondensentrating
		mekanism:electrolytic_separator
		mekanism:energized_smelter
		mekanism:energy_conversion
		mekanism:enrichment_chamber
		mekanism:gas_conversion
		mekanism:infusion_conversion
		mekanism:isotopic_centrifuge
		mekanism:metallurgic_infuser
		mekanism:nutritional_liquifier
		mekanism:osmium_compressor
		mekanism:painting_machine
		mekanism:pigment_extractor
		mekanism:pigment_mixer
		mekanism:precision_sawmill
		mekanism:pressurized_reaction_chamber
		mekanism:purification_chamber
		mekanism:solar_neutron_activator
		mekanism:sps_casing
		mekanism:thermal_evaporation_controller
		
		mekanismgenerators:fission
		
		minecraft:anvil
		minecraft:blasting
		minecraft:brewing
		minecraft:campfire
		minecraft:compostable
		minecraft:crafting
		minecraft:fuel
		minecraft:furnace
		minecraft:smithing
		minecraft:smoking
		minecraft:stonecutting
		
		mob_grinding_utils:solidifier_jei
		
		mysticalagriculture:crux
		mysticalagriculture:infusion
		mysticalagriculture:reprocessor
		mysticalagriculture:soul_extractor
		
		mythicbotany:jei_category_infusion
		mythicbotany:jei_category_rune_ritual
		
		nethersdelight:composition
		
		reliquary:alkahestry_charging
		reliquary:alkahestry_crafting
		reliquary:cauldron
		reliquary:infernal_tear
		reliquary:mortar
		
		spirit:soul_cage_tier
		spirit:soul_engulfing
		spirit:soul_transmutation
		
		tconstruct:alloy
		tconstruct:casting_basin
		tconstruct:casting_table
		tconstruct:entity_melting
		tconstruct:foundry
		tconstruct:melting
		tconstruct:modifiers
		tconstruct:molding
		tconstruct:part_builder
		tconstruct:severing
		
		thermal:bottler
		thermal:brewer
		thermal:centrifuge
		thermal:chiller
		thermal:compression_fuel
		thermal:crucible
		thermal:crystallizer
		thermal:disenchantment_fuel
		thermal:furnace
		thermal:gourmand_fuel
		thermal:insolator
		thermal:insolator_catalyst
		thermal:lapidary_fuel
		thermal:magmatic_fuel
		thermal:numismatic_fuel
		thermal:press
		thermal:pulverizer
		thermal:pulverizer_catalyst
		thermal:pyrolyzer
		thermal:refinery
		thermal:rock_gen
		thermal:sawmill
		thermal:smelter
		thermal:smelter_catalyst
		thermal:stirling_fuel
		thermal:tree_extractor
		
		twilightforest:uncrafting
		
		waterstrainer:garden_trowel
		waterstrainer:strainer
		waterstrainer:worm_bin
		
		waystones:warp_plate
	*/
	
	event.remove("twilightforest:uncrafting")
})