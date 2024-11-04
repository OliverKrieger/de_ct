<template>
    <div class="data-request-component">
        <h1 class="text-xl">Datasets</h1>
        <div v-if="datasets" class="flex flex-wrap">
            <div class="w-1/4 p-2 hover:bg-rose-900 transition-all duration-300 cursor-pointer" v-for="(dataset, index) in datasets.Datasets.Dataset" :key="index">
                <div class="dataset-card" @click="handle_dataset_select(dataset)">
                    <h2 class="text-l">{{ dataset.DatasetName }}</h2>
                    <p><strong>Code:</strong> <span :class="highlightedCodes.includes(dataset.DatasetCode) ? 'text-rose-500' : ''"> {{ dataset.DatasetCode }} </span></p>
                </div>
            </div>
        </div>
        <div class="loader-container" v-else>
            <div class="loader-wrapper">
                <Loader />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';
    import axios from 'axios';
    
    import Loader from '../utils/Loader.vue';

    import { FaostatDatasets, FaostatDataset } from "../../types/type_faostat_dataset";

    import { handlerDatasetStore } from '../../stores/dataset_handler';
    
    const datasetStore = handlerDatasetStore();

    const apiURL = import.meta.env.VITE_API_URL;
    const apiKEY = import.meta.env.VITE_FUNCTION_HOST_KEY;
    const datasetsURL = "https://bulks-faostat.fao.org/production/datasets_E.json"
    const highlightedCodes = ['GCE']

    const datasets = ref<FaostatDatasets | null>(null);

    async function getDatasets(){
        try {
            const response = await axios.get(`${apiURL}/fetch_data?url=${datasetsURL}&code=${apiKEY}`);
            datasets.value = response.data;
        } catch (error) {
            console.error("Error fetching date data:", error);
        }
    }

    function handle_dataset_select(dataset:FaostatDataset) {
        datasetStore.selectDataset(dataset);
    }

    getDatasets() // is ran on setup
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