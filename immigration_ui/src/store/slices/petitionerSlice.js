import { createSlice } from '@reduxjs/toolkit'

let initialState = {
    isPetitionerListLoading: true,
    activePetitioner: "NA",
    petitionerList: [],
    profileData: {
        isPetitionerListLoading: false,
        petitionerName: "NA",
        petitionerID: 0,
        overview: { loading: true },
        incorporation: { loading: true },
        employee: { loading: true },
        immigration: { loading: true },
        authorized: { loading: true },
        contact: { loading: true },
    }
}

const slice = createSlice({
    initialState,
    name: 'petitioner',
    reducers: {
        setPetitionerList(state, { payload }) {
            state.petitionerList = payload
            state.isPetitionerListLoading = false
            return state
        },
        setPetitionerInfo(state, { payload }) {
            state.profileData.isPetitionerListLoading = false
            state.profileData.petitionerName = payload.name
            state.profileData.petitionerID = payload.id
            return state
        },
        setPetitionerListLoading(state, { payload }) {
            state.isPetitionerListLoading = payload
        },
        setTabLoader(state, { payload }) {
            state.profileData[payload.tab]['loading'] = payload.status
            return state
        },
        setPetitionerOverview(state, { payload }) {
            state.profileData.overview = { ...state.profileData.overview, ...payload, loading: false }
            return state
        },
        setPetitionerIncorporation(state, { payload }) {
            state.profileData.incorporation = { ...state.profileData.incorporation, ...payload, loading: false }
            return state
        },
        setPetitionerEmployee(state, { payload }) {
            state.profileData.employee = { ...state.profileData.employee, ...payload, loading: false }
            return state
        },
        setPetitionerImmigration(state, { payload }) {
            state.profileData.immigration = { ...state.profileData.immigration, ...payload, loading: false }
            return state
        },
        setPetitionerAuthorized(state, { payload }) {
            state.profileData.authorized = { ...state.profileData.authorized, ...payload, loading: false }
            return state
        },
        setPetitionerContact(state, { payload }) {
            state.profileData.contact = { ...state.profileData.contact, ...payload, loading: false }
            return state
        },
    },
})

export const actions = slice.actions
export default slice.reducer