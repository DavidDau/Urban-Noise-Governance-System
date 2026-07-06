import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export const analyzeNoise = async (formData) => {
  try {
    // We omit manual headers; Axios handles multipart/form-data seamlessly
    // when passed a real FormData object instance.
    const response = await axios.post(`${API_URL}/analysis/predict`, formData);
    return response.data;
  } catch (error) {
    console.error(
      "API Error in analyzeNoise:",
      error.response?.data || error.message,
    );
    throw error;
  }
};

export const getHistory = async () => {
  try {
    const response = await axios.get(`${API_URL}/history`);
    return response.data;
  } catch (error) {
    console.error("API Error in getHistory:", error.message);
    throw error;
  }
};

export const getDashboard = async () => {
  try {
    const response = await axios.get(`${API_URL}/dashboard`);
    return response.data;
  } catch (error) {
    console.error("API Error in getDashboard:", error.message);
    throw error;
  }
};

export const downloadReport = (id) => {
  window.open(`${API_URL}/report/download/${id}`, "_blank");
};
