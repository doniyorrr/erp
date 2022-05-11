import Axios from "../components/axios/axios";
import { GET_CATEGORY , GET_SUB_CATEGORY } from "./types";

export const getCategory = () => dispatch => {
  Axios.get("/product/categories/")
    .then((res) => {
      dispatch({
          type: GET_CATEGORY,
          payload: res.data
      })
    })
    .catch((err) => console.log(err));
};

export const getSubCategory = () => dispatch => {
  Axios.get("/product/subcategories/")
    .then((res) => {
      dispatch({
          type: GET_SUB_CATEGORY,
          payload: res.data
      })
    })
    .catch((err) => console.log(err));
};
