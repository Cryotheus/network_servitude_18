onEvent("jei.hide.items", event => {
	//ae2 things
	event.hide("ae2things:advanced_inscriber")
	event.hide("ae2things:crystal_growth")
	
	//chisel & bits
	event.hide("chiselsandbits:block_bit")
	
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
})