export interface CountryDataset {
    areaCode: number;
    values: Array<[number, number]>;
}

export interface CountryDatasets {
    [country: string]: CountryDataset;
}