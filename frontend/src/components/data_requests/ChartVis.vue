<template>
    <Bar
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
    />
  </template>
  
  <script setup lang="ts">
  import { defineProps, ref, computed } from 'vue';
  import { Bar } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);
  
  // Define props
  const props = defineProps<{
    labels: string[];
    label: string;
    data: number[];
    backgroundColor?: string; // Optional background color prop
  }>();
  
  // Define chart data based on props
  const chartData = computed(() => ({
    labels: props.labels,
    datasets: [
      {
        label: props.label,
        backgroundColor: props.backgroundColor || '#42A5F5', // Use default color if not provided
        data: props.data,
      },
    ],
  }));
  
  // Declare chart options with typing
  const chartOptions = ref<{
    responsive: boolean;
  }>({
    responsive: true,
  });
  </script>
  
  <style scoped>
  .chart-container {
    position: relative;
    height: 40vh;
    width: 80vw;
  }
  </style>
  