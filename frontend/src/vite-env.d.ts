/// <reference types="vite/client" />

declare var process: {
    env: {
        VITE_API_URL: string; // Add other environment variables as needed
    };
};

declare module '*.vue' {
    import { DefineComponent } from 'vue';
    const component: DefineComponent<{}, {}, any>;
    export default component;
}

declare module 'vue-chartjs' {
    import { DefineComponent } from 'vue';
    import { ChartOptions } from 'chart.js';

    export const Bar: DefineComponent<any, any, any>;
    export const Line: DefineComponent<any, any, any>;
    export const Pie: DefineComponent<any, any, any>;
    export const Doughnut: DefineComponent<any, any, any>;
    export const PolarArea: DefineComponent<any, any, any>;
    export const Radar: DefineComponent<any, any, any>;
    export const Bubble: DefineComponent<any, any, any>;
    export const Scatter: DefineComponent<any, any, any>;

    export interface ChartProps {
        chartData: any; // Adjust the type as needed
        chartOptions?: ChartOptions; // Use ChartOptions for options
    }
}
