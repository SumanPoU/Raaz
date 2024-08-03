<template>
  <div>
    <div class="flex flex-col items-center">
      <h1 class="text-2xl font-bold">Welcome, to Razza !!!</h1>
      <p class="text-lg my-2">An Online CItizen Search Platform.</p>
    </div>
    <form v-on:submit.prevent="performSearch()">
      <div class="min-w-full grid grid-cols-[2fr,6fr,2fr]">
        <select class="border mr-2 px-4 border-gray-100" required id="searchBy">
          <option value="0" selected disabled hidden>
            Select an Option...
          </option>
          <optgroup label="Search By">
            <option
              v-for="option in options"
              :key="option.value"
              :value="option.value"
            >
              {{ option.text }}
            </option>
          </optgroup>
        </select>
        <input
          type="text"
          class="border px-4 py-2"
          placeholder="Input your search query here..."
          id="query"
          required
        />
        <button type="submit" class="border border-gray-100 ml-2">
          Search
        </button>
      </div>
    </form>
  </div>
  <div
    class="max-w-md overflow-hidden shadow-lg mx-auto my-4"
    :class="show ? 'block' : 'hidden'"
  >
    <div class="flex flex-col p-2">
      <h1 class="font-bold uppercase tracking-widest mb-2">Citizen Details:</h1>
      <div class="grid grid-cols-[2fr,7fr]">
        <span>Name:</span>
        <span>{{ name }}</span>
      </div>
      <div class="grid grid-cols-[2fr,7fr]">
        <span>Surname:</span>
        <span>{{ surname }}</span>
      </div>
      <div class="grid grid-cols-[2fr,7fr]">
        <span>DOB:</span>
        <span>{{ dob }}</span>
      </div>
      <div class="grid grid-cols-[2fr,7fr]">
        <span>Email:</span>
        <span>{{ email }}</span>
      </div>
      <div class="grid grid-cols-[2fr,7fr]">
        <span>Address:</span>
        <span>{{ address }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
let show = ref(false);

let name = ref("");
let surname = ref("");
let dob = ref("");
let email = ref("");
let address = ref("");

const options = [
  { value: "name", text: "Name" },
  { value: "phone", text: "Phone Number" },
  { value: "citizenship", text: "Citizenship Number" },
  { value: "bank", text: "Bank A/c Number" },
];

function performSearch() {
  show.value = false;
  const searchBy = document.getElementById("searchBy").value;

  if (searchBy == 0) {
    alert("Please select an option.");
    return;
  }

  const query = document.getElementById("query").value;
  const url = "http://127.0.0.1:8000/search/" + searchBy + "/" + query + "/";

  $fetch(url)
    .then((data) => {
      name.value = data.name;
      surname.value = data.surname;
      dob.value = data.dob;
      email.value = data.email;
      address.value = data.address;
      show.value = true;
    })
    .catch((error) => {
      alert("No such citizen found.");
    });
}
</script>
