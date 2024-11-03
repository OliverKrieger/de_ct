<template>
    <teleport to="body">
        <div v-if="dataset" class="overlay" @click.self="clear">
            <div class="overlay-content bg-gray-900">
                <div class="content">
                    <h2 class="text-l">{{ dataset.DatasetName }}</h2>
                    <p><strong>Code:</strong> {{ dataset.DatasetCode }} </p>
                    <p><strong>Description:</strong> {{ dataset.DatasetDescription }}</p>
                    <p><strong>Contact:</strong> {{ dataset.Contact }}</p>
                    <p><strong>Email:</strong> {{ dataset.Email }}</p>
                    <p><strong>Last Updated:</strong> {{ dataset.DateUpdate }}</p>
                    <p><strong>File Size:</strong> {{ dataset.FileSize }}</p>
                    <p><strong>File Type:</strong> {{ dataset.FileType }}</p>
                    <p><strong>File Location:</strong> {{ dataset.FileLocation }}</p>
                </div>
                <button class="bg-rose-500 hover:bg-rose-700 hover:border-rose-700 text-white font-bold py-2 px-4 rounded transition-all duration-300" @click="clear">Close</button>
            </div>
        </div>
    </teleport>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { handlerDatasetStore } from '../../stores/dataset_handler';
    import { FaostatDataset } from "../../types/type_faostat_dataset";
    const datasetStore = handlerDatasetStore();

    let dataset = ref<FaostatDataset | null>(null);
    datasetStore.$subscribe(() => {
        dataset.value = datasetStore.selectedDataset
    }, { detached: true })

    function clear(){
        datasetStore.clearDataset()
    }
</script>

<style scoped>
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .overlay-content {
        padding: 20px;
        border-radius: 5px;
    }
</style>