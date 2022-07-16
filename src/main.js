import axios from "./plugins/axios"
import { createApp } from "vue"
// import './registerServiceWorker'
import store from "./store"

const app = createApp({})
app.use(store).use(axios).mount("#tasman")
