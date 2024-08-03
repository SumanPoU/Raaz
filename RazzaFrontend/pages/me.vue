<template>
  <div class="flex flex-col justify-left">
    <div class="flex">
      <span class="pr-2">First Name:</span>
      <input type="text" v-model="first" />
    </div>
    <div class="flex">
      <span class="pr-2">Middle Name:</span>
      <input type="text" v-model="middle" />
    </div>
    <div class="flex items-center justify-left">
      <span class="pr-2">Last Name:</span>
      <input type="text" v-model="last" />
    </div>
    <div class="flex items-center justify-left">
      <span class="pr-2">Email Address:</span>
      <input type="email" v-model="email" disabled="true" />
    </div>
  </div>
</template>

<script setup>
let first = ref("");
let middle = ref("");
let last = ref("");
let email = ref("");
let pass = ref("");

onMounted(() => {
  const url =
    "http://127.0.0.1:8000/auth/user/" +
    localStorage.getItem("user.token") +
    "/";
  $fetch(url, {
    method: "GET",
  })
    .then((response) => {
      first.value = response.first_name;
      middle.value = response.middle_name;
      last.value = response.last_name;
      email.value = response.email;
      pass.value = response.password;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>
