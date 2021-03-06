import { GET_PRODUCT , DELETE_PRODUCT, ADD_PRODUCT} from "../actions/types"

const initialState = {
    products: []
}

export default function (state = initialState , action  ) {
    switch (action.type) {
        case GET_PRODUCT:
            return{
                ...state ,
                products: action.payload
            }
        case ADD_PRODUCT:
            return{
                ...state,
                products : [...state.products , action.payload]
            }
        case DELETE_PRODUCT :
            return {
                ...state,
                products: state.products.filter(product => product.id !== action.payload)
            }
        default:
            return state
    }
}

