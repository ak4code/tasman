import axios from "./plugins/axios"
import { createApp } from "vue"
// import './registerServiceWorker'
import store from "./store"
import "./assets/tailwind.css"
import TasHeader from "@/components/base/TasHeader"
import KanbanBoards from "@/components/kanban/KanbanBoards"
import installElementPlus from './plugins/element'

const app = createApp({
  components: {
    TasHeader,
    KanbanBoards
  }
})

installElementPlus(app)

app.use(store).use(axios).mount("#tasman")
