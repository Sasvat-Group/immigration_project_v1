import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    beneficiarySearchModal: {
        isOpen: false,
        searchResult: [
            { name: 'John Derry' },
            { name: 'Lelly Keple' },
            { name: 'Diana Pore' },
            { name: 'Petric Lore' },
            { name: 'Kanam Jore' },
            { name: 'John Derry' },
            { name: 'Lelly Keple' },
            { name: 'Diana Pore' },
            { name: 'Petric Lore' },
            { name: 'Kanam Jore' },
            { name: 'John Derry' },
            { name: 'Lelly Keple' },
            { name: 'Diana Pore' },
            { name: 'Petric Lore' },
            { name: 'Kanam Jore' },
        ]
    }
}

const slice = createSlice({
    initialState,
    name: 'common',
    reducers: {
        setBeneficiarySearchModal(state, action) {
            state.beneficiarySearchModal.isOpen = action.payload
        }
    },
})

export const { setBeneficiarySearchModal } = slice.actions
export default slice.reducer