onEvent("jei.hide.items", event => {
    // extendedcrafting
    event.hide("extendedcrafting:advanced_auto_table")
    event.hide("extendedcrafting:advanced_table")
    event.hide("extendedcrafting:basic_auto_table")
    event.hide("extendedcrafting:basic_table")
    event.hide("extendedcrafting:elite_auto_table")
    event.hide("extendedcrafting:elite_table")
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
    
    event.hide(Item.of("extendedcrafting:singularity", "{Id:\"extendedcrafting:aluminum\"}"))
})

