import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/components/WareHouses.vue"),
  },
  {
    path: "/upload_order",
    name: "upload-file",
    component: () => import("@/components/UploadOrder.vue"),
  },
  {
    path: "/products",
    name: "products",
    component: () => import("@/components/ProductList.vue"),
  },
  {
    path: "/orders",
    name: "orders",
    component: () => import("@/components/OrderList.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

export default router;
