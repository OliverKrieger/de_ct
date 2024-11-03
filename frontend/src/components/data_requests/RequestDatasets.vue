<template>
    <div class="data-request-component">
        <h1 class="text-xl">Datasets</h1>
        <div v-if="datasets" class="flex flex-wrap">
            <div class="w-1/4 p-2 hover:bg-rose-900 transition-all duration-300 cursor-pointer" v-for="(dataset, index) in datasets.Datasets.Dataset" :key="index">
                <div class="dataset-card">
                    <h2 class="text-l">{{ dataset.DatasetName }}</h2>
                    <p><strong>Code:</strong> <span :class="dataset.DatasetCode=='GCE' ? 'text-rose-500' : ''"> {{ dataset.DatasetCode }} </span></p>
                    <!-- <p><strong>Description:</strong> {{ dataset.DatasetDescription }}</p>
                    <p><strong>Contact:</strong> {{ dataset.Contact }}</p>
                    <p><strong>Email:</strong> {{ dataset.Email }}</p>
                    <p><strong>Last Updated:</strong> {{ dataset.DateUpdate }}</p>
                    <p><strong>File Size:</strong> {{ dataset.FileSize }}</p>
                    <p><strong>File Type:</strong> {{ dataset.FileType }}</p>
                    <p><strong>File Location:</strong> {{ dataset.FileLocation }}</p> -->
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

    import { FaostatDatasets } from "../../types/type_faostat_dataset";

    const apiURL = import.meta.env.VITE_API_URL;
    const datasetsURL = "https://bulks-faostat.fao.org/production/datasets_E.json"

    const datasets = ref<FaostatDatasets | null>(null);

    async function getDatasets(){
        try {
            const response = await axios.get(`${apiURL}/fetch_data?url=${datasetsURL}`);
            datasets.value = response.data;
        } catch (error) {
            console.error("Error fetching date data:", error);
        }
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