<template>
  <div>
    <input
      type="text"
      v-model="searchQuery"
      @keyup.enter="performSearch"
      placeholder="Buscar operadoras..."
    />
    <button @click="performSearch">Buscar</button>
    <div v-if="results.length">
      <h3>Resultados:</h3>
      <ul>
        <li v-for="(result, index) in results" :key="index">{{ result }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { searchOperators } from '../services/api';

export default {
  data() {
    return {
      searchQuery: '',
      results: []
    };
  },
  methods: {
    async performSearch() {
      if (this.searchQuery.trim()) {
        try {
          const response = await searchOperators(this.searchQuery);
          this.results = response.data; // Ajuste conforme a estrutura da resposta da API
        } catch (error) {
          console.error('Erro ao buscar operadoras:', error);
        }
      }
    }
  }
};
</script>

<style scoped>
input {
  margin-right: 10px;
}
</style>