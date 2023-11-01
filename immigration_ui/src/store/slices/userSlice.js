import { createSlice } from "@reduxjs/toolkit"
import jwtDecode from "jwt-decode"

let initialState = null

const slice = createSlice({
    initialState,
    name: "app-user",
    reducers: {
        setAppUser(state, { payload }) {

            if (payload) {
                const userData = jwtDecode(payload)
                userData['token'] = payload
                return userData
            }
            return null
        },
    },
})

export const { setAppUser } = slice.actions
export default slice.reducer
