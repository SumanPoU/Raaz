<template>
  <div class="min-h-screen bg-gray-100 flex flex-col justify-center sm:py-12">
    <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md">
      <div class="flex items-center justify-center">
        <img src="~/assets/images/logo.png" class="h-16 justify-center pb-2" />
      </div>
      <h1 class="font-bold text-center text-2xl mb-5">Login</h1>
      <form v-on:submit.prevent="submitForm()" autocomplete="on">
        <div class="bg-white shadow w-full rounded-lg divide-y divide-gray-200">
          <div class="px-5 py-7">
            <label class="font-semibold text-sm text-gray-600 pb-1 block"
              >E-mail</label
            >
            <input
              type="email"
              class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
              v-model="email"
            />
            <label class="font-semibold text-sm text-gray-600 pb-1 block"
              >Password</label
            >
            <input
              type="password"
              class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
              v-model="pass"
            />
            <button
              type="submit"
              class="transition duration-200 bg-blue-500 hover:bg-blue-600 focus:bg-blue-700 focus:shadow-sm focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50 text-white w-full py-2.5 rounded-lg text-sm shadow-sm hover:shadow-md font-semibold text-center inline-block"
            >
              <span class="inline-block mr-2">Login</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                class="w-4 h-4 inline-block"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                />
              </svg>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
let email = ref("");
let pass = ref("");

const url = "http://127.0.0.1:8000/auth/login/";

async function submitForm() {
  await $fetch(url, {
    method: "POST",
    body: {
      email: email.value,
      password: pass.value,
    },
  })
    .then((response) => {
      useAuth().login(email.value, response.token);
      navigateTo("/");
    })
    .catch((error) => {
      if (error.response) {
        alert("Something went wrong.");
      }
    });
}
</script>
