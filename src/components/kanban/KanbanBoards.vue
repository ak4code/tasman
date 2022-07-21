<template>
<div id="kan-ban" class="flex min-h-[93.5vh] bg-slate-400 px-4 py-4 gap-4">
  <div class="board bg-slate-200 px-2 py-1 h-fit w-80 rounded" v-for="board in boards" :key="board.id"
       @drop.prevent="dropHandler($event, board.id)" @dragover.prevent @dragenter.prevent>
    <h3 class="text-cyan-900 font-bold">{{ board.name }}</h3>
    <div class="cards flex flex-col gap-2 my-2 min-h-[150px]">
      <div class="card px-1 py-1 bg-white rounded" v-for="card in board.cards" :key="card.id" draggable="true"
           @dragstart="startDrag($event, card.id)">
        {{ card.title }}
      </div>
    </div>
    <CardAddButton></CardAddButton>
  </div>
</div>
</template>

<script setup>
import CardAddButton from "./CardAddButton"
import { computed } from "vue"
import { useStore } from "vuex"

const store = useStore()

function getBoards() {
  store.dispatch("getBoards")
}

function cardUpdate(payload) {
  store.dispatch("cardUpdate", payload)
}

getBoards()

const boards = computed(() => store.state.boards)

function startDrag(event, id) {
  event.dataTransfer.dropEffect = "move"
  event.dataTransfer.effectAllowed = "move"
  event.dataTransfer.setData("id", id)
}

function dropHandler(event, boardId) {
  const card = { id: event.dataTransfer.getData("id"), board: boardId }
  cardUpdate(card)
}
</script>

<style scoped>
.card {
  cursor: pointer;
}
</style>