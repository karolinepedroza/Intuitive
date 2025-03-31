import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/lista_cadastros_operadoras';  
export const searchOperators = async (query) => {
    try {
        const response = await axios.post(API_URL, { query });
        return response.data;
    } catch (error) {
        console.error('Error fetching operators:', error);
        throw error;
    }
};