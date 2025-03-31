<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <SearchField />
  </div>
</template>

<script>
import SearchField from './components/SearchField.vue';

export default {
  name: 'App',
  components: {
    SearchField
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
</style>