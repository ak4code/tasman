import axios from "./plugins/axios"
import { createApp } from "vue"
// import './registerServiceWorker'
import store from "./store"
import "./assets/tailwind.css"
import TasHeader from "@/components/base/TasHeader"

const app = createApp({
  components: {
    TasHeader
  }
})
app.use(store).use(axios).mount("#tasman")
