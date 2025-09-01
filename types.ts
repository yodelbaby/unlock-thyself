
export enum AppState {
  START = 'START',
  TEST = 'TEST',
  DIAGNOSING = 'DIAGNOSING',
  RESULT = 'RESULT',
}

export interface Diagnosis {
  name: string;
  text: string;
}

export interface UserResponse {
  text: string;
  image: string; // base64 data URL of the SVG
}
