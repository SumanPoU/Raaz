<template>
  <header
    class="grid grid-cols-[2fr,5fr,2fr] p-4 border-b border-gray-100 sticky"
  >
    <NuxtLink to="/">
      <img src="~/assets/images/logo.png" class="h-8" />
    </NuxtLink>

    <div class="justify-self-center">
      <nav>
        <ul class="flex gap-8">
          <li><NuxtLink to="/">Home</NuxtLink></li>
          <li>
            <NuxtLink to="/me">My Account({{ useAuth().user.email }})</NuxtLink>
          </li>
        </ul>
      </nav>
    </div>

    <div class="justify-self-end">
      <span class="cursor-pointer text-red-400" @click="useAuth().logout"
        >Logout</span
      >
    </div>
  </header>
</template>
