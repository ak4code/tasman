<template>
<el-button link @click="dialogVisible = true">Добавить карточку...</el-button>
<el-dialog
    v-model="dialogVisible"
    title="Карточка задачи"
    width="400px"
  >
    <span>This is a message</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogVisible = false"
          >Confirm</el-button
        >
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref } from "vue"

const dialogVisible = ref(false)
</script>

<style scoped>

</style>