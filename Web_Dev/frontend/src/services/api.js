import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

console.log("API URL =", API_URL);

export const analyzeNoise = async (formData) => {
  console.log("Sending analysis request...");

  const response = await axios.post(`${API_URL}/analysis/predict`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  console.log("Analysis response:", response.data);

  return response.data;
};

export const getHistory = async () => {
  console.log("Loading history...");

  const response = await axios.get(`${API_URL}/history`);

  return response.data;
};

export const getDashboard = async () => {
  console.log("Loading dashboard...");

  const response = await axios.get(`${API_URL}/dashboard`);

  return response.data;
};

export const downloadReport = (id) => {
  window.open(`${API_URL}/report/download/${id}`, "_blank");
};
