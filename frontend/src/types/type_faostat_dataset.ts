export interface FaostatDatasets {
    Datasets: {
        "-xmlns:xsi": string;
        Dataset: FaostatDataset[];
    };
}

export interface FaostatDataset {
    DatasetCode: string;
    DatasetName: string;
    Topic: string;
    DatasetDescription: string;
    Contact: string;
    Email: string;
    DateUpdate: string;
    CompressionFormat: string;
    FileType: string;
    FileSize: string;
    FileRows: number;
    FileLocation: string;
}