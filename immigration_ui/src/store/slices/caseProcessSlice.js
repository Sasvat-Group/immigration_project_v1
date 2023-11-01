import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    caseDrafting: {
        drafting: {
            steps: [
                { name: 'Drafting Request Date', value: '22-Mar', type: 'date' },
                { name: 'Other Petitions/Applications to Draft', value: 'No', type: 'string' },
                { name: 'Drafting Status', value: 'Pending', type: 'string' },
                { name: 'Drafting Status Date', value: '23-Mar', type: 'date' },
                { name: 'Link to drafted Petitioner', value: '/', type: 'link' },
            ]
        },
        reDrafting: {
            steps: [
                { name: 'Re-Drafting Request Date', value: '24-Mar', type: 'date' },
                { name: 'Re-Drafting Status', value: 'Pending', type: 'string' },
                { name: 'Re-Drafting Status Date', value: '25-Mar', type: 'date' },
                { name: 'Link to Re-Drafted Petitioner', value: '/', type: 'link' },
            ]
        }
    },
}

const slice = createSlice({
    initialState,
    name: 'case-process',
    reducers: {
        setData() {

        }
    },
})

export const { setData } = slice.actions
export default slice.reducer