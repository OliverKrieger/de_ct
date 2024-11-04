<template>
    <teleport to="body">
        <div v-if="dataset" class="overlay p-4 overflow-y-scroll fixed top-0 left-0 right-0 bottom-0 flex content-center items-center" @click.self="clear">
            <div class="overlay-content bg-gray-900 relative">
                <button class="bg-gray-700 hover:bg-gray-800 hover:border-gray-800 text-white font-bold py-2 px-4 rounded transition-all duration-300 absolute top-4 right-4" @click="clear">X</button>
                <div class="content">
                    <h2 class="text-xl underline text-center max-w-96 mx-auto mt-2">{{ dataset.DatasetName }}</h2>
                    <p><strong>Code:</strong> {{ dataset.DatasetCode }} </p>
                    <p><strong>Contact:</strong> {{ dataset.Contact }}</p>
                    <p><strong>Email:</strong> {{ dataset.Email }}</p>
                    <p><strong>Last Updated:</strong> {{ dataset.DateUpdate }}</p>
                    <p><strong>File Size:</strong> {{ dataset.FileSize }}</p>
                    <p><strong>File Type:</strong> {{ dataset.FileType }}</p>
                    <p><strong>File Location:</strong> {{ dataset.FileLocation }}</p>
                    <p class="my-2"><strong>Description:</strong> {{ dataset.DatasetDescription }}</p>
                </div>
                <DatasetSearchForm @form-submitted="handleFormSubmission" />
            </div>
        </div>
    </teleport>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { handlerDatasetStore } from '../../stores/dataset_handler';
    import { handlerFaoVisStore } from '../../stores/fao_vis_handler';
    import { FaostatDataset } from "../../types/type_faostat_dataset";
    import { DatasetSearchFormPayload } from '../../types/type_dataset_search';
    import DatasetSearchForm from './DatasetSearchForm.vue';
    
    const datasetStore = handlerDatasetStore();
    const faoVisStore = handlerFaoVisStore();

    let dataset = ref<FaostatDataset | null>(null);
    datasetStore.$subscribe(() => {
        dataset.value = datasetStore.selectedDataset;
    }, { detached: true })

    const submittedData = ref<DatasetSearchFormPayload | null>(null);

    function handleFormSubmission(payload:DatasetSearchFormPayload) {
        submittedData.value = payload; // Store the data from the child component
        console.log('Data submitted from child:', payload);
        fetchData();
    }

    function clear(){
        datasetStore.clearDataset()
    }

    function fetchData(){
        clear()
        if(dataset && dataset.value){
            faoVisStore.fetchDataset(dataset.value)
        }
        else{
            console.log("ERROR - No dataset value!")
        }
    }
</script>

<style scoped>
    .overlay {
        background: rgba(0, 0, 0, 0.5);
    }
</style>