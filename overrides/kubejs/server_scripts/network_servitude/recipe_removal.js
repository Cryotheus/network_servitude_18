//this file is only for recipes that cannot be removed using the data pack
onEvent("recipes", event => {
	//extended crafting
	event.remove({id: "extendedcrafting:aluminum_singularity"})
	event.remove({id: "extendedcrafting:platinum_singularity"})
	
	//jaopca
	event.remove({id: "jaopca:dusts.to_material.aluminum"})
	
	//jaopca:mekanism
	event.remove({id: "jaopca:mekanism.raw_storage_block_to_dirty_slurry.aluminum"})
	
	event.remove({id: "jaopca:mekanism.ore_to_dirty_slurry.cobalt"})
	event.remove({id: "jaopca:mekanism.raw_material_to_dirty_slurry.cobalt"})
	event.remove({id: "jaopca:mekanism.raw_storage_block_to_dirty_slurry.cobalt"})
	
	event.remove({id: "jaopca:mekanism.ore_to_dirty_slurry.nickel"})
	event.remove({id: "jaopca:mekanism.raw_material_to_dirty_slurry.nickel"})
	event.remove({id: "jaopca:mekanism.raw_storage_block_to_dirty_slurry.nickel"})
	
	event.remove({id: "jaopca:mekanism.ore_to_dirty_slurry.silver"})
	event.remove({id: "jaopca:mekanism.raw_material_to_dirty_slurry.silver"})
	event.remove({id: "jaopca:mekanism.raw_storage_block_to_dirty_slurry.silver"})
})