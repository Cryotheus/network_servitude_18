onEvent("jei.hide.items", event => {
	event.hide(/draconium/)
	
	//mods entirely hidden
	event.hide(/^everycomp:/)
	event.hide(/^excavated_variants:/)
	
	//ae2
	//event.hide("ae2:facade") //doesn't work
	
	//ae2 things
	event.hide("ae2things:advanced_inscriber")
	event.hide("ae2things:crystal_growth")
	
	//avaritia
	event.hide("avaritia:compressor")
	event.hide("avaritia:extreme_crafting_table")
	event.hide(/avaritia:.*_singularity/)
	
	//blue skies
	event.hide("blue_skies:black_fire")
	event.hide("blue_skies:blue_fire")
	
	//cyclic
	event.hide("cyclic:sleeping_mat")
	
	//extendedcrafting
	event.hide("extendedcrafting:recipe_maker")
	event.hide(/^extendedcrafting:advanced/)
	event.hide(/^extendedcrafting:basic/)
	event.hide(/^extendedcrafting:elite/)
	
	//jaopca
	event.hide(/jaopca:.*\.aluminum/)
	
	//mystical agriculture
	event.hide(/^mysticalagriculture:platinum/)
	
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
	
	//twilightforest
	event.hide("twilightforest:uncrafting_table")
})