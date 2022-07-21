import { createStore } from "vuex"
import { _axios } from "@/plugins/axios"

export default createStore({
  state: {
    boards: []
  },
  getters: {},
  mutations: {
    SET_BOARDS(state, data) {
      state.boards = data
    }
  },
  actions: {
    async getBoards({ commit }) {
      let { data } = await _axios.get("/api/boards/")
      commit("SET_BOARDS", data)
    },
    async cardUpdate({ dispatch }, payload) {
      let { data } = await _axios.patch(`/api/cards/${payload.id}/`, payload)
      console.log(data)
      dispatch("getBoards")
    },
  },
  modules: {}
})
