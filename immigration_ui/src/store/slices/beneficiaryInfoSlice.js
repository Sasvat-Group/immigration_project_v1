import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    vMenu: [{
        title: 'Beneficiary Immigration Timeline (Graph)',
        body: <h1>Beneficiary Immigration Timeline</h1>
    }, {
        title: 'Immigration Status & Key Dates'
    }, {
        title: 'Open Projects'
    }, {
        title: 'Work Authorization Info'
    }, {
        title: 'Beneficiary Quick Assessment Form'
    }, {
        title: 'PR Process Initiation Info'
    }, {
        title: 'PR Process Status Info'
    }, {
        title: 'Employment Info'
    }, {
        title: 'Passport & Travel'
    }, {
        title: 'Personal Data'
    }, {
        title: 'DMS Workspace Link'
    }]
}

const slice = createSlice({
    initialState,
    name: 'beneficiary-info',
    reducers: {
        setData() {

        }
    },
})

export const { setData } = slice.actions
export default slice.reducer