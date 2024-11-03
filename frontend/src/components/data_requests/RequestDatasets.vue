<template>
    <div class="data-request-component">
        <h1>Datasets</h1>
        <div v-if="datasets" v-for="(dataset, index) in datasets.Datasets.Dataset" :key="index">
            <div class="dataset-card">
                <h2>{{ dataset.DatasetName }}</h2>
                <p><strong>Code:</strong> {{ dataset.DatasetCode }}</p>
                <p><strong>Description:</strong> {{ dataset.DatasetDescription }}</p>
                <p><strong>Contact:</strong> {{ dataset.Contact }}</p>
                <p><strong>Email:</strong> {{ dataset.Email }}</p>
                <p><strong>Last Updated:</strong> {{ dataset.DateUpdate }}</p>
                <p><strong>File Size:</strong> {{ dataset.FileSize }}</p>
                <p><strong>File Type:</strong> {{ dataset.FileType }}</p>
                <p><strong>File Location:</strong> {{ dataset.FileLocation }}</p>
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