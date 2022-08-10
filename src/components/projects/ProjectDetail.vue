<template>
<div id="project-detail" class="flex px-4 py-4 gap-4" v-if="project">
  <div class="board bg-slate-200 px-2 py-1 h-fit w-80 rounded" v-for="board in project.active_boards" :key="board.id">
    <h3 class="text-cyan-900 font-bold">{{ board.name }}</h3>
    <draggable :id="board.id" class="cards flex flex-col gap-2 my-2 min-h-[150px]" :list="board.cards" item-key="id"
               @start="drag=true" @end="dropHandler" group="people" :data-board-id="board.id">
      <template #item="{element}">
        <div class="card px-1 py-1 bg-white rounded" :data-card-id="element.id">{{ element.title }}</div>
      </template>
    </draggable>
    <card-add-dialog-button></card-add-dialog-button>
  </div>
</div>
</template>

<script setup>
import draggable from 'vuedraggable';
import { ref, computed, defineProps } from 'vue';
import { useStore } from 'vuex';
import CardAddDialogButton from '@/components/cards/CardAddDialogButton';

const props = defineProps({
  id: Number
});

const drag = ref(false);

const store = useStore();

function getProjects() {
  store.dispatch('getProjects');
}

getProjects();

function cardUpdate(payload) {
  store.dispatch('cardUpdate', payload);
}

const project = computed(() => store.getters.projectById(props.id));

function dropHandler(event) {
  const card = { id: event.item.dataset.cardId, board: event.to.dataset.boardId };
  cardUpdate(card);
  drag.value = false;
}
</script>

<style scoped>

</style>