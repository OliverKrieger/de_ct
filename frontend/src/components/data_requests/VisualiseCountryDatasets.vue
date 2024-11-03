<template>
    <div class="country-datasets-container w-screen max-w-7xl">
        <div v-if="countryDataset">
            <h1 class="text-xl text-rose-500">Crops total (Emissions N2O)</h1>
            <div v-for="(countryData, countryName) in countryDataset" :key="countryName">
                <h2>{{ countryName }}</h2>
                <!-- <p><strong>Area Code:</strong> {{ countryData['Area Code'] }}</p>
                <p><strong>Years:</strong> {{ countryData.Years.join(', ') }}</p>
                <p><strong>Values:</strong> {{ countryData.Values.join(', ') }}</p> -->
                <ChartVis 
                    :labels="countryData.Years"
                    :label="countryName"
                    :data="countryData.Values"
                    backgroundColor="#42A5F5"
                />
            </div>
            <button class="bg-gray-700 hover:bg-gray-800 hover:border-gray-800 text-white font-bold py-2 px-4 rounded transition-all duration-300" @click="clear">Clear</button>
        </div>
        <div class="loader-container" v-else>
            <div class="loader-wrapper">
                <Loader />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { ref, watch } from 'vue'
    import Loader from '../utils/Loader.vue';
    import ChartVis from './ChartVis.vue';

    import { handlerFaoVisStore } from '../../stores/fao_vis_handler';
    import { CountryDatasets } from '../../types/type_country_data';

    const faoVisStore = handlerFaoVisStore();

    let countryDataset = ref<CountryDatasets | null>(null);
    faoVisStore.$subscribe(() => {
        countryDataset.value = faoVisStore.selectedCountryDataset;
    }, { detached: true })

    function clear(){
        faoVisStore.clearDataset();
    }

    watch(countryDataset, (newDataset) => {
        if (newDataset) {
            // const labels = newDataset["Portugal"].Years;
            // const data = newDataset["Portugal"].Values;
        }
    });
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
    .chart-container {
        position: relative;
        height: 40vh; /* Adjust height as needed */
        width: 80vw; /* Adjust width as needed */
    }
</style>