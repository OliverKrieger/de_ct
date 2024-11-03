export interface CountryDataset {
    "Area Code": number;
    Years: Array<number>;
    Values: Array<number>;
}

export interface CountryDatasets {
    [country: string]: CountryDataset;
}