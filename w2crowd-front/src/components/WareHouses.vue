<script setup>
import {
  Heading,
  Input,
  Modal,
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
  await getWarehouses();
});
const isShowModal = ref(false);
const closeModal = () => {
  isShowModal.value = false;
};
const showModal = () => {
  isShowModal.value = true;
};
const saveWarehouse = () => {
  isShowModal.value = false;
  sendNewWarehouse();
};
const warehouses = ref([]);
const newWarehouse = ref({
  name: "",
  sub_stock: "",
});
const sendNewWarehouse = async () => {
  const form = new FormData();
  form.append("sub_stock", newWarehouse.value.sub_stock);
  form.append("name", newWarehouse.value.name);

  try {
    const response = await axios.post(
      "http://localhost:8000/api/v1/warehouses/",
      form
    );
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
  await getWarehouses();
};
const getWarehouses = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/api/v1/warehouses/"
    );
    console.log(response.data);
    warehouses.value = response.data;
  } catch (error) {
    console.error(error);
  }
};
</script>
<template>
  <Heading tag="h1" class="mb-5">ALMACENES</Heading>
  <Table class="mb-5 dark" v-if="warehouses.length">
    <table-head>
      <table-head-cell>Nombre</table-head-cell>
      <table-head-cell>Sub-inventario</table-head-cell>
    </table-head>
    <table-body>
      <table-row v-for="warehouse in warehouses">
        <table-cell>{{ warehouse.name }}</table-cell>
        <table-cell>{{ warehouse.sub_stock }}</table-cell>
      </table-row>
    </table-body>
  </Table>
  <p v-else>No hay almacenes</p>
  <button
    @click="showModal"
    type="button"
    class="mt-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
  >
    Registrar Almacén
  </button>
  <Modal size="md" v-if="isShowModal" @close="closeModal" class="dark">
    <template #header>
      <div class="flex items-center text-lg">Registrar Almacén</div>
    </template>
    <template #body>
      <Input
        v-model="newWarehouse.name"
        placeholder="BCA-XXXX"
        label="Nombre del almacén"
        class="mb-5"
      />
      <Input
        v-model="newWarehouse.sub_stock"
        placeholder="IDBCA00002"
        label="Sub-inventario"
      />
    </template>
    <template #footer>
      <div class="flex justify-between">
        <button
          @click="closeModal"
          type="button"
          class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600"
        >
          Cerrar
        </button>
        <button
          @click="saveWarehouse"
          type="button"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Guardar
        </button>
      </div>
    </template>
  </Modal>
</template>
<style scoped></style>
