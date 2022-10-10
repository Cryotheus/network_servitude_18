onEvent("jei.hide.items", event => {
	//mods entirely hidden
	event.hide(/^everycomp:/)
	event.hide(/^excavated_variants:/)
	
	//ae2
	event.hide("ae2:facade")
	
	//ae2 things
	event.hide("ae2things:advanced_inscriber")
	event.hide("ae2things:crystal_growth")
	
	//blue skies
	event.hide("blue_skies:black_fire")
	event.hide("blue_skies:blue_fire")
	
	//chisel & bits
	event.hide(/^chiselsandbits:block_bit/)
	
	//extendedcrafting
	event.hide(/^extendedcrafting:advanced/)
	event.hide(/^extendedcrafting:basic/)
	event.hide(/^extendedcrafting:elite/)
	
	event.hide(Item.of("extendedcrafting:singularity", "{Id:\"extendedcrafting:aluminum\"}"))
	
	//jaopca
	event.hide("jaopca:dusts.aluminum")
	event.hide("jaopca:mekanism_clean.aluminum")
	event.hide("jaopca:mekanism_clumps.aluminum")
	event.hide("jaopca:mekanism_crystals.aluminum")
	event.hide("jaopca:mekanism_dirty_dusts.aluminum")
	event.hide("jaopca:mekanism_dirty.aluminum")
	event.hide("jaopca:mekanism_shards.aluminum")
	event.hide("jaopca:raw_storage_blocks.aluminum")
	event.hide("jaopca:storage_blocks.aluminum")
	
	//tconstruct
	event.hide("tconstruct:broad_axe")
	event.hide("tconstruct:cleaver")
	event.hide("tconstruct:dagger")
	event.hide("tconstruct:excavator")
	event.hide("tconstruct:hand_axe")
	event.hide("tconstruct:kama")
	event.hide("tconstruct:pickadze")
	event.hide("tconstruct:pickaxe")
	event.hide("tconstruct:mattock")
	event.hide("tconstruct:scythe")
	event.hide("tconstruct:sledge_hammer")
	event.hide("tconstruct:sword")
	event.hide("tconstruct:vein_hammer")
	
	//telepastries
	event.hide("telepastries:custom_cake")
	event.hide("telepastries:custom_cake2")
	event.hide("telepastries:custom_cake3")
	event.hide("telepastries:lost_city_cake")
})