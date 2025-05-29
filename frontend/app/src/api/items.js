import axios from './axios';

const BASE_PATH = (listId) => `/lists/${listId}/items`;

export const getItems = (listId) =>
  axios.get(`${BASE_PATH(listId)}/all`);

export const getItem = (listId, itemId) =>
  axios.get(`${BASE_PATH(listId)}/${itemId}`);

export const createItem = (listId, data) =>
  axios.post(BASE_PATH(listId), data);

export const updateItem = (listId, itemId, data) =>
  axios.put(`${BASE_PATH(listId)}/${itemId}`, data);

export const deleteItem = (listId, itemId) =>
  axios.delete(`${BASE_PATH(listId)}/${itemId}`);

export const completeItem = (listId, itemId) =>
  axios.patch(`${BASE_PATH(listId)}/${itemId}/complete`);

export const uncompleteItem = (listId, itemId) =>
  axios.patch(`${BASE_PATH(listId)}/${itemId}/uncomplete`);
