import { defineStore } from 'pinia';
import { FaostatDataset } from '../types/type_faostat_dataset';
import { CountryDatasets } from '../types/type_country_data';
import { DatasetSearchFormPayload } from '../types/type_dataset_search';
import axios from 'axios';

export const handlerFaoVisStore = defineStore('faoVis', {
    state: () => ({
        selectedDataset: null as FaostatDataset | null,
        selectedCountryDataset: null as CountryDatasets | null,
        loading: false,
        error: null as string | null,
    }),
    actions: {
        async fetchDataset(dataset: FaostatDataset, payload:DatasetSearchFormPayload ) {
            this.selectedDataset = dataset;
            this.loading = true;
            this.error = null;
            
            const jsonString = JSON.stringify(payload);
            const encodedPayload = encodeURIComponent(jsonString);

            try {
                const apiURL = import.meta.env.VITE_API_URL;
                const apiKEY = import.meta.env.VITE_FUNCTION_HOST_KEY;
                const response = await axios.get<CountryDatasets>(
                    `${apiURL}/fetch_emission_data?url=${dataset.FileLocation}&payload=${encodedPayload}&code=${apiKEY}`
                );
                this.selectedCountryDataset = response.data;
            } catch (error) {
                this.error = error instanceof Error ? error.message : 'An error occurred';
            } finally {
                this.loading = false;
            }
        },
        clearDataset() {
            this.selectedDataset = null;
            this.selectedCountryDataset = null;
        },
    },
});