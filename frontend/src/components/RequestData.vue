<template>
    <div class="data-request-component">
        <h1>Data Request Component</h1>
        <div v-if="dateData">
            <p>Current Date: {{ dateData.date }}</p>
            <p>Milliseconds since epoch: {{ dateData.milliseconds_since_epoch }}</p>
            <p>Time: {{ dateData.time }}</p>
        </div>
        <button @click="getData">Fetch Date</button>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';
    import axios from 'axios';

    const apiURL = import.meta.env.VITE_API_URL;

    const dateData = ref<{ date: string; milliseconds_since_epoch: number; time: string } | null>(null);

    async function getData(){
        try {
            const response = await axios.get(`${apiURL}/get-data`);
            dateData.value = response.data;
            return dateData;
        } catch (error) {
            console.error("Error fetching date data:", error);
        }
    }
</script>

<style scoped>

</style>