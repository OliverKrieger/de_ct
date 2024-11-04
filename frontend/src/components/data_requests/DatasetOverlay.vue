<template>
    <teleport to="body">
        <div v-if="dataset" class="overlay fixed max-h-full inset-0 bg-black bg-opacity-50 flex items-center justify-center content-center p-4 sm:p-8" @click.self="clear">
            <div class="overlay-content p-4 bg-gray-900 relative w-full max-h-[100vh] overflow-y-auto">
                <button class="bg-gray-700 hover:bg-gray-800 hover:border-gray-800 text-white font-bold sm:py-2 sm:px-4 py-0.25 px-1.5 rounded transition-all duration-300 absolute top-1 right-1 sm:top-4 sm:right-4" @click="clear">X</button>
                <div class="content">
                    <h2 class="text-xl underline text-center max-w-96 mx-auto mt-2 mb-4 sm:mb-0">{{ dataset.DatasetName }}</h2>
                    <p><strong>Code:</strong> {{ dataset.DatasetCode }} </p>
                    <p><strong>Contact:</strong> {{ dataset.Contact }}</p>
                    <p><strong>Email:</strong> {{ dataset.Email }}</p>
                    <p><strong>Last Updated:</strong> {{ dataset.DateUpdate }}</p>
                    <p><strong>File Size:</strong> {{ dataset.FileSize }}</p>
                    <p><strong>File Type:</strong> {{ dataset.FileType }}</p>
                    <p class="break-words"><strong>File Location:</strong> {{ dataset.FileLocation }}</p>
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
        fetchData();
    }

    function clear(){
        datasetStore.clearDataset()
    }

    function fetchData(){
        clear()
        if(dataset && dataset.value && submittedData && submittedData.value){
            faoVisStore.fetchDataset(dataset.value, submittedData.value)
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