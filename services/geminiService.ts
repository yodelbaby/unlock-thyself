import { diagnoses } from './diagnoses';
import { Diagnosis } from '../types';

export const getGoofyDiagnosis = async (responses: string[]): Promise<Diagnosis> => {
  console.log('User responses:', responses);
  const randomIndex = Math.floor(Math.random() * diagnoses.length);
  const diagnosis = diagnoses[randomIndex];
  return Promise.resolve({
    name: diagnosis.name,
    text: diagnosis.description
  });
};