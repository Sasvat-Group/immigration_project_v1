import { createSlice } from '@reduxjs/toolkit'

let initialState = {
    profileData: {
        beneficiaryList: { loading: true },
        beneficiary: {
            id: 0,
            name: 'NA'
        },
        immigrationTimeline: { loading: true },
        quickAssessmentForm: { loading: true },
        immigrationStatusKeyDates: { loading: true },
        projects: { loading: true },
        workAuthorizationInfo: { loading: true },
        prProcessInfo: { loading: true },
        prPriorityInfo: { loading: true },
        employeeInfo: { loading: true },
        passportTravel: { loading: true },
        personalInfo: { loading: true },
        dmsWorkspaceLink: { loading: true }
    }
}

const slice = createSlice({
    initialState,
    name: 'beneficiary',
    reducers: {
        setBeneficiaryList(state, { payload }) {
            state.profileData.beneficiaryList = {
                ...payload,
                loading: false
            }
            return state
        },
        setBeneficiary(state, { payload }) {
            state.profileData.beneficiary = payload
            return state
        },
        setTabLoader(state, { payload }) {
            state.profileData[payload.tab]['loading'] = payload.status
            return state
        },
        setImmigrationTimeline(state, { payload }) {
            let filderData = {}
            for (let key of Object.keys(payload)) filderData[key] = payload[key][0]

            state.profileData.immigrationTimeline = {
                ...state.profileData.immigrationTimeline,
                ...filderData,
                loading: false
            }
            return state
        },
        setQuickAssessmentForm(state, { payload }) {
            state.profileData.quickAssessmentForm = {
                ...state.profileData.quickAssessmentForm,
                ...payload,
                loading: false
            }
            return state
        },
        setImmigrationStatusKeyDates(state, { payload }) {
            state.profileData.immigrationStatusKeyDates = {
                ...state.profileData.immigrationStatusKeyDates,
                ...payload,
                loading: false
            }
            return state
        },
        setProjects(state, { payload }) {
            state.profileData.projects = { ...state.profileData.projects, ...payload, loading: false }
            return state
        },
        setPrPriorityInfo(state, { payload }) {
            state.profileData.prPriorityInfo = { ...state.profileData.prPriorityInfo, ...payload, loading: false }
            return state
        },
        setWorkAuthorizationInfo(state, { payload }) {
            state.profileData.workAuthorizationInfo = {
                ...state.profileData.workAuthorizationInfo,
                ...payload,
                loading: false
            }
            return state
        },
        setPrProcessInfo(state, { payload }) {
            state.profileData.prProcessInfo = { ...state.profileData.prProcessInfo, ...payload, loading: false }
            return state
        },
        setEmployeeInfo(state, { payload }) {
            state.profileData.employeeInfo = { ...state.profileData.employeeInfo, ...payload, loading: false }
            return state
        },
        setPassportTravel(state, { payload }) {
            state.profileData.passportTravel = { ...state.profileData.passportTravel, ...payload, loading: false }
            return state
        },
        setPersonalInfo(state, { payload }) {
            state.profileData.personalInfo = { ...state.profileData.personalInfo, ...payload, loading: false }
            return state
        },
        setDmsWorkspaceLink(state, { payload }) {
            state.profileData.dmsWorkspaceLink = { ...state.profileData.dmsWorkspaceLink, ...payload, loading: false }
            return state
        }
    }
})

export const actions = slice.actions
export default slice.reducer
