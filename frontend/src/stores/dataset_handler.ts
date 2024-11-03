import { defineStore } from 'pinia';
import { FaostatDataset } from '../types/type_faostat_dataset';

export const handlerDatasetStore = defineStore('dataset', {
    state: () => ({
        selectedDataset: null as FaostatDataset | null,
    }),
    actions: {
        selectDataset(dataset: FaostatDataset) {
            this.selectedDataset = dataset;
        },
        clearDataset() {
            this.selectedDataset = null;
        },
    },
});