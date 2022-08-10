<template>
<div id="projects-list" class="px-2 py-2">
  <el-table :data="projects" class="min-w-full">
    <el-table-column
        prop="id"
        label="ID"
        width="100"
    ></el-table-column>
    <el-table-column label="Название">
      <template #default="scope">
        <a :href="scope.row.link">{{scope.row.name}}</a>
      </template>
    </el-table-column>
    <el-table-column label="Действия" width="250" fixed="right">
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
          >Редактировать</el-button
        >
        <el-button
          size="small"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >Удалить</el-button
        >
      </template>
    </el-table-column>
  </el-table>
</div>
</template>

<script setup>
import { computed } from "vue"
import { useStore } from "vuex"

const store = useStore()
store.dispatch("getProjects")

const projects = computed(() => store.state.projects)

</script>

<style scoped>

</style>