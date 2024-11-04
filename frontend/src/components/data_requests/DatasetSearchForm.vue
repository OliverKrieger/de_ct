<template>
    <div class="dataset-search-form bg-slate-800 p-6">
        <h2 class="text-xl text-rose-500 text-center sm:text-left">Select Data Settings</h2>

        <div v-if="errorMessage">{{ errorMessage }}</div>

        <form @submit.prevent="submitForm">
            <div class="input-settings flex flex-col sm:flex-row justify-between">
                <div>
                    <label class="font-bold text-slate-400" for="startYear">Start Year:</label>
                    <input type="number" v-model="startYear" id="startYear" required />
                </div>

                <div>
                    <label class="font-bold text-slate-400" for="endYear">End Year:</label>
                    <input type="number" v-model="endYear" id="endYear" required />
                </div>

                <div>
                    <label class="font-bold text-slate-400" for="itemSelect">Select Item:</label>
                    <select id="itemSelect" v-model="selectedItem" required>
                        <option value="" disabled>Select an item</option>
                        <option v-for="item in itemsList" :key="item" :value="item">
                            {{ item }}
                        </option>
                    </select>
                </div>

                <div>
                    <label class="font-bold text-slate-400" for="elementSelect">Select Element:</label>
                    <select id="elementSelect" v-model="selectedElement" required>
                        <option value="" disabled>Select an item</option>
                        <option v-for="element in elementList" :key="element" :value="element">
                            {{ element }}
                        </option>
                    </select>
                </div>
            </div>

            <fieldset class="mt-5">
                <legend class="text-center text-xl mb-2 font-bold text-slate-400">Select countries to retrieve data from:</legend>
                <div class="flex justify-center flex-col w-96 m-auto">
                    <div v-for="country in countriesList" :key="country">
                        <label class="flex flex-row items-center justify-between">
                            <span>{{ country }}</span>
                            <div>
                                <input
                                    type="checkbox"
                                    :value="country"
                                    v-model="selectedCountries"
                                    class="w-6 h-6"
                                />
                            </div>
                        </label>
                    </div>
                </div>
            </fieldset>

            <button type="submit" :disabled="!isValidInput" class="bg-rose-500 hover:bg-rose-700 hover:border-rose-700 text-white font-bold py-2 px-4 mt-6 sm:mt-2 rounded transition-all duration-300 cursor-pointer w-full sm:w-auto">Load Data</button>
        </form>
    </div>
</template>

<script setup lang="ts">
    import { ref, computed, defineEmits } from 'vue';
    import { DatasetSearchFormPayload } from '../../types/type_dataset_search';

    const emit = defineEmits<{
        (e: 'form-submitted', payload: { startYear: number; endYear: number; item: string; element:string; countries: string[] }): void;
    }>();

    const itemsList = ['Barley', 'Wheat', 'Oats'];
    const elementList = ['Crops total (Emissions N2O)', 'Crop residues (Emissions N2O)'];
    const countriesList = ['United Kingdom of Great Britain and Northern Ireland', 'Portugal'];

    const startYear = ref<number | null>(1970);
    const endYear = ref<number | null>(2020);
    const selectedItem = ref<string | null>('Barley');
    const selectedCountries = ref<string[]>([]);
    const selectedElement = ref<string | null>('Crops total (Emissions N2O)');
    const errorMessage = ref<string>('');

    const isValidInput = computed(() => {
        const isYearValid = startYear.value !== null && endYear.value !== null && startYear.value <= endYear.value;
        const isItemsSelected = selectedItem.value !== null;
        const isCountriesSelected = selectedCountries.value.length > 0;
        const isElementSelected = selectedElement.value !== null;
        return isYearValid && isItemsSelected && isElementSelected && isCountriesSelected;
    });

    function submitForm() {
        if (!isValidInput.value) {
            errorMessage.value = 'Please ensure the year range is valid and at least one item and one country are selected.';
            return;
        }

        errorMessage.value = ''; // Reset error message

        const payload:DatasetSearchFormPayload = {
            startYear: startYear.value!, // Use non-null assertion
            endYear: endYear.value!, // Use non-null assertion
            item: selectedItem.value!,
            element: selectedElement.value!,
            countries: selectedCountries.value,
        };

        emit('form-submitted', payload);
    }
</script>

<style scoped>
    .search-form {
        max-width: 400px;
        margin: auto;
    }

    input,
    select {
        width: 100%;
        padding: 8px;
        margin-top: 5px;
    }

    .error-message {
        color: red;
        margin-top: 10px;
    }
</style>