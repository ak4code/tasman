import axios from "./plugins/axios"
import { createApp } from "vue"
// import './registerServiceWorker'
import store from "./store"
import "./assets/tailwind.css"
import TasHeader from "@/components/base/TasHeader"
import ProjectsList from "@/components/projects/ProjectsList"
import installElementPlus from './plugins/element'

const app = createApp({
  components: {
    TasHeader,
    ProjectsList
  }
})

installElementPlus(app)

app.use(store).use(axios).mount("#tasman")
