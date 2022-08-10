import { createStore } from 'vuex';
import { _axios } from '@/plugins/axios';

export default createStore({
  state: {
    projects: [],
    boards: []
  },
  getters: {
    projectById: (state) => (id) => {
      return state.projects.find(project => project.id === id)
    }
  },
  mutations: {
    SET_PROJECTS(state, data) {
      state.projects = data;
    },
    SET_BOARDS(state, data) {
      state.boards = data;
    }
  },
  actions: {
    async getProjects({ commit }) {
      let { data } = await _axios.get('/api/projects/');
      commit('SET_PROJECTS', data);
    },
    async getBoards({ commit }) {
      let { data } = await _axios.get('/api/boards/');
      commit('SET_BOARDS', data);
    },
    async cardUpdate({ dispatch }, payload) {
      let { data } = await _axios.patch(`/api/cards/${payload.id}/`, payload);
      console.log(data);
      dispatch('getProjects');
    },
  },
  modules: {}
});
