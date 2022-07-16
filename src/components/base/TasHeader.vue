<template>
<header class="bg-cyan-800 py-1.5 px-1.5">
  <nav class="flex justify-between items-center gap-x-1.5">
    <div class="left w-full">
      <div class="h-12"></div>
    </div>
    <div class="flex justify-center w-2/12">
      <a href="/">
        <svg class="fill-white h-12" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <g>
            <path fill="none" d="M0 0h24v24H0z"/>
            <path
                d="M5 5v14h14V5H5zM4 3h16a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm9 7v7h-2v-7H7V8h10v2h-4z"/>
          </g>
        </svg>
      </a>
    </div>
    <div class="right flex justify-end w-full">
      <button class="bg-white/20 h-12 px-5 align-middle font-bold text-lg text-white rounded">
        +
      </button>
    </div>
  </nav>
</header>
</template>

<script setup>
import { ref } from "vue"

const msg = ref("tas-header")
console.log(msg)
</script>

<style scoped>

</style>