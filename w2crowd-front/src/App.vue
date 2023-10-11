<script setup>
import { NavbarCollapse, NavbarLink } from "flowbite-vue";
</script>
<template>
  <div class="flex flex-row w-full p-6">
    <NavbarCollapse class="dark mx-auto">
      <NavbarLink>
        <router-link :to="{ name: 'home' }"> Almacenes </router-link>
      </NavbarLink>
      <NavbarLink>
        <router-link :to="{ name: 'products' }"> Productos </router-link>
      </NavbarLink>
      <NavbarLink>
        <router-link :to="{ name: 'orders' }"> Ordenes </router-link>
      </NavbarLink>
      <NavbarLink>
        <router-link :to="{ name: 'upload-file' }">
          Subir orden de compra
        </router-link>
      </NavbarLink>
    </NavbarCollapse>
  </div>
  <router-view></router-view>
</template>
<style scoped></style>
