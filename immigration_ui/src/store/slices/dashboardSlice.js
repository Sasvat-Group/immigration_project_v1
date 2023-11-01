import { createSlice } from '@reduxjs/toolkit'

let initialState = {
    isLoading: true,
    "project_graph": {
        "filed": {
            "previous_filed": [],
            "this_filed": []
        },
        "initiated": {
            "previous_initiated": [],
            "this_initiated": []
        }
    },
    "total_beneficiary": {
        "total_firm_beneficiary": 0,
        "total_my_beneficiary": 0,
        "total_new_firm_beneficiary": 0,
        "total_new_my_beneficiary": 0
    },
    "total_petitioner": {
        "total_firm_petitioner": 0,
        "total_my_petitioner": 0,
        "total_new_firm_petitioner": 0,
        "total_new_my_petitioner": 0
    },
    "total_projects": {
        "total_firm_projects": 0,
        "total_my_projects": 0
    }

}

const slice = createSlice({
    initialState,
    name: 'dashboard',
    reducers: {
        setInitialData(state, { payload }) {
            payload['isLoading'] = false
            return payload
        },
        setTileName(state, { payload }) {
            console.log(payload)
        },
        setLoading(state, { payload }) {
            state.isLoading = payload
        },
    },
})

export const { setTileName, setInitialData, setLoading } = slice.actions
export default slice.reducer