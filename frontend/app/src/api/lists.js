import axios from './axios';

const BASE_PATH = '/lists';

export const getAllLists = () =>
  axios.get(BASE_PATH);

export const getList = (id) =>
  axios.get(`${BASE_PATH}/${id}`);

export const createList = (data) =>
  axios.post(BASE_PATH, data);

export const updateList = (id, data) =>
  axios.put(`${BASE_PATH}/${id}`, data);

export const deleteList = (id) =>
  axios.delete(`${BASE_PATH}/${id}`);
