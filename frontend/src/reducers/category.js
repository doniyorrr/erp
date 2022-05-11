import { GET_CATEGORY , GET_SUB_CATEGORY} from "../actions/types"

const initialState = {
    category: []
}

export default function (state = initialState , action  ) {

    const {type , payload} = action

    switch (type) {
        case GET_CATEGORY:
            return{
                ...state ,
                category: payload
            }
        case GET_SUB_CATEGORY : 
            return {
                ...state,
                category: payload
            }    
        default:
            return state
    }
}

