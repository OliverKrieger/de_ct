<template>
    <div>
        <div v-if="selectedCountryDatasets">
            <VisualiseCountryDatasets />
        </div>
        <div v-else>
            <RequestData />
        </div>
        <DatasetOverlay />
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import RequestData from '../data_requests/RequestDatasets.vue'
    import DatasetOverlay from '../data_requests/DatasetOverlay.vue'
    import VisualiseCountryDatasets from '../data_requests/VisualiseCountryDatasets.vue';

    import { handlerFaoVisStore } from '../../stores/fao_vis_handler';
    import { FaostatDataset } from '../../types/type_faostat_dataset';

    const faoVisStore = handlerFaoVisStore();

    let selectedCountryDatasets = ref<FaostatDataset | null>(null);
    faoVisStore.$subscribe(() => {
        selectedCountryDatasets.value = faoVisStore.selectedDataset
    }, { detached: true })
</script>

<style scoped></style>