<script setup>
import {
  Heading,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeadCell,
  TableRow,
} from "flowbite-vue";
import { ref, onBeforeMount } from "vue";
import axios from "axios";

onBeforeMount(async () => {
  await getProducts();
});
const products = ref([]);
const getProducts = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/v1/products/");
    console.log(response.data);
    products.value = response.data;
  } catch (error) {
    console.error(error);
  }
};
</script>
<template>
  <Heading tag="h1" class="mb-5">PRODUCTOS</Heading>
  <Table class="mb-5 dark" v-if="products.length">
    <table-head>
      <table-head-cell>Sku</table-head-cell>
      <table-head-cell>Nombre</table-head-cell>
      <table-head-cell>Imei</table-head-cell>
    </table-head>
    <table-body>
      <table-row v-for="product in products">
        <table-cell>{{ product.sku }}</table-cell>
        <table-cell>{{ product.name }}</table-cell>
        <table-cell>{{ product.imei }}</table-cell>
      </table-row>
    </table-body>
  </Table>
  <p v-else>No hay productos</p>
</template>
<style scoped></style>
