import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const analyzeNoise = async (formData) => {
  console.log("API URL:", API_URL);
  console.log("Sending request to:", `${API_URL}/analysis/predict`);

  const response = await axios.post(`${API_URL}/analysis/predict`, formData);

  console.log("Response:", response);

  return response.data;
};
