<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
onMounted(() => {
  useAuth().initUser();

  if (!localStorage.getItem("user.token")) {
    navigateTo("/login");
  } else {
    navigateTo("/");
  }
});
</script>
