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
import { ref, onBeforeMount, computed } from "vue";
import axios from "axios";

onBeforeMount(async () => {
  await getProducts();
});
const orders = ref([]);
const getProducts = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/api/v1/orders_sell/"
    );
    console.log(response.data);
    orders.value = response.data;
  } catch (error) {
    console.error(error);
  }
};
const productsFormatter = (products) => {
  return products.join(", ");
};
</script>
<template>
  <Heading tag="h1" class="mb-5">ORDENES</Heading>
  <Table class="mb-5 dark" v-if="orders.length">
    <table-head>
      <table-head-cell>Almacén</table-head-cell>
      <table-head-cell>Status</table-head-cell>
      <table-head-cell>Productos</table-head-cell>
    </table-head>
    <table-body>
      <table-row v-for="order in orders">
        <table-cell>{{ order.warehouse }}</table-cell>
        <table-cell>{{ order.status }}</table-cell>
        <table-cell>{{ productsFormatter(order.products) }}</table-cell>
      </table-row>
    </table-body>
  </Table>
  <p v-else>No hay productos</p>
</template>
<style scoped></style>
