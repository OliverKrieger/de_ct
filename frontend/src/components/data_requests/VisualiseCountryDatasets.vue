<template>
    <div class="country-datasets-container">
        <div v-if="countryDataset">
            {{ countryDataset }}
        </div>
        <div class="loader-container" v-else>
            <div class="loader-wrapper">
                <Loader />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import Loader from '../utils/Loader.vue';

    import { handlerFaoVisStore } from '../../stores/fao_vis_handler';
    import { CountryDatasets } from '../../types/type_country_data';

    const faoVisStore = handlerFaoVisStore();

    let countryDataset = ref<CountryDatasets | null>(null);
    faoVisStore.$subscribe(() => {
        countryDataset.value = faoVisStore.selectedCountryDataset
    }, { detached: true })
</script>

<style scoped>
    .loader-wrapper{
        position: absolute;      
        margin: 0;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);  
    }
    .loader-container{
        width: 100%;
        position: relative;
        height: 100px;
    }
</style>