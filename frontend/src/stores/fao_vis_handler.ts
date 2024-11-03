import { defineStore } from 'pinia';
import { FaostatDataset } from '../types/type_faostat_dataset';
import { CountryDatasets } from '../types/type_country_data';
import axios from 'axios';

export const handlerFaoVisStore = defineStore('faoVis', {
    state: () => ({
        selectedDataset: null as FaostatDataset | null,
        selectedCountryDataset: null as CountryDatasets | null,
        loading: false,
        error: null as string | null,
    }),
    actions: {
        async fetchDataset(dataset: FaostatDataset) {
            console.log("Fetching data: ", dataset.FileLocation)
            this.selectedDataset = dataset;
            this.loading = true;
            this.error = null;
            try {
                const apiURL = import.meta.env.VITE_API_URL;
                const apiKEY = import.meta.env.VITE_FUNCTION_HOST_KEY;
                const response = await axios.get<CountryDatasets>(`${apiURL}/fetch_emission_data?url=${dataset.FileLocation}&code=${apiKEY}`);
                this.selectedCountryDataset = response.data;
            } catch (error) {
                this.error = error instanceof Error ? error.message : 'An error occurred';
            } finally {
                this.loading = false;
            }
        },
        clearDataset() {
            this.selectedDataset = null;
        },
    },
});